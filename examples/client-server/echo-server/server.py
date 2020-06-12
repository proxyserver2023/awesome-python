import socket


HOST_FOR_ALL_AVAILABLE_INTERFACES = ''
ARBITRARY_NON_PRIVILEGED_PORT = 29999


def get_address():
    return (HOST_FOR_ALL_AVAILABLE_INTERFACES,
            ARBITRARY_NON_PRIVILEGED_PORT)


def parse_request(raw_data):
    try:
        parsed_data = raw_data.decode()
        print(parsed_data)
        return parsed_data
    except UnicodeDecodeError as e:
        print(e)
        return None


def render_response(parsed_data):
    rendered_data = b''
    if parsed_data:
        try:
            rendered_data = parsed_data.encode()
            print(f'Rendered data - {rendered_data!r}')
        except UnicodeEncodeError as e:
            print(f'Failed to Encode to bytes - {e}')
    return rendered_data


def create_server():

    # socket() --> bind() --> listen() --> accept() --> recv()
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind(get_address())
        sock.listen(1)
        conn, addr = sock.accept()

        with conn:
            print(f'Connected with - {addr}')
            while True:
                raw_data = conn.recv(1024)
                if not raw_data:
                    break  # <-- possibilities to keep the server open?

                parsed_data = parse_request(raw_data)
                rendered_data = render_response(parsed_data)
                conn.sendall(rendered_data)


create_server()
