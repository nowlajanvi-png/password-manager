
import json
import os

FILE = "passwords.json"

def load_passwords():
    if os.path.exists(FILE):
        with open(FILE, "r") as file:
            return json.load(file)
    return {}

def save_passwords(passwords):
    with open(FILE, "w") as file:
        json.dump(passwords, file, indent=4)

def main():
    passwords = load_passwords()

    while True:
        print("\n--- Password Manager ---")
        print("1. Add password")
        print("2. View passwords")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            website = input("Enter website: ")
            username = input("Enter username: ")
            password = input("Enter password: ")

            passwords[website] = {
                "username": username,
                "password": password
            }

            save_passwords(passwords)
            print("Password saved successfully!")

        elif choice == "2":
            for website, details in passwords.items():
                print("\nWebsite:", website)
                print("Username:", details["username"])
                print("Password:", details["password"])

        elif choice == "3":
            print("Thank you for using Password Manager!")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
