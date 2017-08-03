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
        self.start_over = True
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

    start_over = True
    my_users = Network("The new social network")
    newly_added_users = User("The new social network users")
    while start_over:
        print("Welcome to the new social network!  Would you like to Explore the Users or Sign Up?")
        first_choice = input("Please type 'explore' to Explore the Users or 'sign up' to Sign Up: ")

        if first_choice == "explore":
            print("")
            second_choice = input()

        elif first_choice == "sign up":
            new_user_name = input("Please type the user name you want: ")
            if new_user_name not in my_users.username_list:
                my_users.add_user("new_user_name")
                print(("Welcome to your new social network, {}!").format(new_user_name))
            else:
                print("Sorry, that username is already taken...")
                see_entire_list = input("If you would like to see to the entire list of usernames, type 'why not': ")
                if see_entire_list =="why not":
                    for everybody in ny_users.username_list:
                        print(("{}").format(everybody))

        else:
            Print("Please only type 'log in' or 'sign up'.")
