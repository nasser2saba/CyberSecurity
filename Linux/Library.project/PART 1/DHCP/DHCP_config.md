# Configuring DHCP server

Many people used kea, unlike me I worked with isc-dhcp-server
Apparently isc-dhcp-server isn't managed anymore but it still works and did the job so :)

first, updating & uprading everything: 
$ sudo apt update && sudo apt upgrade



$ sudo apt install isc-dhcp-server
--> installing necessary packages for dhcp service


checked my ip address & name of interface: 
$ ip a 
 name of interface is written after 2: ( next to <BROADCAST,MULTICAST,UP,LOWER_UP>) and ip address is written 3 lines under it 
10.0.1.x
enp0s3


start & enable dhcp server: 
$ sudo systemctl start isc-dhcp-server
$ sudo systemctl enable isc-dhcp-server 

configured dhcp server: 

$ sudo nano /etc/default/isc-dhcp-server
or 
$ sudo vim /etc/default/isc-dhcp-server

at the end of the file, you'll see "interfacesv4" , add your interface (check $ ip a  command )
my interface= enp0s3


edit the DHCP configuration file :
$ sudo nano /etc/dhcp/dhcpd.conf


option domain-name "library.com";
option domain-name-servers ns1.library.com

default-lease-time 600;
maximum-lease-time 7200;

ddns-update-style none;



subnet 10.0.2.0 netmask 255.255.255.0 {
    range 10.0.2.10 10.0.2.250;
    option routers 10.0.2.1;
    option domain-name-servers ns1.library.com;
    option domain-name library.com;
    option broadcast-address 10.0.2.255;
    option subnet-mask 255.255.255.0;
    default-lease-time 600;
    maximum-lease-time 7200;

}


then restart the dhcp server with this command:
$ sudo systemctl restart isc-dhcp-server


to verify that it's running without errors: 
$ sudo systemctl status isc-dhcp-server

to check dhcp server logs for any potential issues: 
$ sudo journalctl -u isc-dhcp-server



I followed instruction w this video: 

https://www.youtube.com/watch?v=1csFmQeXHlg

and double checked everything with chatgpt

for troubleshooting: 
$ sudo named-checkconf /etc/dhcp/dhcpd.conf

-> named-checkconf command = life saver