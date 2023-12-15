# Phase 3 Project - Applicant Tracking System

##  Project Goals

- Build an ORM using Python with 2 related data models
- Build a CLI to query and execute updates to the database

---

## Introduction

For a recruiter, and applicant tracking system is a tool used to maintain all of the candidates interviewing for open roles.
It is helpful for providing recruiting updates to teams, communicating with candidates, and tracking data related to the the hiring process for specific roles. 

## File Structure
Below is the directory structure:

```console
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

## Job Model 

The Job model represents the various open roles the recruiter may be hiring for. It is the "one" component the one-to-many relationship with Candidates.
In otherwords one job can have many candidates, but candidates can only belong to one job. Jobs are initialized with Name, Team, Location, and Level attributes.
Level refers the the level of seniority or years of experience the team is targeting or the ideal candidate. 

Each attribute is decorated with a property that restricts what type of input must be used that particular attribute. In the Job model, each attribute must be inputted as a String.

The model contains the following Class methods:
1. create_table - creates a jobs table in the database if none exists
2. drop_table - deletes the jobs table from the database if one exists
3. create - creates and saves a  new job to the database
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
3. create - creates and saves a  new candidate to the database
4. instance_from_db - returns a candidate from the database
5. get_all - returns all of the candidates from the database
6. find_by_id - returns a specific candidate based on it's ID number
7. find_by_name - returns a specific candidate based on it's name

The model contains the following Instance methods:
1. save - saves a candidate to the database
2. update - updates a candidate in the database
3. delete - deletes a candidate from the database

---

## Helpers

The helpers file contains a number of functions that will prompt the user for information, and use that information along with methods from the Job and Candidate models to execute their commands from the command line interface. The helper functions will provide statements to validate user actions, and alert the user when a particular action cannot be executed. The validation statements will also provide information on why the user's actions could not be executed. 

The helper functions included in the file include:
1. exit_program - allows the user to exit out of the CLI menue and program
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

## CLI

A CLI is, simply put, an interactive script and prompts the user and performs
operations based on user input.

The project template has a sample CLI in `lib/cli.py` that looks like this:

```py
# lib/cli.py

from helpers import (
    exit_program,
    helper_1
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            helper_1()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Some useful function")


if __name__ == "__main__":
    main()
```

The helper functions are located in `lib/helpers.py`:

```py
# lib/helpers.py

def helper_1():
    print("Performing useful function#1.")


def exit_program():
    print("Goodbye!")
    exit()
```

You can run the template CLI with `python lib/cli.py`, or include the shebang
and make it executable with `chmod +x`. The template CLI will ask for input, do
some work, and accomplish some sort of task.

Past that, CLIs can be whatever you'd like, as long as you follow the project
requirements.

Of course, you will update `lib/cli.py` with prompts that are appropriate for
your application, and you will update `lib/helpers.py` to replace `helper_1()`
with a useful function based on the specific problem domain you decide to
implement, along with adding other helper functions to the module.

In the `lib/models` folder, you should rename `model_1.py` with the name of a
data model class from your specific problem domain, and add other classes to the
folder as needed. The file `lib/models/__init__.py` has been initialized to
create the necessary database constants. You need to add import statements to
the various data model classes in order to use the database constants.

You are also welcome to implement a different module and directory structure.
However, your project should be well organized, modular, and follow the design
principal of separation of concerns, which means you should separate code
related to:

- User interface
- Data persistence
- Problem domain rules and logic

---


### What Goes into a README?

Describe your actual CLI script first, and with a good level of detail. The rest
should be ordered by importance to the user. (Probably functions next, then
models.)

---

## Conclusion

A lot of work goes into a good CLI, but it all relies on concepts that you've
practiced quite a bit by now. Hopefully this template and guide will get you off
to a good start with your Phase 3 Project.

Happy coding!

---

## Resources

- [Markdown Cheat Sheet](https://www.markdownguide.org/cheat-sheet/)
