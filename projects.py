import json
from datetime import datetime
from tabulate import tabulate
from utilities import validate_date

data_file = "projects.json"


def load_projects():
    try:
        with open(data_file, "r") as file:
            return json.load(file)
    except Exception as e:
        print(f"Error loading projects: {e}")
        return []


def save_projects(projects):
    try:
        with open(data_file, "w") as file:
            json.dump(projects, file, indent=4)
    except Exception as e:
        print(f"Error saving projects: {e}")


def create_project(user):
    print("\n--- Create Project ---")
    try:
        title = input("Title: ")
        details = input("Details: ")
        target = input("Target Amount (EGP): ")
        if not target.isdigit() or int(target) <= 0:
            print("Invalid target amount.")
            return

        start_date = input("Start Date (YYYY-MM-DD): ")
        if not validate_date(start_date):
            print("Invalid start date format.")
            return

        end_date = input("End Date (YYYY-MM-DD): ")
        if not validate_date(end_date) or datetime.strptime(end_date, "%Y-%m-%d") <= datetime.strptime(start_date,"%Y-%m-%d"):
            print("Invalid or conflicting end date.")
            return

        project = {
            "user_email": user["email"],
            "title": title,
            "details": details,
            "target": int(target),
            "start_date": start_date,
            "end_date": end_date
        }

        projects = load_projects()
        projects.append(project)
        save_projects(projects)

        print("Project created successfully.")
    except Exception as e:
        print(f"An error occurred while creating the project: {e}")


def view_projects():
    print("\n--- View Projects ---")
    try:
        projects = load_projects()
        if not projects:
            print("No projects available.")
            return

        table = [
            [index + 1, project["title"], project["target"], project["start_date"], project["end_date"]]
            for index, project in enumerate(projects)
        ]
        headers = ["ID", "Title", "Target (EGP)", "Start Date", "End Date"]
        print(tabulate(table, headers=headers, tablefmt="grid"))
    except Exception as e:
        print(f"An error occurred while viewing projects: {e}")


def edit_project(user):
    print("\n--- Edit Project ---")
    try:
        projects = load_projects()
        user_projects = [p for p in projects if p["user_email"] == user["email"]]

        if not user_projects:
            print("You have no projects to edit.")
            return

        view_projects()
        project_id = input("Enter the ID of the project to edit: ")
        if not project_id.isdigit() or int(project_id) < 1 or int(project_id) > len(user_projects):
            print("Invalid project ID.")
            return

        project = user_projects[int(project_id) - 1]
        project["title"] = input(f"Title ({project['title']}): ") or project["title"]
        project["details"] = input(f"Details ({project['details']}): ") or project["details"]
        target = input(f"Target Amount ({project['target']} EGP): ")
        project["target"] = int(target) if target.isdigit() else project["target"]

        start_date = input(f"Start Date ({project['start_date']}): ")
        if validate_date(start_date):
            project["start_date"] = start_date

        end_date = input(f"End Date ({project['end_date']}): ")
        if validate_date(end_date):
            project["end_date"] = end_date

        save_projects(projects)
        print("Project updated successfully.")
    except Exception as e:
        print(f"An error occurred while editing the project: {e}")


def delete_project(user):
    print("\n--- Delete Project ---")
    try:
        projects = load_projects()
        user_projects = [p for p in projects if p["user_email"] == user["email"]]

        if not user_projects:
            print("You have no projects to delete.")
            return

        view_projects()
        project_id = input("Enter the ID of the project to delete: ")
        if not project_id.isdigit() or int(project_id) < 1 or int(project_id) > len(user_projects):
            print("Invalid project ID.")
            return

        projects.remove(user_projects[int(project_id) - 1])
        save_projects(projects)
        print("Project deleted successfully.")
    except Exception as e:
        print(f"An error occurred while deleting the project: {e}")


def search_projects():
    print("\n--- Search Projects ---")
    try:
        start_date = input("Start Date (YYYY-MM-DD): ")
        end_date = input("End Date (YYYY-MM-DD): ")
        if not validate_date(start_date) or not validate_date(end_date):
            print("Invalid date format.")
            return

        projects = load_projects()
        filtered_projects = [
            p for p in projects
            if datetime.strptime(start_date, "%Y-%m-%d") <= datetime.strptime(p["start_date"],
                                                                              "%Y-%m-%d") <= datetime.strptime(end_date,
                                                                                                               "%Y-%m-%d")
        ]

        if not filtered_projects:
            print("No projects found within the specified date range.")
            return

        table = [
            [index + 1, project["title"], project["target"], project["start_date"], project["end_date"]]
            for index, project in enumerate(filtered_projects)
        ]
        headers = ["ID", "Title", "Target (EGP)", "Start Date", "End Date"]
        print(tabulate(table, headers=headers, tablefmt="grid"))
    except Exception as e:
        print(f"An error occurred while searching for projects: {e}")
