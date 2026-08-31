from getpass import getpass
from manager import Passsword_manager
from credential import Credential
from master import MasterAuth
auth = MasterAuth()
if not auth.master_exists():
    auth.create_master_password()
else:
    if not auth.verify_master_password():
        exit()
manager = Passsword_manager()
print("\n==== Credential Manager ====\n")
while True:
    print("\n1. Add Credential\n2. View Credentials\n3. Search Credential\n4. Update Credential\n5. Delete Credential\n6. Exit\n")
    while True:
        try:
            choice = int(input("Enter choice : "))
            break
        except ValueError:
            print("Enter a valid choice")
    if choice == 1:
        website = input("Enter website name : ")
        email = input("Enter your email : ")
        username = input("Enter your username : ")
        while True:
            option = input("Do you want to generate password? (y/n) : ").lower()
            if option == "y":
                password = manager.generate_password()
                print(f"Your password is generated successfuly.\n  Your password is {password}\n")
                break
            elif option == "n":
                password = getpass("Enter your password : ")
                print("Password saved. \n")
                break
            else :
                print("Enter a valid choice.")
        credential = Credential(website,email,username,password)
        manager.add_credential(credential)
    elif choice == 2:
        manager.view_credential()
    elif choice == 3:
        web = input("Enter website name: ")
        manager.search_by_website(web)
    elif choice == 4:
        web = input("Enter website name : ")
        manager.update_credential(web)
    elif choice == 5:
        email = input("Enter your email : ")
        manager.delete_credential(email)
    elif choice == 6:
        print("\n ==== Thanks for visiting ====\n")
