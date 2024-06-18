import json

with open("vaccination_centre.json") as infile:
    centre_data = json.load(infile)

def adminSetAppointment(state):
    with open("vaccination_centre.json") as infile:
        centre_data = json.load(infile)

    adminSetApptDate    = str(input("Date: "))
    adminSetApptTime    = str(input("Time: "))

    dateTimeMatch = False
    for i in range(1, len(centre_data[state])):
        if adminSetApptDate == centre_data[state][i]["date"] and adminSetApptTime == centre_data[state][i]["time"]:
            dateTimeMatch = True

            adminSetApptName    = str(input("Name: "))
            adminSetApptId      = str(input("ID: "))
            adminSetApptPhone   = str(input("Phone: "))
            adminSetApptRiskGrp = str(input("RiskGrp: "))

            center_data = open("vaccination_centre.json", "r")
            appt_data = json.load(center_data)
            center_data.close()

            appt_data[state][i]["name"] = adminSetApptName
            appt_data[state][i]["id"] = adminSetApptId
            appt_data[state][i]["rsvp"] = "n"
            appt_data[state][i]["phone"] = adminSetApptPhone
            appt_data[state][i]["risk_group"] = adminSetApptRiskGrp

            center_data = open("vaccination_centre.json", "w")
            json.dump(appt_data, center_data, indent=4)
            center_data.close()

    if dateTimeMatch == False:
        print("Date and time entered do not match any appointments.")