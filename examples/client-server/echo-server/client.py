import socket


HOST = 'localhost'
PORT = 29999


def get_server_address():
    return (HOST, PORT)


def create_request():
    return b'Hello World'


def create_client_and_call_server():

    # socket() --> connect() --> send/sendall() --> recv()
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect(get_server_address())  # <-- possible errors?
        request_payload = create_request()
        client.sendall(request_payload)
        response_bytes = client.recv(1024)  # <-- handling timeout
        print(f'Received Respose -> {response_bytes.decode()}')


create_client_and_call_server()
