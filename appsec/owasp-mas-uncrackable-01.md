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

<img src="using-jadx-for-disassembling-android-code-uncrackable-mobile-appsec">

