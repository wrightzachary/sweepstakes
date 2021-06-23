import os


class UserInterface:
    @staticmethod
    def run_user_interface():
        validate_user_selection = (True, None)
        while validate_user_selection[0] is True:
            UserInterface.display_message("Welcome to our marketing firm")
            UserInterface.display_message("Press -1- to see sweepstakes menu")
            UserInterface.display_message("Press -2- to see marketing firm menu")
            print("Enter Selection:")
            input()
        return validate_user_selection[1]

    @staticmethod
    def display_message(messages):
        print(messages)

    @staticmethod
    def get_user_input_string(prompt):
        response = input(prompt)
        return response

    @staticmethod
    def get_user_input_number(prompt):
        response = int(input(prompt))
        return response

    @staticmethod
    def display_contestant_info(contestant):
        pass

    @staticmethod
    def display_sweepstakes_info(sweepstakes):
        pass

    @staticmethod
    def display_sweepstakes_selections_menu(sweepstakes):
        pass

    @staticmethod
    def display_marketing_firm_menu_options(marketing_firm_name):
        pass

    @staticmethod
    def display_sweepstakes_menu_options(sweepstakes_name):
        pass
