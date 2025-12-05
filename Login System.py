# Introduce User to Program
def main():
    while True:
        try:  # Main Program Screen
            selection = int(input(
                "Welcome to the Python Login Calculator! \n"
                "Please Choose an Option listed below by typing the number next to the option you would like to use\n"
                "1. Create a New Account\n"
                "2. Login Using Existing Credentials\n\n"
                "Please input your option of choice here: "
            ))

            if selection == 1:
                createAccount()
            elif selection == 2:
                login()
            else:
                print("Please select one of the listed options (1 or 2).")
        except ValueError:
            print("Invalid input! Please enter a number (1 or 2).")


# Shift Program Towards the Account Creation Phase
def createAccount():
    print("\nYou have chosen to Create a New Account. To cancel at any point, type 'Cancel' into the input box.\n")

    while True:
        createdAccount = input("Please enter a username here: ")

        if createdAccount.lower() == "cancel":
            print("Account creation canceled.\n")
            return

        if userExists(createdAccount):
            print("Username already exists. Please choose a different one.\n")
        else:
            break

    createdPassword = input("Please enter a password here: ")

    if createdPassword.lower() == "cancel":
        print("Account creation canceled.\n")
        return

    # Save to users.txt
    with open("users.txt", "a") as f:
        f.write(f"{createdAccount},{createdPassword}\n")

    print("\nAccount created successfully!")
    print(f"Username: {createdAccount}")
    print(f"Password: {createdPassword}\n")


# Helper function to check if username already exists
def userExists(username):
    try:
        with open("users.txt", "r") as f:
            for line in f:
                stored_username, _ = line.strip().split(",", 1)
                if stored_username == username:
                    return True
    except FileNotFoundError:
        return False
    return False


# Login function
def login():
    print("\nYou have chosen to Login with an Existing Account.\n")

    while True:
        username = input("Enter your username: ")
        if username.lower() == "cancel":
            print("Login canceled.\n")
            return

        user_found, correct_password = getUserCredentials(username)
        if not user_found:
            print("Username not found. Please try again.\n")
            continue

        while True:
            password = input("Enter your password: ")
            if password.lower() == "cancel":
                print("Login canceled.\n")
                return

            if password == correct_password:
                print(f"\nLogin Successful! Welcome back, {username}.\n")
                return
            else:
                print("Incorrect password. Please try again.\n")


# Helper to fetch user info from users.txt
def getUserCredentials(username):
    try:
        with open("users.txt", "r") as f:
            for line in f:
                stored_username, stored_password = line.strip().split(",", 1)
                if stored_username == username:
                    return True, stored_password
    except FileNotFoundError:
        pass
    return False, None


# Run The Program
main()

 
