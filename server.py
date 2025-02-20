#website server

import socket
import hashlib
import os
import subprocess
from time import sleep
import mysql.connector



# db connect

def db_connect(recv_id, todo):
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "ism",
        password = "password",
        database = "tcap"
    )
    cursor = mydb.cursor()
    print(recv_id)
    if (todo == 1):
        query = "SELECT algo FROM algo_map where id={};".format(recv_id)
        cursor.execute(query)
        results = cursor.fetchall()
        num = int(results[0][0])
    elif (todo == 2):
        query = "update algo_map set algo=algo+1 where id={};".format(recv_id)   ########################## 
        cursor.execute(query)
        mydb.commit()
        num = 'Done'
    cursor.close()
    mydb.close()
    return num


# get file from images folder and hash it


def hashing_image(num):
    algos = ['sha512', 'sha1', 'sha3_384', 'shake_128', 'shake_256', 'md5', 'sha384', 'sha3_256', 'sha3_224', 'sha224', 'sha3_512', 'blake2s', 'blake2b', 'sha256']
    excepts = ['shake_128', 'shake_256']
    file = r"C:\Users\USER\Downloads\ism\images\{}.png".format(recv_id)
    file = str(file)
    with open(file, "rb") as f:
        digest = hashlib.file_digest(f, algos[num])
    if (algos[num] in excepts):
        hashs = digest.hexdigest(32)
    else:
        hashs = digest.hexdigest()
    return hashs,recv_hash



# establish connection if hash matches


def connection(hashs,recv_hash,ids):
    if (hashs != recv_hash):
        print("no")
        #############reply to client for attacker possibilities
    else:
        path = r"C:\Users\USER\Downloads\ism\images\{}.png".format(ids)
        os.remove(path)
        num = db_connect(recv_id,2)
        print(num)      #################
        print("connection")
        while True:
            cmd = c.recv(1024).decode()
            sleep(1)
            if (cmd == 'exit' or cmd == 'Exit'):
                break
            else:
                print(cmd)
                output = subprocess.check_output(cmd, shell=True, text=True)    
                c.send(bytes(output,'utf-8'))
                sleep(1)




# receive hash from employee


s = socket.socket()		 
print ("Socket successfully created")
port = 12345			
s.bind(('', port))		 
print ("socket binded to %s" %(port)) 
s.listen(5)	 
print ("socket is listening")
while True:  
    c, addr = s.accept()	 
    print ('Got connection from', addr )########
    c.send('Enter your id  :  '.encode())
    recv_id = c.recv(1024).decode()
    c.send('Enter file path  : '.encode())
    recv_hash = c.recv(1024).decode()
    print('id',recv_id)
    print('hash',recv_hash)
    num = db_connect(recv_id,1)
    hashs,recv_hash = hashing_image(num)
    connection(hashs,recv_hash,recv_id)
    break



s.close()
c.close()
    
