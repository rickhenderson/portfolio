import java.util.Arrays;

/**
 * Educational simulation of the CVE-2026-114938 ("Java4Shell") masked-store
 * underflow, described in the JFrog advisory as living in OpenJDK's
 * AVX-512 VBMI Base64 decode intrinsic.
 *
 * This does NOT touch unsafe memory and does NOT require AVX-512 hardware.
 * It reproduces the described arithmetic:
 *
 *   outLen  = (len / 4) * 3          // bytes this tail block should produce
 *   outLen -= paddingChars           // one '=' removes one output byte
 *   mask    = BZHI(ALL_ONES, outLen) // low `outLen` bits set, rest cleared
 *   store 64 bytes at outPtr, masked // only the set bits are actually written
 *
 * BZHI only reads the low 8 bits of its count operand. If outLen underflows
 * to a negative int, (byte) outLen is 255 instead of 0, so instead of "write
 * nothing" the stub computes "write everything" — a full 64-byte masked
 * store where zero bytes were meant to be written.
 *
 * To make the overflow visible without unsafe memory, we lay out a single
 * byte array as [ output buffer | canary region ] end-to-end, exactly the
 * adjacency the advisory describes on the real heap, and run the *same*
 * mask/length math against it.
 */
public final class MaskUnderflowSim {

    // Simulated masked store: writes `maskPopcount(mask)` bytes of VALUE
    // starting at `offset` into `heap`, exactly mirroring VMOVDQU8+mask.
    private static final byte WRITE_VALUE = (byte) 0x9a; // per advisory

    private static long bzhi(long allOnes, int index) {
        // Real BZHI reads only bits [7:0] of the index operand.
        int idx = index & 0xFF;
        if (idx >= 64) return allOnes;       // "all bits" (the bug's path)
        return allOnes & ((1L << idx) - 1);  // low `idx` bits set
    }

    private static int popcount(long mask) {
        return Long.bitCount(mask);
    }

    /**
     * Simulates decoding one 4-character base64 tail block.
     *
     * @param len         number of base64 chars remaining in this tail (<=4 normally)
     * @param padding     number of '=' characters in the tail
     * @param heap        the backing array, laid out [outputBuffer][canary]
     * @param outputStart offset of the output buffer within heap
     * @param outputSize  real/intended size of the output buffer (bytes already valid)
     */
    static void simulateTailStore(int len, int padding, byte[] heap, int outputStart, int outputSize) {
        int outLen = (len / 4) * 3;   // step 1 from the advisory
        outLen -= padding;            // step 2 from the advisory — can underflow

        long mask = bzhi(-1L, outLen); // step 3: BZHI(ALL_ONES, outLen & 0xFF)
        int bytesWritten = popcount(mask);

        System.out.printf(
            "  tail(len=%d, padding=%d): outLen=%d  -> BZHI index=%d (0x%02x)  -> mask=0x%016x  -> writes %d bytes%n",
            len, padding, outLen, outLen & 0xFF, outLen & 0xFF, mask, bytesWritten);

        // Where the real stub would start writing: right after the bytes
        // already decoded from earlier full blocks in this output buffer.
        int writeAt = outputStart + outputSize;

        int inBounds = 0, spilled = 0;
        for (int i = 0; i < bytesWritten; i++) {
            int addr = writeAt + i;
            if (addr < heap.length) {
                boolean insideIntendedBuffer = addr < outputStart + outputSize + 2; // 2 "real" tail bytes for =-padding case
                if (addr >= outputStart && addr < outputStart + outputSize + 2) inBounds++;
                else spilled++;
                heap[addr] = WRITE_VALUE;
            }
        }
        System.out.printf("  -> %d byte(s) landed in/near the intended buffer, %d byte(s) spilled into adjacent (canary) memory%n",
            inBounds, spilled);
    }

    public static void main(String[] args) {
        System.out.println("== Java4Shell masked-store underflow: arithmetic + layout simulation ==");
        System.out.println("(No unsafe memory access; no AVX-512 required. For education only.)\n");

        // Layout: 50-byte "output buffer" (as in the advisory's worked example,
        // decoding 128 'A' chars + 1 '=' on JDK 17) followed by a 64-byte
        // canary region standing in for "whatever the heap put next".
        int outputStart = 0;
        int outputSize = 48; // bytes already filled by the prior full blocks
        int canarySize = 64;
        byte[] heap = new byte[outputStart + outputSize + canarySize];
        Arrays.fill(heap, (byte) 0x00);
        // Mark the canary region distinctly so corruption is obvious.
        for (int i = outputStart + outputSize; i < heap.length; i++) heap[i] = (byte) 0xCC;

        System.out.println("Case 1: WELL-FORMED tail, e.g. \"AA==\" (len=4 chars in block, 2 '=' padding)");
        System.out.println("  Expected: outLen = (4/4)*3 - 2 = 1 -> mask should have exactly 1 bit set.");
        simulateTailStoreFresh(4, 2, outputStart, outputSize, canarySize);

        System.out.println();
        System.out.println("Case 2: MALFORMED tail, e.g. a lone \"=\" (len=0 chars before the '=', 1 '=' padding)");
        System.out.println("  This is the advisory's trigger: (0/4)*3 - 1 underflows to -1.");
        simulateTailStoreFresh(0, 1, outputStart, outputSize, canarySize);

        System.out.println();
        System.out.println("Case 3: MALFORMED tail \"===\" (len=0, 3 '=' padding) — same underflow, different padding count");
        simulateTailStoreFresh(0, 3, outputStart, outputSize, canarySize);

        System.out.println();
        System.out.println("Summary: a malformed tail with only padding characters drives `outLen` negative.");
        System.out.println("BZHI reading the low byte of that negative number yields 255, producing an all-ones");
        System.out.println("mask instead of all-zero, so the masked store writes 64 bytes where it should write 0.");
        System.out.println("On real AVX-512 hardware with the unpatched intrinsic, those 64 bytes land on the real");
        System.out.println("process heap, 2 bytes inside the output array and 62 bytes past its end — exactly the");
        System.out.println("primitive the advisory uses to corrupt an adjacent array's length header.");
    }

    private static void simulateTailStoreFresh(int len, int padding, int outputStart, int outputSize, int canarySize) {
        byte[] heap = new byte[outputStart + outputSize + canarySize];
        for (int i = outputStart + outputSize; i < heap.length; i++) heap[i] = (byte) 0xCC;
        simulateTailStore(len, padding, heap, outputStart, outputSize);
    }
}
