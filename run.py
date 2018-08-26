import sys
import getpass
from user_data import Users
from format_outputs import *
import random
from time import sleep
from credentials import Credentials


def create_acc(u_name, u_pass):
    # u_pass= hashlib.new(u_pass)
    # encrypted_pass=sdigest(u_pass)
    new_acc =Users(u_name,u_pass)
    return new_acc
    
def display_credentials():
    return Credentials.display_credentials()

def verify_user(uname,upass):
    '''
	Function that verifies the existance of the user before creating credentials
	'''
    checking_user = Users.check_user(uname,upass)
    return checking_user

def save_acc_info(accout):
    accout.save_user()

def save_credentials(cred):
    Credentials.save_credential(cred)


def create_credentials(site_name,username, user_password):
    new_credential = Credentials(site_name,username, user_password)
    return new_credential

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
        
        if short_code == 'LI':
            print(credentials_message)
            print ("\tEnter Your Username: ")
            uname = input("\t\t")
            print("\tEnter your Password: ")
            upass = getpass.getpass("\t\t")
            user_exists = verify_user(uname,upass)
            if user_exists == uname:
                while True:
                    print("Please choose one of the following options\n \tSC - Save Credentials \n \tDC - Display Credentials \n \tDL - DeleteCredential")
                    cred_input=input("\t\t")
                    if cred_input== "SC":
                        username = input("\n\tEnter site username: ")
                        site_name= input("\tEnter the site name: ").strip()
                        print("\t\tPlease choose one of the following options\n") 
                        print_y("\t\tAG-Autogenerate password \n\t\tTPass- Type Your Password")
                        pass_option = input("\t").strip()
                        if pass_option == "AG":
                            chars = '12The5S@un6789Out450Come23SUHaha' #characters to choose from
                            print_y("\tEnter the length of password you want:")
                            length = int(input("\t"))
                            user_password = ''
                            for c in range(length):
                                user_password+= random.choice(chars) #generate random password
                                # wait= load()
                                # print(wait)
                            sleep(1)
                            print ("\t",user_password)
                            print_s(f"\tYour username is:{username} Your password is:{user_password} ")
                        elif pass_option == "TPass":
                            user_password = input("\t").strip()
                        else:
                            print_e("Use the available")
                        # add_cred(save_credentials_info(username,site_name,user_password))
                        save_credentials(create_credentials(site_name,username, user_password))

                    elif cred_input == "DC":
                        if display_credentials():
                            print("Here is a list of all your credentials")
                            print('\n')
                            print_s(f" {site_name} {username}")
                            print('\n')
                        else:
                            print('\n')
                            print("You dont seem to have any contacts saved yet")
                            print('\n')
                    
                    elif cred_input == "CP":
                        copied_object = input("\tEnter password:")
                        copy_credential(copied_object) 

                    elif cred_input == "SMC":
                        while True:
                            print_y("Enter EX to exit or go back")
                            username = input("\n\tEnter site username: ")
                            site_name= input("\tEnter the site name: ").strip()
                            print("\t\tPlease choose one of the following options\n") 
                            print_y("\t\tAG-Autogenerate password \n\t\tTPass- Type Your Password")
                            pass_option = input("\t").strip()
                            if pass_option == "AG":
                                chars = '12The5S@un6789Out450Come23SUHaha' #characters to choose from
                                print_y("\tEnter the length of password you want:")
                                length = int(input("\t"))
                                user_password = ''
                                for c in range(length):
                                    user_password+= random.choice(chars) #generate random password
                                    # wait= load()
                                    # print(wait)
                                    sleep(1)
                                    print ("\t",user_password)
                                    print_s(f"\tYour username is:{username} Your password is:{user_password} ")
                            elif pass_option == "TPass":
                                user_password = input("\t").strip()

                            if pass_option == "EX":
                                print_y("See you soon, hope you enjoyed")
                                break
                            else:
                                print("Oops! Something went wrong, please try again!")
                            
                    else:
                        print("Oops! Something went wrong, please try again!")
            else:
                print("User does not exist")
                
    else:
        print("Enter the specified options")
        # break

if __name__ == '__main__':
    main()