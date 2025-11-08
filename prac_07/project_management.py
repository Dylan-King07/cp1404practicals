"""
CP1404 prac_07 Project Management Program
Estimated time: 1 hour
Actual time:
"""


from project import Project
from datetime import datetime

FILENAME = "projects.txt"
MENU = ("- (L)oad projects\n"
        "- (S)ave projects\n"
        "- (D)isplay interface\n"
        "- (F)ilter projects by date\n"
        "- (A)dd new project\n"
        "- (U)pdate project\n"
        "- (Q)uit")


def main():
    """Main menu options."""
    print("Welcome to Pythonic Project Management")
    loaded_projects = load_projects(FILENAME)
    print(f"Loaded {len(loaded_projects)} projects from {FILENAME}")
    print(MENU)
    menu_option = input(">>> ").lower()
    while menu_option != "q":
        if menu_option == "l":
            filename = input("Enter name of file to load: ")
            load_projects(filename)
        elif menu_option == "s":
            filename = input("Enter name of file to save to: ")
            save_project(filename, loaded_projects)
        # elif menu_option == "d":
        #     # Display project function
        # elif menu_option == "f":
        #     # Filter projects in order of date function
        # elif menu_option == "a":
        #     # Add new project function
        # elif menu_option == "u":
        #     # Update project function
        else:
            print("Please choose a valid option")
        print(MENU)
        menu_option = input(">>> ").lower()


def load_projects(filename):
    """Open file and load projects from it."""
    projects = []
    with open(filename, "r", encoding="utf-8") as in_file:
        in_file.readline()  # Skip header row
        for line in in_file:
            project_fields = line.strip().split("\t")
            if len(project_fields) < 5:
                continue
            name, print_start_date, priority, cost_estimate, completion = project_fields
            start_date = datetime.strptime(print_start_date, "%d/%m/%Y").date()
            projects.append(Project(name, start_date, int(priority),float(cost_estimate), int(completion)))
    return projects


def save_project(filename, projects):
    """Save projects to file."""
    file_header = ["Name", "Start Date", "Priority", "Cost Estimate", "Completion Percentage"]
    with open(filename, "w", encoding="utf-8") as out_file:
        print("\t".join(file_header), file=out_file)
        for project in projects:
            file_row = [project.name, project.start_date.strftime("%d/%m/%Y"),
                        str(project.priority), f"{project.cost_estimate}",
                        str(project.completion_percentage)]
            print("\t".join(file_row), file=out_file)


if __name__ == "__main__":
    main()
