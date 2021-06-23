class Sweepstakes:
    def __init__(self, name):
        self.name = name
        self.contestants = []

    def register_contestants(self, contestant):
        pass

    def pick_winner(self):
        pass

    def view_contestants(self):
        pass

    def menu(self):
        self.register_contestants()
        self.pick_winner()
        self.view_contestants()
