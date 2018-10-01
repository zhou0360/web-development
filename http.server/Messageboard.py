#!/usr/bin/env python3
#
# Instructions:
#
# Step one: An echo server for POST requests: this server should accept a POST request and return the value of the
# "message" field in that request：
# 1. Find the length of the request data.
# 2. Read the correct amount of request data.
# 3. Extract the "message" field from the request data.
#
# Step two: A server that handles both GET and POST requests.
# 1. Add a string variable that contains the form from Messageboard.html.
# 2. Add a do_GET method that returns the form.
#
# Step two in building the messageboard server.
#
# Instructions:
#   1. In the do_POST method, send a 303 redirect back to the / page.
#   2. In the do_GET method, put the response together and send it.

from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs

past_mssg = []

form = '''<!DOCTYPE html>
  <title>Message Board</title>
  <form method="POST">
    <textarea name="message"></textarea>
    <br>
    <button type="submit">Post it!</button>
  </form>
  <pre>
{}
  </pre>
'''

class MessageHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        # 1. How long was the message? (Use the Content-Length header.)
        length = int(self.headers.get('content-length', 0))
            #convert string to int
            #The method get() returns a value for the given key. 

        # 2. Read the correct amount of data from the request.
        data = self.rfile.read(length).decode() # data = 'message=user_input'

        # 3. Extract the "message" field from the request data.
        # parse_qs will return a dictionary 'message=user_input' => {'message': ['user_input']} 

        message = parse_qs(data)["message"][0] 

        # Escape HTML tags in the message so users can't break world+dog.
        message = message.replace("<", "&lt;")

        # Store every message in a list called past_mssg.
        past_mssg.append(message)

        # 1. Send a 303 redirect back to the root page.

        self.send_response(303)
        self.send_header('Location', '/')
        self.end_headers()
#        self.wfile.write(message.encode())

    def do_GET(self):
        # First, send a 200 OK response.
        self.send_response(200)

        # Then send headers.
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()

        # 2. Put the response together out of the form and the stored messages.
        # <pre>\n[\'past_mssg\']\n
        # str.format: anything within the brackets {} will be replaced 
        #   "The sum of 1 + 2 is {0}".format(1+2) 
        # ==> 'The sum of 1 + 2 is 3'
        response = form.format("\n".join(past_mssg)) # "\n" is used to start a new line every time a new messagei is posted 

        # 3. Send the response.
        self.wfile.write(response.encode())


if __name__ == '__main__':
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, MessageHandler)
    httpd.serve_forever()



