from library import Library
import datetime
import sys
import os
import sqlite3
import pathlib

#https://docs.python.org/3/library/sqlite3.html

#create our database
#change current working direcotry to Database and create it there

os.chdir("/DataBase management system/Database")
con = sqlite3.connect("Books.db") #creates in current working working direcotry (Can chnage)
#crate cursor to do useful lstuff with database
cus = con.cursor()

print("Welcome User\n" + datetime.datetime.now().strftime("%X"))

#Options
print('''\n
a.) View Database\n
b.) add to database\n
c.) delete from database\n
e.) Exit\n
''')
userInput = input("\n>")
while(True):
    if userInput == "a":
        #print("\nView databse\n")
        #get info from database
        result = cus.execute("SELECT * FROM sqlite_master")
        if result.fetchone() == None:
            print("Database is Empty")
        pass
    elif userInput == "b":
        print("\nAdd to database\n")
    elif userInput == "c":
        print("\nDelete from databse\n")
    elif userInput == "e":
        print("\nThank you for using the application\n")
        sys.exit(0)
    else:
        print("User input could not be parsed")
    userInput = input("\n>")
