from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs
import json

class HelloHandler(BaseHTTPRequestHandler):
### Class Start
	def do_GET(self):
		if self.path == "/plants":
			# ACTION:
			self.handlePlantsList()
		else:
			#404
			self.handle404()

	def do_POST(self):
		if self.path == "/plants":
			# ACTION: plants create
			self.handlePlantsCreate()
		else:
			self.handle404()

	# GET /plants
	def handlePlantsList(self):
		my_data = ["tree", "rose", "cattails", "ugly bush", "ferns"]
		json_string = json.dumps(my_data)

		print ("JSON: ", json_string)

		self.send_response(200)
		self.send_header("Access-Control-Allow-Origin", "*")
		self.send_header("Content-type", "applicaton/json")
		self.end_headers()
		self.wfile.write(bytes(json_string, "utf-8"))
		return

	# POST /plants
	def handlePlantsCreate(self):
		#print(self.headers)
		length = self.headers['Content-Length']
		length = int(length)
		# if you are reading the request body self.rfile
		# if you are reading the write body self.wfile

		body = self.rfile.read(length).decode("utf-8")

		data = (parse_qs(body))

		fname = data['message'][0]
		print(fname)

		self.send_response(201)
		self.send_header("Access-Control-Allow-Origin", "*")
		self.end_headers()
		#self.send_header("Content-type", "applicaton/x-www-form-urlencoded")
		return

	def handle404(self):
		#404
		self.send_response(404)
		self.send_header("Access-Control-Allow-Origin", "*")
		self.send_header("Content-type", "text/html")
		self.end_headers()
		self.wfile.write(bytes("<strong>Not Found</strong>", "utf-8"))

# fin = open(filename, "r")
# fin.read.splitlines()

### Class End

def main():
	listen = ('127.0.0.1', 8080)
	server = HTTPServer(listen, HelloHandler)
	#  HTTPServer will instantiate the class, not me

	print("Listening...")
	server.serve_forever()

main()

"""
404 not found

Notes:

		origin

		null		X	localhost
Us	->	apple.com	->	google.com // I, google must be careful to authorize what data is being accessed
						myjson.com // I, myjson, have no 'secrets'. Anyone can look at my data without restrictions


CORS

Example

Big Picture


Post plants

1) read request body (get the 'length' first to know how much to read it)
2) append to "DATA" (save)
3) respond with a '201' (or a different code if something went wrong)
	-no headers
	-no body


applicaton/x-www-form-urlencoded
'percent encoding'

example:

Name: Gareth Wylie
Age: 24
Formula: a + b == 13%

Name=Gareth+Wylie&Age=24&Formula=a+%2B+b%3D%3D


member == element

protocol://hostname:post/path? query=string#fragment

Web Service

	action resource

1.) list messages
	-how should the client make requests based on http and rest?
	-request:
		1.) method
			-the general catagory or type of request
		2.) URL (protocol, hostname, path)
2.) create message



-HTTPS
-REST
	."the way"
	.Representional state transfer
	.or RESTful Web services
	.defacto set of rules used by webservices

-CRUD
	.Create, Read, Update(change), Delete

Resource - a noun, something we care about
	examples: a service, a product, a 'tweet'


Product
	-attributes
		.quantity
		.price
		.color
		.etc
	-presentation
		.html/css
		.mobile view
		.images
	-User Interface (basically presentation)
		.how the user uses the view
	-UX
	-Marketing/Brand
	-database
		.records
		.search
	-logic
		.brain
		.code
		."how do I apply discount codes"
		.helps to differ from other web services



Plant

collection /plants

member /plants/77

according to REST

list/index: GET /plants => CODE used when you just want info.
create: POST/plants => CODE used when we want a 'side effect' to happen.


All headers have a 'name' and a 'value'

Body
Headers: content-type "standard name"

read about MIME types

"""
