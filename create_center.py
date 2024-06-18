import json

with open("vaccination_centre.json") as infile:
    centerData = json.load(infile)

def createVaccinationCenter():
    global newCenter, centerName, apptName

    newCenter = {}
    print("Please input which state your new vaccination center is located in.")

    centerName = str(input("> "))
    apptName = centerName.lower() + "_appointment"

    center_data = open("vaccination_centre.json", "r")
    appt_data = json.load(center_data)
    center_data.close()

    appt_data[apptName] = []

    center_data = open("vaccination_centre.json", "w")
    json.dump(appt_data, center_data, indent=4)
    center_data.close()

    inputCenterInfo()

def inputCenterInfo():
    with open("vaccination_centre.json") as infile:
        centerData = json.load(infile)

    centerInfo = {}
    centerInfo["center_name"] = str(input("\nPlease input the name of the vaccination center: "))
    centerInfo["district"] = str(input("Please input the district the center is located in: "))
    centerInfo["state"] = centerName.capitalize()
    
    print("\nA new vaccination center has been created.")

    centerData[apptName].append(centerInfo)
    with open('vaccination_centre.json', 'w') as outfile:
        json.dump(centerData, outfile, indent=4)

def chooseApptCreationState():
    global stateKey

    print("Please enter the state that you would like to create an appointment for.")

    chooseState = str(input("> "))
    chooseState.lower()

    stateKey = chooseState + "_appointment"

def createAppointment():
    with open("vaccination_centre.json") as infile:
        centerData = json.load(infile)

    print("Please input the state in which your chosen vaccination centre is located.")
    inputCenterState = str(input("> "))

    centerState = inputCenterState + "_appointment"

    print("Please input the date of your newly created appointment in the format DD/MM/YY.")
    inputApptDate = str(input("> "))

    print("Please input the time of your newly created appointment in the format HH:MM:SS.")
    inputApptTime = str(input("> "))

    newAppt = {}
    newAppt["date"] = inputApptDate
    newAppt["time"] = inputApptTime
    newAppt["name"] = ""
    newAppt["id"] = ""
    newAppt["rsvp"] = ""
    newAppt["phone"] = ""
    newAppt["risk_group"] = ""

    centerData[centerState].append(newAppt)

    print("New appointment has been created.")

    with open('vaccination_centre.json', 'w') as outfile:
        json.dump(centerData, outfile, indent=4)