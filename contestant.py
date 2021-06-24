from userInterface import UserInterface


class Contestant:
    def __init__(self):
        self.first_name = UserInterface.get_user_input_string("\tEnter first name")
        self.last_name = UserInterface.get_user_input_string("\tEnter last name")
        self.email = UserInterface.get_user_input_string("\tEnter email")
        self.address = UserInterface.get_user_input_string("\tEnter address")
        self.registration_number = 0

    def notify(self, is_winner):
        pass
