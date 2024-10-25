import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('', 13337))  

s.listen(1)
conn, addr = s.accept()

while True:

    try:
        # On reçoit le calcul du client
        nb1 = conn.recv(3)
        nb2 = conn.recv(3)
        if not nb1: break
        print(f"Données reçues du client : {nb1}")

        if not nb2: break
        print(f"Données reçues du client : {nb2}")

        nb1 = int.from_bytes(nb1, byteorder='big')
        nb2 = int.from_bytes(nb2, byteorder='big')

        print(f"Nombre 1 reçu (int) : {nb1}")
        print(f"Nombre 2 reçu (int) : {nb2}")

        nb1_binaire = bin(nb1)[2:]  # [2:] pour retirer le préfixe '0b'
        nb2_binaire = bin(nb2)[2:]

        print(f"Nombre 1 en binaire : {nb1_binaire}")
        print(f"Nombre 2 en binaire : {nb2_binaire}")
        
        # Evaluation et envoi du résultat
        # res  = eval(data.decode())
        # conn.send(str(res).encode())
         
    except socket.error:
        print("Error Occured.")
        break

conn.close()
