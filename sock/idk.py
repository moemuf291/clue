import os
import socket
import json
from datetime import datetime


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind(("localhost", 1234))

server_socket.listen(1)
print("server listening.....")


conn, addr = server_socket.accept()

if not os.path.exists("server_data.json"):
    with open("server_data.json", "w") as file:
        json.dump({}, file)


try:
    while True:
        data = conn.recv(1024)

        if not data:
            break
        print(f"{data.decode()}")

        
        try:
            with open("server_data.json", "r") as file:
                get_data = json.load(file)


                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                get_data[timestamp] = data.decode()

                message_sve = "data was saved to file"
                conn.sendall(message_sve.encode())


                with open("server_data.json", "w") as file:
                    json.dump(get_data, file, indent=4)

        except (FileNotFoundError, Exception) as e:
            print(e)
            message = "failed to get data"
            conn.sendall(message.encode())
finally:
    print("connection eneded")
    conn.close()    
