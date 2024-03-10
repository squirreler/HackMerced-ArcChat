import socket
import errno #match error codes
import sys
import app







def client_f(user,text_msg,x):
    
    HEADERLENGTH= 10


    SERVER_IP = '10.34.61.195'
    PORT = 7893


    my_username = user



    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((SERVER_IP,7893))
    client_socket.setblocking(False)



    username = my_username.encode("utf-8")
    username_header = f"{len(username):<{HEADERLENGTH}}".encode("utf-8")
    client_socket.send(username_header + username)





    while x != 1:
        while True:

            
            message = text_msg #fix it so that it doesnt hold the message


            file_path = "C:\\Users\\anbha\\OneDrive\\Documents\\Projects\\chatbot\\messages.txt"
            with open(file_path, 'a') as f:
                f.write(f" {username}> {message}" + "\n")

            if message:
                message = message.encode("utf-8")
                message_header = f"{len(message):<{HEADERLENGTH}}".encode("utf-8")
                client_socket.send(message_header + message)


            try:
                while True:

                    
                    # receive things
                    username_header = client_socket.recv(HEADERLENGTH)
                    if not len(username_header):
                        print("Connection Closed by server")
                        sys.exit()
                    username_length = int(username_header.decode("utf-8").strip())
                    username = client_socket.recv(username_length).decode("utf-8")

                    
                    message_header = client_socket.recv(HEADERLENGTH)
                    message_length = int(message_header.decode("utf-8").strip())
                    message = client_socket.recv(message_length).decode("utf-8")

                    print(f" {username}> {message}")

            except IOError as e:
                if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
                    print('Reading Error',str(e))
                    sys.exit()
                continue



            except Exception as e:
                print('General Error', str(e))
                sys.exit()




