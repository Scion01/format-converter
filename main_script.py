import sys
from convert_script import *

def initiate_exit_seq():
    print("Exiting...Bye")
    sys.exit()

def welcome_seq():
    print("--------WELCOME----------")
    print("The File formats supported: ",format_glob)

def print_all_usages():
    #print("convert foramt1 to format2")
    print("convert format1 format2")
    print("exit  ->> to exit")
    print("usage  ->> for usage")
    print("support  ->> for supported formats")
    #print("File formats supproted: ", format_glob)

def parse_user_input(user_input):
    if(len(user_input) <=0):
        print("Invalid command! Find all the commands below: ")
        print_all_usages()
        return

    parts=user_input.split(' ')
    if(parts[0] == "exit"):
        initiate_exit_seq()
        print("File formats supproted: ", format_glob)
    elif (parts[0] == "usage"):
        print_all_usages()
    elif (parts[0] == "support"):
        print(format_glob)
    elif(len(parts)<3):
        print("Invalid command! Find all the commands below: ")
        print_all_usages() 
    elif(parts[0] == "convert"):
        if(parts[1].upper() in format_glob and parts[2].upper() in format_glob):
            initiate_convert_seq(parts[1].upper(),parts[2].upper())
        else:
            print("File format not supported! Supported file formats: ", format_glob)
    else:
        print("Invalid command! Find all the commands below: ")
        print_all_usages() 
        

def get_user_input():
    print(">",end=" ")
    user_input = input()
    parse_user_input(user_input)

first_time_seq = True
while(True):
    if first_time_seq:
        welcome_seq()
        first_time_seq = not first_time_seq
    get_user_input()
