# Remote-Login-protocol
Interpretation of the project :
https://youtu.be/UE-pOjy_Uvg

Project : 

To enable a system administrator to access the shell of the server remotely, this protocol is proposed. Upon successful completion, provides the user with a remote shell.

Working :

Works with a fact that every organizations owns a website, that has a login for the employees. (Under an assumption, this website is strong)


        1. Employee logs into the website and acquires a number(0-13) and a image.
        2. Enters these into a python tool.
        3. In the backend, when the user enters the downloadpic page, a image is produced , stored in the backend and the backend fetches the integer stored for the respective employee.
        4. This number points to the index number of one of the Hash algorithms (hashlib.algorithms_guaranteed) to be used to hash this image and is stored in the database.
        5. Hence, using the number got from the website, the employee hashes the image and sends it to the server.
        6. And the server does the same and checks compatibility, if similar, offers a shell for the employee. 
        7. If not, terminated.

Files involved :

Backend  :  server.js, image.py, queries.sql, server.py

Frontend : login.html, downloadpic.html, script2.js, style1.css, client.py

The tool that the employee uses to get the remote shell - client.py

