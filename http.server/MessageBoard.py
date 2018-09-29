from http.server import HTTPServer, BaseHTTPRequestHandler, urllib

class MessageHandler(BaseHTTPRequestHandler): 

	def do_POST(self): 

		length = int(self.headers.get('content-length', 0)) #convert string to int
		#The method get() returns a value for the given key. 

		dat = self.rfile.read(length).decode()

		mssg = urllib.parse.parse_qs.message 

		
