#SANIKA PRAVIN RAUT
#UTA ID 1001101016


#Importing all Python libraries used in the program
import socket
import thread
import threading

from _socket import timeout #socket module and timeout module

#handle_request deals with checking thread count and sending the response back to client
def handle_request(connectionsocket, addr,threadCount):

    print "Request Received from Client!"
    print "Client IP = " + addr[0] + " Client Port Number = " + str(addr[1])
#Check for Successful Response, If successful response not found return that particular Response
    while True:
        try:
            connectionsocket.settimeout(120.0) #Setting Timeout for the Connection
            result = connectionsocket.recv(1024)
            print "Connection on Thread :" + str(threadCount)
            if len(result) > 0 :
                connectionsocket.settimeout(None)

            if len(result) < 1:
                print "The message from one of the request is empty on thread:" + str(threadCount)
                print 'Server Is Ready, Waiting for a New Request'
                return
            filename = result.split()[1].partition("/")[2]
            print "filename:" +filename
            if (len(filename.split()))==0:
                filename= 'home.html'
            f = open(filename)
            connectionsocket.send(f.read())

            print "Request :" + result
            print "HTTP/1.1 200 OK"
        except timeout:
            print "Timeout has occured"
            connectionsocket.send("Connection: Timedout\r\n")
            break
        except IOError:
            print "Request :" + result
            print "HTTP/1.1 404 Not Found"
            connectionsocket.send("HTTP/1.1 404 Not Found\r\n")
            connectionsocket.send("Content-Type:text/html\r\n")
            connectionsocket.send("Connection: close\r\n")
            connectionsocket.send("\r\n")
            connectionsocket.send(
                    "<html><body><h1>HTTP/1.1 404 Not Found</h1></body></html>")
    connectionsocket.close()

#Counter is used for Threading purpose
threadCount = 1

#Create server socket, bind it to a port and start listening
serverport = input("Enter a port number for the Server: ")
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(('', serverport))
serversocket.listen(5)
print "Server is Ready, Connected to Port: " + str(serverport)

threadCount = 1
#Start receiving data from the Client
while 1:
    connectionsocket, addr = serversocket.accept()
    thread.start_new_thread(handle_request,(connectionsocket, addr,threadCount))
    threadCount = threadCount + 1
serversocket.close()
