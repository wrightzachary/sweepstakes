import random
from userInterface import UserInterface


class Sweepstakes:
    def __init__(self, name):
        self.sweepstakes_name = name
        self.contestants = {
            "First name", "",
            "Last name", "",
            "Email name", "",
            "Address", "",
            "Registration number", "",
        }
        # self.contestants = Contestant

    def register_contestant(self, contestant):
        UserInterface.get_user_input_string(contestant)
        self.contestants.update(self.contestants)

    @staticmethod
    def get_registration_number(contestant):
        contestant.contestant_registration_number = 0000
        for x in range(10):
            print(random.randint(1, 101))

    @staticmethod
    def pick_winner():
        print(random.randint(0, 101))

    def view_contestants(self):
        print(self.contestants)

    def menu(self):
        UserInterface.display_sweepstakes_menu_options(self.sweepstakes_name)
        user_response = int(input("\tPlease enter your selection: "))
        if user_response == 1:
            self.register_contestant(self.sweepstakes_name)
        if user_response == 2:
            self.view_contestants()
        if user_response == 3:
            self.pick_winner()
        if user_response == 4:
            UserInterface.display_marketing_firm_menu_options(self.contestants)
        else:
            print("\tNot a valid selection")
            Sweepstakes.menu(self)
