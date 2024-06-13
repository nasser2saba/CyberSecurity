

# errors & how i fixed them 

apache2 

i configured apache2, when i do this command: sudo systemctl status apache , everthing is active  (running) but this message is shown below: 
"apache2 couldn't reliably determine the server's fully qualified domain name , using 127.0.1.1 set the ' servername' directive globally to surpress this message"

--> Apache2 is using a default server name because it couldn't identify the FQDN of my server.


$ sudo nano /etc/apache2/apache2.conf

added this : 
ServerName library.com


then restarted server
$ sudo systemctl restart apache2

to test if it works
go on browser 
type either : 


http://example.com
or
http://ip_address

for example

http://library.com or http://10.0.2.15