from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs
import json

class itemHandler(BaseHTTPRequestHandler):
### Class Start
	def do_GET(self):
		if self.path == "/items":
			# ACTION: Display list
			self.handleItemsList()
		else:
			#404
			self.handle404()

	def do_POST(self):
		if self.path == "/items":
			#ACTION: Create new item and add to list
			self.handleItemsCreate()
		else:
			self.handle404()

	# GET /items, must respond with 200
	def handleItemsList(self):
		dataList = open("myData.txt").read().splitlines()
		#my_data = ["eggs", "ham", "brocoli", "sponge", "ice"]
		json_string = json.dumps(dataList)

		#print ("JSON: ", json_string)

		self.send_response(200)
		self.send_header("Access-Control-Allow-Origin", "*")
		self.send_header("Content-type", "applicaton/json")
		self.end_headers()
		self.wfile.write(bytes(json_string, "utf-8"))
		return

	# POST /items, must respond with 201
	def handleItemsCreate(self):
		length = self.headers['Content-Length']
		length = int(length)
		body = self.rfile.read(length).decode("utf-8")

		data = (parse_qs(body))

		itemName = data['item'][0]

		myData = open("myData.txt", "a").write(itemName + "\n")

		self.send_response(201)
		self.send_header("Access-Control-Allow-Origin", "*")
		self.end_headers()
		return

	def handle404(self):
		#404
		self.send_response(404)
		self.send_header("Access-Control-Allow-Origin", "*")
		self.send_header("Content-type", "text/html")
		self.end_headers()
		self.wfile.write(bytes("<strong>Not Found</strong>", "utf-8"))
		return

def main():
	listen = ('127.0.0.1', 8080)
	server = HTTPServer(listen, itemHandler)
	#  HTTPServer will instantiate the class, not me

	print("Listening...")
	server.serve_forever()

main()
