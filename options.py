#features

import json

def signup():
    try:
        data = json.load(open("details.json", "r+"))
        uname = input("Enter username: ")
        pwd = input("Enter password: ")
        sav = float(input("Enter savings(if any): "))
        for user in data["accounts"]:
            if user["username"] == uname:
                print("Username Already taken!! Use another username")
                signup()
            else:
                data = data["accounts"].append({"username": uname, "password": pwd, "savings": sav, "earnings": 0, "expenditure": 0})
    except ValueError:
        print("Enter a number")
        signup()
    except Exception as e:
        print(f"Oops! Error: {e}")
        signup()

def login():
    print("login")
