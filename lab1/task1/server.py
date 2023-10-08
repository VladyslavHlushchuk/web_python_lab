import socket
import time

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1', 12345))
server_socket.listen(5)

print("Сервер слухає на порту 12345...")

while True:
    client_socket, client_address = server_socket.accept()
    print(f"З'єднано з {client_address}")

    data = client_socket.recv(1024).decode()
    print(f"Отримано: {data}")

    # Затримка на сервері на 5 секунд
    time.sleep(5)

    # Перевірка, чи відправлені всі дані
    if data:
        response = f"Сервер отримав: {data}\nВсі дані успішно відправлені"
    else:
        response = "Дані не були відправлені"

    client_socket.send(response.encode())
    client_socket.close()
