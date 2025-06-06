# Security Engineer Study Notes For Interview

Tips from https://github.com/gracenolan/Notes/blob/master/interview-study-notes-for-security-engineering.md#learning-tips.

## STRIDE

Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Priviledge

## Lockheed-Martin Kill Chain

Reconnaisance, Weaponization, Delivery, Exploitation, Installation, Command and Control, Actions on Objectives

recon weapon
deliver exploit
install c2
actions on objectives

## Mitre ATT&CK

https://attack.mitre.org/#

Reconnaisance, Resource Development, Initial Access, Persistence, Priv Esc, Defence Evasion, Credential Access, Lateral Movement, Collection, Command and Control, Exfiltration, Impact

## OSI Layer

Application, Presentation, Session, Transport (tcp/udp), Network (layer 3 switch, IP), Data Link (ethernet, mac address, switches), Physical (cables, bits)

https://www.guru99.com/layers-of-osi-model.html, https://newserverlife.com/articles/osi-network-model-for-beginners-device-layers-protocols/, https://int0x33.medium.com/day-51-understanding-the-osi-model-f22d5f3df756

## Firewalls

### Snort Rules

* contains a header and body
* alert tcp $EXTERNAL_NET 80 -> $HOME_NET any: rule will trigger an alert of any tcp traffic comes into the home network from the external network on port 80.
* uses # and /* for comments */
* Snort rule: [action] [protocol] [addresses] [ports] [direction operator]
* Five classic rule actions: alert, block, drop, log, pass; also Snort 3 adds react, reject, rewrite

## Reverse Engineering

* radare2, rabin2, rasm2, radiff2, rafind2, rahash2, rax2, ragg2-cc, ragg2

## Linux System Logs

Source: https://phoenixnap.com/kb/how-to-view-read-linux-log-files

Types of Linux logs:

* System
* Event
* Application
* Service

### System Logs

* /var/log/syslog, /var/log/messages
  * Jun  2 11:19:48 remnux /usr/lib/gdm3/gdm-x-session[727]: (II) Initializing extension SELinux
  * Jun  2 11:19:52 remnux systemd[712]: Started GNOME Terminal Server.
  * Jun  2 11:19:52 remnux snort[1357]: Writing PID "1357" to file "/var/run//snort_enp0s3.pid"
  * Jun  2 11:25:01 remnux CRON[2055]: (root) CMD (command -v debian-sa1 > /dev/null && debian-sa1 1 1)

* /var/log/kern.log
  * Jun  2 11:19:47 remnux kernel: [    4.639837] 15:19:47.701951 main     VBoxService 7.1.2 r164945 (verbosity: 0) linux.amd64 (Sep 26 2024 15:45:30) release log
  * Jun  2 11:19:47 remnux kernel: [    0.770646] AppArmor: AppArmor Filesystem Enabled
  * Jun  2 11:19:47 remnux kernel: [    0.000000] Linux version 5.4.0-216-generic (buildd@lcy02-amd64-014) (gcc version 9.4.0 (Ubuntu 9.4.0-1ubuntu1~20.04.2)) #236-Ubuntu SMP Fri Apr 11 19:53:21 UTC 2025 (Ubuntu 5.4.0-216.236-generic 5.4.291)
  * Jun  2 11:19:47 remnux kernel: [    0.000000] Hypervisor detected: KVM

* /var/log/faillog: logs unsuccessful user logins
* /var/log/lastlog
* /var/log/bootlog
* /var/log/auth.log: All authentication logs

    ```Log
    Jun  2 12:22:12 remnux polkitd(authority=local): Unregistered Authentication Agent for unix-session:c1 (system bus name :1.95, object path /org/freedesktop/PolicyKit1/AuthenticationAgent, locale en_US.UTF-8) (disconnected from bus)
    Jun  2 12:22:22 remnux systemd: pam_unix(systemd-user:session): session closed for user gdm
    Jun  2 12:25:01 remnux CRON[3796]: pam_unix(cron:session): session opened for user root by (uid=0)
    Jun  2 12:25:01 remnux CRON[3796]: pam_unix(cron:session): session closed for user root
    Jun  2 12:25:06 remnux sudo:   remnux : TTY=pts/0 ; PWD=/home/remnux ; USER=root ; COMMAND=/usr/bin/cat /var/log/boot.log
    Jun  2 12:25:06 remnux sudo: pam_unix(sudo:session): session opened for user root by (uid=0)
    Jun  2 12:25:06 remnux sudo: pam_unix(sudo:session): session closed for user root
    ```

* /var/log/cron: related scheduled cron tasks

* /var/log/debug: debugging and specific system operations
* /var/log/yum, /var/log/dpkg

    ```Log - Dpkg
    2025-06-01 14:29:01 status installed linux-image-5.4.0-216-generic:amd64 5.4.0-216.236
    2025-06-02 11:47:07 startup archives unpack
    2025-06-02 11:47:08 install whois:amd64 <none> 5.5.6
    2025-06-02 11:47:08 status half-installed whois:amd64 5.5.6
    2025-06-02 11:47:08 status triggers-pending man-db:amd64 2.9.1-1
    2025-06-02 11:47:08 status unpacked whois:amd64 5.5.6
    2025-06-02 11:47:08 startup packages configure
    ```

### Application Logs

* Apache Access Logs: /var/log/apache/access.log, /etc/httpd/logs/access_log
  * 127.0.0.1 - - [09/Feb/2024:15:36:14 +0100] "GET / HTTP/1.1" 200 3460 "-" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:120.0) Gecko/20100101 Firefox/120.0"
* Apache Error Logs: /var/log/apache2/error.log, /etc/httpd/logs/error_log
  * [Fri Feb 09 15:35:24.252107 2024] [core:notice] [pid 6672:tid 139657266624384] AH00094: Command line: '/usr/sbin/apache2'

* /var/log/nginx/error.log

```Log
remnux@remnux:~$ cat /var/log/nginx/error.log
2025/06/02 12:38:29 [emerg] 3917#3917: bind() to 0.0.0.0:80 failed (98: Address already in use)
2025/06/02 12:38:29 [emerg] 3917#3917: bind() to [::]:80 failed (98: Address already in use)
2025/06/02 12:38:29 [emerg] 3917#3917: bind() to 0.0.0.0:80 failed (98: Address already in use)
2025/06/02 12:38:29 [emerg] 3917#3917: bind() to [::]:80 failed (98: Address already in use)
2025/06/02 12:38:29 [emerg] 3917#3917: bind() to 0.0.0.0:80 failed (98: Address already in use)
2025/06/02 12:38:29 [emerg] 3917#3917: bind() to [::]:80 failed (98: Address already in use)
2025/06/02 12:38:29 [emerg] 3917#3917: bind() to 0.0.0.0:80 failed (98: Address already in use)
2025/06/02 12:38:29 [emerg] 3917#3917: bind() to [::]:80 failed (98: Address already in use)
2025/06/02 12:38:29 [emerg] 3917#3917: bind() to 0.0.0.0:80 failed (98: Address already in use)
2025/06/02 12:38:29 [emerg] 3917#3917: bind() to [::]:80 failed (98: Address already in use)
2025/06/02 12:38:29 [emerg] 3917#3917: still could not bind()
```

* nginx.service

```Log
Jun 02 12:38:30 remnux nginx[3917]: nginx: [emerg] bind() to 0.0.0.0:80 failed (98: Address already in use)
Jun 02 12:38:30 remnux nginx[3917]: nginx: [emerg] bind() to [::]:80 failed (98: Address already in use)
Jun 02 12:38:30 remnux nginx[3917]: nginx: [emerg] bind() to 0.0.0.0:80 failed (98: Address already in use)
Jun 02 12:38:30 remnux nginx[3917]: nginx: [emerg] bind() to [::]:80 failed (98: Address already in use)
Jun 02 12:38:31 remnux nginx[3917]: nginx: [emerg] bind() to 0.0.0.0:80 failed (98: Address already in use)
Jun 02 12:38:31 remnux nginx[3917]: nginx: [emerg] bind() to [::]:80 failed (98: Address already in use)
Jun 02 12:38:31 remnux nginx[3917]: nginx: [emerg] still could not bind()
Jun 02 12:38:31 remnux systemd[1]: nginx.service: Control process exited, code=exited, status=1/FAILURE
Jun 02 12:38:31 remnux systemd[1]: nginx.service: Failed with result 'exit-code'.
Jun 02 12:38:31 remnux systemd[1]: Failed to start A high performance web server and a reverse proxy server.
```

* /var/log/apt/history.log

```Log
    Start-Date: 2025-06-01  13:04:05
    Commandline: apt autoremove
    Requested-By: remnux (1000)
    Remove: librhash0:amd64 (1.3.9-1), cmake-data:amd64 (3.16.3-1ubuntu1.20.04.1), libssh-gcrypt-4:amd64 (0.9.3-2ubuntu2.5), libjsoncpp1:amd64 (1.7.4-3.1ubuntu2)
    End-Date: 2025-06-01  13:04:05

    Start-Date: 2025-06-01  13:59:38
    Commandline: apt-get install libdnet-dev
    Requested-By: remnux (1000)
    Install: libdnet:amd64 (2.65build2, automatic), libdnet-dev:amd64 (2.65build2)
    End-Date: 2025-06-01  13:59:40
```

* /var/log/samba/log.smbd
* /var/log/dmesg - kernel ring buffer: often the first place to look for errors.

    ```Log
        remnux@remnux:~$ cat /var/log/dmesg
    [    0.000000] kernel: Linux version 5.4.0-216-generic (buildd@lcy02-amd64-014) (gcc version 9.4.0 (Ubuntu 9.4.0-1ubuntu1~20.04.2)) #236-Ubuntu SMP Fri Apr 11 19:53:21 UTC 2025 (Ubuntu 5.4.0-216.236-generic 5.4.291)
    [    0.000000] kernel: Command line: BOOT_IMAGE=/boot/vmlinuz-5.4.0-216-generic root=UUID=b5d95a05-618e-490e-8135-09a83da0cad4 ro splash quiet
    [    0.000000] kernel: KERNEL supported cpus:
    [    0.000000] kernel:   Intel GenuineIntel
    [    0.000000] kernel:   AMD AuthenticAMD
    [    0.000000] kernel:   Hygon HygonGenuine
    [    0.000000] kernel:   Centaur CentaurHauls
    [    0.000000] kernel:   zhaoxin   Shanghai  
    [    0.000000] kernel: BIOS-provided physical RAM map:
    [    0.000000] kernel: BIOS-e820: [mem 0x0000000000000000-0x000000000009fbff] usable
    [    0.000000] kernel: BIOS-e820: [mem 0x000000000009fc00-0x000000000009ffff] reserved
    [    0.000000] kernel: BIOS-e820: [mem 0x00000000000f0000-0x00000000000fffff] reserved
    [    0.000000] kernel: BIOS-e820: [mem 0x0000000000100000-0x00000000dbfeffff] usable
    [    0.000000] kernel: BIOS-e820: [mem 0x00000000dbff0000-0x00000000dbffffff] ACPI data
    [    0.000000] kernel: BIOS-e820: [mem 0x00000000fec00000-0x00000000fec00fff] reserved
    [    0.000000] kernel: BIOS-e820: [mem 0x00000000fee00000-0x00000000fee00fff] reserved
    [    0.000000] kernel: BIOS-e820: [mem 0x00000000fffc0000-0x00000000ffffffff] reserved
    [    0.000000] kernel: BIOS-e820: [mem 0x0000000100000000-0x0000000123ffffff] usable
    [    0.000000] kernel: NX (Execute Disable) protection: active
    [    0.000000] kernel: SMBIOS 2.5 present.
    [    0.000000] kernel: DMI: innotek GmbH VirtualBox/VirtualBox, BIOS VirtualBox 12/01/2006
    [    0.000000] kernel: Hypervisor detected: KVM
    [    3.520941] [drm] Fifo max 0x00200000 min 0x00001000 cap 0x00000355
    [    3.521375] [drm] Using command buffers with DMA pool.
    [    3.521379] [drm] Atomic: yes.
    [    3.521399] [drm:vmw_host_log [vmwgfx]] *ERROR* Failed to send host log message.
    [    3.523148] [drm:vmw_host_log [vmwgfx]] *ERROR* Failed to send host log message.
    [    3.532180] fbcon: svgadrmfb (fb0) is primary device
    ```

  * Also: dmesg --time-format=iso

      2025-06-02T11:19:50,281640-04:00 Bluetooth: Core ver 2.22
      2025-06-02T11:19:50,281660-04:00 NET: Registered protocol family 31

### Viewing logs

* tail, head, cat, less, grep, awk, sed
  * sudo awk '/error/ {print $1, $2, $3, $5}' /var/log/syslog

* control logs with rsyslog.conf

## Finding Suspicious Activity on Linux

* find /var/log/ -type f -mtime -15 -ls

    ```Log
    1703967   8192 -rw-r-----   1 root     systemd-journal  8388608 Jun  1 12:24 /var/log/journal/be825d95d05e40f9935fc830a49e93cc/user-1000@c83427c05a3d4835a8f3da94e64a8488-0000000000001cdd-000623ed5ae56f76.journal
    1706487  16388 -rw-r-----   1 root     systemd-journal 16777216 Jun  2 13:17 /var/log/journal/be825d95d05e40f9935fc830a49e93cc/user-1000.journal
    1704182   8196 -rw-r-----   1 root     systemd-journal  8388608 Jun  1 12:24 /var/log/journal/be825d95d05e40f9935fc830a49e93cc/system@f0c7b28b8b3f492193bfeebb953ccad0-0000000000001cd4-000623ed595ec8f4.journal
    1707823   8192 -rw-r-----   1 root     systemd-journal  8388608 Jun  2 13:16 /var/log/journal/be825d95d05e40f9935fc830a49e93cc/user-1001.journal
    1703971  16388 -rw-r-----   1 root     systemd-journal 16777216 Jun  2 13:17 /var/log/journal/be825d95d05e40f9935fc830a49e93cc/system.journal
    find: ‘/var/log/gdm3’: Permission denied
    1704219     12 -rw-rw-r--   1 root     utmp               11136 Jun  2 12:22 /var/log/wtmp
    1704279      8 -rw-r--r--   1 root     root               32064 Jun  2 13:11 /var/log/faillog
    1704540    832 -rw-r-----   1 root     adm               845828 Jun  2 11:47 /var/log/apt/term.log
    1704717    172 -rw-r--r--   1 root     root              171532 Jun  2 11:47 /var/log/apt/history.log
    ```

* Stat
* Basically auth.log, faillog, wtmp, apt, syslog
* netstat -an
* netstat -an | grep LISTENING
* lsof -i tcp:50537 -P -R
* crontab -l, crontab -e
* check /etc, /tmp
* RootKitHunter: https://rkhunter.sourceforge.net/

## Splunk

* Log forwarder, Splunk Enterprise cloud, Splunk platform index

## PKI and PitM

* PitM is possible with RSA/AES encryption, but the use of trustworthy CAs mitigates this risk.
  * ARP spoofing/poisoning is used to re-direct traffic to a host the attacker controls so it can be tapped

## TOR

* https://ayosecu.com/entry/Investigating-Individuals-on-Tor-Networks
* Investigators can take advantage of vulnerabilities in the TOR infrastructure to identify individuals, NITS, JS and Flash
  * Exit node fingerprinting
  * Social Engineering and undercover
  * Metadata and behavioural analysis
  * https://programminghistorian.org/en/lessons/introduction-to-stylometry-with-python

## SSL / TLS

* HEARTBLEED: Long-term secret keys were compromised.
  * Bug in the OpenSSL crypto library.
  * Introduced in 2011 but not disclosed until 2014. CVE2014-0160. Fix made available same day.
  * A buffer over-read in the TLS heartbeat extension.
    * https://github.com/openssl/openssl/commit/bd6941cfaa31ee8a3f8661cb98227a5cbcc0f9f3#diff-38dc72994741420e2b6c5ee074941a45 (before)
    * Information disclosure by allowing attacker to read memory of a vulnerable system. Eavesdropping and data theft including passwords and content.
  * A large number of private encryption keys across the internet were publicly exposed.
  * Mitigation: recompile OpenSSL with the handshake removed from the code by compile time option -DOPENSSL_NO_HEARTBEATS
  * Only 1.0.1 and 1.0.2-beta releases were affected. Found by Google researchers:

  ```text
  Thanks for Neel Mehta of Google Security for discovering this bug and to
  Adam Langley <agl@chromium.org> and Bodo Moeller <bmoeller@acm.org> for
  preparing the fix.
  ```

  * https://openssl-library.org/news/secadv/20140407.txt

  * Detect with NMAP (ssl-heartbleed), exploit with Metasploit
    * https://nmap.org/nsedoc/scripts/ssl-heartbleed.html
    * https://svn.nmap.org/nmap/scripts/ssl-heartbleed.nse, https://pypi.org/project/ssltest/
    * Send some packets, check the response.

## Server Side Request Forgeries

* The server may mishandle badly formed or maliciously formed URLs.
* images, WebHooks, internal requests to interact with another server
* Mitigate with input validation, or regex string validation
* Trusted IP address

## sqlmap

* https://sqlmap.org/

## Recursion

* needs a base case, and a repeating calculation
* more intuitive, simpler code, more overhead with stack frames
* Fibonacci and Factorial

## Dynamic Programming

* Often used with recursion
* Breaking problems into sub-problems
* Memoization: storing the results for later use to save on computation speed at the expense of memory.

## Authentication

* Certificates
  * The PKI consists of a series of trusted Certificate Authorities who can say "yep! we trust that!"
  * https://www.cisa.gov/news-events/news/understanding-website-certificates
  * The web server providing the web page has a certificate, indicated by the https and the padlock.
  * Common Name (CN), Organization (O), and Organizational Unit (OU)
  * Name, Validity period, Fingerprints
    * Fingerprints include a certificate hash and a Public Key hash
    * X.509 connects an **identity** to a **public key** using a **digital signature**
    * The cert CONTAINS an identity and a public key.
    * Binary: .cer, .crt, .der, encoded in Base64
    * TexT: .pem  - Base64 encoded DER certs
    * PKCS#7 is the standard for siging (called enveloping) data

## Malware

### Conficker

* https://attack.mitre.org/software/S0608/
* (SANS) https://web.archive.org/web/20200125132645/https://www.sans.org/security-resources/malwarefaq/conficker-worm
* https://learn.microsoft.com/en-us/security-updates/SecurityBulletins/2008/ms08-067
* https://nvd.nist.gov/vuln/detail/CVE-2008-4250
* https://learn.microsoft.com/en-us/windows/win32/rpc/tutorial

Conficker was a virus discovered in 2008 that was able to infect a massive number of computers to create a botnet that could be used for further malicious purposes. The malware made use of a vulnerability in the Server service of certain versions of Microsoft Windows. The vulnerability allowed an attacker to submit a malformed RPC (remote procedure call) that causes a buffer overflow and allows remote execution.

Once an endpoint was infected, the virus patches the original vulnerability to ensure it cannot be infected again.

There was concern that compromised devices would execute a wide-spread attack on April 1, 2009, but that never occurred. (SANS)

In 2010 Symantec reported that Conficker variants A and B were still infecting 6.5 million machines. Variants called C, D, & E were also detected, but were found to be decrease or self-deleting.

#### Detections and Mitigations

* Monitoring new files copied to %systemroot%\system32
* Monitor for new services being registered
* Detect the following Registry entries:
  * HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\<name>.dll ImagePath = %SystemRoot%\system32\svchost.exe -k netsvcs
  * HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\netsvcs\Parameters\"ServiceDll" = "<name>.dll"
* Block traffic going out to sites like getmyip.org, getmyip.co.uk, and checkip.dyndns.org
* Block installation and execution of `ladadv.exe`, and traffic from `http://trafficconverter.biz`.
* Alert and block on scans for vulnerable machines (how are the scans done?)
* Shut of Computer Browser and Server services. Limited loss of functionality for the majority of users.
* Block RPC requests with UUID 4b324fc8-1670-01d3-1278-5a47bf6ee188 through a firewall.

### Morris Worm

* Internet's first worm
* Developed by Robert Morris Jr., Morris Sr. was a security researcher
* Travelled the early internet via Unix vulnerabilities
* https://en.wikipedia.org/wiki/Robert_Tappan_Morris
* https://www.fbi.gov/history/famous-cases/morris-worm

Morris was indicted, served 3 years probation and fined $10,200, then finished his PhD. a year later.

## More Structures

* Sets
  * Unordered, no duplicates. set() is a blank set, {'a','b','c'} is a set
* List comprehensions have for and if
* tuples
* sequence packing and unpacking

### Looping

* items() or enumerate
* reversed, sorted
* map()
  * apply a function/transformation to every element in a set:
  * ```Python
    values = ['34.3', '27.5', '3.14']
    data = map(int, values)
    print(list(data))
    ```
  * usually have to convert maps to lists
* lambda functions: anonymous functions - https://www.geeksforgeeks.org/python-lambda-anonymous-functions-filter-map-reduce/
* len works for basically everything. Maybe not maps?
