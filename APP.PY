from db_helper import DBhelper
import sys

class flipkart:

    def __init__(self):
        #connect to the database
        self.db=DBhelper()
        self.menu()
    def menu(self):
        user_input=input("""
        1. Enter 1 to register
        2. Enter 2 to login
        3. Anything else to leave\n""")
        if user_input=='1':
            self.register()
        elif user_input=='2':
            self.login()
        else:
            self.exit(101)
    def register(self):
        name= input("Enter you Name ")
        email=input("Enter you email  ")
        passw = input("Enter your password: ")
        # call register using the new parameter name; we expect a boolean
        response = self.db.register(name, email, passw)
        if response:
            print("Registration successful")
        else:
            print("Registration failed")
        #again call the main finction
        self.menu()
    
    def login(self):
        email = input("Enter your email: ")
        passw = input("Enter your password: ")
        response = self.db.login(email, passw)
        if response:
            print("Login successful")
        else:
            print("Login failed")
        self.menu()
    
    def exit(self, code):
        print("Thank you for using Flipkart")
        sys.exit(code)


obj=flipkart()

