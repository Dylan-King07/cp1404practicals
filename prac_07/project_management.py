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


def load_projects(filename):
    projects = []
    with (open(filename, "r", encoding="utf-8") as in_file):
        in_file.readline()  # Skip header row
        for line in in_file:
            project_fields = line.strip().split("\t")
            if len(project_fields) < 5:
                continue
            name, print_start_date, priority, cost_estimate, completion = project_fields
            start_date = datetime.strptime(print_start_date, "%d/%m/%Y").date()
            projects.append(Project(name, start_date, int(priority),float(cost_estimate), int(completion)))
    return projects


if __name__ == "__main__":
    main()
