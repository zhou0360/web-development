from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import cgi #common geteway interface

# indicates what code to execute based on the type of HTTP request
class webserverHandler(BaseHTTPRequestHandler):
    #the do_GET function will handle all GET requests that our web server receives
    def do_GET(self):
        try:
            if self.path.endswith("/annsway"):
                self.send_response(200) #indicates successful get request
                self.send_header('Content-type', 'text/html')
                self.end_headers() #indicates the end of our HTTP headers in the response

                output = ""
                output += "<html><body>"
                output += "<h1>Hello!</h1>"
                output += '''<form method='POST' enctype='multipart/form-data' action='/annsway'><h2>What's your name? </h2><input name="message" type="text"><input type="submit" value="Submit"></form>'''
                output += "</body></html>"
                self.wfile.write(output) #sends a message to the client
                print output
                return

            if self.path.endswith("/annsway2"):
                self.send_response(200) #indicates successful get request
                self.send_header('Content-type', 'text/html')
                self.end_headers() #indicates the end of our HTTP headers in the response

                output = ""
                output += "<html><body>"
                output += "<h1>Hello!</h1>"
                output += '''<form method='POST' enctype='multipart/form-data' action='/annsway'><h2></h2><input name="message" type="text"><input type="submit" value="Submit"></form>'''
                output += "</body></html>"
                self.wfile.write(output) #sends a message to the client
                print output
                return

        except IOError:
            self.send_error(404, "File Not Found %s" % self.path)

    def do_POST(self):
        try:
            self.send_response(301)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            ctype, pdict = cgi.parse_header(
                self.headers.getheader('content-type'))
            if ctype == 'multipart/form-data':
                fields = cgi.parse_multipart(self.rfile, pdict)
                messagecontent = fields.get('message')
            output = ""
            output += "<html><body>"
            output += " <h2> Hello, </h2>"
            output += "<h1> %s </h1>" % messagecontent[0]
            output += '''<form method='POST' enctype='multipart/form-data' action='/annsway'><h2>What's your name?</h2><input name="message" type="text" ><input type="submit" value="Submit"> </form>'''
            output += "</body></html>"
            self.wfile.write(output)
            print output
        except:
            pass

# instantiate our web server and specify what port it will listen on
def main():
    try:
        port = 8080
        server = HTTPServer(('',port), webserverHandler)
        print("Web server running on port %s" % port)
        server.serve_forever()

    except KeyboardInterrupt:
        print("^C entered, stopping web server...")
        server.socket.close()

if __name__ == '__main__':
    main()
#instantiate vagrant
#execute this script by entering python WebServer.py in your terminal
#enter localhost:8080/annsway in your web browser
