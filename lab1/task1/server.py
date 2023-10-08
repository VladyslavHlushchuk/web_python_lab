import socket
import datetime

# Створення TCP-сервера
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1', 12345))  # Підключення до локальної адреси на порту 12345
server_socket.listen(5)  # Очікування до 5 клієнтів одночасно

print("Сервер слухає на порту 12345...")

while True:
    client_socket, client_address = server_socket.accept()  # Очікування з'єднання
    print(f"З'єднано з {client_address}")

    data = client_socket.recv(1024).decode()  # Отримання даних від клієнта (максимум 1024 байти)
    print(f"Отримано: {data}")

    current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    response = f"Отримано: {data}\nЧас отримання: {current_time}"
    client_socket.send(response.encode())  # Надсилання відповіді до клієнта
    client_socket.close()  # Закриття з'єднання
