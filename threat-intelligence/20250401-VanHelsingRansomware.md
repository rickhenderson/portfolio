# VanHelsing Ransomware

## Summary

VanHelsingRAAS is a new ransomware-as-a-service that was released on March 7, 2025 and malware from the service was first discovered on March 16, 2025 by researchers at [Check Point Research](https://research.checkpoint.com/2025/vanhelsing-new-raas-in-town/).

The creators request the software not be used against CIS countries, indicating that the developers are Russian or pro-Russian, or possibly trying to make it appear to be pro-Russian in an attempt at disinformation.

The malware uses SMB to replicate itself over network shares, giving it worm-like capabilities.

## Rapid Detection

* Attempts to delete Windows shadow copies using `cmd.exe /c C:\\Windows\\System32\\wbem\\WMIC.exe shadowcopy where \"ID='%s'\" delete`
* Creates a file called `README.txt`
* [UNIQUE] Creates a file called `vhlocker.png` in C:\Windows\Web
* [UNIQUE] Creates a file called `vhlocker.ico` in C:\Windows\Web
* [UNIQUE] Creates registry entry in HKLM\Software\Classes\.vanlocker\DefaultIcon with Data: `C:\Windows\Web\vhlocker.ico`
* Performs an IP scan of all 255 addresses on the compromised subnets looking for SMB services on port 445
* [UNIQUE] Copies itself to network shares as `$SHARE\\vanlocker.exe` and executes `$Temp\psexec.exe` which it dropped
* [UNIQUE] `cmd.exe /c $TEMP/psexec.exe -accepteula \\\\$SHARE -c -f $SHARE\\vanlocker.exe -d --no-mounted --no-network < NUL`

## Recommendations

* Use [Shadow Copies Deletion Using Operating Systems Utilities](https://github.com/SigmaHQ/sigma/blob/78a78c79ffd2998cd864618c538395a4e8c23902/rules/windows/process_creation/proc_creation_win_susp_shadow_copies_deletion.yml#L4) by Florian Roth (Nextron Systems) for detection of attempted shadow file deletion.
* Also [PowerShell Module File Created by Non-PowerShell Process](https://github.com/SigmaHQ/sigma/blob/78a78c79ffd2998cd864618c538395a4e8c23902/rules/windows/file/file_event/file_event_win_powershell_module_uncommon_creation.yml#L2) by Nasreddine Bencherachali (Nextron Systems).
* Create rules for your detection engine based on unique characteristics of VanHelsing or more general detections for defense-in-width (I think I made that up).
* Preference should be given to detect the loader before it can download or execute the encryption binary.

For more details on how the malware operates, please read the [Check Point article](https://research.checkpoint.com/2025/vanhelsing-new-raas-in-town/).

## IOCs

These are file IOCs in SHA256, taken from the CPR article which listed them as MD5.

* 8c272d63d9a37651b81283f0273609db8b9cd7af0b20e917529c7c9ca8687d59 (loader)
* 86d812544f8e250f1b52a4372aaab87565928d364471d115d669a8cc7ec50e17
* 99959c5141f62d4fbb60efdc05260b6e956651963d29c36845f435815062fd98

## ANY.RUN Analysis

As of April 1, 2025, there were already a number of tasks executing VanHelsing available on [ANY.RUN](https://any.run/), starting on March 17. My investigation can be seen [here](https://app.any.run/tasks/a05d1e58-3521-4c10-a60e-b31401e15e35) but I was unable to get the malware to do much of anything, likely due to the initial creation of the mutex which ANY.RUN was able to indicate.

In [this task](https://app.any.run/tasks/39efe72c-eeb9-4ebe-83cd-73a7d28cc567) I was able to get the malware to execute and begin encrypting files. Feel free to use the analysis for your own detections.


Note: Some reference links were gathered via [Feedly](https://feedly.com/i/collection/content/user/cc20e8e3-2a63-40bf-9046-a038677236c9/category/f7345f24-0352-440c-9614-6d78f9ec9dce).

### References

* https://research.checkpoint.com/2025/vanhelsing-new-raas-in-town/ (March 23, 2025)
* https://www.tripwire.com/state-of-security/vanhelsing-ransomware-what-you-need-know
* https://www.infosecurity-magazine.com/news/vanhelsing-raas-expands-rapidly/ 
