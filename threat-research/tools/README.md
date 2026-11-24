# Threat Research Tools

These tools were written sometimes for learning or a single purpose so please check before using.

* [malcheck.py](malcheck.py) - A simple binary analysis tool. It uses a raw `requests` call to the VirusTotal API endpoint when you provide your own API key. It does other things too. 
* [logan.py](logan.py) - The beginning of a log analyzer using Didier Stevens' public domain starter code. See https://DidierStevens.com.



**Output from malcheck.py**:

```
    ▪  .▄▄ ·     ▪  ▄▄▄▄▄    • ▌ ▄ ·.  ▄▄▄· ▄▄▌  ▄▄▌ ▐ ▄▌ ▄▄▄· ▄▄▄  ▄▄▄ . ██████╗
    ██ ▐█ ▀.     ██ •██      ·██ ▐███▪▐█ ▀█ ██•  ██· █▌▐█▐█ ▀█ ▀▄ █·▀▄.▀· ╚════██╗
    ▐█·▄▀▀▀█▄    ▐█· ▐█.▪    ▐█ ▌▐▌▐█·▄█▀▀█ ██▪  ██▪▐█▐▐▌▄█▀▀█ ▐▀▀▄ ▐▀▀ ▄   ▄███╔╝
    ▐█▌▐█▄▪▐█    ▐█▌ ▐█▌·    ██ ██▌▐█▌▐█ ▪▐▌▐█▌▐▌▐█▌██▐█▌▐█ ▪▐▌▐█•█▌▐█▄▄▌   ▀▀══╝
    ▀▀▀ ▀▀▀▀     ▀▀▀ ▀▀▀     ▀▀  █▪▀▀▀ ▀  ▀ .▀▀▀  ▀▀▀▀ ▀▪ ▀  ▀ .▀  ▀ ▀▀▀    ██╗
                                                                            ╚═╝

[+] Requesting malware search from VirusTotal...

Reputation: 0
Type Extention: exe
Stats: {'malicious': 0, 'suspicious': 0, 'undetected': 70, 'harmless': 0, 'timeout': 1, 'confirmed-timeout': 0, 'failure': 0, 'type-unsupported': 4}
Magic string: PE32 executable (GUI) Intel 80386, for MS Windows, Nullsoft Installer self-extracting archive
Unique Sources: 43
Resource Language: ENGLISH US
Likely Compiler: [ C ] Windows Server 2003 SP1 DDK build 4035 count=2
Import List: [{'library_name': 'ADVAPI32.dll', 'imported_functions': ['AdjustTokenPrivileges', 'LookupPrivilegeValueW', 'OpenProcessToken', 'RegCloseKey', 'RegCreateKeyExW', 'RegDeleteKeyW', 'RegDeleteValueW', 'RegEnumKeyW', 'RegEnumValueW', 'RegOpenKeyExW', 'RegQueryValueExW', 'RegSetValueExW', 'SetFileSecurityW']}, {'library_name': 'SHELL32.dll', 'imported_functions': ['SHBrowseForFolderW', 'ShellExecuteExW', 'SHFileOperationW', 'SHGetFileInfoW', 'SHGetPathFromIDListW', 'SHGetSpecialFolderLocation']}, {'library_name': 'ole32.dll', 'imported_functions': ['CoCreateInstance', 'CoTaskMemFree', 'IIDFromString', 'OleInitialize', 'OleUninitialize']}, {'library_name': 'COMCTL32.dll', 'imported_functions': ['ImageList_AddMasked', 'ImageList_Create', 'ImageList_Destroy', 'Ord(17)']}, {'library_name': 'USER32.dll', 'imported_functions': ['AppendMenuW', 'BeginPaint', 'CallWindowProcW', 'CharNextA', 'CharNextW', 'CharPrevW', 'CheckDlgButton', 'CloseClipboard', 'CreateDialogParamW', 'CreatePopupMenu', 'CreateWindowExW', 'DefWindowProcW', 'DestroyWindow', 'DialogBoxParamW', 'DispatchMessageW', 'DrawTextW', 'EmptyClipboard', 'EnableMenuItem', 'EnableWindow', 'EndDialog', 'EndPaint', 'ExitWindowsEx', 'FillRect', 'FindWindowExW', 'GetClassInfoW', 'GetClientRect', 'GetDC', 'GetDlgItem', 'GetDlgItemTextW', 'GetMessagePos', 'GetSysColor', 'GetSystemMenu', 'GetSystemMetrics', 'GetWindowLongW', 'GetWindowRect', 'InvalidateRect', 'IsWindow', 'IsWindowEnabled', 'IsWindowVisible', 'LoadCursorW', 'LoadImageW', 'MessageBoxIndirectW', 'OpenClipboard', 'PeekMessageW', 'PostQuitMessage', 'RegisterClassW', 'ReleaseDC', 'ScreenToClient', 'SendMessageTimeoutW', 'SendMessageW', 'SetClassLongW', 'SetClipboardData', 'SetCursor', 'SetDlgItemTextW', 'SetForegroundWindow', 'SetTimer', 'SetWindowLongW', 'SetWindowPos', 'SetWindowTextW', 'ShowWindow', 'SystemParametersInfoW', 'TrackPopupMenu', 'wsprintfA', 'wsprintfW']}, {'library_name': 'GDI32.dll', 'imported_functions': ['CreateBrushIndirect', 'CreateFontIndirectW', 'DeleteObject', 'GetDeviceCaps', 'SelectObject', 'SetBkColor', 'SetBkMode', 'SetTextColor']}, {'library_name': 'KERNEL32.dll', 'imported_functions': ['CloseHandle', 'CompareFileTime', 'CopyFileW', 'CreateDirectoryW', 'CreateFileW', 'CreateProcessW', 'CreateThread', 'DeleteFileW', 'ExitProcess', 'ExpandEnvironmentStringsW', 'FindClose', 'FindFirstFileW', 'FindNextFileW', 'FreeLibrary', 'GetCommandLineW', 'GetCurrentProcess', 'GetDiskFreeSpaceW', 'GetExitCodeProcess', 'GetFileAttributesW', 'GetFileSize', 'GetFullPathNameW', 'GetLastError', 'GetModuleFileNameW', 'GetModuleHandleA', 'GetModuleHandleW', 'GetPrivateProfileStringW', 'GetProcAddress', 'GetShortPathNameW', 'GetSystemDirectoryW', 'GetTempFileNameW', 'GetTempPathW', 'GetTickCount', 'GetVersion', 'GetWindowsDirectoryW', 'GlobalAlloc', 'GlobalFree', 'GlobalLock', 'GlobalUnlock', 'LoadLibraryExW', 'lstrcatW', 'lstrcmpiA', 'lstrcmpiW', 'lstrcmpW', 'lstrcpyA', 'lstrcpynW', 'lstrlenA', 'lstrlenW', 'MoveFileExW', 'MoveFileW', 'MulDiv', 'MultiByteToWideChar', 'ReadFile', 'RemoveDirectoryW', 'SearchPathW', 'SetCurrentDirectoryW', 'SetEnvironmentVariableW', 'SetErrorMode', 'SetFileAttributesW', 'SetFilePointer', 'SetFileTime', 'Sleep', 'WaitForSingleObject', 'WideCharToMultiByte', 'WriteFile', 'WritePrivateProfileStringW']}]
```
