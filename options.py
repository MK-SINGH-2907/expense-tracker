#features

import json
import maskpass

def signup():
    while True:
        try:
            data = json.load(open("details.json"))
            uname = input("Enter username: ")
            pwd = maskpass.askpass("Enter password: ", mask="*")
            sav = float(input("Enter savings(if any): "))
            found = False
            for user in data["accounts"]:
                if user["username"] == uname:
                    found = True
                    break
            if not found:
                data["accounts"].append({"username": uname, "password": pwd, "savings": sav, "earnings": 0, "expenditure": 0})
                with open("details.json", "w+") as f:
                    json.dump(data, f)
                    print("Signed In!!")
                login()  
            else:
                print("Oops! Username already taken!")
        except ValueError:
            print("Enter a number")
        except Exception as e:
            print(f"Oops! Error: {e}")

def login():
    while True:
        try:
            data = json.load(open("details.json"))
            uname = input("Enter username: ")
            pwd = maskpass.askpass("Enter password: ", mask="*")
            found = False
            for user in data["accounts"]:
                if user["username"] == uname and user["password"] == pwd:
                    found = True
                    break
            if found:
                print("\t Logged in!!")
                menu(uname, pwd)
                exit()
        except Exception as e:
            print(f"Oops! Error: {e}")

def getinfo(uname, pwd):
    try:
        data = json.load(open("details.json"))
        found = False
        info = ""
        for user in data["accounts"]:
            if user["username"] == uname and user["password"] == pwd:
                info = user
                found = True
                break
        if found:
            return info
    except Exception as e:
        print(f"Oops! Error: {e}")

def menu(uname, pwd):
    while True:
        try:
            userinfo = getinfo(uname, pwd)
            savings = userinfo["savings"]
            expenditure = userinfo["expenditure"]
            earnings = userinfo["earnings"]

            print("\t MENU")
            print(f"Current Savings: {savings}")
            print(f"Total expenditure: {expenditure}")
            print(f"Total earnings: {earnings}")
            print()
            print("1. Add earnings \n2. Add expenditure \n3. Exit")
            uinput = int(input("Enter your choice: "))
            if uinput == 1:
                addear(uname, pwd)
            elif uinput == 2:
                addexp(uname, pwd)
            elif uinput == 3:
                exit()
            else:
                print("Enter correct value!!")
        except Exception as e:
            print(f"Oops! Error: {e}")

def addear(uname, pwd):
    try:
        data = json.load(open("details.json"))
        for user in data["accounts"]:
            if user["username"] == uname and user["password"] == pwd:
                ear = float(input("Enter amount earned: "))
                user["earnings"] += ear
                user["savings"] += ear
                with open("details.json", "w+") as f:
                    json.dump(data, f)
                    print("Data added successfully")
    except ValueError:
        print("Oops! Enter correct Value")
    except Exception as e:
        print(f"Oops! Error: {e}")
def addexp(uname, pwd):
    try:
        data = json.load(open("details.json"))
        for user in data["accounts"]:
            if user["username"] == uname and user["password"] == pwd:
                exp= float(input("Enter amount spent: "))
                user["expenditure"] += exp
                user["savings"] = user["savings"] - exp
                with open("details.json", "w+") as f:
                    json.dump(data, f)
                    print("Data added successfully")
    except ValueError:
        print("Oops! Enter correct Value")
    except Exception as e:
        print(f"Oops! Error: {e}")
