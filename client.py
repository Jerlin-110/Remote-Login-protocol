### employee side script

import sys
import hashlib
import socket
from time import sleep




# sending hash to server
s = socket.socket()          
port = 12345                
s.connect(('127.0.0.1', port))
    ###########


print(s.recv(1024).decode())   ####enter id
ids = input()
s.send(str(ids).encode())
print(s.recv(1024).decode())
file = input()
 





# generating hash digest

algos = ['sha512', 'sha1', 'sha3_384', 'shake_128', 'shake_256', 'md5', 'sha384', 'sha3_256', 'sha3_224', 'sha224', 'sha3_512', 'blake2s', 'blake2b', 'sha256']
excepts = ['shake_128', 'shake_256']

file = str(file)
num =  int(sys.argv[1])

with open(file, "rb") as f:
    digest = hashlib.file_digest(f, algos[num])
if (algos[num] in excepts):
    hashs = digest.hexdigest(32)
else:
    hashs = digest.hexdigest()


s.send(hashs.encode())
print('id',ids)
print('hash',hashs)





# open netcat connection




def listen():
        print(s.recv(1024).decode())
        sleep(1)


def send():
        cmd = input("Enter command  :  ")    
        s.send(bytes(cmd,'utf-8'))
        if (cmd == 'exit'):
            return 0
        sleep(1)


while True:
    val = send()
    if (val == 0):
        break
    listen()

s.close()




