import socket

host = "127.0.0.1"
port = 40406

http_response = (
        f"HTTP/1.0 200 OK\r\n"
        f"Server: otusdemo\r\n"
        f"Date: Sat, 01 Oct 2022 09:39:37 GMT\r\n"
        f"Content-Type: text/html; charset=UTF-8\r\n"
        f"\r\n"
        )

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:

    print(f"Binding server on {host}:{port}")
    server.bind((host, port))
    server.listen()
    while True:
        connection, address = server.accept()

        with connection:
            connection.send(http_response.encode())