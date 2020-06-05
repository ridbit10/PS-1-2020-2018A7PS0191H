from http.server import BaseHTTPRequestHandler
from urllib import parse


class GetHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        parsed_path = parse.urlparse(self.path)
        a=int(input("Input number1 "))
        b=int(input("Input number2 "))
        c=input("enter operator")
        if(c=="+"):
            message=a+b
        elif(c=='-'):
            message=a-b
        elif(c=='*'):
            message=a*b
        elif(c=='/'):
            if(b==0):
                message="zero error"
            else:
                message=(a/b)
        else:
            message="error"
        message=str(message)
        self.send_response(200)
        self.send_header('Content-Type',
                         'text/plain; charset=utf-8')
        self.end_headers()
        self.wfile.write(message.encode('utf-8'))


if __name__ == '__main__':
    from http.server import HTTPServer
    server = HTTPServer(('localhost', 8080), GetHandler)
    print('Starting server, use <Ctrl-C> to stop')
    server.serve_forever()
