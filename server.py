import socket
import threading
from cryptography.fernet import Fernet


key = Fernet.generate_key()
cipher = Fernet(key)


traffic_data = []

def log_traffic(data):
    traffic_data.append(data)
    print(f"Traffic logged: {data}")


def handle_client(client_socket):
    while True:
        message = client_socket.recv(1024)
        if not message:
            break
        decrypted_message = cipher.decrypt(message).decode('utf-8')
        log_traffic(decrypted_message)  
        print(f"Received: {decrypted_message}")
        
        response = cipher.encrypt(b"Message received!")
        client_socket.send(response)
    
    client_socket.close()

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 5000))
    server_socket.listen(5)
    print("Server is listening...")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Connection from {addr} has been established!")
        thread = threading.Thread(target=handle_client, args=(client_socket,))
        thread.start()

if __name__ == "__main__":
    start_server()
