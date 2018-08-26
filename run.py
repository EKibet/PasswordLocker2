import sys
import getpass
from user_data import Users
from format_outputs import *


def create_acc(u_name, u_pass):
    # u_pass= hashlib.new(u_pass)
    # encrypted_pass=sdigest(u_pass)
    if u_name != " " or u_pass != " ":
        new_acc =Users(u_name,u_pass)
        return new_acc
    else:
        print_e("Cannot save empty fields!")

def verify_user(uname,upass):
	'''
	Function that verifies the existance of the user before creating credentials
	'''
	checking_user = Users.check_user(uname,upass)

def save_acc_info(accout):
    accout.save_user()

credentials_message="\t\t\tBeware that the CM is case sensitive!"

def main():
    while True:
        print("Use these short code :\n\tCA - Create Acount,\n\tLI - Log in")
        short_code = input("\t")

        if short_code == 'CA':
            print_w (credentials_message)
            print("-"*10)

            print ("\tEnter Username: ")
            u_name = input("\t")

            print ("\tEnter Password:")
            u_pass = getpass.getpass("\t")
            save_acc_info(create_acc(u_name,u_pass))
            print_s(f"\t\t{u_name} account Successfully created\n")
        
        elif short_code == 'LI':
            print(credentials_message)
            print ("\tEnter Your Username: ")
            uname = input("\t\t")
            print("\tEnter your Password: ")
            upass = getpass.getpass("\t\t")
            user_exists = verify_user(uname,upass)
            if user_exists == uname:
                print_s("Welcome!")
        
        else:
            print("User does not exist")
            break
    else:
        print("Enter the specified options")
        # break

if __name__ == '__main__':
    main()