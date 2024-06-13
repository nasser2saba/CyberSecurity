

#		Weekly Backup for Configuration Files

~create a weekly backup of configuration files for each service and compress them into a single archive~


Create Backup Script:

Create a bash script to backup the configuration files.for example) backup_config.sh.
you can put the script in any directory you want, most scripts tho, are put in the directory
/usr/local/bin 
or /opt/scripts

$ cd /usr/local/bin
$ sudo touch backup_config.sh

$ sudo nano backup_config.sh

#!/bin/bash

# Define backup directory
BACKUP_DIR="/path/to/backup"

# Create directory if it doesn't exist
mkdir -p "$BACKUP_DIR"

# Backup DHCP configuration
cp /etc/dhcp/dhcpd.conf "$BACKUP_DIR/dhcpd.conf"

# Backup DNS configuration
cp /etc/bind/named.conf.local "$BACKUP_DIR/named.conf.local"
cp /etc/bind/db.<your_domain> "$BACKUP_DIR/db.<your_domain>"

# Backup Apache or Nginx configuration
cp /etc/apache2/apache2.conf "$BACKUP_DIR/apache2.conf"  # if using Apache
# cp /etc/nginx/nginx.conf "$BACKUP_DIR/nginx.conf"      # if using Nginx

# Backup MariaDB configuration
cp /etc/mysql/my.cnf "$BACKUP_DIR/my.cnf"

# Compress backup directory
tar -czf "$BACKUP_DIR/backup_$(date +'%Y%m%d').tar.gz" -C "$(dirname $BACKUP_DIR)" "$(basename $BACKUP_DIR)"


Make sure to replace <your_domain> with your actual domain name in the script.
and replace /path/to/backup
with the actually path to your backup file :)

Make Script Executable:
$ chmod +x backup_config.sh


Test Backup Script:
$ ./backup_config.sh

return :
"tar: backup: file changed as we read it 

Schedule Weekly Backup:

Use cron to schedule the script to run weekly. Open cron jobs for editing
$ crontab -e

Add the following line to run the backup script every Sunday at midnight
 0 0 * * 0 /path/to/backup_config.sh

Save and exit the editor.