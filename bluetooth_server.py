import bluetooth

def start_bluetooth_server():
    server_socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    server_socket.bind(("", bluetooth.PORT_ANY))
    server_socket.listen(1)

    port = server_socket.getsockname()[1]
    uuid = "00001101-0000-1000-8000-00805F9B34FB"
    bluetooth.advertise_service(server_socket, "BluetoothServer", service_id=uuid)

    print("Bluetooth server is listening on port:", port)
    client_socket, address = server_socket.accept()
    print(f"Accepted connection from {address}")

    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        print(f"Received: {data.decode('utf-8')}")
        client_socket.send(b"Message received!")

    client_socket.close()
    server_socket.close()

if __name__ == "__main__":
    start_bluetooth_server()
