import json

with open("vaccination_centre.json") as infile:
    centre_data = json.load(infile)

def stateAppointmentList():
    with open("vaccination_centre.json") as infile:
        centre_data = json.load(infile)
        
    print("Please enter which state you would like the appointment listing for.")

    inputState = str(input("> "))
    inputState.lower()

    apptCenter = inputState + "_appointment"

    apptList = []
    apptList.append(centre_data)

    if (apptCenter in apptList[0]):
        #list of appt dates
        dateList = []

        #assigns all the date values in the json file to DateList
        apptData = centre_data[apptCenter]
        for d in apptData:
            dates = d.get("date", "")
            dateList.append(dates)

        #list of appt times
        timeList = []

        apptData = centre_data[apptCenter]
        for t in apptData:
            times = t.get("time", "")
            timeList.append(times)

        #list of patient names
        nameList = []

        apptData = centre_data[apptCenter]
        for n in apptData:
            names = n.get("name", "")
            nameList.append(names)

        #list of patient ids
        idList = []

        apptData = centre_data[apptCenter]
        for id in apptData:
            ids = id.get("id", "")
            idList.append(ids)

        #list of patient rsvp
        rsvpList = []

        apptData = centre_data[apptCenter]
        for r in apptData:
            rsvps = r.get("rsvp", "")
            rsvpList.append(rsvps)

        #list of patient phone numb
        phoneList = []

        apptData = centre_data[apptCenter]
        for p in apptData:
            phones = p.get("phone", "")
            phoneList.append(phones)

        #list of patient risk group
        riskGrpList = []

        apptData = centre_data[apptCenter]
        for risk in apptData:
            riskGrps = risk.get("risk_group", "")
            riskGrpList.append(riskGrps)

        centerName = centre_data[apptCenter][0]["center_name"]
        centerDistrict = centre_data[apptCenter][0]["district"]
        centerState = centre_data[apptCenter][0]["state"]

        print(f"\nAppointment List: {centerName}, {centerDistrict}, {centerState}\n")
        print(f'{"Date":9} {"Time":9} {"Name":45} {"ID":15} {"RSVP":5} {"Phone Number":13} {"Risk Group":1}')

        for i in range(len(centre_data[apptCenter])):
                print(f'{dateList[i]:9} {timeList[i]:9} {nameList[i]:45} {idList[i]:15} {rsvpList[i]:5} {phoneList[i]:13} {riskGrpList[i]:1}')
    
    else:
        print("Appointment list does not exist for that state.")
