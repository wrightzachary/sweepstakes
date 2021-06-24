from sweepstakes import Sweepstakes
from userInterface import UserInterface


class MarketingFirm:
    def __init__(self):
        self.marketing_firm_name = ""
        self.sweepstakes_storage = ["Boat", "Weekend getaway"]

    def create_sweepstakes(self):
        chosen_name = UserInterface.get_user_input_string("\tEnter new sweepstakes name")
        UserInterface.display_message('')
        sweepstakes = Sweepstakes()
        self.sweepstakes_storage.append(self.sweepstakes_storage)
        print(f"\tYou created {chosen_name} ")
        UserInterface.display_message('')
        MarketingFirm.menu(self)

    def change_marketing_firm_name(self):
        change_name = UserInterface.get_user_input_string("\tChange firm name:")
        new_name = change_name
        print(f'\tMarketing firm name changed to {new_name}')
        UserInterface.display_message('')
        self.marketing_firm_name = f'{new_name}'
        UserInterface.display_message('')
        # UserInterface.display_marketing_firm_menu_options(self.marketing_firm_name)
        MarketingFirm.menu(self)

    def select_sweepstakes(self):
        self.marketing_firm_name = UserInterface.get_user_input_string("\tSelect your desired sweepstake")
        UserInterface.display_message('')
        UserInterface.display_message(f'\tYou Selected {self.marketing_firm_name}')
        UserInterface.display_message('')
        UserInterface.display_sweepstakes_info('')
        response = int(input("\tPlease enter your selection: "))
        if response == 1:
            UserInterface.display_marketing_firm_menu_options(self.marketing_firm_name)
        else:
            UserInterface.display_message("Not a valid selection")
            MarketingFirm.select_sweepstakes(self)

    def menu(self):
        UserInterface.display_marketing_firm_menu_options(self.marketing_firm_name)
        response = int(input("\tPlease enter your selection: "))
        UserInterface.display_message('')
        if response == 1:
            self.create_sweepstakes()
        elif response == 2:
            self.change_marketing_firm_name()
        elif response == 3:
            self.select_sweepstakes()
        elif response == 4:
            UserInterface.display_sweepstakes_menu_options(self.sweepstakes_storage)
        else:
            print("\tNot a valid selection")
            UserInterface.display_sweepstakes_info(self.marketing_firm_name)
