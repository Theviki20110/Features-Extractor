import sys
import socket
import urllib3
import pandas as pd
import os


HOSTs=['10.0.1.2', '10.0.2.2', '10.0.3.2']
PORTs = [85, 86, 87]

n = int(sys.argv[1])
p = pd.read_csv('top500Domains.csv', sep=',')
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
http = urllib3.PoolManager()

s.bind((HOSTs[n], PORTs[n]))
s.listen()
while True:
    connection, client_addr = s.accept()
    child_pid = os.fork()
    if child_pid == 0:
        with connection as c:
            data = c.recv(1024).decode('utf-8')
            msg = data.split(' ')
            if p['Root Domain'].values[int(msg[1])].find('www.') == 0:
                url = 'http://' + p['Root Domain'].values[int(msg[1])]
            else:
                url = 'http://www.' + p['Root Domain'].values[int(msg[1])]
            print('url: ' + url)
            text = http.request('GET', url)   
            try:
                c.sendall(text.data)
            except:
                print("Closed by user")
        sys.exit()
