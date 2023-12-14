# lib/helpers.py
from models.job import Job
from models.candidate import Candidate




def exit_program():
    print("Goodbye! You have now exited the Applicant Tracking System")
    exit()


def add_new_job():
    name = input("Enter the job's title: ")
    team = input("Enter the team's name: ")
    location = input("Enter the job location: ")
    level = input("Enter the target level: ")
    try:
        job = Job.create(name, team, location, level)
        print(f'Successfully created: {job}')
    except Exception as exc:
        print("Error creating new job: ", exc)


def list_all_jobs():
    jobs = Job.get_all()
    for job in jobs:
        print(job)


def find_job_by_name():
    name = input("Enter the job's title: ")
    job = Job.find_by_name(name)
    print(job) if job else print(f'Sorry, the job {name} was not found')


def find_job_by_id():
    id_ = input("Enter the job ID: ")
    job = Job.find_by_id(id_)
    print(job) if job else print(f'Sorry, the job {id_} was not found')



def update_job():
    id_ = input("Enter the job's ID: ")
    if job := Job.find_by_id(id_):
        try:
            name = input("Enter the job's title: ")
            job.name = name
            team = input("Enter the team's name: ")
            job.team = team
            location = input("Enter the job's location: ")
            job.location = location
            level = input("Enter the job's target level: ")
            job.level = level
            job.update()

            print(f'Successfuly updated: {job}')
        except Exception as exc:
            print("Error updating job: ", exc)
    else:
        print(f'Job {id_} was not found')


def delete_job():
    id_ = input("Enter the job's ID: ")
    if job:= Job.find_by_id(id_):
        job.delete()
        print(f'Job {id_} was deleted')
    else:
        print(f'Job {id_} was not found')



def add_new_candidate():
    name = input("Enter the candidate's name: ")
    title = input("Enter the candidate's current title: ")
    location = input("Enter the candidate's location: ")
    stage = input("Enter the candidate's current interview stage: ")
    id_ = input("Enter the candidate's job ID: ")

    job = Job.find_by_id(id_)

    if job:
        try:
            candidate = Candidate.create(name, title, location, stage, int(id_))
            print(f'Successfully added: {candidate}')
        except Exception as exc:
            print("Error adding new candidate: ", exc)
    else:
        print(f"Error: Job with ID {id} was not found.")
    

def list_all_candidates():
    candidates = Candidate.get_all()
    for candidate in candidates:
        print(candidate)



def find_candidate_by_name():
    name = input("Enter the candidate's name: ")
    candidate = Candidate.find_by_name(name)
    print(candidate) if candidate else print(f'Candidate {name} was not found')


def find_candidate_by_id():
    id_ = input("Enter the candidate's ID: ")
    candidate = Candidate.find_by_id(id_)
    print(candidate) if candidate else print(f'Candidate {id_} was not found')


def update_candidate():
    id_ = input("Enter the candidate's ID: ")
    if candidate := Candidate.find_by_id(id_):
        try:
            name = input("Update the candidate's new name: ")
            candidate.name = name
            title = input("Update the candidate's current title: ")
            candidate.title = title
            location = input("Update the candidate's location: ")
            candidate.location = location
            stage = input("Update the candidate's current stage: ")
            candidate.stage = stage
            new_id = input("Update the candidate's Job ID: ")
            candidate.job_id = int(new_id)

            candidate.update()
            print(f'Succesfully updated: {candidate}')
        except Exception as exc:
            print("Error updating the candidate: ", exc)
    else:
        print(f'Candidate {id_} was not found')


def delete_candidate():
    id_ = input("Enter the candidate's ID: ")
    if candidate := Candidate.find_by_id(id_):
        candidate.delete()
        print(f'Candidate {id_} was deleted')
    else:
        print(f'Candidate {id_} was not found')

        
def list_candidates_from_job():
    id_ = input("Enter the job ID: ")
    if job := Job.find_by_id(id_):
        candidates = job.candidates()
        if candidates:
            for candidate in candidates:
                print(candidate)
        else:
            print(f'No candidates interviewing for job {job.name}')
    else:
        print(f'Job {id_} not found')
    