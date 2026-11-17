class chatbook:
    def __init__(self):
        self.username=""
        self.password=""
        self.loggedin=False
        self.menu()

    def menu(self):
        user_input=input("""Welcome to chatbook!! how would  you look to proceed?
                           1.press 1 to signup
                           2. press 2 to signin
                           3. press 3 to write a post
                           4. press 4 to messaage a friend
                           5. press any other key to exit""")    

        if user_input == "1":
            self.signup()
        elif user_input == "2":
            self.signin()
        elif user_input == "3":
            pass
        elif user_input == "4":
            pass
        else:
            exit()

    def signup(self):
        email = input("Enter email")
        pwd = input("set up password")
        self.username = email
        self.password = pwd
        print("you have signed up successfully")
        print("\n")
        self.menu()
    def signin(self):
        if self.username =='' and self.password=='':
            print("please signup first by pressing 1 in the main menu")
        else:
            uname = input("enter your username")
            pwd = input("enter password")
            if self.username == uname and self.password==pwd:
                print("you have signed in successfully")
                self.loggedin = True
            else:
                print("please input correct credentials")
        print("\n")
        self.menu()                   

obj = chatbook()            