
# AD Windows Project

## Info 
to run server configuration tool :

sConfig



Promote the Domain Controller VM to a domain controller.:
Install-WindowsFeature -Name AD-Domain-Services -IncludeManagementTools


serverpool :
10.0.2.15

root domain name: 
windows.server.local
192.168.0.1


Domain Service Restore Mode Password: 
SssLll&06DSRM


 NetBIOS domain name:
 WINDOWS



 Database folder: C:\Windows\DB
 Log files folder: C:\Windows\LOG
 SYSVOL folder: C:\Windows\SYSVOL


OU's:
- Organizational Unit Head
- Middle Class 
- Peasants


 ## Promoting a domain controller VM 

 
> Promote the Domain Controller VM to a domain controller.
> Create a new Active Directory forest and domain structure.
> Configure DNS service on the Domain Controller VM.


1. **Install Active Directory Domain Services (AD DS)**:
   - Go to the Server Manager dashboard.
   - Click on "Add roles and features".
   - Select "Role-based or feature-based installation".
   - Choose the appropriate server from the server pool.
   - Select "Active Directory Domain Services" from the list of roles.
   - Follow the wizard to complete the installation.

2. **Promote the Server to a Domain Controller**:
   - After installing AD DS, a notification will appear in Server Manager. Click on it to start the Active Directory Domain Services Configuration Wizard.
   - In the wizard, select "Add a new forest" if this is the first domain controller in a new forest. Otherwise, choose "Add a domain controller to an existing domain".
   - Enter the fully qualified domain name (FQDN) for the forest root domain.
   - Set the Forest Functional Level and Domain Functional Level as appropriate for your environment.
   - Choose a Directory Services Restore Mode (DSRM) password.
   - Review the NetBIOS domain name, and if necessary, change it.
   - Specify the paths for the AD DS database, log files, and SYSVOL folder, or accept the default paths.
   - Review the options on the Review Options page, and then click Next.
   - The wizard will run prerequisite checks. If any issues are found, resolve them before proceeding.
   - Click Install to promote the server to a domain controller.


   - After the promotion process completes, the VM will automatically restart.

3. **Verify Promotion**:
   - Log in to the VM using domain administrator credentials.
   - Open Server Manager and verify that Active Directory Domain Services is listed under Roles and that the server is listed as a domain controller.
   - Use Active Directory Users and Computers or other appropriate tools to verify that the domain controller is functioning correctly.




> Create organizational units (OUs) for user and group management.



1. **Open Active Directory Users and Computers**:
   - Log in to the server where Active Directory Domain Services (AD DS) is installed.
   - Open Server Manager.
   - Click on "Tools" in the top-right corner.
   - Select "Active Directory Users and Computers" from the dropdown menu.

2. **Navigate to the Domain**:
   - In Active Directory Users and Computers, expand the domain node in the left pane to view the organizational structure of the domain.

3. **Create an Organizational Unit**:
   - Right-click on the domain node or an existing OU where you want to create the new OU.
   - Select "New" -> "Organizational Unit".
   - Enter a name for the new OU and click "OK".

4. **(Optional) Organize OUs into a Hierarchy**:
   - You can create multiple levels of OUs to build a hierarchical structure for organizing objects within your domain.
   - To create an OU within an existing OU, right-click on the parent OU, select "New" -> "Organizational Unit", and specify a name for the new OU.

5. **Move Objects into the OUs**:
   - Once you've created OUs, you can move users, groups, computers, and other objects into them to organize your Active Directory environment effectively.
   - To move an object, simply drag and drop it from its current location to the desired OU in Active Directory Users and Computers.

6. **Verify the OU Structure**:
   - After creating and organizing OUs, you can verify the OU structure by refreshing Active Directory Users and Computers and ensuring that the OUs are displayed in the desired hierarchy.



## Configuring network


On VM:
Click on machine 
- Go to network 
Attached to > select internal network 
Advanced > Promiscous mode > Select allow all

Do that on all related machines 

configuring ip add: 
 in search bar type ncpa.cpl
 Left click on Ethernet > Properties > Internet Protocol Version 4 > Properties 
 put ip address in and subnet mask, & make preffered dns server the same ip address as 



## DHCP

Scope Name: WINDOWZIPv4

![alt text](image.png)




Wasn't able to add client through dhcp, 
configured it manually 
added ip address inside of range
ip address 192.168.0.51
subnet mask 255.255.255.0
default gateway  192.168.0.1
(preferred) domein server 192.168.0.1
(alternative) domein server 8.8.8.8
and it worked , now i can add the client vm to the domain 

## Adding client to domain 

Control panel > System and Security > System > advanced system settings > change 
input domain name 
enter username and password
you're added to the domain 



## Adding OU's & Users

server manager > tools > Active Directory Users and Computer 

Left click on the server > New > Organizational Unit 


Left Click on wanted OU > New > User

Add the Users you desire 



