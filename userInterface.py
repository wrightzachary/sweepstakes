class UserInterface:
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
    def display_contestant_info(contestants):
        UserInterface.display_message(f'\t{contestants.values()}')
        UserInterface.display_sweepstakes_menu_options(contestants)
        # print(contestants.first_name)
        # print(contestants.last_name)
        # print(contestants.email)
        # print(contestants.address)
        # print(contestants.registration_number)

    @staticmethod
    def display_sweepstakes_info(sweepstakes):
        UserInterface.display_message(f'\tWelcome!')
        UserInterface.display_message('')
        UserInterface.display_message("\tPress -1- to exit to sweepstakes menu")

    @staticmethod
    def display_sweepstakes_selections_menu(sweepstakes):
        sweepstakes_name = ""
        UserInterface.display_message("\tWelcome to sweepstakes menu")
        UserInterface.display_sweepstakes_menu_options(sweepstakes_name)

    @staticmethod
    def display_marketing_firm_menu_options(marketing_firm_name):
        UserInterface.display_message("\tWelcome!")
        UserInterface.display_message('')
        UserInterface.display_message("\tPress -1- to create a sweepstake")
        UserInterface.display_message("\tPress -2- to change firm name")
        UserInterface.display_message("\tPress -3- to select a sweepstake")
        UserInterface.display_message("\tPress -4- to register")
        UserInterface.display_message('')

    @staticmethod
    def display_sweepstakes_menu_options(sweepstakes_name):
        UserInterface.display_message('')
        UserInterface.display_message("\tSweepstakes Menu")
        UserInterface.display_message('')
        UserInterface.display_message("\tPress -1- to register")
        UserInterface.display_message("\tPress -2- to view contestants")
        UserInterface.display_message("\tPress -3- to pick winner")
        UserInterface.display_message("\tPress -4- to terminate session")
        UserInterface.display_message('')

