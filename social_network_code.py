class User:
    #Not sure how this will work.  It may need to be in the network class
    empCount = 0
    def __init__(self,name):
        self.name = name
        self.username = []
        #extention/don't focus on this yet.
        self.favorites = []
        self.connection = []
        #not too sure if I need the next 2:
        self.logged_on = False
        self.logged_off = True
        #see first comment
        User.empCount += 1

    #this will be used to create a new user name, which will be stored in the username_list int he network class.
    def create_new_user(self,new_user):
        self.username.append(new_user)

    #This will be an extention if there is time
    def add_favorites(self,favorite_things):
        self.favorites.append(favorite_things)

    #This will add a connection to a user that is already in the system.
    def add_user_connection(self,user_connection):
        self.connection.append(user_connection)






class Network:

    def __init__(self,name):
        self.name = name
        #This probably will not work, unless I do a dictionary with the user entered and their connections as the two pieces.
        self.connections = []
        self.username_list = []

    #This may not work.  Medium importance.
    def update_connection(self,connection):
        self.connections.append(connection)

    #This will be used to add users to the total list of users.
    def add_user(self,users):
        self.username_list.append(users)



def main():

    print("Welcome to the new social network!  Would you like to Log In or Sign Up?")
    first_choice = input("Please type 'log in' to Log In or 'sign up' to Sign Up: ")
    my_users = Users()
    while logged_off:
        #Check for the correct syntax for strings
        if first_choice == "log in":
            logged_on = True

        elif first_choice == "sign up":
            new_user_name = input("Please type the user name you want: ")
            if new_user_name not in my_users.username_list:
                

        else:
