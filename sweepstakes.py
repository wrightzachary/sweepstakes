import random
from userInterface import UserInterface


class Sweepstakes:
    def __init__(self):
        self.sweepstakes_name = "sweepstakes"
        self.contestants = {

        }

    def register_contestant(self):
        UserInterface.display_message(f'\tEnter contestant data: ')
        self.contestants["First name: "] = UserInterface.get_user_input_string("\tFirst name: ")
        self.contestants["Last name: "] = UserInterface.get_user_input_string("\tLast name: ")
        self.contestants["Email: "] = UserInterface.get_user_input_string("\tEmail: ")
        self.contestants["Address "] = UserInterface.get_user_input_string("\tAddress: ")
        self.contestants["Registration number: "] = UserInterface.get_user_input_string(f"\tRegistration number: {random.randint(1, 100)}")
        Sweepstakes.menu(self)

    @staticmethod
    def get_registration_number(contestant):
        pass

    def pick_winner(self):
        print(f'\tWinner is {random.randint(1, 100)}')
        value = int
        if value in self.contestants:
            print(f'\t Congratulations!')
        else:
            print(f'\tSorry, no winner present!')
            Sweepstakes.menu(self)

    def view_contestants(self):
        UserInterface.display_contestant_info(self.contestants)
        Sweepstakes.menu(self)

    def menu(self):
        UserInterface.display_sweepstakes_menu_options(self.sweepstakes_name)
        response = int(input("\tPlease enter your selection: "))
        UserInterface.display_message('')
        if response == 1:
            self.register_contestant()
        elif response == 2:
            self.view_contestants()
        elif response == 3:
            self.pick_winner()
        elif response == 4:
            UserInterface.display_message("See you again!")
        else:
            print("\tNot a valid selection")
            UserInterface.display_sweepstakes_menu_options(self.sweepstakes_name)
