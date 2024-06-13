# Configuring Firewall


ensuring firewall rules allows necessary trafic ( DHCP, DNS, HTTP,MARIADB)


To ensure that the firewall allows necessary traffic for DHCP, DNS, HTTP, and MariaDB, you'll need to configure your firewall settings accordingly.
1. **Check UFW Status**:
   First, check if `ufw` is installed and its current status:

   
   $ sudo ufw status


2. **Allow Necessary Traffic**:
   Based on the services you're running:

   - **DHCP**: DHCP uses UDP port 67. Allow incoming UDP traffic on port 67:

  
    $ sudo ufw allow 67/udp


   - **DNS**: DNS typically uses UDP and TCP ports 53. Allow both UDP and TCP traffic on port 53:

   
   $  sudo ufw allow 53
   $ sudo ufw allow 53/tcp
   $ sudo ufw allow 53/udp
   

   - **HTTP**: HTTP uses TCP port 80. Allow incoming TCP traffic on port 80:

   
   $  sudo ufw allow 80/tcp
    

   - **MariaDB**: MariaDB uses TCP port 3306. Allow incoming TCP traffic on port 3306:

    
    $ sudo ufw allow 3306/tcp
    

3. **Enable UFW**:
   Once you've allowed the necessary traffic, enable `ufw`:

  
  $ sudo ufw enable
   

4. **Verify Changes**:
   You can verify the changes you've made:


$  sudo ufw status


   This should show the updated firewall rules allowing traffic for DHCP, DNS, HTTP, and MariaDB.