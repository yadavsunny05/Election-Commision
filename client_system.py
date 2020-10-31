from new_system import *
from selenium import webdriver
import socket
import xlrd

##########################################################################################################################
##
##  Change MTech and all that from 18 -> 17
##
##########################################################################################################################


host = raw_input("Enter host: ")
port = int(raw_input("Enter the port number: "))
client = Client()
client.connect(host, port)
browser = webdriver.Chrome()

book = xlrd.open_workbook('Current List of Students On Roll.xlsx')
sheet = book.sheet_by_name('Sheet3')
data = [[sheet.cell_value(r, c) for c in range(sheet.ncols)] for r in range(sheet.nrows)]
student_data = []

while(True):
    client.get_roll()
    roll_number = float(client.roll + '.0')
    #if client.check == True:
    #print data
    print "\n"
    for i in data:
        if roll_number in i:
            student_data = i
    print student_data
    roll_number = str(roll_number)

    token  = client.code

    print token

    ####################################################################################################################################
    ##
    ##  For BTech we check the 1x11 part but for higher we check their Department
    ##
    ####################################################################################################################################

    # BTech 18
    # if roll_number[:4] == "1811" and "CL" in student_data:
    #     print "BTech 17 CL\n"
    #     browser.get("http://localhost:3000/election")
    # elif roll_number[:4] == "1811" and "CE" in student_data:
    #     print "BTech 17 CE\n"
    #     browser.get("https://docs.google.com/forms/d/e/1FAIpQLSe0hAO3UJ9xIfTSf_N6td9ZNDdZTJo62n4N95UsrSA_pZ9Etg/viewform?usp=pp_url&entry.187535728=" + token)
    #
    # elif roll_number[:4] == "1811" and "EE" in student_data:
    #     print "BTech 17 EE\n"
    #     browser.get("https://docs.google.com/forms/d/e/1FAIpQLSeWhHNdBP7iUJiEBTQerpaLMXDjl-t4Q_fH1WZ2GbQ3eUYMUw/viewform?usp=pp_url&entry.187535728=" + token)
    #
    # elif roll_number[:4] == "1811" and "ME" in student_data:
    #     print "BTech 17 ME\n"
    #     browser.get("https://docs.google.com/forms/d/e/1FAIpQLSeBU3e_q2e9qubRjE3yKIhtEOAxbO-8PpcV78-LGYdFHp99_A/viewform?usp=pp_url&entry.187535728=" + token)
    #
    # elif roll_number[:4] == "1811" and "CSE" in student_data:
    #     print "BTech 17 ME\n"
    #     browser.get("https://docs.google.com/forms/d/e/1FAIpQLSfFYl1UkKL4pyWjkNIw-m2BEhUOFQGbuSpLiHSDSgXiizbIEQ/viewform?usp=pp_url&entry.187535728=" + token)
    #
    # else:
    #     print "BTech 17 ME\n"
    #     browser.get("https://docs.google.com/forms/d/e/1FAIpQLSeU6n0iCqXIbD_7_i0R_pU0JMPk9N8-6lS5iUFFZ2bcEhWKoA/viewform?usp=pp_url&entry.187535728=" + token)

    # BTech 17
    if roll_number[:4] == "1711" and "F" not in student_data and "Female" not in student_data :
        print "BTech 17 Boy\n"
        browser.get("http://localhost:3000/election?key=btech17")
    elif roll_number[:4] == "1711":
        print "BTech 17 Girl\n"
        browser.get("http://localhost:3000/election?key=btech17_girls")
    # elif roll_number[:4] == "1711" and "F" not in student_data and "Female" not in student_data and "ME" in student_data:
    #     print "BTech 17 ME Boy\n"
    #     browser.get("https://docs.google.com/forms/d/e/1FAIpQLSfrORXvEWEEBzLwvM-uUgvQi87h1T9NM0SPJ1_Y7Kk0Ine6_w/viewform?usp=pp_url&entry.717047873=" + token)
    #
    # elif roll_number[:4] == "1711" and "F" not in student_data and "Female" not in student_data and "CSE" in student_data:
    #     print "BTech 17 CSE Boy\n"
    #     browser.get("https://docs.google.com/forms/d/e/1FAIpQLSdexTvnpJg4lQhKt4VWv6gPl4zqG5iEUUEu5Z2vdhqi3UHvGw/viewform?usp=pp_url&entry.309019178=" + token)
    # elif roll_number[:4] == "1711" and "CSE" in student_data:
    #     print "BTech 17 CSE Girl\n"
    #     browser.get("https://docs.google.com/forms/d/e/1FAIpQLScB4ANSRI7lTQOauwAE8zrvKm5RCbMDRmg5IALJCnGXPeyThg/viewform?usp=pp_url&entry.1540027253=" + token)
    #
    # elif roll_number[:4] == "1711" and "F" not in student_data and "Female" not in student_data and "CE" in student_data:
    #     print "BTech 17 CE Boy\n"
    #     browser.get("https://docs.google.com/forms/d/e/1FAIpQLSeWQS9NR3aOU5Sho3sHuimapd2dJs_U0-3MvBHIP1XWnymvtA/viewform?usp=pp_url&entry.309019178=" + token)
    # elif roll_number[:4] == "1711" and "CE" in student_data:
    #     print "BTech 17 CE Girl\n"
    #     browser.get("https://docs.google.com/forms/d/e/1FAIpQLSdCuR5t_2wX-oBv-dPKBUpO70yD2dD9l73ZeBYx2P5yjVz-DA/viewform?usp=pp_url&entry.1540027253=" + token)
    elif roll_number[:4] == "1811" and "F" not in student_data and "Female" not in student_data :
        print "BTech 18 Boy\n"
        browser.get("http://localhost:3000/election?key=btech18")
    elif roll_number[:4] == "1811":
        print "BTech 18 Girl\n"
        browser.get("http://localhost:3000/election?key=btech18_girls")

    elif roll_number[:4] == "1611" and "F" not in student_data and "Female" not in student_data :
        print "BTech 16 Boy\n"
        browser.get("http://localhost:3000/election?key=btech16")
    elif roll_number[:4] == "1611":
        print "BTech 16 Girl\n"
        browser.get("http://localhost:3000/election?key=btech16_girls")
    elif roll_number[:4] == "1511" and "F" not in student_data and "Female" not in student_data :
        print "BTech 15 Boy\n"
        browser.get("http://localhost:3000/election?key=btech15")
    elif roll_number[:4] == "1511":
        print "BTech 15 Girl\n"
        browser.get("http://localhost:3000/election?key=btech15_girls")


    elif roll_number[:2] == "18" and "F" not in student_data and "Female" not in student_data and "M.Tech" in student_data :
        print "MTECH 18 Boy\n"
        browser.get("http://localhost:3000/election?key=Mtech18")
    elif roll_number[:2] == "18" and "M.Tech" in student_data:
        print "MTECH 18 Girl\n"
        browse.get("http://localhost:3000/election?key=Mtech18_girls")
    elif roll_number[:2] == "18" and "F" not in student_data and "Female" not in student_data and "M.Sc" in student_data :
        print "MSC 18 Boy\n"
        browser.get("http://localhost:3000/election?key=MSC18")
    elif roll_number[:2] == "18" and "M.Sc" in student_data:
        print "MSC 18 Girl\n"
        browser.get("http://localhost:3000/election?key=MSC18_girls")

    elif roll_number[:2] == "18" and "F" not in student_data and "Female" not in student_data and "MASC" in student_data :
        print "MA 18 Boy\n"
        browser.get("http://localhost:3000/election?key=MA18")
    elif roll_number[:2] == "18" and "MASC" in student_data:
        print "MA 18 Girl\n"
        browser.get("http://localhost:3000/election?key=MA18_girls")
    #M.Tech 17 Boy
    elif roll_number[:2] == "17" and "Male" in student_data and "M.Tech" in student_data:
        print "MTech 17 Boy\n"
        browser.get("http://localhost:3000/election?key=btech15_boys")
    #M.Tech 17 Girl
    elif roll_number[:2] == "17" and "Female" in student_data and "M.Tech" in student_data:
        print "MTech 17 Girl\n"
        browser.get("http://localhost:3000/election?key=PG(2nd Year) Girls (Masters)")
    #B.Tech - M.Sc Dual Degree Boy
    elif roll_number[:2] == "14" and "Male" in student_data and "B.Tech-M.Sc Dual degree" in student_data:
        print "M.Sc 14 Dual Degree Boy\n"
        browser.get("http://localhost:3000/election?key=MSC_18_Boys")
    #B.Tech - M.Sc Dual Degree Boy
    elif roll_number[:2] == "14" and "Female" in student_data and "B.Tech-M.Sc Dual degree" in student_data:
        print "M.Sc 14 Dual Degree Girl\n"
        browser.get("http://localhost:3000/election?key=MSC_18_Girls")
    #M.Sc 17 Boy
    elif roll_number[:2] == "17" and "Male" in student_data and "M.Sc" in student_data:
        print "M.Sc 17 Boy\n"
        browser.get("http://localhost:3000/election?key=btech15_boys")
    #M.Sc 17 Girl
    elif roll_number[:2] == "17" and "Female" in student_data and "M.Sc" in student_data:
        print "M.Sc 17 Girl\n"
        browser.get("http://localhost:3000/election?key=PG(2nd Year) Girls (Masters)")
#M.A 17 Boy
    elif roll_number[:2] == "17" and "Male" in student_data and "MASC" in student_data:
        print "MASC 17 Boy\n"
        browser.get("http://localhost:3000/election?key=btech15_boys")
    #M.A 17 Girl
    elif roll_number[:2] == "17" and "Female" in student_data and "MASC" in student_data:
        print "MASC 17 Girl\n"
        browser.get("http://localhost:3000/election?key=PG(2nd Year) Girls (Masters)")
    #Ph.D - Boy
    elif "Male" in student_data and "Ph.D" in student_data:
        print "Ph.D Boy\n"
        browser.get("http://localhost:3000/election?key=Phd_Boys")
    #Ph.D - Girl
    elif "Female" in student_data and "Ph.D" in student_data:
        print "Ph.D Girl\n"
        browser.get("http://localhost:3000/election?key=Phd_Boys")

    #B.Tech M.Tech Dual Degree Boy
    elif roll_number[:2] == "14" and "Male" in student_data and "B.Tech-M.Tech Dual degree" in student_data:
        print "MTech 14 Dual Degree Boy\n"
        browser.get("http://localhost:3000/election?key=Mtech_18_Boys")
    #B.Tech M.Tech Dual Degree Boy
    elif roll_number[:2] == "14" and "Female" in student_data and "B.Tech-M.Tech Dual degree" in student_data:
        print "MTech 14 Dual Degree Girl\n"
        browser.get("http://localhost:3000/election?key=Mtech_18_Girls")

    else:
        print "Rest"
        browser.get("http://localhost:3000/election?key=btech15_boys")
