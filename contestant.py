from userInterface import UserInterface


# make contestant class
class Contestant:
    def __init__(self):
        self.first_name = UserInterface.get_user_input_string("\tEnter first name")
        self.last_name = UserInterface.get_user_input_string("\tEnter last name")
        self.email = UserInterface.get_user_input_string("\tEnter email")
        self.address = UserInterface.get_user_input_string("\tEnter address")
        self.registration_number = 0


# class to notify
class Subject:
    def __init__(self):
        self._observers = []

    def notify(self, is_winner, modifier=None):
        for observer in self._observers:
            if modifier != observer:
                observer.update(self)

    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        try:
            self._observers.remove(observer)
        except ValueError:
            pass
