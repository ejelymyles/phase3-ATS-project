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
            print("creating new job helper function")
        elif choice == "2":
            print("seeing all jobs helper function")
        elif choice == "3":
            print("finding job by name helper function")
        elif choice == "4":
            print("finding job by id helper function")
        elif choice == "5":
            print("updating an existing job helper function")
        elif choice == "6":
            print("deleting a job helper function")
        elif choice == "7":
            print("adding a new candidate helper function")
        elif choice == "8":
            print("seeing all active candidates helper function")
        elif choice == "9":
            print("finding a candidate by name helper function")
        elif choice == "10":
            print("finding a candidate by id helper function")
        elif choice == "11":
            print("updating a candidate helper function")
        elif choice == "12":
            print("rejecting a candidate helper function")
        elif choice == "13":
            print("see all candidates from a job helper function ")
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Create a job")
    print("2. See all open jobs")
    print("3. Find a job by name")
    print("4. Find a job by id")
    print("5. Update an existing job")
    print("6. Delete a job")
    print("7. Add a new candidate")
    print("8. See all active candidates")
    print("9. Find a candidate by name")
    print("10. Find a candidate by id ")
    print("11. Update a candidate")
    print("12. Reject a candidate")
    print("13. List all candidates from a job")



if __name__ == "__main__":
    main()
