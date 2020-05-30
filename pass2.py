import csv
import getpass
def getMe():
        f = "pass.txt"
        pw = "123"    
        inp = getpass.getpass()
        if inp == pw :
            print("Success")
            print("------------------------") 
            return
        else:
            print("Access Denied") 
            return
        
def find(): 
        user = input("Enter username:")  
        file = open("pass.txt" , "r") 
        file.reader = csv.reader(file)
        temp = []
        return
        
def read(file):
    
        file = open("pass.txt" , "r")
        for row in file:
            if row[0] == user :
                print("the password for this ID is: " , row[1] )
                return
            else:
                print("The ID does not exist") 
                return   
def main():
    getMe()
    find()
    read(file)
main()
