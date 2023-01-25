import socket

def main():
    # Set the IP and port of the server
    server_ip = "192.168.56.102"
    server_port = 8888

    # Create a socket 
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    client_socket.connect((server_ip, server_port))

    # Request a quote from the server
    quote = client_socket.recv(1024)
    print("Quotes Of The Day! : \n %s" % quote.decode())

    # Close the socket
    client_socket.close()

#execute main function
main()