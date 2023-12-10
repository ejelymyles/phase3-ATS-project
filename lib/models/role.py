from models.__init__ import CURSOR, CONN

class Role:

    all = {}

    def __init__(self, name, team, location, level, id=None):
        self.id = id
        self.name = name
        self.team = team
        self.location = location
        self.level = level
