# Malware Intelligence & Analysis of GhostWriter's Excel Macros

* Ukranian government and military, and activists in Belarus were targeted to drop a new variant of PicassoLoader
* GhostWriter aka UAC-0057 or UNC1151 is thought to be aligned with the Government of Belarus
* First reported by SentinelLABS on February 25, 2025
* According SentinelLABS, GhostWriter has been running since 2016 and the current campaign featuring obfuscated Excel Macros may have begun in November 2024 and is currently still active.
 
The malicious Excel file was titled "Political Prisoners in Minsk Courts" (translated from the original Russian title "политзаключенные(по судам минска).xls") and was sent via email from a typical Gmail account. It was originally stored as a RAR file, so it would have to be uncompressed by the user to first make the .xls file accessible.

The file contained a VBA macro set to run automatically when the opened in Excel. SentinelLABS displayed a screenshot of the obfuscated macro but does not provide a text version of the code. With an Enterprise account on VirusTotal you can download the sample, but sadly I don't have an Enterprise account and haven't been able to find the sample on Malware Bazaar or VXUnderground.

Below is a simplified example of what is displayed:

```VB
Private Function first_function() As String
    Dim var1 As String
    var1 = ""
    var1 = second_function(second_function(second_function(second_function...)))
    var1 = second_function(second_function(second_function(second_function...)))
    ' ...
    var1 = second_function(second_function(second_function(second_function...)))
    first_function = var1 ' The return statement.
End Function 

Private Function third_function() As String
    Dim var1 As String
    var1 = ""
    var1 = var1 + fourth_function()
    var1 = var1 + fifth_function()
    var1 = var1 + sixth_function()
    ' ...
End Function
```

In the screenshot shared by SentinelLABS, the left side of the code has been cut off, so it's hard to identify the code's purpose with any certainty.

However, just by its format it is likely meaningless code. Without seeing the definition of `second_function()` my analysis can't be completed.

1. Download benign JPG file and save it as CertificateCenter.dll
2. File is set to autorun by changing a registry key (writing to HKEY CurrentUser - HKCU - Does not require Admin Rights)
3. Set `rundll32.exe` to execute a specific function in the .dll (function with ordinal 1 in this case) whenever the user logs on

SentinelLABS believes that during an actual attack, a malicious DLL would be stored on a users's computer instead of the benign jpg.

A second Excel file contained macro code that was obfuscated using macro_pack, a tool to automate obfuscation of code by Emeric Nasi. The Github project hasn't been maintained since 2021, but the repo was updated in August 2024 to indicate it is now a project of BallisKit, a red teaming tool provider that sells MacroPack for 1350 EUR, or just over $2100 CAD.

When the second Excel file is opened, a .NET dll obfuscated with ConfuserEx (`bruhdll32.dll`) and again executed with `rundll32`. This drops a decoy Excel file which opens automatically. The decoy files are to convince the user that they are receiving the information they expected, and have not just been compromised by a threat actor.

This decoy also downloads a benign image file, saves it to the %APPDATA%\Roaming folder of the user as CertificateCenter.dll, and also creates a config file:

```XML
<Project xmlns="http://schemas.microsoft.com/developer/msbuild/2003">
 <PropertyGroup>
  <AssemblyName>Certificate</AssemblyName>
  <OutputPath>Bin\</OutputPath>
 </PropertyGroup>
 <ItemGroup>
  <Compile Include="CertificateCenter.dll" />
 </ItemGroup>
 <Target Name="Build">
  <MakeDir Directories="$(OutputPath)" Condition="!Exists('$(OutputPath)')" />
  <Csc Sources="@(Compile)" OutputAssembly="$(OutputPath)$(AssemblyName).exe" />
 </Target>
</Project>
```

The config file contains instructions to MSBuild to construct a new application. This indicates the .dll file is likely not an actual DLL file, but is source code that is included in to the project to create a complete executable.

The presence of news articles from many companies and reporting of known incidents by other security organizations can make it difficult to know where the original samples were first detected and investigated. In my estimation, first party research was done by Cyble in 2024 and SentinelLABS in 2025. See the Cyble article titled "UNC1151 Strikes Again" for an in-depth technical report on the 2024 activity also involving obfuscated Excel macros.

## References

* https://thehackernews.com/2025/02/belarus-linked-ghostwriter-uses.html
* https://www.sentinelone.com/labs/ghostwriter-new-campaign-targets-ukrainian-government-and-belarusian-opposition/
* https://mkaring.github.io/ConfuserEx/
* https://cyble.com/blog/unc1151-strikes-again-unveiling-their-tactics-against-ukraines-ministry-of-defence/
* https://www.virustotal.com/gui/file/7c065bc99b79a2485f823a5fdf862627e9e4d25fa8d12d673810ea39d56e2be2
* https://github.com/sevagas/macro_pack
* https://superuser.com/questions/1417787/edit-registry-without-administrator-permission

## Other Sources for Malware Analysis

* https://metadefender.opswat.com/
* https://thehackernews.com/2023/07/picassoloader-malware-used-in-ongoing.html - PicassoLoader: Dropping CobaltStrike and njRAT 
* https://cert.gov.ua/article/6280345 - Ukrainian Computer Emergency Response Team (CERT-UA) first description of ANONVNC / MESHAGENT campaign
* https://thehackernews.com/2024/08/ukraine-warns-of-new-phishing-campaign.html - PicassoLoader
