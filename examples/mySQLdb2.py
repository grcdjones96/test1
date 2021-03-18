#!/usr/bin/env python3
#Login to DB2 and configure mysql
#Davy Jones
#Feb 7, 2020

from pexpect import pxssh

# Connect to remote system
session = pxssh.pxssh()
session.login('192.168.0.122', 'justincase', 'Password01')
print('SSH login successful')

# Add apache2
#session.prompt()
session.sendline('sudo apt-get update')
session.prompt()
session.sendline('Password01')
session.prompt()
session.sendline('sudo apt-get install mysql')
session.prompt()
session.sendline('Y')
print('mysql installed')
#print(session.before)

# add user with password
session.sendline('sudo useradd -c "Ed Goad" edgoad')
#session.prompt()
session.sendline('sudo passwd edgoad')
#session.prompt()
session.sendline('RubberDuck!')
#session.prompt()
session.sendline('RubberDuck!')
print('user and password create')
#print(session.before)

# Configure to load mysql at restart
session.sendline('sudo systemctl enable mysql')
print('apache enabled')
#print(session.before)


# Logout
session.logout()