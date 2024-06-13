
#

#
#                          The Library Project 

### After 7843 hours of linux 
### 1564 hours of youtube, chatgpt, text docs
### and 7 bowls of ice cream

I can finally present this project to you. 


#
## CONTENT: 

Part 1:
  - DHCP configuration
  - DNS bind9 configuration
  - HTTP + MariaDB apache2 configuration
  - Weekly backup configuration
  - Configuring Firewall
  - SSH configuration

Part 2: 
  - LibreOffice
  - Gimp
  - Mullvad
  - Configuring automatic addressing
  - Seperate Partition


In every folder, you'll find a 'support' file , documented with the errors ive encountered , how i fixed them, extra tips and whatever else. 

#
#

!!!!!!!! REALLY IMPORTANT SHORT VIDEO MUST WATCH !!!!!!!!
https://www.youtube.com/watch?v=dQw4w9WgXcQ





#
#
#

## Project Context

The local library in your little town has no funding for Windows licenses so the director is considering Linux. Some users are sceptical and ask for a demo. The local IT company where you work is taking up the project and you are in charge of setting up a server and a workstation.
To demonstrate this setup, you will use virtual machines and an internal virtual network (your DHCP must not interfere with the LAN).

You may propose any additional functionality you consider interesting.

## Must Have

Set up the following Linux infrastructure:

1. One server (no GUI) running the following services:
    - DHCP (one scope serving the local internal network)  isc-dhcp-server
    - DNS (resolve internal resources, a redirector is used for external resources) bind
    - HTTP+ mariadb (internal website running GLPI)
    - **Required**
        1. Weekly backup the configuration files for each service into one single compressed archive
        2. The server is remotely manageable (SSH)
    - **Optional**
        1. Backups are placed on a partition located on  separate disk, this partition must be mounted for the backup, then unmounted

2. One workstation running a desktop environment and the following apps:
    - LibreOffice
    - Gimp
    - Mullvad browser
    - **Required** 
        1. This workstation uses automatic addressing
        2. The /home folder is located on a separate partition, same disk 
    - **Optional**
        1. Propose and implement a solution to remotely help a user
