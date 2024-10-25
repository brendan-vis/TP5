import socket
import re

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# # s.connect(('10.1.1.11', 13337))
s.connect(('192.168.1.87', 13337))

# Récupération d'une string utilisateur
msg = input("Calcul à envoyer: ")

motif = r"^\s*(-?\d{1,7})\s*([\+\-\*\/])\s*(-?\d{1,7})\s*$"
match = re.match(motif, msg)
if match:
    nombre1 = int(match.group(1))
    operateur = match.group(2)
    nombre2 = int(match.group(3))
    if -1048575 <= nombre1 <= 1048575 and -1048575 <= nombre2 <= 1048575:
        print(f"Expression valide : {nombre1} {operateur} {nombre2}")
match operateur:
    case "+":
        operateur = 0
    case "-":
        operateur = 1
    case "*":
        operateur = 2
    case "/":
        operateur = 3

shifted_operateur = operateur << 22


if nombre1 < 0:
    nombre1bin = 0
if nombre2 < 0:
    nombre2bin = 0
if nombre1 > 0:
    nombre1bin = 1
if nombre2 > 0:
    nombre2bin = 1

shifted_nombre1 = nombre1bin << 21
shifted_nombre2 = nombre2bin << 20

shifted1 = shifted_nombre1 | shifted_operateur | shifted_nombre2 | nombre1
print(shifted1)
shifted2 = nombre2
shifted = shifted1.to_bytes(3, byteorder='big') + shifted2.to_bytes(3, byteorder='big')
print(shifted)


# On envoie
s.send(shifted)

# # Réception et affichage du résultat
s_data = s.recv(1024)
print(s_data.decode())
s.close()
