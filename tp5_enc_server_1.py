import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('', 13337))  

s.listen(1)
conn, addr = s.accept()

while True:

    try:
        data = conn.recv(2)
        if not data:break
        print(data)
        print(f"data rcv {data.decode()}")

        data = str(data.decode().strip())

        print(f"data |{data}|")

        # Evaluation et envoi du résultat
        res = eval(data)
        conn.send(str(res).encode())
    except socket.error:
        print("Error Occured.")
        break

conn.close()
