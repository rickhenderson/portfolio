import com.sun.net.httpserver.BasicAuthenticator;
import com.sun.net.httpserver.HttpExchange;
import com.sun.net.httpserver.HttpHandler;
import com.sun.net.httpserver.HttpServer;

import java.io.IOException;
import java.io.OutputStream;
import java.net.InetSocketAddress;
import java.util.Base64;
import java.util.List;
import java.util.Map;

/**
 * Educational demo server illustrating the REACHABLE CODE PATTERN described
 * in the Java4Shell (CVE-2026-114938) advisory: an HTTP endpoint that runs
 * java.util.Base64.Decoder.decode() on attacker-supplied input as part of
 * (or before) authentication — the same shape Xray's "applicable" example
 * uses (BasicAuthenticator + Base64.getDecoder + HttpClient.send).
 *
 * IMPORTANT: this server is NOT exploitable. java.util.Base64 on this JVM
 * is memory-safe; the real bug only exists in the AVX-512 VBMI JIT
 * intrinsic on specific x86-64 hardware, which this code does not contain
 * and cannot trigger. Use it only to see which requests WOULD reach the
 * vulnerable call site on affected hardware/JDKs, and pair it with
 * MaskUnderflowSim.java to see the underlying arithmetic bug.
 */
public class VulnServer {

    // Mirrors the advisory's "applicable" pattern: Base64 decoding happens
    // inside the authenticator, i.e. before any credential check succeeds.
    static class DemoAuthenticator extends BasicAuthenticator {
        DemoAuthenticator() {
            super("demo");
        }

        @Override
        public boolean checkCredentials(String username, String password) {
            // By the time we get here, BasicAuthenticator.authenticate()
            // has ALREADY called Base64.getDecoder().decode(...) on the raw
            // Authorization header value to produce username/password —
            // that decode is the vulnerable call site on affected
            // hardware/JDKs, and it runs before this method, i.e. before
            // any credential check. We just log that we got this far.
            System.out.println("[server] decoded Basic credentials for user=" + username);
            return "demo".equals(username) && "demo".equals(password);
        }
    }

    static class UploadHandler implements HttpHandler {
        @Override
        public void handle(HttpExchange exchange) throws IOException {
            byte[] body = exchange.getRequestBody().readAllBytes();
            String b64 = new String(body).trim();
            System.out.println("[server] /upload received base64 payload, tail=\""
                + b64.substring(Math.max(0, b64.length() - 8)) + "\"");
            try {
                byte[] decoded = Base64.getDecoder().decode(b64); // reachable pre-auth decode site
                respond(exchange, 200, "decoded " + decoded.length + " bytes\n");
            } catch (IllegalArgumentException e) {
                System.out.println("[server] rejected malformed base64: " + e.getMessage());
                respond(exchange, 400, "bad base64: " + e.getMessage() + "\n");
            }
        }
    }

    static class RootHandler implements HttpHandler {
        @Override
        public void handle(HttpExchange exchange) throws IOException {
            // getRequestHeaders() already ran through BasicAuthenticator
            // (attached in main()) before we get here.
            respond(exchange, 200, "authenticated OK\n");
        }
    }

    private static void respond(HttpExchange exchange, int status, String body) throws IOException {
        byte[] bytes = body.getBytes();
        exchange.sendResponseHeaders(status, bytes.length);
        try (OutputStream os = exchange.getResponseBody()) {
            os.write(bytes);
        }
    }

    public static void main(String[] args) throws IOException {
        int port = args.length > 0 ? Integer.parseInt(args[0]) : 8099;
        HttpServer server = HttpServer.create(new InetSocketAddress(port), 0);

        var root = server.createContext("/", new RootHandler());
        root.setAuthenticator(new DemoAuthenticator()); // Base64 decode happens here, pre-auth

        server.createContext("/upload", new UploadHandler()); // direct decode of request body

        server.setExecutor(null);
        server.start();
        System.out.println("[server] listening on http://127.0.0.1:" + port);
        System.out.println("[server] GET /        -> Base64-decodes the Authorization header pre-auth");
        System.out.println("[server] POST /upload -> Base64-decodes the raw request body");
        System.out.println("[server] (this JVM is memory-safe here; see README for why)");
    }
}
