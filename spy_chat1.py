from steganography.steganography import Steganography
from termcolor import colored
from PIL import Image
from datetime import datetime
from spy_details import spy, Spy, ChatMessage, friends

#staus messages...
STATUS_MESSAGES = ['sleeping', 'busy', 'cant talk only messaage!', 'using spychat!']

print "Hello! Let\'s get started"

question = "Do you want to continue as " + spy.salutation + " " + spy.name + " (Y/N)? "
existing = raw_input(question)

################################################################## ADD STATUS ###############################################################################
def add_status():

    updated_status_message = None

    if spy.current_status_message != None:

        print 'Your current status message is %s \n' % (spy.current_status_message)
    else:
        print 'You don\'t have any status message currently \n'

    default = raw_input("Do you want to select from the older status (y/n)? ")

    if default.upper() == "N":
        new_status_message = raw_input("What status message do you want to set? ")


        if len(new_status_message) > 0:
            STATUS_MESSAGES.append(new_status_message)
            updated_status_message = new_status_message

    elif default.upper() == 'Y':

        item_position = 1

        for message in STATUS_MESSAGES:
            print '%d. %s' % (item_position, message)
            item_position = item_position + 1

        message_selection = int(raw_input("\nChoose from the above messages "))

#condition chck whether len of status_message is greater than or equal to message_selection then
        if len(STATUS_MESSAGES) >= message_selection:
            updated_status_message = STATUS_MESSAGES[message_selection - 1]

    else:
        print 'The option you chose is not valid! Press either y or n.'

    if updated_status_message:
        print 'Your updated status message is: %s' % (updated_status_message)
    else:
        print 'You current don\'t have a status update'

    return updated_status_message



#############################################################  ADD FRIEND   #################################################################################
def add_friend():
    #create a list to hold friend names,friend ages and friend rating
    new_friend = Spy('','',0,0.0)

    new_friend.name = raw_input("Please add your friend's name: ")
    new_friend.salutation = raw_input("Are they Mr. or Ms.?: ")

    new_friend.name = new_friend.salutation + " " + new_friend.name
    #ask the user age
    new_friend.age = raw_input("Age?")
    new_friend.age = int(new_friend.age)
    #ask the user_rating
    new_friend.rating = raw_input("Spy rating?")
    new_friend.rating = float(new_friend.rating)
    #check condition if name is not empty ,age is gretaer than 12 and rating of the friend spy is greater than or equal to the user spy rating
    if len(new_friend.name) > 0 and new_friend.age > 12 and new_friend.rating >= spy.rating:
        friends.append(new_friend)
        #print the appropiate message
        print 'Friend Added!'
    else:
        print 'Sorry! Invalid rating entry. We can\'t add spy with the details you provided'

   #return no of friends the user has
    return len(friends)

################################################################################ SELECT A FRIEND ######################################################################
def select_a_friend():
    item_number = 0
    #list all spy friends added by the user
    for friend in friends:
        print '%d. %s %s aged %d with rating %.2f is online' % (item_number +1, friend.salutation, friend.name,
                                                   friend.age,
                                                   friend.rating)
        item_number = item_number + 1
    #select one of the one friend
    friend_choice = raw_input("Choose from your friends")

    friend_choice_position = int(friend_choice) - 1

    return friend_choice_position


###################################################################### SEND A MESSAGE ########################################################################
def send_message():

    friend_choice = select_a_friend()
#ask the user for the name of the image they want to encode the secret message with
    original_image = raw_input("What is the name of the image?")
    # original_image = 'images.jpg'

    output_path = "new.jpg"
    #ask the user for the secret message they want to hide
    text = raw_input(colored("What do you want to say?" ,"red"))
    #Steganography.encode(original_image, output_path, text)
    if text:
        if len(text) <100:
            Steganography.encode(original_image, output_path, text)
        else:
            print "the length of message should not exceed 100"
    else:
        print "empty string not allowed"
    new_chat = ChatMessage(text,True)

    friends[friend_choice].chats.append(new_chat)

    print "Your secret message image is ready!"


############################################################################# READ MESSAGE ###########################################################################
def read_message():

    sender = select_a_friend()

    output_path = raw_input("What is the name of the file?")

    secret_text = Steganography.decode(output_path)
    print secret_text
    new_chat = ChatMessage(secret_text,False)

    friends[sender].chats.append(new_chat)

    print "Your secret message has been saved!"



##################################################################READ_CHAT########################################################################################
def read_chat_history():
    """
        Represents the spychat history between the owner of
        the history and their contacts.
        """
    read_for = select_a_friend()#call the select_a_friend mrthod to get which friend is to be communicated with

    print '\n6'

    for chat in friends[read_for].chats:


        if chat.sent_by_me:
            print colored('[%s] %s: %s' % (chat.time.strftime("%d %B %Y"), "You said:", chat.message), "blue")
        else:
            print colored( '[%s] %s said: %s' % (chat.time.strftime("%d %B %Y"), friends[read_for].name, chat.message),"blue")

 ########################################################### DELETE SPY ################################################

# delete the spy when speaking too much(100   words)
#def delete_spy(secret_text, spy_index):
   # if len(secret_text.split()) > 100:
               # print "spy is speaking too much so remove the spy."
                #del friends[spy_index]
                #print "spy is deleted."


#########################################################################  MENU  #########################################################################################

def start_chat(spy):
        current_status_message = None


# menu for spy to choose any option from the menu...
show_menu = True

while show_menu:
    menu_choices = raw_input(colored(
        "What do you want to do? \n 1. Add a status update \n 2. Add a friend \n 3. Send a secret message \n 4. Read a secret message \n 5. Read Chats from a user \n 6. Close Application \n",
        "green"))
    menu_choice = menu_choices

    if len(menu_choice) > 0:
        menu_choice = int(menu_choice)
        # we are selecting the choices from menu
        if menu_choice == 1:
            print'you choose to update the status'
            spy.current_status_message = add_status()

        elif menu_choice == 2:
            print 'This choice choose to add the friend'
            number_of_friends = add_friend()
            print 'You have %d friends' % (number_of_friends)
        elif menu_choice == 3:
            print 'choose to send a secret message'
            send_message()
        elif menu_choice == 4:
            print 'choose to read message from the user '
            read_message()
        elif menu_choice == 5:
            print 'choose for tp read chat history'
            read_chat_history()
        elif menu_choice == 6:
            show_menu = False
        else:
            print "wrong choice"

print "Let's get started"
user = raw_input(" if they want to continue with \n1-default user \n2-create their own\n")

# for default user
if int(user) == 1:
    # spy rating displaying if, elif and else sequence
    if spy.rating > 4.5:
        print "Great ace!"
    elif spy.rating > 3.5 and  spy.rating <=4.5:
        print "You are one of the good ones."
    elif spy.rating > 2.5 and spy.rating <=3.5:
        print "You can always do better."
    else:
        print "We can always use somebody to help in the office."
    # welcome message with the name, salutation, age and rating of the spy.
    print "Authentication complete \n Welcome %s age: %d and rating : %.1f .Proud to be have you onboard\n" % (
        spy.name, spy.age, spy.rating)
    # Entering into menu
    start_chat(spy)

# For custom user app should ask for the name of the user
elif int(user) == 2:
    spy.name = raw_input("Welcome to spy chat, you must tell your spy name first:")
    # check that the user has not entered an invalid name
    if len(spy.name) > 0:
        print "Welcome " +  spy.name  + " .Glad to have you back with us."
        # input the salutaion the user wants to be used in front of their name
        spy.salutation = raw_input("Should I call you Mr. or Ms.?")
        spy.name = spy.salutation + " " + spy.name
        print "Alright " + spy.name + " I'd like to know a little bit more about you!"
    else:
        print "A Spy needs to have a valid name. Try again please."

    spy.age = raw_input("What is your age?")
    spy.age = int(spy.age)
    # age of the user is greater than 12 and less than 50
    if spy.age > 12 or spy.age < 50:
        spy.rating = raw_input("What is your spy rating?")
        spy.rating = float(spy.rating)
    else:
        print "sorry you are not of the correct age to be a spy"
    spy.is_online = True
    # spy rating displaying if, elif and else sequence
    if spy.rating > 4.5:
        print "Great ace!"
    elif spy.rating > 3.5 and spy.rating <= 4.5:
        print "You are one of the good ones."
    elif spy.rating > 2.5 and spy.rating <= 3.5:
        print "You can always do better."
    else:
        print "We can always use somebody to help in the office."
    # welcome message with the name, salutation, age and rating of the spy
    print "Authentication complete \n Welcome %s age: %d and rating : %.1f .Proud to be have you onboard\n" % (
        spy.name, spy.age, spy.rating)
    # Entering into menu
    start_chat(spy)