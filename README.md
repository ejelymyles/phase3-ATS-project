# Phase 3 Project - Applicant Tracking System

##  Project Goals

- Build an ORM using Python with 2 related data models
- Build a CLI to query and execute updates to the database

---

## Introduction

For a recruiter, an applicant tracking system is a tool used to manage all of the candidates interviewing for open roles.
It is helpful for providing recruiting updates to teams, communicating with candidates, and tracking data related to the hiring process for specific roles. 

## File Structure
Below is the directory structure:

```
.
├── Pipfile
├── Pipfile.lock
├── README.md
└── lib
    ├── models
    │   ├── __init__.py
    |   └── candidate.py
    │   └── job.py
    ├── cli.py
    ├── debug.py
    └── helpers.py
```
---

## The CLI

The CLI is an interactive script that prompts the user for information and performs operations based on the user's input.

The project has a CLI in `lib/cli.py` that looks like this:

```py
# lib/cli.py

from helpers import (
    exit_program,
    add_new_job,
    list_all_jobs,
    find_job_by_name,
    find_job_by_id,
    update_job,
    delete_job,
    add_new_candidate,
    list_all_candidates,
    find_candidate_by_name,
    find_candidate_by_id,
    update_candidate,
    delete_candidate,
    list_candidates_from_job,
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            add_new_job()
        elif choice == "2":
            list_all_jobs()
        elif choice == "3":
            find_job_by_name()
        elif choice == "4":
            find_job_by_id()
        elif choice == "5":
            update_job()
        elif choice == "6":
            delete_job()
        elif choice == "7":
            add_new_candidate()
        elif choice == "8":
            list_all_candidates()
        elif choice == "9":
            find_candidate_by_name()
        elif choice == "10":
            find_candidate_by_id()
        elif choice == "11":
            update_candidate()
        elif choice == "12":
            delete_candidate()
        elif choice == "13":
            list_candidates_from_job()
        else:
            print("Invalid Choice: You must choose an option from the menu")


def menu():
    print("Please select an option:")
    print("0. Exit the Applicant Tracking System")
    print("1. Create a new job")
    print("2. Vew all jobs")
    print("3. Find a job by name")
    print("4. Find a job by id")
    print("5. Update an existing job")
    print("6. Delete a job")
    print("7. Add a new candidate")
    print("8. See all active candidates")
    print("9. Find a candidate by name")
    print("10. Find a candidate by id ")
    print("11. Update a candidate")
    print("12. Reject/delete a candidate")
    print("13. List all candidates from a specific job")


if __name__ == "__main__":
    main()
    
```

You can run the CLI with `python lib/cli.py`, or include the shebang
and make it executable with `chmod +x`. 
The CLI will ask for input related to managing the applicant tracking system, query the database, and/or accomplish some sort of task.
From the CLI menu you can create, view, find (by name or ID), update, and delete Jobs and Candidates. You can also view all candidates from a specific job

---

## The Helper Functions

The helpers file contains a number of functions that will prompt the user for information, and use that information along with methods from the Job and Candidate models to execute their commands from the command line interface. The helper functions will provide statements to validate user actions, and alert the user when a particular action cannot be executed. The validation statements will also provide information on why the user's actions could not be executed. 

The helper functions included in the file include:
1. exit_program - allows the user to exit out of the CLI menu and program
2. add_new_job - adds a new job to the database based on inputs from the user
3. list_all_jobs - displays all of the jobs from the database
4. find_job_by_name - displays a specific job matching a name inputted by the user
5. find_job_by_id - displays a specific job matching an ID inputted by the user
6. update_job - updates a specific job based on inputs from the user
7. delete_job - deletes a specific job based on the job ID inputted by the user
8. add_new_candidate - adds a new candidate to the database based on inputs from the user 
9. list_all_candidates - displays all of the candidates from the database
10. find_candidate_by_name - displays a specific candidate matching a name inputted by the user
11. find_candidate_by_id - displays a specific candidate matching an ID inputted by the user
12. update_candiate - updates a specific candidate based on inputs from the user
13. delete_candidate - deletes a specific candidate based on the candidate ID inputted by the user
14. list_candidates_from_job - displays all of the candidates associated with a specific job

---

## Job Model 

The Job model represents the various open roles the recruiter may be hiring for. It is the "one" component of the one-to-many relationship with Candidates.
In otherwords one job can have many candidates, but candidates can only belong to one job. Jobs are initialized with Name, Team, Location, and Level attributes.
Level refers the the level of seniority or years of experience the team is targeting for the ideal candidate. 

Each attribute is decorated with a property that restricts what type of input must be used for that particular attribute. In the Job model, each attribute must be inputted as a String.

The model contains the following Class methods:
1. create_table - creates a jobs table in the database if none exists
2. drop_table - deletes the jobs table from the database if one exists
3. create - creates and saves a new job to the database
4. instance_from_db - returns a job from the database
5. get_all - returns all of the jobs from the database
6. find_by_id - returns a specific job based on it's ID number
7. find_by_name - returns a specific job based on it's name

The model contains the following Instance methods:
1. save - saves a job to the database
2. update - updates a job in the database
3. delete - deletes a job from the database
4. candidates - returns all of the candidates associated with a specific job in the database

---

## Candidate Model

The Candidate model represents the candidates that are interviewing for various jobs. It is the "many" component of the one-to-many relationship with Jobs.
In otherwords one job can have many candidates, but candidates can only interview for one job. Candidates are initialized with Name, Title, Location, Stage, and Job ID attributes.
Stage refers to the specific interview round the candidate is currently going through, or will go through next. 

Each attribute is decorated with a property that restricts what type of input must be used for that particular attribute. In the Candidate model the Name, Title, Location, and Stage attributes must be inputted as a string. the Job ID attribute must be inputted as an Integer. 

The model contains the following Class methods:
1. create_table - creates a candidates table in the database if none exists
2. drop_table - deletes the candidates table from the database if one exists
3. create - creates and saves a new candidate to the database
4. instance_from_db - returns a candidate from the database
5. get_all - returns all of the candidates from the database
6. find_by_id - returns a specific candidate based on it's ID number
7. find_by_name - returns a specific candidate based on it's name

The model contains the following Instance methods:
1. save - saves a candidate to the database
2. update - updates a candidate in the database
3. delete - deletes a candidate from the database

---

## Conclusion

This CLI application sums up the concepts learned in Phase 3 of my time at Flatiron School. I built this CLI to assist me in my daily life as a Technical Recruiter by helping to manage the real-world task of tracking my candidates through their interviewing process. 

---
