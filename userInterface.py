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
        print(f'\t{contestants.values()}')
        UserInterface.display_sweepstakes_menu_options(contestants)
        # print(contestants.first_name)
        # print(contestants.last_name)
        # print(contestants.email)
        # print(contestants.address)
        # print(contestants.registration_number)

    @staticmethod
    def display_sweepstakes_info(sweepstakes):
        UserInterface.display_message(f'\tWelcome!')
        print('')
        print("\tPress -1- to exit to sweepstakes menu")

    @staticmethod
    def display_sweepstakes_selections_menu(sweepstakes):
        sweepstakes_name = ""
        print("\tWelcome to sweepstakes menu")
        UserInterface.display_sweepstakes_menu_options(sweepstakes_name)

    @staticmethod
    def display_marketing_firm_menu_options(marketing_firm_name):
        print("\tWelcome!")
        print('')
        print("\tPress -1- to create a sweepstake")
        print("\tPress -2- to change firm name")
        print("\tPress -3- to select a sweepstake")
        print("\tPress -4- to register")
        print('')

    @staticmethod
    def display_sweepstakes_menu_options(sweepstakes_name):
        print('')
        print("\tSweepstakes Menu")
        print('')
        print("\tPress -1- to register")
        print("\tPress -2- to view contestants")
        print("\tPress -3- to pick winner")
        print("\tPress -4- to terminate session")
        print('')

