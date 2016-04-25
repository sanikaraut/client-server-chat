#SANIKA PRAVIN RAUT
#UTA ID 1001101016

#Importing all Python libraries used in the program
import socket
import sys

#handle requests deals with determining http method is GET or POST
def handle_GET(file, server, port , s):
    request = "GET /"+ file + " HTTP/1.1\nHost: " + server + "\n\n"
    s.send(request.encode())

    result = s.recv(1024)
    print(result)
    return result
#
def handle_POST(file, server, port , s):
    headers = """\
    POST /{url} HTTP/1.1\r
    Content-Type: {content_type}\r
    Content-Length: {content_length}\r
    Host: {host}\r
    Connection: close\r
    \r\n"""


    body = 'emailId=sanika&age=23'
    body_bytes = body.encode('ascii')
    header_bytes = headers.format(
    url = file,
    content_type="application/html",
    content_length=len(body_bytes),
    host=str(server) + ":" + str(port)
    ).encode('iso-8859-1')

    payload = header_bytes + body_bytes
    s.sendall(payload)
    result1 = s.recv(1024)
    print(result1)
    return result1

#Creating a Client that is able to connect to the server
port = input("Enter a port number of the server to be connected: ")
server = "localhost"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((server, port))
def Main():

    file = raw_input("Enter the file path:")

    if file == ' ':
        file = "home.html"

    method = raw_input("Enter the HTTP method GET or POST:")

    if method == ' ':
        method = "GET"

    if method == "POST":
       output1 = handle_POST(file,server,port,s)
       if "Connection: Timeout" in output1:
            print "Your connection with the Server has timedout"
            print "Connect to the Server again"
            sys.exit(0)
    else:
        output = handle_GET(file,server,port,s)
        if "Connection: Timeout" in output:
            print "Your connection with server timeout"
            print "Connect to the server again"
            sys.exit(0)

    print "Send another request"
    Main()

if __name__=='__main__':
    Main()

