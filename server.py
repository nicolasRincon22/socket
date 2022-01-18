#server.py
import socket
import json
HOST = '127.0.0.1'
PORT=65432

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.bind((HOST,PORT))
    s.listen()
    print("[*] In ascolto su %s:%d"%(HOST,PORT))
    clientsocket, address=s.accept() # accetta la connessione del clientsocket
    with clientsocket as cs:
     print("Conessione da ",address)
     while True:
        data=cs.recv(1024)
        if not data: 
            break
        data=data.decode()
        data=json.loads(data)
        primoNumero=data['primoNumero']
        operazione=data['operazione']
        secondoNumero=data['secondoNumero']
        ris=""
        if operazione=="+":
            ris=primoNumero+secondoNumero
        elif operazione=="-":
            ris=primoNumero-secondoNumero
        elif operazione=="*":
            ris=primoNumero*secondoNumero
        elif operazione=="/":
          if secondoNumero==0:
              ris='Non puoi dividere per 0'
          else:
              ris=primoNumero/secondoNumero
        elif operazione=="%":
            ris=primoNumero%secondoNumero
        else:
            ris="Operazione non riconoscita"
        ris=str(ris)
        cs.sendall(ris.encode("UTF-8"))


