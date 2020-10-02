class players:

    def __init__(self, name, piece, points):
        self.name = name
        self.piece = piece
        self.points = points


    def set_name(self, name):
        self.name = name

    def get_name(self):
        return str(self.name)

    def add_win(self, points):
        self.points = self.points + 1

    def set_score(self, score):
        self.points = score

    def get_score(self):
        return str(self.points)
