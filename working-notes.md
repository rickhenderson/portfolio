# Unsorted Working Notes

In this file I'm tracking the kinds of things I do that apply to new projects or general research.

## May 2025

**May 28, 2025:** I applied for a job that mentioned requiring knowledge of botnets and botnet infrastructure. After first thinking of [Sliver](https://github.com/BishopFox/sliver) and [Havoc](https://github.com/HavocFramework/Havoc) which are both command and control (C2) frameworks, I did a search for `botnet frameworks` and the first hit is the open botnet framework called [BYOB - Bring Your Own Botnet](https://github.com/malwaredllc/byob).

BYOB is an open botnet framework designed for education purposes, but is fully functional. I first encountered it during an investigation involving bots, when I was reading a threat intelligence article from some researcher that included a particular portion of code that looked unusual. This was when I began checking Github for unique code fragments and this particular fragment turned up in BYOB. This "educational tool" had been successfully used in an attack. Alas, memory fails me now - 2 years later - to remember what case. Though maybe I have notes about it somewhere. At that time I had cloned the repo and got it working to test out some of the bot agents.

So I cloned BYOB to re-familiarize myself with it in case it comes up in the interview.
* There were a number of problems with out of date or deprecated libraries like pyhook. Couldn't get it to run. May have to verify the libraries that are used and manually find replacements. An issue on the main repo suggests one change that doesn't completely solve the problem.

* Started looking at malware analysis, started up an account with IDA 9.0 online with a 1 year license (free), and was writing a short Python script to get information fom the Malshare API when I did some reading on PyJWT and started an account on Auth0.
* Was looking at an analysis of [WhisperGate](https://www.crowdstrike.com/en-us/blog/technical-analysis-of-whispergate-malware/), which is malware that I investigated in 2022.
  
**May 31, 2025:** BYOB won't install correctly because of out of date libraries and some deprecated ones I think. I did some work in Python yesterday and today I completed a crackme with Android Studio and the OWASP MAS.
