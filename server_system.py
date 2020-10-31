from new_system import *
import socket

codes_list = []
f = open("codes.txt","r")
while True:
	line = f.readline()
	if not line:
		break
	codes_list.append(line[:-1])
f.close()
used_codes = open("used_codes.txt", "r")
while True:
	line = used_codes.readline()
	if not line:
		break
	codes_list.remove(line[:-1])


used_codes = open("used_codes.txt","a+")
already_voted = []
virtualserver_list = []
port_list = []
number_of_booths = int(raw_input("Enter number of polling booths: "))

for i in range(number_of_booths):
	msg = "Enter the port number for Booth %s: ", i
	port = int(raw_input(msg))
	port_list.append(port)

for i in range(number_of_booths):
	virtual_server = VirtualServer()
	virtualserver_list.append(virtual_server)
	virtual_server.create_server(port_list[i])

print virtualserver_list
print port_list
print "Connect clients"
for vs in virtualserver_list:
	vs.open_for_client()

while(True):
	print "--------------------------------------------------------------------------------------------------------------------------------"
	#print already_voted
	roll_number = raw_input("Enter a roll number: ")
	if(roll_number == "POLLING ENDS"):
		break
	if roll_number not in already_voted:
		try:		
			booth_id = int(raw_input("Enter the booth number: "))
		except:
			continue
		data = str(roll_number) + codes_list[0]
		try:
			virtualserver_list[booth_id].send_roll(data)
		except:
			continue
		used_codes.write(codes_list[0] + "\n")
		codes_list.pop(0)
		already_voted.append(roll_number)
	else:
		print "Already Voted"

used_codes.close()
for vs in virtualserver_list:
	vs.close()







