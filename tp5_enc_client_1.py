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
        print(f"yo {encoded_msg}")
    else:
        print("Erreur : Les nombres doivent être entre -1048575 et +1048575.")
else:
    print("Erreur : Format incorrect. Utilisez la forme 'x opérateur y' avec +, -, ou *.")

# On envoie
# s.send(msg.encode())

# Réception et affichage du résultat
s_data = s.recv(1024)
print(s_data.decode())
s.close()
