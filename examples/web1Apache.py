#!/usr/bin/env python3
#Login to Web1 and configure apache2
#Davy Jones
#Feb 7, 2020

from pexpect import pxssh

# Connect to remote system
session = pxssh.pxssh()
session.login('192.168.0.111', 'justincase', 'Password01')
print('SSH login successful')

# Add apache2
#session.prompt()
session.sendline('sudo apt-get update')
session.prompt()
session.sendline('Password01')
session.prompt()
session.sendline('sudo apt-get install apache2')
session.prompt()
session.sendline('Y')
print('apache2 installed')
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

# Configure to load apache2 at restart
session.sendline('sudo systemctl enable apache2')
print('apache enabled')
#print(session.before)


# Logout
session.logout()