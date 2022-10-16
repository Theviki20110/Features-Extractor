from random import randint
import os
import sys

oid = randint(1, 396)

#Needs manager-agent configuration
user = sys.argv[1]
password = sys.argv[2]
mibwalk = 'snmpwalk -u ' + user + '-l authPriv -a MD5 -x DES -A ' + password + '-X ' + password

with open("MIBclean.txt", "r") as f:
        for i in range(0, oid - 1):
            command = f.readline()
        
        command = f.readline()
        
#Lauch command
os.system(mibwalk + sys.argv[1] + ' ' + command[:-1])