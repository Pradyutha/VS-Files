import sys
import csv
import getpass
import argparse

global_store_file_name = "pass.txt"
global_super_password = "123"

def print_usage():
        print("Usage of this tool - ")
        print(" Pass the location of the text file or create-new")
        print("     Example - pass2.py --dir=<Location of file> or --New")

def parse_arguments():
        print("Pradyu to try parsing arguments")
    
def getMe():
        inp = getpass.getpass()
        if inp == global_super_password:
            print("Success")
            print("------------------------")
        else:
            print("Access Denied")
            raise Exception("Password not recognized, you may not proceed")
        
def find():
        user = input("Enter username:")
        try:
            file = open(global_store_file_name , "r")
            file.reader = csv.reader(file)
            temp = []
        except Exception as error:
            print("Exception while trying to open and read file %s"%str(error))
            raise Exception(error)
        
def read(file):
        file = open(global_store_file_name, "r")
        for row in file:
            if row[0] == user :
                print("the password for this ID is: " , row[1])
            else:
                print("The ID does not exist")

if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print("Invalid number of arguments")
        print_usage()
        sys.exit()
    
    try:
        parse_arguments()
        getMe()
        find()
        read(file)
    except Exception as error:
        print("Couldn't complete execution of program as we had the following error - %s"%str(error))
