#features

import json

def signup():
    while True:
        try:
            data = json.load(open("details.json", "r+"))
            uname = input("Enter username: ")
            pwd = input("Enter password: ")
            sav = float(input("Enter savings(if any): "))
            for user in data["accounts"]:
                if user["username"] == uname:
                    print("Username Already taken!! Use another username")
                else:
                    data = data["accounts"].append({"username": uname, "password": pwd, "savings": sav, "earnings": 0, "expenditure": 0})
                    with open("details.json", "w+") as f:
                        json.dump(data, f)
                    exit()
        except ValueError:
            print("Enter a number")
        except Exception as e:
            print(f"Oops! Error: {e}")

def login():
    print("login")
