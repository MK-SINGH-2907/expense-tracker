#functions

import options as op

while True:
    print("\t MENU")
    print("1. Sign up \n2. Log in \n3. Exit")
    try:
        userinput = int(input("Choose the option: "))
        if userinput == 1:
            op.signup()
        elif userinput == 2:
            op.login()
        elif userinput == 3:
            exit()
        else:
            print("Choose the right option.")
    except ValueError:
        print("Choose the right option.")
    except Exception as e:
        print(f"Oops! Error: {e}")
