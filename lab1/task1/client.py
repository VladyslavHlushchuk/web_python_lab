import socket

# Створення TCP-клієнта
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', 12345))  # Підключення до сервера за адресою 127.0.0.1:12345

# Введення тексту від користувача
message = input("Введіть текст для відправки на сервер: ")

# Надсилання даних на сервер
client_socket.send(message.encode())

# Отримання відповіді від сервера
response = client_socket.recv(1024).decode()
print(f"Відповідь від сервера: {response}")

client_socket.close()  # Закриття з'єднання
