from models.__init__ import CURSOR, CONN
from models.job import Job

class Candidate:
    
    all = {}

    def __init__(self, name, title, location, stage, job_id, id=None ):
        self.id = id
        self.name = name
        self.title = title
        self.location = location
        self.stage = stage
        self.job_id = job_id


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

    @property
    def job_id(self):
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        if type(job_id) is int and Job.find_by_id(job_id):
            self._job_id = job_id
        else:
            raise ValueError(
                "job_id must reference a job in the database")