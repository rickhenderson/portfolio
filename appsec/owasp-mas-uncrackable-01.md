# AppSec - OWASP Mobile Application Security Crackmes

## Android Uncrackable L1

May 31,2025:

This morning I had watched John Hammond do one of the Android crackmes in his [video explaining 3 ways to hack a mobile app](https://www.youtube.com/watch?v=QwwLSyRzNwo) and decided to give it a try.

Yesterday I had already downloaded Android Studio, but hadn't installed it yet, so this was a good thing to get started trying.

When he disassembled the Java code using `jadx-gui` ([Jadx on Github](https://github.com/skylot/jadx/releases/tag/v1.5.1)) I thought: Why doesn't he decode the Base64 string, it's probably the password?

Of course, I was wrong.

<img src="img\using-jadx-for-disassembling-android-code.png">

In order to really figure this out you need to run the code, but it helps to understand more about the Javax.Crypto library.

The code displayed was disassembled from Dex bytecode by Jadx, which is why the function names are meaningless. Usually when I debug obfuscated code, I will at least rename the functions to something meaningful.

Further on we find the code which does the decryption of the secret:

<img src="img\using-jadx-for-disassembling-android-code-uncrackable-mobile-appsec.png">

So now we know the secret is encrypted with AES, using ECB with Padding. 

I wanted to read how the crypto library worked so I found it here: https://docs.oracle.com/javase/8/docs/api/javax/crypto/spec/SecretKeySpec.html so I could look up `SecretKeySpec`, `Cipher.getInstance`, and `Cipher.init`.

The `opmode` value of 2 threw me for a moment. [The docs for crypto/Cipher](https://docs.oracle.com/javase/8/docs/api///javax/crypto/Cipher.html) state the possible values are ENCRYPT_MODE, DECRYPT_MODE, WRAP_MODE or UNWRAP_MODE but they don't include the numeric values. It's clearly an enumeration but did they start at 0 or 1? Since I'm dealing with decryption and I didn't know what WRAP_MODE is, I could assume it was decrypt mode, but to be sure I looked up the source code for [javax.crypto.Cipher.java](https://github.com/frohoff/jdk8u-jdk/blob/master/src/share/classes/javax/crypto/Cipher.java).

There we find 2 = Decrypt mode. Reading source code is awesome!

And before going any further I did some googling and some Clauding ( ;) ) and renamed the functions and classes:

<img src="img\is-this-android-rooted-hacking-android-mobile-application-security.png">
