from sweepstakes import Sweepstakes
from userInterface import UserInterface


class MarketingFirm:
    def __init__(self):
        self.marketing_firm_name = "devFirm"
        self.sweepstakes_storage = []

    def create_sweepstakes(self):
        chosen_name = UserInterface.get_user_input_string("\tEnter new sweepstakes name")
        sweepstakes = Sweepstakes(chosen_name)
        self.sweepstakes_storage.append(sweepstakes)

    @staticmethod
    def change_marketing_firm_name():
        change_name = UserInterface.get_user_input_string("\tChange firm name:")
        new_name = change_name
        print(f'\tMarketing firm name changed to {new_name}')

    def select_sweepstakes(self):
        self.marketing_firm_name = UserInterface.get_user_input_string("\tSelect your desired sweepstake")

    def menu(self):
        UserInterface.display_marketing_firm_menu_options(self.marketing_firm_name)
        response = int(input("\tPlease enter your selection: "))
        if response == 1:
            self.create_sweepstakes()
        if response == 2:
            self.change_marketing_firm_name()
        if response == 3:
            self.select_sweepstakes()
        if response == 4:
            UserInterface.display_sweepstakes_menu_options(self.sweepstakes_storage)
        else:
            print("\tNot a valid selection")
            MarketingFirm.menu(self)
