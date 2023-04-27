import time
import getch

login_attempts = 3

while login_attempts > 0:
    login = input("Enter your login: ")
    password = ""

    print("Enter your password: ", end="")
    while True:
        key = getch.getch()
        if key == "\n":
            break
        password += key
        print("*", end="", flush=True)

    if login == "my_login" and password == "my_password":
        print("\nLogin effectuated with success!")
        break
    else:
        print("\nLogin failed. Please try again.")
        login_attempts -= 1

if login_attempts == 0:
    print("Maximum login attempts reached. Program exiting.")
else:
    print("Loading...", end="")
    for i in range(30):
        print(".", end="", flush=True)
        time.sleep(1)
    print("\nProgram finished.")