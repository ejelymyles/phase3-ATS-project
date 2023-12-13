from models.__init__ import CURSOR, CONN

class Job:

    all = {}

    def __init__(self, name, team, location, level, id=None):
        self.id = id
        self.name = name
        self.team = team
        self.location = location
        self.level = level

    def __repr__(self):
        return f"<Job {self.id}: {self.name}, {self.team}, {self.location}, {self.level}>"

    
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
    def team(self):
        return self._team

    @team.setter
    def team(self, team):
        if isinstance(team, str) and len(team):
            self._team = team
        else:
            raise ValueError("Team must be a non-empty string")

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
    def level(self):
        return self._level

    @level.setter
    def level(self, level):
        if isinstance(level, str) and len(level):
            self._level = level
        else:
            raise ValueError("Level must be a non-empty string")
    #add rule about length (no more than 3 letters = len(level) < 4)





    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS jobs (
            id INTEGER PRIMARY KEY,
            name TEXT,
            team TEXT,
            location TEXT,
            level TEXT)
         """
        CURSOR.execute(sql)
        CONN.commit()
    
    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS jobs;
         """
        CURSOR.execute(sql)
        CONN.commit()

    
    def save(self):
        sql="""
            INSERT INTO jobs (name, team, location, level)
            VALUES (?, ?, ?, ?)
         """
        CURSOR.execute(sql, (self.name, self.team, self.location, self.level))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self 


    @classmethod
    def create(cls, name, team, location, level):
        job = cls(name, team, location, level)
        job.save()
        return job
    

    def update(self):
        sql = """
            UPDATE jobs
            SET name = ?, team = ?, location = ?, level = ?
            WHERE id = ?
         """
        CURSOR.execute(sql, (self.name, self.team, self.location, self.level, self.id))
        CONN.commit()
        

    def delete(self):
        sql = """
            DELETE FROM jobs
            WHERE id = ?
         """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id]
        self.id = None

    

    @classmethod
    def instance_from_db(cls, row):
        job = cls.all.get(row[0])
        if job:
            job.name = row[1]
            job.team = row[2]
            job.location = row[3]
            job.level = row[4]
        else:
            job = cls(row[1], row[2], row[3], row[4])
            job.id = row[0]
            cls.all[job.id] = job
        return job

    @classmethod
    def get_all(cls):
        sql = """
            SELECT * 
            FROM jobs
        """
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]


    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM jobs
            WHERE id = ?
         """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None


    @classmethod
    def find_by_name(cls, name):
        sql = """
            SELECT *
            FROM jobs
            WHERE name is ?
         """
        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None

    def candidates(self):
        from models.candidate import Candidate
        sql = """
            SELECT * FROM candidates
            WHERE job_id = ?
         """
        CURSOR.execute(sql, (self.id,),)
        rows = CURSOR.fetchall()
        return[Candidate.instance_from_db(row) for row in rows]
    

        