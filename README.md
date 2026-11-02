
### Instructions to run the Client-Server python files locally

#### Server:
In the terminal, go to the directory that has the server file and type in:
```
python3 server.py
```

Once running, the server should ask to input  a host and port number (ex 8080). 

After inputting port the server listens for the client file. (CTRL C to terminate early)

ex
```python 
> python3 server.py
Enter a hostname: 
Enter a port number: 
Listening from 8080...
```

#### Client:
In the terminal, go to the directory of the client file and type:
```
python3 client.py
```

Input the ip address of the server (ex. 'localhost') followed by the server port number (ex. 8080). 

Once a connection is established, enter a message to get a reply. The server should reply the same message in uppercase.

Enter 'q' to disconnect as the message.

ex
```python
> python3 client.py
Server IP Address: localhost
Server Port: 8080
Enter a Message ('q' to Quit): hello
HELLO
Enter a Message ('q' to Quit): q
Closing socket ...
```

