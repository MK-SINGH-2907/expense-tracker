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
                    exit()
            else:
                print("Oops! Username already taken!")
        except ValueError:
            print("Enter a number")
        except Exception as e:
            print(f"Oops! Error: {e}")

def login():
    print("login")
