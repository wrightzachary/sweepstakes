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
    def display_contestant_info(contestant):
        print(contestant.first_name)
        print(contestant.last_name)
        print(contestant.email)
        print(contestant.address)
        print(contestant.registration_number)

    @staticmethod
    def display_sweepstakes_info(sweepstakes):
        print(sweepstakes.sweepstakes_name)
        print(f'{len(sweepstakes.contestants)} contestants')

    @staticmethod
    def display_sweepstakes_selections_menu(sweepstakes):
        print("\tWelcome to sweepstakes menu")

    @staticmethod
    def display_marketing_firm_menu_options(marketing_firm_name):
        print("\tWelcome to devFirm!")
        print('')
        print("\tWhat would you like to do?")
        print('')
        print("\tPress -1- to create a sweepstake")
        print("\tPress -2- to change firm name")
        print("\tPress -3- to select a sweepstake")
        print("\tPress -4- to register")
        print('')

    @staticmethod
    def display_sweepstakes_menu_options(sweepstakes_name):
        print("\tSweepstakes Menu")
        print('')
        print("\tWhat would you like to do?")
        print('')
        print("\tPress -1- to register")
        print("\tPress -2- to view contestants")
        print("\tPress -3- to pick winner")
        print("\tPress -4- to return to marketing firm")
        print('')
        UserInterface.get_user_input_number("\tPlease enter your selection: ")
