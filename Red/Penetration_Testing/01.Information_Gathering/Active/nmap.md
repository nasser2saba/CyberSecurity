# Nmap

Nmap (Network Mapper) is a network scanner created by Gordon Lyon (also known by his pseudonym Fyodor Vaskovich). Nmap is used to discover hosts and services on a computer network by sending packets and analyzing the responses.

Nmap provides a number of features for probing computer networks, including host discovery and service and operating system detection. These features are extensible by scripts that provide more advanced service detection, vulnerability detection, and other features. Nmap can adapt to network conditions including latency and congestion during a scan.

Source Wikipedia :  https://en.wikipedia.org/wiki/Nmap

## 1. Discover how nmap works by following this room on try hack me.

https://tryhackme.com/room/furthernmap

## 2. Connect to the vpn and use the 10.12.1.36 to answer the following questions:

Please save your answers. Your coaches may ask you for a copy of all your answers at the end of the challenge.

Ip : 10.12.1.36

1. How many tcp ports are open on the box? What command did you use?
    > Your response 28
    > command: `nmap  -p- 10.12.1.36`  

1. How many udp ports are open on the box? What command did you use?
    > Your response 8  
    > command `sudo nmap -sU 10.12.1.36`

1. What is the version of ftp?
    > Your response vsftpd 2.3.4

1. What is the version of ssh?
    > Your response OpenSSH 4.7p1 Debian 8ubuntu1

1. What is the version of Apache?
    > Your response Apache 2.2.8 

1. Is anonymous ftp access allowed on the box? What command did you use? (Use only nmap)
    > Your response Yes
    > command `nmap -p 21 --script ftp-anon 10.12.1.40`
    or `nmap -p 21 --script ftp-anon 10.12.1.36`

1. Do a SYN scan. Which command did you use?
    > Your response `sudo nmap -sS 10.12.1.36`
    or `nmap -sS --source-port 80 10.12.1.40`

1. Do a scan that bypasses a firewall. What command did you use?
    > Your response `sudo nmap -sS 10.12.1.36`
    or `nmap -sS --source-port 80 10.12.1.40`

1. Run a scan with the default NSE scripts. Which flag do you use?
    > Your response `nmap -sC 10.12.1.40 or nmap --script=default 10.12.1.40`

1. What service occupies port 8180?
    > Your response Apache-Coyote/1.1

1. What is the salt of the mysql service?
    > Your response E$%*E\}$8+mf9)a,WSw}
    > Command: `nmap -p 3306 --script mysql-info 10.12.1.36`

1. What is the domain name ?
1. What is the FQDN of the box ? 
1. What is the os version ? 
1. What is the version of Samba ?
1. Wat is the name of the box ?
> Command: `nmap -p 445 --script smb-os-discovery 10.12.1.36`
>Domain Name: localdomain
>Fully Qualified Domain Name (FQDN): metasploitable.localdomain
>Operating System Version: Unix (Samba 3.0.20-Debian)
>Samba Version: Samba 3.0.20-Debian
>Box Name: metasploitable

1. Do a scan on the subnet 10.xx.1.0/24. How many IP addresses respond?  What command did you use?
   Charleroi : 10.11.0.1/24
   Bruxelles : 10.12.0.1/24
   Ghent : 10.13.0.1/24
    > Your response 

1. Do the same thing but with the top port option at 10. What command did you use?
    > Your response 

