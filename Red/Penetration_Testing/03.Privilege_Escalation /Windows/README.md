# Windows Privilege escalation 
Make the 2 rooms of tryhackme which are free: 

1. https://tryhackme.com/room/windows10privesc
1. https://tryhackme.com/room/windowsprivescarena


Then do the following exercises:  

1. [Recon](./readme.md)
1. [Exploits](./Exploit.md)

## Recon
Once again, the first thing to do when you want to elevate your privilege is to proceed with a recognition step. 

Here are some questions you should ask yourself before undertaking elevation of privilege right. 

1. What is the username? 
1. What group do you have? 
1. What other users have?
1. What is the hostname ?
1. What is the OS version?
1. What is the ip ?
1. What are the routes? 
1. What are the connections on a system?
1. Are there any rules for the firewall?
1. Are there any scheduled tasks?
1. What are the versions of the installed packages?
1. Which files and directories have write and read permissions?
1. Are there any hard drives or mounted directories?
1. Are there any kernel modules?
1. Is there a MSI file that can change the suid rights?


**Enumerating Users**  
What is the username? 
```powershell
whoami
```
```powershell
net user USERNAME
```

If you are `LOCAL SERVICE` or `NETWORK SERVICE`, you can check this : https://github.com/itm4n/FullPowers


What privilege do you have? 
```powershell
net user USERNAME /priv
```

What other users have?
```powershell
net user 
```

**Enumerating the Hostname**  
What is the hostname ?
```powershell
hostname
```


**Enumerating the Operating System Version and Architecture**  
What is the OS version ? 
````powershell
systeminfo | findstr /B /C:"OS Name" /C:"OS Version" /C:"System Type"
````

**Enumerating Networking Information**  
What is the ip ?
````cmd
ipconfig
````
What are the routes? 
````cmd
route print
````
What are the connections on a system?
````cmd
netstat -ano
````

**Enumerating Firewall Status and Rules**  
Are there any rules for the firewall?
````cmd
netsh advfirewall show currentprofile
````

````cmd
netsh advfirewall firewall show rule name=all
````

**Enumerating Scheduled Tasks**  
Are there any scheduled tasks?
```cmd
schtasks /query /fo LIST /v
```

**Enumerating Readable/Writable Files and Directories**  
Which files and directories have write and read permissions?
````cmd
accesschk.exe -uws "Everyone" "C:\Program Files"
````

````powershell
#Powershell
Get-ChildItem "C:\Program Files" -Recurse | Get-ACL | ?{$_.AccessToString -match "Everyone\sAllow\s\sModify"}
````

**Enumerating Unmounted Disks**  
Are there any hard drives or mounted directories?
````
mountvol
````


**Enumerating Device Drivers and Kernel Modules**  
Are there any kernel modules?
````powershell
#powershell
driverquery.exe /v /fo csv | ConvertFrom-CSV | Select-Object 'Display Name', 'Start Mode', Path
````

````powershell
#powershell
Get-WmiObject Win32_PnPSignedDriver | Select-Object DeviceName, DriverVersion, Manufacturer | Where-Object {$_.DeviceName -like "*VMware*"}
````

**Enumerating MSI That AutoElevate**  
Is there a MSI that can change the suid rights?
````cmd
reg query HKEY_CURRENT_USER\Software\Policies\Microsoft\Windows\Installer
````

````cmd
reg query HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\Installer
````

If this setting is enabled, we could craft an MSI file and run it to elevate our privileges
````diff
+ AlwaysInstallElevated REG_DWORD 0x1
````

## Add ressources
- https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation
- https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Windows%20-%20Privilege%20Escalation.md
- https://sushant747.gitbooks.io/total-oscp-guide/content/privilege_escalation_windows.html