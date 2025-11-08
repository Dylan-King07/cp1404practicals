"""
CP1404 prac_07 Project Management Program
Estimated time: 1 hour
Actual time: 1 day
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
        elif menu_option == "d":
            display_projects(loaded_projects)
        elif menu_option == "f":
            filter_project_dates(loaded_projects)
        elif menu_option == "a":
            add_project(loaded_projects)
        elif menu_option == "u":
            update_project(loaded_projects)
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
            projects.append(Project(name, start_date, int(priority), float(cost_estimate), int(completion)))
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


def display_projects(projects):
    """Display projects which are complete and incomplete."""
    sort_projects = sorted(projects)
    complete_projects = [project for project in projects if project.is_job_complete(True)]
    incomplete_projects = [project for project in projects if project.is_job_complete(False)]

    print("Incomplete Projects: ")
    for project in incomplete_projects:
        print(f"{project}")
    print("Complete Projects: ")
    for project in complete_projects:
        print(f"{project}")


def filter_project_dates(projects):
    """Display projects which start after specified date."""
    choose_date = input("Show projects that start after date (dd/mm/yy): ")
    convert_to_datetime = datetime.strptime(choose_date, "%d/%m/%Y").date()
    filtered_dates = sorted([project for project in projects if project.start_date >= convert_to_datetime],
                            key=lambda x: x.start_date)
    for project in filtered_dates:
        print(f"{project}")


def add_project(projects):
    """Input details of new project and add to list"""
    print("Let's add a new project")
    project_name = input("Name: ")
    project_start_date = datetime.strptime(input("Start date (dd/mm/yyyy): "), "%d/%m/%Y").date()
    project_priority = int(input("Priority: "))
    project_cost_estimate = float(input("Cost estimate: $"))
    project_completion = int(input("Percent complete: "))
    new_project = Project(project_name, project_start_date, project_priority, project_cost_estimate, project_completion)
    projects.append(new_project)


def update_project(projects):
    """Update the details of a project"""
    for index, project in enumerate(projects):
        print(f"{index} {project}")
    project_to_update = int(input("Project choice: "))
    project = projects[int(project_to_update)]
    print(project)
    update_completion = input("New percentage: ")
    if update_completion:
        project.completion_percentage = int(update_completion)
    update_priority = input("New priority: ")
    if update_priority:
        project.priority = int(update_priority)


if __name__ == "__main__":
    main()
