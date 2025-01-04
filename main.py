import auth
import projects


def main_menu():
    while True:
        print("\n--- Crowd-Funding Console App ---")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Choose an option: ")
        try:
            if choice == "1":
                auth.register()
            elif choice == "2":
                user = auth.login()
                if user:
                    project_menu(user)
            elif choice == "3":
                print("Exiting... Goodbye!")
                break
            else:
                print("Invalid choice. Please select a valid option.")
        except Exception as e:
            print(f"An error occurred: {e}")


def project_menu(user):
    while True:
        print("\n--- Project Management ---")
        print("1. Create Project")
        print("2. View Projects")
        print("3. Edit Project")
        print("4. Delete Project")
        print("5. Search Projects")
        print("6. Logout")

        choice = input("Choose an option: ")
        try:
            if choice == "1":
                projects.create_project(user)
            elif choice == "2":
                projects.view_projects()
            elif choice == "3":
                projects.edit_project(user)
            elif choice == "4":
                projects.delete_project(user)
            elif choice == "5":
                projects.search_projects()
            elif choice == "6":
                print("Logging out...")
                break
            else:
                print("Invalid choice. Please select a valid option.")
        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    main_menu()
