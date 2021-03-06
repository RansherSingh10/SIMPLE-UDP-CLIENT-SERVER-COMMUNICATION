import socket

serverAddressPort   = ("127.0.0.1", 20001)

bufferSize          = 1024

# Create a UDP socket at client side

UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

while(True): 

    msgFromClient = input("Please input a message: ")

    if(msgFromClient == 'quit'):
        break

    bytesToSend = str.encode(msgFromClient)

    # Send to server using created UDP socket

    UDPClientSocket.sendto(bytesToSend, serverAddressPort)

    msgFromServer = UDPClientSocket.recvfrom(bufferSize)

    msg = "Message from Server {}".format(msgFromServer[0])

    print(msg)