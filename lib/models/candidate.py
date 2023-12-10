from models.__init__ import CURSOR, CONN
from models.role import Role

class Candidate:
    
    all = {}

    def __init__(self, name, title, location, stage, id=None ):
        self.id = id
        self.name = name
        self.title = title
        self.location = location
        self.stage = stage