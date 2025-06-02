import socket
import os
import json
from cryptography.fernet import Fernet

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind(("localhost", 1234))

server_socket.listen(1)
print("server is listening......")

conn, addr = server_socket.accept()

data = conn.recv(1024)
decoded_data = data.decode()




try:
    client_data = json.loads(decoded_data)
    client_name = client_data["name"]
    client_key = client_data["key"]
except (ConnectionError, Exception) as e:
    print(e)


if not os.path.exists("to_server.json"):
    with open("to_server.json", "x") as file:
        json.dump({}, file)
else:
    pass


with open("to_server.json", "w") as file:
    json.dump({client_name:client_key}, file, indent=4)

with open("server_keys.json", "r") as file:
    server_key = json.load(file)

    if client_name in server_key and server_key[client_name] == client_key:
        succ_message = "welcome"
        conn.sendall(succ_message.encode())
    else:
        error_message = f"{client_name} was not found"
        conn.sendall(error_message.encode())
        conn.close()

print("connection closed")
conn.close()


