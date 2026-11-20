# Java4Shell (CVE-2026-114938): How It Works

> **A security education project.** A safe, local walkthrough of the bug class behind Java4Shell, an out-of-bounds write in OpenJDK's AVX-512 Base64 decoder. Nothing here corrupts real memory, and nothing here needs vulnerable hardware.

## What is Java4Shell?

Java4Shell is a memory-corruption vulnerability in the Base64 decoder of OpenJDK, the most widely used Java runtime. Base64 is everywhere: HTTP `Authorization` headers, file uploads, tokens, and network messages. That makes a decoder bug unusually reachable. A server often decodes untrusted Base64 *before* it has checked who is sending it.

To decode quickly, HotSpot (OpenJDK's JVM) replaces the Java code for `Base64.Decoder` with a hand-written x86-64 assembly routine called an **intrinsic**. On CPUs with AVX-512 VBMI, that routine processes 64 bytes at a time and uses a **masked store** to write only the output bytes that are valid.

The bug is in how the routine computes that mask for input with unusual padding:

1. The output length is estimated as `(len / 4) * 3`.
2. The padding count (`=` characters) is subtracted from it.
3. For a malformed tail such as `=`, `X=` or `===`, the result goes **negative** (for example `-1`).
4. The mask is built with the BMI2 instruction `BZHI`, which reads only the **low 8 bits** of its count operand. So `-1` is read as `255`.
5. A count of 255 produces an **all-ones mask**. The store that should have written nothing now writes a full 64 bytes, past the end of the output buffer.

The result is an attacker-influenced heap overwrite. Overwrites like this can be turned into crashes, memory disclosure, or code execution, depending on what sits next to the buffer.

**In short:** a signed-length underflow becomes an unsigned 8-bit count. That becomes a mask of "write everything", and the write lands in adjacent memory.

## Who is affected?

| | |
|---|---|
| **Affected** | OpenJDK-based runtimes on **x86-64 CPUs with AVX-512 VBMI** (plus BMI2) |
| **Not affected** | ARM64, and x86-64 hosts without AVX-512 VBMI (they use the safe scalar or AVX2 path) |
| **Exposure** | Any code path that decodes untrusted Base64, such as pre-authentication `Authorization: Basic ...` parsing |

Check the advisory for the exact affected version ranges for your distribution.

## Why a simulation?

The vulnerable code is a native assembly stub inside the JIT compiler. It is only reachable on specific hardware, and reproducing it would mean building a working memory-corruption primitive. This project does not do that. It shows the same **logic** in plain, memory-safe Java:

| File | What it teaches |
|---|---|
| `MaskUnderflowSim.java` | Re-implements the length, padding and `BZHI` arithmetic and runs a simulated masked store into a byte array. A labeled "canary" region sits right after the output buffer, so you can watch the overflow land in it. |
| `VulnServer.java` | A minimal HTTP server that calls `Base64.getDecoder().decode()` on the raw `Authorization` header *before* the credential check. This is the **vulnerable pattern**: untrusted input reaching the decoder before authentication. |
| `PocClient.java` | Sends malformed-padding `Authorization` headers (for example, 64 `A`s followed by `=`) to the server. On real vulnerable hardware this is the kind of input that reaches the buggy code. Here it only produces the normal `IllegalArgumentException`. |

> The server and client are **not exploitable** on any JDK. `java.util.Base64` is memory-safe except through the specific AVX-512 intrinsic bug, and this code does not contain that intrinsic.

## Running it

No build step is needed. Modern `java` runs source files directly (JDK 11+).

```sh
# 1. See the underflow and mask bug in isolation
java MaskUnderflowSim.java

# 2. See the vulnerable pattern (pre-auth Base64 decode) in a real server
java VulnServer.java &
java PocClient.java
```

If you have a full JDK, `javac *.java && java MaskUnderflowSim` works too.

## What to look for in the output

- `outLen` going negative for malformed tails.
- `BZHI` turning that negative count into `255`, so the mask becomes all-ones.
- The simulated store writing 64 bytes where it should write 0.
- The canary bytes after the output buffer being overwritten.

## Lessons for developers

- **Length arithmetic is a security boundary.** Subtracting without checking for underflow is a classic source of memory bugs, and it matters more when a hardware instruction truncates the value.
- **Validate before you optimize.** Fast paths still need to match the safe path on malformed input. Fuzz them with bad padding, short tails and odd lengths.
- **Don't parse untrusted input before authentication if you can avoid it.** Where you can't, keep the parser small and well-tested.
- **Native intrinsics are part of your attack surface**, even when your own code is entirely "safe" Java.

## Mitigations (for real affected hosts)

- Update to a fixed OpenJDK build, or your distribution's equivalent.
- Or disable the vulnerable path at JVM startup:
  - `-XX:-UseBASE64Intrinsics`, or
  - `-XX:UseAVX=2`
- Confirm whether your hardware is exposed by checking CPU flags for `avx512f`, `avx512bw`, `avx512vbmi` and `bmi2`.

## References

- The original Java4Shell advisories and write-ups (see the advisory links for current fixed-version numbers)
- Intel documentation for `BZHI` (BMI2) and AVX-512 VBMI masked stores

## Disclaimer

This repository is for education and defensive awareness. It contains no exploit code and no working memory-corruption primitive. Only test systems you own or have permission to test.

