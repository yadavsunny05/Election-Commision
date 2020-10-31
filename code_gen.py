import random

alphabet = "qwertyuiopasdfghjklzxcvbnm123456789"

code_list = []

while len(code_list) < 2000:
	code = ""
	for i in range(4):
		code += alphabet[random.randint(0,len(alphabet) - 1)]
	if code not in code_list:
		code_list.append(code)

f = open("codes.txt","w")
for i in code_list:
	f.write(i+"\n")
f.close()
