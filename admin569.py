import json

def openUsersInfo():
    global user
    with open('users_info.json') as infile:
        user = json.load(infile)

#categorize the public users into high-risk or low-risk based on their medical history
def categorize_by_risk():
    openUsersInfo()
    users_info = user
    for x in users_info:
        if "y" in list(x.values()):         #lower case or upper case
            x["covid_19_risk"]="high risk"
        else:
            x["covid_19_risk"]="low risk"
    return users_info

#categorize the public users into priority ranking
# from 1(lowest priority) to 5(highest priority)
#based on occupations
def categorize_priority_ranking():
    openUsersInfo()
    users_info = user
    for x in users_info:
        if x["occupation"]=="Health and medical":
            x["priority_ranking"]=5
        elif x["occupation"]=="Government" or x["occupation"]=="Education":
            x["priority_ranking"]=4
        elif x["occupation"]=="Transportation" or x["occupation"]=="Retired":
            x["priority_ranking"]=3
        elif x["occupation"]=="Manufactoring":
            x["priority_ranking"]=2
        else:
            x["priority_ranking"]=1
    return users_info

#sort user data based on postcode, age, Covid-19 Status, priority
def sort_user_data(users_info):
    print("Sort by")
    print("1. postcode")  
    print("2. age")
    print("3. Covid-19 Risk")
    print("4. Priority Ranking")
    sort = int(input("Please enter the number of which the list be sorted by?"))
    while sort not in (1,2,3,4):
        print("Invalid number. Please reenter the number.")
        sort = int(input("Please enter the number of which the list be sorted by?---->"))
    if sort == 1:
        sort_by_postcode = sorted(users_info,key=lambda i:i["postcode"])   
        return sort_by_postcode   
    elif sort == 2:
        sort_by_age = sorted(users_info,key=lambda i:i["age"])               
        return sort_by_age  
    elif sort == 3:
        sort_by_covid_19_risk = sorted(users_info,key=lambda i:i["covid_19_risk"])
        return sort_by_covid_19_risk
    elif sort == 4:
        sort_by_priority_ranking = sorted(users_info,key=lambda i:i["priority_ranking"])
        return sort_by_priority_ranking

#print all user info in a table
def print_user_data(sort_data):
    for i in sort_data:
        for key,info in i.items():
            print(f"{key:25}|{info}")
        print()

# categorize_by_risk()
# categorize_priority_ranking()
# sort_user_data()
# print_user_data()