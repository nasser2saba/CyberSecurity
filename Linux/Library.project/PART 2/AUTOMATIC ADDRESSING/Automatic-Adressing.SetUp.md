
# configuring automatic addressing

`$ nmcli connecition modify <connection_name> ipv4.method auto 
`

replace connection name
to list available connections: 
`
$ nmcli connection show
`


edit network configuration file:
`
$ sudo nano /etc/network/interfaces`



Find the configuration for your network interface and ensure it's configured to use DHCP:

auto eth0
iface eth0 inet dhcp

save and restart : 
```
$ sudo systemctl restart networking
$ sudo systemctl status networking
```
