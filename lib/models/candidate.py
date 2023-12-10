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


    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise ValueError("Name must be a non-empty string")

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if isinstance(title, str) and len(title):
            self._title = title
        else:
            raise ValueError("Title must be a non-empty string")

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, location):
        if isinstance(location, str) and len(location):
            self._location = location
        else:
            raise ValueError("Location must be a non-empty string")

    @property
    def stage(self):
        return self._stage

    @stage.setter
    def stage(self, stage):
        if isinstance(stage, str) and len(stage):
            self._stage = stage
        else:
            raise ValueError("Stage must be a non-empty string")