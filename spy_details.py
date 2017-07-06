
from datetime import datetime
#class has details of each spy as declare variables for age, rating and online status with appropriate values for your spy



class Spy:

    def __init__(self, name, salutation, age, rating):

        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chats = []
        self.current_status_message = None


class ChatMessage:

    def __init__(self,message,sent_by_me):
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me

#deafult user
spy = Spy('Ashish', 'Mr.', 24, 4.7)

friend_one = Spy('Reetu', 'Ms.', 4.9, 27)
friend_two = Spy('rahul', 'Mr.', 4.39, 21)
friend_three = Spy('Anamika', 'Dr.', 4.95, 37)



friends = [friend_one, friend_two, friend_three]


