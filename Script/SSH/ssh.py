from random import randint
import os
import sys

#randint(1, n° rows in commands.txt)
number = randint(1,21)
target = sys.argv[1]
password = sys.argv[2]

#sshpass needs target's password
openssh = 'sshpass -p'+ password + ' ssh '+ target +'@' + sys.argv[1]

with open("commands.txt", "r") as f:
            
    #Iterate until reach selected command
    for lines in range(0, number-1):
            f.readline()
    command = f.readline()
    
os.system(openssh + ' ' + command[:-1])