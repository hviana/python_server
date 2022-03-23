from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import time

port = 41425

class JSONHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        input_string = self.rfile.read(int(self.headers.get('content-length')))
        input_obj = json.loads(input_string);
        print('JSON received: '+str(input_obj));

        output_obj = { "time": time.time() }; #example object
        print('Sending data as JSON : '+str(output_obj));

        self.send_response(200)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.end_headers()
        self.wfile.write(json.dumps(output_obj).encode('utf-8'))
        return
server_object = HTTPServer(server_address=('', port), RequestHandlerClass=JSONHandler)
print('starting server at port: '+str(port))
server_object.serve_forever()
