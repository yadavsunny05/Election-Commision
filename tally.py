code = []
f = open("codes.txt", "r")
while True:
	line = f.readline()
	if not line:
		break
	codes.append(line[:-1])
f.close()
################################################
rahul_bharti = 0
welf_nota = 0

rachelle = 0
acad_nota = 0

rahul_cult = 0
priyang_cult = 0
lavlesh_cult = 0
alrick_cult = 0
nota_cult = 0

harsh_msc = 0
nota_msc = 0 

akshay_mtech = 0
alok_mtech = 0
neelay_mtech = 0
nota_mtech = 0

shivani_girl = 0
amitha_girl = 0
nota_girl = 0


rajesh_phd = 0
adarsh_phd = 0
nota_phd = 0


deepika_ee17 = 0
utsav_ee17 = 0

dhruvin_me = 0
shivang_me = 0
parth_me = 0

utkarsh_ce = 0
nishant_ce = 0

harshil_cse = 0
vraj_cse = 0
################################################################################################
r = open("EC18 - Msc 18 Senator (Responses).csv", "r")
while True:
	line = r.readline()
	if not line:
		break
	lst = line.split(',')
	if lst[1] in codes:
		codes.remove(lst[1])
		if lst[2] == "Alrick Dsouza":
			alrick_cult += 1
		if lst[2] == "Lavalesh Kumar Bajpayee":
			lavlesh_cult += 1
		if lst[2] == "Priyang Priyadarshi":
			priyang_cult += 1
		if lst[2] == "Rahul Upadhyay":
			rahul_cult += 1
		if lst[2] == "NOTA":
			nota_cult += 1
		if lst[3] == "Rachelle C":
			rachelle += 1
		if lst[3] == "NOTA":
			acad_nota += 1
		if lst[4] == "Rahul Bharti":
			rahul_bharti += 1
		if lst[4] == "NOTA":
			welf_nota += 1
		if lst[5] == "HARSH KUMAR":
			harsh_msc += 1
		if lst[5] == "NOTA":
			nota_msc += 1

r.close()



r = open("EC18 - MTech 18 Senator (Responses).csv", "r")
while True:
	line = r.readline()
	if not line:
		break
	lst = line.split(',')
	if lst[1] in codes:
		codes.remove(lst[1])
		if lst[2] == "Alrick Dsouza":
			alrick_cult += 1
		if lst[2] == "Lavalesh Kumar Bajpayee":
			lavlesh_cult += 1
		if lst[2] == "Priyang Priyadarshi":
			priyang_cult += 1
		if lst[2] == "Rahul Upadhyay":
			rahul_cult += 1
		if lst[2] == "NOTA":
			nota_cult += 1
		if lst[3] == "Rachelle C":
			rachelle += 1
		if lst[3] == "NOTA":
			acad_nota += 1
		if lst[4] == "Rahul Bharti":
			rahul_bharti += 1
		if lst[4] == "NOTA":
			welf_nota += 1
		if lst[5] == "Alok Kumar Thakur":
			alok_mtech += 1
		if lst[5] == "Akshay Srivastava":
			akshay_mtech += 1
		if lst[5] == "Neelay Upadhyaya":
			neelay_mtech += 1
		if lst[5] == "NOTA":
			nota_mtech += 1

r.close()


r = open("EC18 - Phd Senator (Responses).csv", "r")
while True:
	line = r.readline()
	if not line:
		break
	lst = line.split(',')
	if lst[1] in codes:
		codes.remove(lst[1])
		if lst[2] == "Alrick Dsouza":
			alrick_cult += 1
		if lst[2] == "Lavalesh Kumar Bajpayee":
			lavlesh_cult += 1
		if lst[2] == "Priyang Priyadarshi":
			priyang_cult += 1
		if lst[2] == "Rahul Upadhyay":
			rahul_cult += 1
		if lst[2] == "NOTA":
			nota_cult += 1
		if lst[3] == "Rachelle C":
			rachelle += 1
		if lst[3] == "NOTA":
			acad_nota += 1
		if lst[4] == "Rahul Bharti":
			rahul_bharti += 1
		if lst[4] == "NOTA":
			welf_nota += 1
		if lst[5] == "Adarsh kumar":
			adarsh_phd += 1
		if lst[5] == "Rajesh Pavan Pothukuchi":
			rajesh_phd += 1
		if lst[5] == "NOTA":
			nota_phd += 1

r.close()

r = open("EC18 - Rest (Responses).csv", "r")
while True:
	line = r.readline()
	if not line:
		break
	lst = line.split(',')
	if lst[1] in codes:
		codes.remove(lst[1])
		if lst[2] == "Alrick Dsouza":
			alrick_cult += 1
		if lst[2] == "Lavalesh Kumar Bajpayee":
			lavlesh_cult += 1
		if lst[2] == "Priyang Priyadarshi":
			priyang_cult += 1
		if lst[2] == "Rahul Upadhyay":
			rahul_cult += 1
		if lst[2] == "NOTA":
			nota_cult += 1
		if lst[3] == "Rachelle C":
			rachelle += 1
		if lst[3] == "NOTA":
			acad_nota += 1
		if lst[4] == "Rahul Bharti":
			rahul_bharti += 1
		if lst[4] == "NOTA":
			welf_nota += 1
r.close()

r = open("EC18 - Council BTech Girls (Responses).csv", "r")
while True:
	line = r.readline()
	if not line:
		break
	lst = line.split(',')
	if lst[1] in codes:
		codes.remove(lst[1])
		if lst[2] == "Alrick Dsouza":
			alrick_cult += 1
		if lst[2] == "Lavalesh Kumar Bajpayee":
			lavlesh_cult += 1
		if lst[2] == "Priyang Priyadarshi":
			priyang_cult += 1
		if lst[2] == "Rahul Upadhyay":
			rahul_cult += 1
		if lst[2] == "NOTA":
			nota_cult += 1
		if lst[3] == "Rachelle C":
			rachelle += 1
		if lst[3] == "NOTA":
			acad_nota += 1
		if lst[4] == "Rahul Bharti":
			rahul_bharti += 1
		if lst[4] == "NOTA":
			welf_nota += 1
		if lst[5] == "Shivani Patley":
			shivani_girl += 1
		if lst[5] == "Mulastham Amitha Rani":
			amitha_girl += 1
		if lst[5] == "NOTA":
			nota_girl += 1
r.close()


r = open("EC18 - B.TECH 17 CSE CR BOYS (Responses).csv", "r")
while True:
	line = r.readline()
	if not line:
		break
	lst = line.split(',')
	if lst[1] in codes:
		codes.remove(lst[1])
		if lst[2] == "Alrick Dsouza":
			alrick_cult += 1
		if lst[2] == "Lavalesh Kumar Bajpayee":
			lavlesh_cult += 1
		if lst[2] == "Priyang Priyadarshi":
			priyang_cult += 1
		if lst[2] == "Rahul Upadhyay":
			rahul_cult += 1
		if lst[2] == "NOTA":
			nota_cult += 1
		if lst[3] == "Rachelle C":
			rachelle += 1
		if lst[3] == "NOTA":
			acad_nota += 1
		if lst[4] == "Rahul Bharti":
			rahul_bharti += 1
		if lst[4] == "NOTA":
			welf_nota += 1
		if lst[5] == "Harshil Jain":
			harshil_cse += 1
		if lst[5] == "Vraj Patel":
			vraj_cse += 1
r.close()

r = open("EC18 - B.Tech 17 EE CR Boys (Responses).csv", "r")
while True:
	line = r.readline()
	if not line:
		break
	lst = line.split(',')
	if lst[1] in codes:
		codes.remove(lst[1])
		if lst[2] == "Alrick Dsouza":
			alrick_cult += 1
		if lst[2] == "Lavalesh Kumar Bajpayee":
			lavlesh_cult += 1
		if lst[2] == "Priyang Priyadarshi":
			priyang_cult += 1
		if lst[2] == "Rahul Upadhyay":
			rahul_cult += 1
		if lst[2] == "NOTA":
			nota_cult += 1
		if lst[3] == "Rachelle C":
			rachelle += 1
		if lst[3] == "NOTA":
			acad_nota += 1
		if lst[4] == "Rahul Bharti":
			rahul_bharti += 1
		if lst[4] == "NOTA":
			welf_nota += 1
		if lst[5] == "Jethva Utsav":
			utsav_ee17 += 1
		if lst[5] == "Deepika Soni":
			deepika_ee17 += 1
r.close()

r = open("EC18 - B.Tech 17 ME CR (Responses).csv", "r")
while True:
	line = r.readline()
	if not line:
		break
	lst = line.split(',')
	if lst[1] in codes:
		codes.remove(lst[1])
		if lst[2] == "Alrick Dsouza":
			alrick_cult += 1
		if lst[2] == "Lavalesh Kumar Bajpayee":
			lavlesh_cult += 1
		if lst[2] == "Priyang Priyadarshi":
			priyang_cult += 1
		if lst[2] == "Rahul Upadhyay":
			rahul_cult += 1
		if lst[2] == "NOTA":
			nota_cult += 1
		if lst[3] == "Rachelle C":
			rachelle += 1
		if lst[3] == "NOTA":
			acad_nota += 1
		if lst[4] == "Rahul Bharti":
			rahul_bharti += 1
		if lst[4] == "NOTA":
			welf_nota += 1
		if lst[5] == "Parth Shinde":
			parth_me += 1
		if lst[5] == "Shah Dhruvin":
			dhruvin_me += 1
		if lst[5] == "Shivang Pareek":
			shivang_me += 1
r.close()

r = open("EC18 - B.TECH 17 Civil CR BOYS (Responses).csv", "r")
while True:
	line = r.readline()
	if not line:
		break
	lst = line.split(',')
	if lst[1] in codes:
		codes.remove(lst[1])
		if lst[2] == "Alrick Dsouza":
			alrick_cult += 1
		if lst[2] == "Lavalesh Kumar Bajpayee":
			lavlesh_cult += 1
		if lst[2] == "Priyang Priyadarshi":
			priyang_cult += 1
		if lst[2] == "Rahul Upadhyay":
			rahul_cult += 1
		if lst[2] == "NOTA":
			nota_cult += 1
		if lst[3] == "Rachelle C":
			rachelle += 1
		if lst[3] == "NOTA":
			acad_nota += 1
		if lst[4] == "Rahul Bharti":
			rahul_bharti += 1
		if lst[4] == "NOTA":
			welf_nota += 1
		if lst[5] == "Utkarsh Sandeep Gangwal":
			utkarsh_ce += 1
		if lst[5] == "Nishant":
			nishant_ce += 1
r.close()


r = open("EC18 - B.Tech 17 EE CR Girls (Responses).csv", "r")
while True:
	line = r.readline()
	if not line:
		break
	lst = line.split(',')
	if lst[1] in codes:
		codes.remove(lst[1])
		if lst[2] == "Alrick Dsouza":
			alrick_cult += 1
		if lst[2] == "Lavalesh Kumar Bajpayee":
			lavlesh_cult += 1
		if lst[2] == "Priyang Priyadarshi":
			priyang_cult += 1
		if lst[2] == "Rahul Upadhyay":
			rahul_cult += 1
		if lst[2] == "NOTA":
			nota_cult += 1
		if lst[3] == "Rachelle C":
			rachelle += 1
		if lst[3] == "NOTA":
			acad_nota += 1
		if lst[4] == "Rahul Bharti":
			rahul_bharti += 1
		if lst[4] == "NOTA":
			welf_nota += 1
		if lst[6] == "Utkarsh Sandeep Gangwal":
			utkarsh_ce += 1
		if lst[6] == "Nishant":
			nishant_ce += 1
		if lst[5] == "Shivani Patley":
			shivani_girl += 1
		if lst[5] == "Mulastham Amitha Rani":
			amitha_girl += 1
r.close()



r = open("EC18 - B.TECH 17 CSE CR GIRLS (Responses).csv", "r")
while True:
	line = r.readline()
	if not line:
		break
	lst = line.split(',')
	if lst[1] in codes:
		codes.remove(lst[1])
		if lst[2] == "Alrick Dsouza":
			alrick_cult += 1
		if lst[2] == "Lavalesh Kumar Bajpayee":
			lavlesh_cult += 1
		if lst[2] == "Priyang Priyadarshi":
			priyang_cult += 1
		if lst[2] == "Rahul Upadhyay":
			rahul_cult += 1
		if lst[2] == "NOTA":
			nota_cult += 1
		if lst[3] == "Rachelle C":
			rachelle += 1
		if lst[3] == "NOTA":
			acad_nota += 1
		if lst[4] == "Rahul Bharti":
			rahul_bharti += 1
		if lst[4] == "NOTA":
			welf_nota += 1
		if lst[5] == "Harshil Jain":
			harshil_cse += 1
		if lst[5] == "Nishant":
			nishant_ce += 1
		if lst[6] == "Shivani Patley":
			shivani_girl += 1
		if lst[6] == "Mulastham Amitha Rani":
			amitha_girl += 1
r.close()


r = open("EC18 - B.TECH 17 CSE CR GIRLS (Responses).csv", "r")
while True:
	line = r.readline()
	if not line:
		break
	lst = line.split(',')
	if lst[1] in codes:
		codes.remove(lst[1])
		if lst[2] == "Alrick Dsouza":
			alrick_cult += 1
		if lst[2] == "Lavalesh Kumar Bajpayee":
			lavlesh_cult += 1
		if lst[2] == "Priyang Priyadarshi":
			priyang_cult += 1
		if lst[2] == "Rahul Upadhyay":
			rahul_cult += 1
		if lst[2] == "NOTA":
			nota_cult += 1
		if lst[3] == "Rachelle C":
			rachelle += 1
		if lst[3] == "NOTA":
			acad_nota += 1
		if lst[4] == "Rahul Bharti":
			rahul_bharti += 1
		if lst[4] == "NOTA":
			welf_nota += 1
		if lst[5] == "Jethva Utsav":
			utsav_ee17 += 1
		if lst[5] == "Deepika Soni":
			deepika_ee17 += 1
		if lst[6] == "Shivani Patley":
			shivani_girl += 1
		if lst[6] == "Mulastham Amitha Rani":
			amitha_girl += 1
r.close()

#################################################################################################
print "CULTURAL"
print "RAHUL = " + str(rahul_cult)
print "Priyang = " + str(priyang_cult)
print "Alrick = " + str(alrick_cult)
print "Lavalesh = " + str(lavlesh_cult)
print "NOTA = " + str(nota_cult)


print "---------------------------------------------------------------------------"

print "WELFARE"
print "Rahul = " + str(rahul_bharti)
print "NOTA = " + str(welf_nota)

print "---------------------------------------------------------------------------"

print "ACAD"
print "Rachelle = " + str(rachelle)
print "NOTA = " + str(acad_nota)

print "---------------------------------------------------------------------------"

print "MTECH 18"
print "Alok = " + str(alok_mtech)
print "Akshay = " + str(akshay_mtech)
print "Neelay = " + str(neelay_mtech)
print "NOTA = " + str(nota_mtech)

print "---------------------------------------------------------------------------"

print "MSC 18"
print "Harsh = " + str(harsh_msc)
print "NOTA = " + str(nota_msc)

print "---------------------------------------------------------------------------"

print "Girls Senator UG"
print "Shivani = " + str(shivani_girl)
print "Amitha = " + str(amitha_girl)
print "NOTA = " + str(nota_girl) 

print "---------------------------------------------------------------------------"

print "PhD"
print "Adarsh = " + str(adarsh_phd)
print "Rajesh = " + str(rajesh_phd)

print "---------------------------------------------------------------------------"

print "EE 17 CR"
print "Deepika = " + str(deepika_ee17)
print "Utsav = " + str(utsav_ee17)

print "---------------------------------------------------------------------------"

print "ME 17 CR"
print "Dhruvin = " + str(dhruvin_me)
print "Shivang = " + str(shivang_me)
print "Parth = " + str(parth_me)

print "---------------------------------------------------------------------------"

print "CE 17 CR"
print "Utkarsh = " + str(utkarsh_ce)
print "Nishant = " + str(nishant_ce)

print "---------------------------------------------------------------------------"

print "CSE 17 CR"
print "Harshil = " + str(harshil_cse)
print "Vraj = " + str(vraj_cse)

print "---------------------------------------------------------------------------"