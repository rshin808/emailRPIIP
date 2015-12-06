# emailRPIIP
This copies the output of "ifconfig" into "IPADDRESS.txt", and it sends the information to an email.  
It can be used to email the IPAddress of the RPI on reboot.  

# Running on startup  
1)  Become a super user with "sudo su".    
2)  Edit the "/etc/rc.local" file.  
    Make sure that the path is correct.
```
#!/bin/sh -e
#
# rc.local
#
# This script is executed at the end of each multiuser runlevel.
# Make sure that the script will "exit 0" on success or any other
# value on error.
#
# In order to enable or disable this script just change the execution
# bits.
#
# By default this script does nothing.

# Email IP
python /home/pi/emailIP/emailIP.py &

# Print the IP address
_IP=$(hostname -I) || true
if [ "$_IP" ]; then
  printf "My IP address is %s\n" "$_IP"
fi

exit 0
```
