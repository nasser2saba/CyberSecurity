# setting up SSH 

install SSH Server: 
$ sudo apt update
$ sudo apt install openssh-server

configure SSH

ssh configuration file :  /etc/ssh/sshd_config 

$ sudo nano /etc/ssh/sshd_config
-> adjust setting based on your security requirements
this is what i did : 

1 Port
changing default ssh port (22) to a custom port
-> reduces nr of unauthorized login attempts

Port 222

2 Permit Root Login: 
disable root login via SSH for added security 

PermitRootLogin no 

3 passw authentication 

disable passw authentication & enforce SSH key-based authentication 
-> more secure 

PasswordAuthentication no 

4 AllowUsers/groups

specifying the users or groups allowed to log in via SSH 

AllowUsers librarian1 librarian2 

5 Max authentication attemps

MaxAuthTries 3

6 Protocol:
Specify the SSH protocol version. It's recommended to use version 2, which is more secure.

Protocol 2


after you're done adjusting :

$ sudo systemctl restart sshd
$ sudo systemctl status sshd