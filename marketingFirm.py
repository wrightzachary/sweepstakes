from sweepstakes import Sweepstakes
from userInterface import UserInterface


class MarketingFirm:
    def __init__(self):
        self.marketing_firm_name = "devFirm"
        self.sweepstakes_storage = []

    def create_sweepstakes(self):
        chosen_name = UserInterface.get_user_input_string("Enter sweepstakes name")
        sweepstakes = Sweepstakes(chosen_name)
        self.sweepstakes_storage.append(sweepstakes)

    @staticmethod
    def change_marketing_firm_name():
        change_name = UserInterface.get_user_input_string("Change firm name:")
        new_name = change_name
        return new_name

    def select_sweepstakes(self):
        pass

    def menu(self):
        self.create_sweepstakes()
        self.change_marketing_firm_name()
        self.select_sweepstakes()

