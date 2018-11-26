from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import cgi

# import CRUD Operations
from database_setup import Base, Restaurant, MenuItem
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Create session and connect to DB
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

class webServerHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            if self.path.endswith("/restaurants/new"):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                output = ""
                output += "<html><body>"
                output += "<h3>Create a New Restaurant</h3>"
                #enctype='multipart/form-data' means no characters will be encoded
                output += '''<form method='POST' enctype='multipart/form-data' action='/restaurants/new'>'''
                output += '''<input name = 'new_restaurant' type='text' placeholder = 'New Restaurant Name'>'''
                output += '''<input type='submit' value='Create'>'''
                output += "</form></body></html>"
                self.wfile.write(output)
                return

            if self.path.endswith("/restaurants"):
                restaurants = session.query(Restaurant).all()
                output = ""

                # create a link to /restaurants/new
                output += "<a href='/restaurants/new'>Create a new restaurant</a></br></br>"

                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                output += "<html><body>"
                output += "<h3>List of Restaurants</h3>"
                for restaurant in restaurants:
                    output += restaurant.name
                    output += "</br>"
                    # Edit and Delete
                    output += "<a href='#'>Edit</a>"
                    output += "</br>"
                    output += "<a href=' #'>Delete</a>"
                    output += "</br></br>"
                output += "</body></html>"
                self.wfile.write(output)
                return
        except IOError:
            self.send_error(404, 'File Not Found: %s' % self.path)

    def do_POST(self):
        try:
            if self.path.endswith("/restaurants/new"):
                # parse_header will parse an HTML form header, e.g. content-type into a main value and **dictionary** of parameters
                ctype, pdict = cgi.parse_header(
                    self.headers.getheader('content-type'))
                if ctype == 'multipart/form-data':
                    # collect all the fields in a form
                    fields = cgi.parse_multipart(self.rfile, pdict)
                    # get a set of fields and store them in an array
                    # name the field as **message** when creating the HTML form
                    messagecontent = fields.get('new_restaurant')

                    ### create a new Restaurant entry in the database
                    new_restaurant = Restaurant(name=messagecontent[0])
                    session.add(new_restaurant)
                    session.commit()

                    self.send_response(301)
                    self.send_header('Content-type', 'text/html')
                    self.send_header('Location', '/restaurants')
                    self.end_headers()

        except:
            pass

def main():
    try:
        server = HTTPServer(('', 8080), webServerHandler)
        print 'Web server running...open localhost:8080/restaurants in your browser'
        server.serve_forever()
    except KeyboardInterrupt:
        print '^C received, shutting down server'
        server.socket.close()

if __name__ == '__main__':
    main()
