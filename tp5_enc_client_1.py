import socket
import re

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('10.1.1.11', 13337))
s.send('Hello'.encode())

# On reçoit la string Hello
data = s.recv(1024)

# Récupération d'une string utilisateur
msg = input("Calcul à envoyer: ")

motif = r"^\s*(-?\d{1,7})\s*([\+\-\*])\s*(-?\d{1,7})\s*$"
match = re.match(motif, msg)
if match:
    nombre1 = int(match.group(1))
    operateur = match.group(2)
    nombre2 = int(match.group(3))
    if -1048575 <= nombre1 <= 1048575 and -1048575 <= nombre2 <= 1048575:
        print(f"Expression valide : {nombre1} {operateur} {nombre2}")
        encoded_msg = msg.encode('utf-8')

        # on calcule sa taille, en nombre d'octets
        msg_len = len(encoded_msg)

        # on encode ce nombre d'octets sur une taille fixe de 4 octets
        header = msg_len.to_bytes(4, byteorder='big')

        # on peut concaténer ce header avec le message, avant d'envoyer sur le réseau
        payload = header + encoded_msg

        # on peut envoyer ça sur le réseau
        sock.send(payload)
    else:
        print("Erreur : Les nombres doivent être entre -1048575 et +1048575.")
else:
    print("Erreur : Format incorrect. Utilisez la forme 'x opérateur y' avec +, -, ou *.")

# On envoie
s.send(msg.encode())

# Réception et affichage du résultat
s_data = s.recv(1024)
print(s_data.decode())
s.close()
