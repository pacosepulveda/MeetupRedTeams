#!/usr/bin/env python
# Paco Sepúlveda
# Script básico para escanear puertos desde Python usando sockets

from threading import Thread
import socket
host = "wpdemomeetup.eastus2.cloudapp.azure.com"
puerto_inicial = 20
puerto_final = 80   
puertos_abiertos = []
puertos_cerrados = []
threads = []

def scan(port):
    s = socket.socket()
    s.settimeout(3)
    result = s.connect_ex((host,port))
    print('probando el puerto > '+(str(port)))      
    if result == 0:
        puertos_abiertos.append(port)
        print ("-" * 60)
        print((str(port))+' -> abierto')
        print ("-" * 60)
        s.close()
    else:
        puerto_cerrados.append(port)
        s.close()

for i in range(puerto_inicial, puerto_final+1):
    t = Thread(target=scan, args=(i,))
    threads.append(t)
    t.start()

[x.join() for x in threads]

print('Los puertos que hemos encontrado abiertos son > ' + (str(puertos_abiertos)))
