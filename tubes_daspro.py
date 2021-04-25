import os, math, sys, time, argparse, datetime
import login

folder_name = "a"

#Fungsi Load
load_condition = False

parser = argparse.ArgumentParser()
parser.add_argument("--location", "-l", help = "Masukkan nama folder", default = "")
args = parser.parse_args()

if(args.location == folder_name):
    load_condition = True
    print("Welcome sire")
elif(args.location != ""):
    print("Nama folder salah")
else:
    print("Silahkan masukkan nama folder")

if(load_condition):
    print("Please login first")

    login_succed = False
    while(not login_succed):
        is_admin, login_succed  = login.user_login()
        if(not login_succed):
            print("Please repeat your log in")
        time.sleep(0.5)
    
    while(is_admin):
        do_action = False
        while(not do_action):
            print("Currently avaiable action:\n  Register\n  login")
            action = input()
            if(action.lower() == "register"):
                login.user_register()
                do_action = True
            elif(action.lower() == "login"):
                valid = False
                while(not valid):
                    check = input("Wanna log in on another account? (Y/N)? ")
                    if(is_admin):
                        print("Currently log in as admin")
                    else:
                        print("Currently log in as " +  login.get_username())
                    
                    if(check.upper() == "Y"):
                        login_succed = False    
                        while(not login_succed):
                            is_admin, login_succed  = login.user_login()
                            if(not login_succed):
                                print("Please repeat your log in")
                            time.sleep(0.5)
                        valid = True
                        do_action = True
                    elif(check.upper() == "N"):
                        valid = True
                        print("Cancel Log in")
                    else:
                        print("Input tidak valid")
                    time.sleep(0.5)

            else:
                print("Invalid action")
                print("Input another action please")
            time.sleep(0.5)

        if(do_action):
            break
