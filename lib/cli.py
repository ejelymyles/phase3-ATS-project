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
    list_job_candidates,
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
