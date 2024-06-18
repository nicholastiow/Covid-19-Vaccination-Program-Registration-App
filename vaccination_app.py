# *******************************************************************************************
# Program : Group_5.py
# Course : PSP0101 PROBLEM SOLVING AND PROGRAM DESIGN
# Class : TL5V
# Trimester : 2110
# Year : 2021/22 Trimester 1
# Member_1 : 1211102285 | CHIN SHUANG YING      | 1211102285@student.mmu.edu.my | 016-6703743
# Member_2 : 1211101022 | ASHLEY SIM CI HUI     | 1211101022@student.mmu.edu.my | 016-7674038
# Member_3 : 1211102398 | NICHOLAS TIOW KAI BO  | 1211102398@student.mmu.edu.my | 012-5935388
# Member_4 : 1211100925 | ANG JIN NAN           | 1211100925@student.mmu.edu.my | 016-2601883
# *******************************************************************************************
# Task Distribution
# Member_1 : Categorize the public users into high-risk or low-risk based on their medical history, categorize public users into priority ranking based on their occupations, sort the public users according to their postcode, age, Covid-19 status, priority, group, etc
# Member_2 : Create vaccination centers: location and appointment slots, set appointment for public users, generate the list of assigned appointments
# Member_3 : Sign up and login authentication
# Member_4 : View appointment and RSVP
# *******************************************************************************************

import json
from datetime import datetime
from os import system

import admin569, state_appointment, state_assign, create_center

with open("users_info.json") as infile:
    users_info = json.load(infile)

def openUsersInfo():    
    with open ("users_info.json") as infile:
        users_info = json.load(infile)
    return users_info
    
def dumpUsersInfo(users_info):
    with open ("users_info.json", "w") as outfile:
        json.dump(users_info, outfile, indent = 4)

with open("vaccination_centre.json") as vaccine:
    appointmentData = json.load(vaccine)

def menu():
    print (" .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .-----------------. .----------------. ")
    print ("| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |")
    print ("| | ____   ____  | || |      __      | || |     ______   | || |     ______   | || |     _____    | || | ____  _____  | || |  _________   | |")
    print ("| ||_  _| |_  _| | || |     /  \     | || |   .' ___  |  | || |   .' ___  |  | || |    |_   _|   | || ||_   \|_   _| | || | |_   ___  |  | |")
    print ("| |  \ \   / /   | || |    / /\ \    | || |  / .'   \_|  | || |  / .'   \_|  | || |      | |     | || |  |   \ | |   | || |   | |_  \_|  | |")
    print ("| |   \ \ / /    | || |   / ____ \   | || |  | |         | || |  | |         | || |      | |     | || |  | |\ \| |   | || |   |  _|  _   | |")
    print ("| |    \ ' /     | || | _/ /    \ \_ | || |  \ `.___.'\  | || |  \ `.___.'\  | || |     _| |_    | || | _| |_\   |_  | || |  _| |___/ |  | |")
    print ("| |     \_/      | || ||____|  |____|| || |   `._____.'  | || |   `._____.'  | || |    |_____|   | || ||_____|\____| | || | |_________|  | |")
    print ("| |              | || |              | || |              | || |              | || |              | || |              | || |              | |")
    print ("| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |")
    print (" '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------' ")
    print ("----------------------------------------------------------")
    print ("Welcome to Covid-19 Vaccination Program Registration App!")
    print ("----------------------------------------------------------")
    print (" 1 ----> Sign up ")
    print (" 2 ----> User login ")
    print (" 3 ----> Admin login")
    print (" 4 ----> Vaccine information ")
    print (" 5 ----> Log out ")
    users_choice = int(input("Please enter your choice : "))
    if users_choice == 1 :
        sign_up()
    elif users_choice == 2:
        login()
    elif users_choice == 3:
        admin_login()
    elif users_choice == 4:
        vaccine_info()
    elif users_choice == 5:
        logout()

def sign_up():
    users_info = openUsersInfo()
    print ("---------------------------------------------")
    print ("========== Welcome to Sign Up page ==========")
    print ("---------------------------------------------\n")
    user = {}
    global name
    name = input("Please enter your full name ----> ")
    while name == "":
        print("Invalid input....")
        name = input("Please enter your full name ----> ")
    user["name"] = name
    print("\n")
    while True:
        try:
            age = int(input("Please enter your current age ----> "))
            user["age"] = str(age)
        except:
            print("Invalid input....")
            continue
        else:
            break

    print("\n")

    birthday = input("Please enter your birthday (DD/MM/YY) ---> ")
    user["birthday"] = birthday

    print("\n")
    
    while True:
        try:
            ic = str(input("Please enter your IC/Passport number (xxxxxx-xx-xxxx) ---> "))
            user["ic_passport_no"] = str(ic)
        except:
            print("Invalid input....")
            continue
        else:
            break

    print("\n")

    while True:
        try:
            phone_no = str(input("Please enter your phone number (xxx-xxxxxxxx) ---> "))
            user["phone_no"] = str(phone_no)
        except:
            print("Invalid input....")
            continue
        else:
            break
    
    print("\n")
    
    user["address"] = input("Please enter your current address ---> ")
    print("""
    1. Johor
    2. Malacca
    3. Selangor
    4. Kedah
    5. Kelantan
    6. Negeri Sembilan
    7. Pahang
    8. Penang
    9. Perak
    10. Perlis
    11. Sabah
    12. Sarawak
    13. Terengganu
    """)
    state = ["Johor","Melacca","Selangor","Kedah","Kelantan","Negeri Sembilan","Pahang","Penang","Perak","Perlis","Sabah","Sarawak","Terengganu"]
    stateChoice = input("Please enter your current state (1/2/3/4/5/6/7/8/9/10/11/12/13) ---> ")
    while stateChoice not in ("1","2","3","4","5","6","7","8","9","10","11","12","13"):
        print("Not an appropriate choice....Please enter again....")
        stateChoice = input("Please enter your current state (1/2/3/4/5/6/7/8/9/10/11/12/13) ---> ")
    
    u_state = state[int(stateChoice)-1]
    user["state"] = u_state
    print("\n")

    district = input("Please enter your current district ---> ")
    while district == "":
        print("Not an appropriate choice....Please enter again....")
        district = input("Please enter your current district ---> ")
    user["district"] = district

    print("\n")
    
    while True:
        try:
            postcode = str(input("Please enter your postcode ---> "))
        except:
            print("Invalid...\n")
            continue
        else:
            break
    
    while len(str(postcode)) != 5:
        print("Invalid...\n")
        while True:
            try:
                postcode = int(input("10. Please enter your postcode >>>"))
            except:
                print("Invalid...\n")
                continue
            else:
                break
        print("\n")
    
    str_post = str(postcode)
    user["postcode"] = str_post
    
    print("""
    Occupation/Career Fields\n
    1. Education
    2. Health and medical
    3. Transportation
    4. Manufacturing
    5. Government 
    6. Retired 
    7. Student
    8. Others
    """)
    occupation = ["Education","Health and medical","Transportation","Manufacturing","Government","Retired","Student","Others"]
    occupationChoice = input("Please choose your occupation (1/2/3/4/5/6/7/8) ---> ")
    while occupationChoice not in ("1","2","3","4","5","6","7","8"):
        print("Not an appropriate choice....Please enter again....")
        occupationChoice = input("Please choose your occupation (1/2/3/4/5/6/7/8) ---> ")
    occu = occupation[int(occupationChoice)-1]
    user["occupation"] = occu
    print("\n")
    password1 = input("Please enter your password ---> ")
    print("\n")
    password = input("Please enter your password again ---> ")
    if password1 == password:
        user["password"] = password1
    else:
        while password1 != password :
            print("Please ensure you type the same password as the first one.")
            user["password"] = input("Please enter your password again --->")

    input("Enter to continue some question....")

    print("------------------Medical History---------------------\n")
    print("""
        1. Are you exhibiting 2 or more symptoms as listed below? 
        - Fever
        - Chills
        - Shivering (rigor)
        - Body ache
        - Headache
        - Sore throat
        - Nausea or vomiting
        - Diarrhea
        - Fatigue
        - Runny nose or nasal congestion

        y - Yes
        n - No
        """)
    state1 = input(">>>")
    state1 = state1.lower()
    while state1 not in ('y','n'):
        print("Not an appropriate choice.\n")
        state1 = input(">>>")
        state1= state1.lower()
    user["mildsymptoms"] = state1
    print("\n")
    
    print("""
        2. Besides the above, are you exhibiting any of the symptoms listed below? 
        - Cough
        - Difficulty breathing
        - Loss of smell
        - Loss of taste

        y - Yes
        n - No
        """)
    state2 = input(">>>")
    state2= state2.lower()
    while state2 not in ('y','n'):
        print("Not an appropriate choice. \n")
        state2 = input(">>>")
        state2 = state2.lower()
    user["severe_symptoms"] = state2
    print("\n")

    print("""
        3. Have you attended any event/ areas associated with known COVID-19 cluster?
         
        y - Yes
        n - No
        """)
    state3 = input(">>>")
    state3 = state3.lower()
    while state3 not in ('y','n'):
        print("Not an appropriate choice.\n")
        state3 = input(">>>")
        state3 = state3.lower()
    user["cluster_risk"] = state3
    print("\n")

    print("""
        4. Have you travelled to any country outside Malaysia within 14 days before onset of symptoms? 
            
        y - Yes
        n - No
        """)
    state4 = input(">>>")
    state4= state4.lower()
    while state4 not in ('y','n'):
        print("Not an appropriate choice.\n")
        state4 = input(">>>")
        state4 = state4.lower()
    user["international_travel"] = state4
    print("\n")

    print("""
        5. Have you had close contact to confirmed or suspected case of COVID-19 within 14 days before onset of illness? 
                             
        y - Yes
        n - No
        """)
    state5 = input(">>>")
    state5 = state5.lower()
    while state5 not in ('y','n'):
        print("Not an appropriate choice.\n")
        state5 = input(">>>")
        state5 = state5.lower()
    user["close_contact"] = state5
    print("\n")

    print("""
        6. Are you a MOH COVID-19 volunteer in the last 14 days?
                                
        y - Yes
        n - No
        """)
    state6 = input(">>>")
    state6 = state6.lower()
    while state6 not in ('y','n'):
        print("Not an appropriate choice!\n")
        state6 = input(">>>")
        state6= state6.lower()
    user["covid_volunteer"] = state6
    print("\n")

    print("""
        7. Are you under quarantined?

        y - Yes
        n - No
        """)
    state7 = input(">>>")
    state7 = state7.lower()
    while state7 not in ('y','n'):
        print("Not an appropriate choice.\n")
        state7 = input(">>>")
        state7 = state7.lower()
    user["covid19_status"] = state7
    print("\n")

    print("""
        8. Have you received COVID-19 vaccine?

        0 - no
        1 - only one dose
        2 - completed two dose
        """)
    state8 = input(">>>")
    while state8 not in ('0','1','2'):
        print("Not an appropriate choice.\n")
        state8 = input(">>>")
    user["vaccination_status"] = state8

    print("Your Final Data..\n")
    print("\t1.  Name: ",name)
    print("\t3.  Age: ",str(age))
    print("\t4.  Birthday: ",birthday)
    print("\t5.  Password: ",password)
    print("\t6.  IC: ",ic)
    print("\t7.  HpNum: ",phone_no)
    print("\t8.  Occupation: ",occu)
    print("\t9.  Address: ",u_state)
    print("\t10. Postcode: ",str(postcode))
    print("\t11. District: ",district)

    print("\nQuestion...Double Comfirm\n")
    print("\ti.   Mild Symptoms: ",state1)
    print("\tii.  Severe Symptoms: ",state2)
    print("\tiii. Covid-19 Cluster Risk: ",state3)
    print("\tiv.  International Travel: ",state4)
    print("\tv.   Close Contact: ",state5)
    print("\tvi.  Covid-19 volunteer: ",state6)
    print("\tvii. Quarantined Status: ",state7)
    print("\tvii. Vaccination Status: ",state8)
    print("\n\n")


    print("\nIf everything fine...")
    print("\t1. Save")
    print("\t2. Delete\n")
    ans = input(">>>")
    while ans not in('1','2'):
        print("Invalid...\n")
        ans = input(">>>")
    
    if ans == '1':
        users_info.append(user)
        dumpUsersInfo(users_info)
        print("Your data had been recorded!")
        input("Press Enter Back To Main Menu..")
        menu()
    if ans == '2':
        print("Back To starting..\n")
        input("Enter To continue")
        sign_up()

def medicalHistory2():
    global user_login, history
    history = openUsersInfo()
    len_his = (len(history))
    for i in range(len_his):
        if history[i]["name"] == user_login:
            print("------------------Medical History---------------------")
            print("\t\t\t\tUsername: ",user_login,"\n")
            print("""
                1. Are you exhibiting 2 or more symptoms as listed below? 
                - Fever
                - Chills
                - Shivering (rigor)
                - Body ache
                - Headache
                - Sore throat
                - Nausea or vomiting
                - Diarrhea
                - Fatigue
                - Runny nose or nasal congestion

                y - Yes
                n - No
                """)
            state1 = input(">>>")
            state1=state1.lower()
            while state1 not in ('y','n'):
                print("Not an appropriate choice.\n")
                state1 = input(">>>")
                state1=state1.lower()
            history[i]["mildsymptoms"] = state1

            print("\n")
            
            print("""
                2. Besides the above, are you exhibiting any of the symptoms listed below? 
                - Cough
                - Difficulty breathing
                - Loss of smell
                - Loss of taste

                y - Yes
                n - No
                """)
            state2 = input(">>>")
            state2=state2.lower()
            while state2 not in ('y','n'):
                print("Not an appropriate choice. \n")
                state2 = input(">>>")
                state2=state2.lower()
            history[i]["severe_symptoms"] = state2

            print("\n")
        
            print("""
                3. Have you attended any event/ areas associated with known COVID-19 cluster?
                
                y - Yes
                n - No
                """)
            state3 = input(">>>")
            state3=state3.lower()
            while state3 not in ('y','n'):
                print("Not an appropriate choice.\n")
                state3 = input(">>>")
                state3=state3.lower()
            history[i]["cluster_risk"] = state3

            print("\n")
        
            print("""
                4. Have you travelled to any country outside Malaysia within 14 days before onset of symptoms? 
                    
                y - Yes
                n - No
                """)
            state4 = input(">>>")
            state4=state4.lower()
            while state4 not in ('y','n'):
                print("Not an appropriate choice.\n")
                state4 = input(">>>")
                state4=state4.lower()
            history[i]["international_travel"] = state4

            print("\n")
        
            print("""
                5. Have you had close contact to confirmed or suspected case of COVID-19 within 14 days before onset of illness? 
                                    
                y - Yes
                n - No
                """)
            state5 = input(">>>")
            state5=state5.lower()
            while state5 not in ('y','n'):
                print("Not an appropriate choice.\n")
                state5 = input(">>>")
                state5=state5.lower()
            history[i]["close_contact"] = state5

            print("\n")
        
            print("""
                6. Are you a MOH COVID-19 volunteer in the last 14 days?
                                        
                y - Yes
                n - No
                """)
            state6 = input(">>>")
            state6=state6.lower()
            while state6 not in ('y','n'):
                print("Not an appropriate choice!\n")
                state6 = input(">>>")
                state6=state6.lower()
            history[i]["covid_volunteer"] = state6

            print("\n")
        
            print("""
                7. Are you under quarantined?

                y - Yes
                n - No
                """)
            state7 = input(">>>")
            state7=state7.lower()
            while state7 not in ('y','n'):
                print("Not an appropriate choice.\n")
                state7 = input(">>>")
                state7=state7.lower()
            history[i]["covid19_status"] = state7

            print("\n")
        
            print("""
                8. Have you received COVID-19 vaccine?

                0 - no
                1 - only one dose
                2 - completed two dose
                """)
            state8 = input(">>>")
            state8=state8.lower()
            while state8 not in ('0','1','2'):
                print("Not an appropriate choice.\n")
                state8 = input(">>>")
                state8=state8.lower()
            history[i]["vaccination_status"] = state8

            print("\n")
            
            # history.append(history)

            admin569.categorize_by_risk()
            admin569.categorize_priority_ranking()
            
            with open ("users_info.json", "w") as outfile:
                json.dump(history, outfile, indent = 4)
    # else:
    #     print("Cannot find ...")
    #     input("Enter to continue...")
    #     menu()
    input("Press enter to continue...")

def login():
    global user_login
    with open ("users_info.json") as infile:
        users_info = json.load(infile)
    print ("-------------------------------------------")
    print ("========== Welcome to Login page ==========")
    print ("-------------------------------------------")
    user_login = input("Please enter your full name (same as the name when you sign up) ---> ")
    user_password = input("Please enter your password ---> ")
    for i in range (len(users_info)):
        if user_login == users_info[i]["name"] and user_password == users_info[i]["password"]:
            print(f"Welcome back, {user_login}!")
            user_menu()
        else:
            continue
    print("You have not sign up....Please sign up first before login....")
    menu()

def user_menu():
    print("==========User Menu==========")
    print("1 - Update personal information")
    print("2 - Update medical history")
    print("3 - Check Vaccination Appointment")
    print("4 - Back to main menu")
    choice = int(input("> "))

    if choice == 1:
        users_info = openUsersInfo()
        for i in range (len(users_info)):
            if users_info[i]["name"]==user_login:
                while True:
                    try:
                        age = int(input("Please enter your current age ----> "))
                        users_info[i]["age"] = str(age)
                    except:
                        print("Invalid input....")
                        continue
                    else:
                        break

                print("\n")

                birthday = input("Please enter your birthday (DD/MM/YY) ---> ")
                users_info[i]["birthday"] = birthday

                print("\n")
                
                while True:
                    try:
                        ic = str(input("Please enter your IC/Passport number ---> "))
                        users_info[i]["ic_passport_no"] = str(ic)
                    except:
                        print("Invalid input....")
                        continue
                    else:
                        break

                print("\n")

                while True:
                    try:
                        phone_no = str(input("Please enter your phone number ---> "))
                        users_info[i]["phone_no"] = str(phone_no)
                    except:
                        print("Invalid input....")
                        continue
                    else:
                        break
                
                print("\n")
                
                users_info[i]["address"] = input("Please enter your current address ---> ")

                print("""
                    1. Johor
                    2. Malacca
                    3. Selangor
                    4. Kedah
                    5. Kelantan
                    6. Negeri Sembilan
                    7. Pahang
                    8. Penang
                    9. Perak
                    10. Perlis
                    11. Sabah
                    12. Sarawak
                    13. Terengganu
                """)
                state = ["Johor","Melacca","Selangor","Kedah","Kelantan","Negeri Sembilan","Pahang","Penang","Perak","Perlis","Sabah","Sarawak","Terengganu"]
                stateChoice = input("Please enter your current state (1/2/3/4/5/6/7/8/9/10/11/12/13) ---> ")
                while stateChoice not in ("1","2","3","4","5","6","7","8","9","10","11","12","13"):
                    print("Not an appropriate choice....Please enter again....")
                    stateChoice = input("Please enter your current state (1/2/3/4/5/6/7/8/9/10/11/12/13) ---> ")
                
                u_state = state[int(stateChoice)-1]
                users_info[i]["state"] = u_state
                print("\n")

                district = input("Please enter your current district ---> ")
                while district == "":
                    print("Not an appropriate choice....Please enter again....")
                    district = input("Please enter your current district ---> ")
                users_info[i]["district"] = district

                print("\n")
                
                while True:
                    try:
                        postcode = str(input("Please enter your postcode --->"))
                    except:
                        print("Invalid...\n")
                        continue
                    else:
                        break
                
                while len(str(postcode)) != 5:
                    print("Invalid...\n")
                    while True:
                        try:
                            postcode = int(input("10. Please enter your postcode >>>"))
                        except:
                            print("Invalid...\n")
                            continue
                        else:
                            break
                    print("\n")
                
                str_post = str(postcode)
                users_info[i]["postcode"] = str_post
                
                print("""
                Occupation/Career Fields\n
                    1. Education
                    2. Health and medical
                    3. Transportation
                    4. Manufacturing
                    5. Government 
                    6. Retired 
                    7. Student
                    8. Others
                """)
                occupation = ["Education","Health and medical","Transportation","Manufacturing","Government","Retired","Student","Others"]
                occupationChoice = input("Please choose your occupation (1/2/3/4/5/6/7/8) ---> ")
                while occupationChoice not in ("1","2","3","4","5","6","7","8"):
                    print("Not an appropriate choice....Please enter again....")
                    occupationChoice = input("Please choose your occupation (1/2/3/4/5/6/7/8) ---> ")
                occu = occupation[int(occupationChoice)-1]
                users_info[i]["occupation"] = occu
                print("\n")
        dumpUsersInfo(users_info)

    elif choice == 2:
        medicalHistory2()
        dumpUsersInfo(history)

    #check vaccination appointment
    elif choice == 3:
        with open("vaccination_centre.json") as apptData:
            center_data = json.load(apptData)

        with open("users_info.json") as infile:
            user_info = json.load(infile)

        # check state user is located in
        for i in range(len(user_info)):
            if user_login == user_info[i]["name"]:

                global userState

                userState = user_info[i]["state"]
                userState = userState.lower()

        # check if user_login matches any of the names in vaccination_centre
                stateName = userState + "_appointment"
        
                assignAppt = False
                for r in range(1, len(center_data[stateName])):
                    if user_login == center_data[stateName][r]["name"]:
                        assignAppt = True
                    # if yes, print center_name, district, state, date, time
                        print(f'''
    Location: {center_data[stateName][0]["center_name"]}, {center_data[stateName][0]["district"]}, {center_data[stateName][0]["state"]}
    Date: {center_data[stateName][r]["date"]}
    Time: {center_data[stateName][r]["time"]}
    RSVP: {center_data[stateName][r]["rsvp"]}
                        ''')

                        if center_data[stateName][r]["rsvp"] == "n":
                            print("Would you like to RSVP for your appointment? (y/n)")

                            rsvpConfirm = str(input("> "))
                            rsvpConfirm = rsvpConfirm.lower()

                            if rsvpConfirm == "y":
                                center_data[stateName][r]["rsvp"] = "y"

                                with open('vaccination_centre.json', 'w') as outfile:
                                    json.dump(center_data, outfile, indent=4)

                            elif rsvpConfirm == "n":
                                center_data[stateName][r]["rsvp"] = "n"
                            
                            else:
                                print("Not an appropriate choice.")
                                user_menu()

                # if no, print that the user has not been assigned an appointment yet
                if assignAppt == False:
                    print("You have not been assigned an appointment yet.")

    elif choice == 4:
        menu()

    input("Press Enter Back To User Menu...")
    user_menu()

def admin_menu():
    print("""
    1 - Create vaccination center or appoinment slot
    2 - Set appointment for users
    3 - Sort user info
    4 - List of appointments
    5 - Back to main menu
    """)

    admin_choice = int(input("> "))

    #create vaccination center & appointment times
    if admin_choice == 1:
        print("""
    Please choose whether you would like to:
    1 - Create a vaccination center
    2 - Create an appointment slot
        """)
        centerOrAppt = int(input("> "))

        if centerOrAppt == 1:
            create_center.createVaccinationCenter()
        
        elif centerOrAppt == 2:
            create_center.createAppointment()

        else:
            print("Invalid input.")
            
        input("Press Enter Back To Admin Menu...")
        admin_menu()

    #set appointment
    elif admin_choice == 2:
        print("Please input the state of the vaccination centre for the appointment you would like to update.")

        inputState = str(input("> "))
        inputState.lower()
        apptUpdateState = inputState + "_appointment"
        
        state_assign.adminSetAppointment(apptUpdateState)
        #appointment_assign.adminUpdateAppointment()

    elif admin_choice == 3:
        #sort postcode etc
        sort_data = admin569.sort_user_data(users_info)
        admin569.print_user_data(sort_data)

    elif admin_choice == 4:
        state_appointment.stateAppointmentList()

    elif admin_choice == 5:
        menu()

    else:
        print("Invalid input.")

    input("Press Enter Back To Admin Menu...")
    admin_menu()

def admin_login():
    with open("admin.json") as admin_file:
        admin = json.load(admin_file)
    print("=====Welcome to Admin Login=====")
    admin_id = str(input("Please enter your admin id --->"))
    admin_password = str(input("Please enter your password --->"))
    #check admin id and password

    for i in admin:
        if admin_id == i["admin_id"] and admin_password == i["password"]:
            print(f"=====Welcome back, {admin_id}!=====")
            admin_menu()

    else:
        print("Wrong admin id or password...")
        input("Press Enter Back To Main Menu...")
        menu()

def vaccine_info():
    print("=====Vaccine Information=====")
    print("1. Pfizer-BioNTech")
    print("2. Sinovac")
    print("3. AstraZeneca")
    print("4. Back to main menu")
    vaccine = int(input("> "))
    while vaccine not in (1, 2, 3, 4):
        print("Invalid input. Please enter again.")
        vaccine = int(input("Please choose the type of vaccine by entering the number--->"))

    if vaccine == 1:
        print("=====Pfizer-BioNTech=====")
        print("""
        Name: BNT162b

        Manufacturer: Pfizer, Inc., and BioNTech

        Type of Vaccine: mRNA

        Number of Shots: 2 shots, 21 days apart
        Moderately to severely immunocompromised people should get an additional shot(3rd dose
        at least 28 days after their 2nd shot.

        Booster Shot:Some groups of people are recommended to get a booster shot at least 6 months
        after getting their second shot.

        How Given: shot in the muscle of the upper arm

        Does NOT Contain: eggs, preservatives, latex, metals

        Who should get vaccinated:
        →The Pfizer-BioNTech vaccine is recommended for people 12 years and older.

        Who should NOT get vaccinated:
        →If you had a severe allergic reaction(anaphylaxis) or an immediate allergic reaction.
        →If you had a severe or immediate allergic reaction after getting the first dose of a Pfizer-
         BioNTech COVID-19 Vaccine.

        If you are not able to get this vaccine, you may still be able to get a different type
        of COVID-19 vaccine.

        Possible Side Effects:
        →In the arm where you got shot:
            *pain
            *rednedd
            *swelling

        →throughout the rest of your body:
            *tiredness
            *headache
            *muscle pain
            *chills
            *fever
            *nausea

        """)

    elif vaccine == 2:
        print("=====Sinovac=====")
        print("""
        Research Name: CoronaVac
        Manufacturer: Sinovac
        Type of Vaccine: Inactivated

        Administration method: Intramuscular injection
        Number of Shots: 2 shots, 2 to 4 weeks apart

        Based on information provided by the manufacturer, the CoronaVac vaccine has shown to be 51% effective against symptomatic infection.
        It was also shown to be 100% effective against hospitalization and severe disease.

        Common side effects after the SinoVac vaccine include:

        →Pain at the injection site
        →Headache
        →Tiredness
        →Muscle aches

        The vaccine is not recommended for persons younger than 18 years of age, pending the results of further studied in that age group.

        Vaccination is recommended for persons with comorbidities that have been identified as increasing the risk of severe COVID-19, including obesity, cardiovascular disease, respiratory disease and diabetes.

        Vaccination can be offered to people who have had COVID-19 in the past.

        Vaccine effectiveness is expected to be similar in lactating women as in other adults.
        
        Persons living with HIV or auto-immune conditions or who are immunocompromised may be vaccinated after receiving information and counselling. 

        Individuals with a history of anaphylaxis to any component of the vaccine should not take it.

        Persons with acute PCR-confirmed COVID-19 should not be vaccinated until after they have recovered from acute illness and the criteria for ending isolation have been met.

        Anyone with a body temperature over 38.5°C should postpone vaccination until they no longer have a fever.
        """)

    elif vaccine == 3:
        print("=====AstraZeneca=====")
        print("""
        AstraZeneca COVID-19 vaccine is effective at preventing hospitalisations, intensive care unit (ICU) 
        admissions and deaths due to COVID-19. The most common side effects are usually mild or moderate and get 
        better within a few days. The most serious side effects are very rare cases of unusual blood clots with 
        low blood platelets, which are estimated to occur in 1 in 100,000 vaccinated people. People should seek medical 
        assistance if they have symptoms.

        Research name: AZD1222 (ChAdOx1)

        Manufacturer/developer: AstraZeneca, University of Oxford

        Vaccine type: Non-Replicating Viral Vector

        How Given: shot in the muscle of the upper arm

        number of shots: 2 shots, 4 to 12 weeks apart

        who is the vaccine not recommended for:
        The vaccine is not recommended for persons younger than 18 years of age pending the results of further studies.

        Should pregnant women be vaccinated?:
        While pregnancy puts women at higher risk of severe COVID-19, very little data are available to assess vaccine safety in pregnancy. 

        Pregnant women may receive the vaccine if the benefit of vaccinating a pregnant woman outweighs the potential vaccine risks. 

        For this reason, pregnant women at high risk of exposure to SARS-CoV-2 (e.g. health workers) or who have comorbidities which add 
        to their risk of severe disease, may be vaccinated in consultation with their health care provider.

        common side effects:
        →Pain or tenderness at the injection site
        →Headache
        →Tiredness
        →Muscle or joint aches
        →Fever
        →Chills
        →Nausea
        """)

    elif vaccine == 4:
        menu()

    print("""
1 - Back to vaccine information menu
2 - Back to main menu
""")

    vaccineOrMain = int(input("> "))

    if vaccineOrMain == 1:
        vaccine_info()

    if vaccineOrMain == 2:
        menu()
    

def logout():
    print(" ██████╗  ██████╗  ██████╗ ██████╗ ██████╗ ██╗   ██╗███████╗██╗██╗██╗")
    print("██╔════╝ ██╔═══██╗██╔═══██╗██╔══██╗██╔══██╗╚██╗ ██╔╝██╔════╝██║██║██║")
    print("██║  ███╗██║   ██║██║   ██║██║  ██║██████╔╝ ╚████╔╝ █████╗  ██║██║██║ ")
    print("██║   ██║██║   ██║██║   ██║██║  ██║██╔══██╗  ╚██╔╝  ██╔══╝  ╚═╝╚═╝╚═╝")
    print("╚██████╔╝╚██████╔╝╚██████╔╝██████╔╝██████╔╝   ██║   ███████╗██╗██╗██╗")
    print(" ╚═════╝  ╚═════╝  ╚═════╝ ╚═════╝ ╚═════╝    ╚═╝   ╚══════╝╚═╝╚═╝╚═╝")
    timeline = datetime.now()
    print(timeline)
    exit()

menu()