import random
import threading
import socket

#array of quotes
quotes = ["“We cannot solve problems with the kind of thinking we employed when we came up with them.” — Albert Einstein",
          "“Learn as if you will live forever, live like you will die tomorrow.” — Mahatma Gandhi",
          "“Stay away from those people who try to disparage your ambitions. Small minds will always do that, but great minds will give you a feeling that you can become great too.” — Mark Twain",
          "“When you give joy to other people, you get more joy in return. You should give a good thought to happiness that you can give out.”— Eleanor Roosevelt",
          "“When you change your thoughts, remember to also change your world.”—Norman Vincent Peale",
          "“Success is not final; failure is not fatal: It is the courage to continue that counts.” — Winston S. Churchill",
          "“It is better to fail in originality than to succeed in imitation.” — Herman Melville",
          "“Success usually comes to those who are too busy looking for it.” — Henry David Thoreau"]

#choose random quotes from array and send to client
def handle_client(client_socket):
    quote = random.choice(quotes)
    client_socket.sendall(quote.encode())
    client_socket.close()

def main():
    #declare server ip and port
    bind_ip = "192.168.56.102"
    bind_port = 8888

    #create and bind socket
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((bind_ip, bind_port))

    #listen for connections
    server.listen(5)
    print("[*] Listening on %s:%d" % (bind_ip, bind_port))

    #start connections and execute handle_client function
    while True:
        client, addr = server.accept()
        print("[*] Accepted connection from: %s:%d" % (addr[0], addr[1]))
        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()

#call for main function
main()