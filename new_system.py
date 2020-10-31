
import socket


class VirtualServer:

	def __init__(self):
		self.count = 1
		self.server = None  
		self.client = None

	def create_server(self, port):
	    s = socket.socket()
	    host = socket.gethostname()
	    s.bind(('', port))
	    self.server = s
	    print self.count
	    self.count += 1

	def open_for_client(self):
		self.server.listen(1)
		(client, client_address) = self.server.accept()
		print "Got connection from ", client_address
		client.send("Thanks for connecting!")
		self.client = client
		

	def send_roll(self, data):
		self.client.send(str(data))
		print self.client.recv(1024)

	def close(self):
		self.server.close()


class Client:
	
	def __init__(self):
		self.client = 0
		self.roll = 0
		self.code = None
		#self.voted = []
		#self.check = True

	def connect(self, host, port):
		s = socket.socket()
		s.connect((host, port))
		print s.recv(1024)
		#s.send("Received Connection")
		self.client = s

	def get_roll(self):
		data = self.client.recv(1024)
		#if roll_number not in self.voted:
		#self.voted.append(roll_number)
		self.client.send("Roll Number Recieved")
		self.roll = data[:-4]
		self.code = data[-4:]
			#self.check = True
		#else:
			#self.client.send("Already Voted")
			#self.check = False


	def close(self):
		self.client.close()






