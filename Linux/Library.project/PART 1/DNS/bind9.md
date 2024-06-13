


# Configuring DNS bind9

I've documented 2 ways to configure the DNS server, basically after configuring the DNS server the first time, out of curiousity ended up restarting from 0 to see the differences in outcome...
just to end up with the same outcome .


I'll be mentioning both configuration methods, method 1 is the easier one:
The one i've got currently running is method 2, so i don't remember all the things i filled in method 1 but i'll make it up for you with a smiley :)



# METHOD 1 - Configuring DNS - bind9

configuring dns - bind9: 

install necessary packages: 
$ sudo apt install bind9

configur BIND:

$ sudo nano /etc/bind/named.conf.local 
(or vim)

zone "<your_domain>" {
    type master;
    file "/etc/bind/db.<your_domain>";
};

my domain = library.com




create a zone file : 
$ touch db.<domain_name>

( $ touch library.com.db )

and add following code: 


; Zone file for example.org
$TTL 1h
@       IN      SOA     ns1.example.org. admin.example.org. (
                        2022040201      ; Serial
                        1d              ; Refresh
                        2h              ; Retry
                        1w              ; Expire
                        1h )            ; Minimum TTL

; Name servers
        IN      NS      ns1.library.com
        IN      NS      ns2.library.com

; Define hostname to IP address mappings for internal resources
ns1     IN      A       10.0.2.200
ns2     IN      A       10.0.2.201

; Additional hostnames for internal resources
www     IN      A       10.0.2.3
mail    IN      A       10.0.2.4

; Redirector for external resources
*       IN      A       10.0.2.x ( forgot :) )




After saving the changes, you can verify the syntax of your BIND configuration to ensure there are no errors:
$ sudo named-checkconf

dont forget to make sure that your file is in the right directory: 
/etc/bind/example.org
$ mv /current/path/to/db.example.org /etc/bind/

which was /etc/bind/db.library.com


Finally, restart the BIND service to apply the changes:
$ sudo systemctl restart bind9

to check that it's working: 
$ sudo systemctl status bind9

and
$ dig @localhost library.com
$ dig library.com


for troubleshooting: 
$ dig +trace @localhost library.com


--------------------------------------------------------------------------------------------------------------------------------------
							Method nr 2 
--------------------------------------------------------------------------------------------------------------------------------------


dns bind9

install necessary packages: 
$ sudo apt install 
$ sudo apt-get install bind9 bind9utils bind9-doc dnsutils


configuring dns bind9:

configuration directory of bind9 is /etc/bind/
global configuration used for local dns is /etc/bind/named.conf.local


creating zones: 

$ sudo nano /etc/bind/named.conf.local
u can use vim instead


zone "<your_domain>" IN { // Domain name

    type master; // Primary DNS

    file "/etc/bind/<your_domain>.db"; // Forward lookup file
    
    allow-update { none; }; // Since this is the primary DNS, it should be none.

};


my domain = library.com


library.com.db
<your_domain>.db = name of your forward lookup zone
reverse ip : f.e) your ip = 192.168.1, reverse ip = 1.168.192



reverse ip (2.0.10)

zone "<reverse.ip>.in-addr.arpa" IN { //Reverse lookup name, should match your network in reverse order

     type master; // Primary DNS

     file "/etc/bind/reverse.<your_domain>.db"; //Reverse lookup file
 allow-update {none; }; //Since this is the primary DNS, it should be none.

};



configure bind dns zone lookup files:

to create the forward zone lookup file , we'll copy the sample zone lookup file
$ sudo cp /etc/bind/db.local /etc/bind/<your_domain>.db

Remember that there is syntax, and domain names end with a dot (.)

Also, there are acronyms that we need to understand.

SOA – Start of Authority
A – A record
MX – Mail for Exchange
NS – Name Server
CN – Canonical Name


Edit the zone file: 
$sudo nano /etc/bind/<your_domain>.db


$TTL    604800
@       IN      SOA     ns1.library.com. root.ns1.library.com. (
                              3		; Serial
                         604800         ; Refresh
                          86400         ; Retry
                        2419200         ; Expire
                         604800 )       ; Negative Cache TTL
;
;@      IN      NS      localhost.
;@      IN      A       10.0.2.1
;@      IN      AAAA    ::1

;Name Server Information

@        IN      NS      ns1.library.com.

;IP address of Name Server

ns1     IN      A       10.0.2.2

;Mail Exchanger

<your_domain>.   IN     MX   10   mail.library.com.

;A – Record HostName To Ip Address

www     IN       A      10.0.2.3
mail    IN       A      10.0.2.4

;CNAME record

ftp     IN      CNAME   www.library.com


copy the sample reverse zone file in /etc/bind called reverse.library.com.db
$ sudo cp /etc/bind/db.127 /etc/bind/reverse.library.com.db



Edit the contents of the file:
$ sudo nano /etc/bind/reverse.library.com.db


;
; BIND reverse data file for local loopback interface
;
$TTL    604800
@       IN      SOA     <your_domain>. root.<your_domain>. (
                              3         ; Serial
                         604800         ; Refresh
                          86400         ; Retry
                        2419200         ; Expire
                         604800 )       ; Negative Cache TTL
;

;Name Server Information

@       IN      NS     ns1.library.com.
ns1     IN      A       10.0.2.2
;Reverse lookup for Name Server

2      IN      PTR    ns1.library.com.

;PTR Record IP address to HostName

3     IN      PTR    www.library.com.
4     IN      PTR    mail.library.com.


check bind dns syntax:

$ sudo named-checkzone library.Ccom /etc/bind/library.com.db
zone <your_domain>/IN: loaded serial 3
OK
                        (reverse.ip = 2.0.10)
$ sudo named-checkzone <reverse.ip>.in-addr.arpa /etc/bind/reverse.library.com.db
zone 2.0.10.in-addr.arpa/IN: loaded serial 3
OK


reverse ip (2.0.10)


Restart and enable the BIND DNS server:

$sudo systemctl restart bind9
$sudo systemctl enable bind9


Check the status of the service:
$ systemctl status bind9


$ dig www.<your_domain>

Test Bind DNS Server on client machine:
$sudo vim /etc/resolv.conf
add dns server ip

nameserver 10.0.2.xxx