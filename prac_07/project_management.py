import csv
from datetime import datetime
from project import Project

FILENAME = 'projects.txt'


def main():
    projects = load_projects(FILENAME)
    print(f"Loaded {len(projects)} projects from {FILENAME}")

    while True:
        print("\nMenu:")
        print("(L)oad projects")
        print("(S)ave projects")
        print("(D)isplay projects")
        print("(F)ilter projects by date")
        print("(A)dd new project")
        print("(U)pdate project")
        print("(Q)uit")
        choice = input(">>> ").upper()

        if choice == 'L':
            filename = input("Enter filename to load projects from: ")
            projects = load_projects(filename)
        elif choice == 'S':
            filename = input("Enter filename to save projects to: ")
            save_projects(filename, projects)
        elif choice == 'D':
            display_projects(projects)
        elif choice == 'F':
            date_string = input("Show projects that start after date (dd/mm/yyyy): ")
            filter_projects_by_date(projects, date_string)
        elif choice == 'A':
            add_new_project(projects)
        elif choice == 'U':
            update_project(projects)
        elif choice == 'Q':
            save_choice = input(f"Would you like to save to {FILENAME}? (Y/N): ").upper()
            if save_choice == 'Y':
                save_projects(FILENAME, projects)
            break
        else:
            print("Invalid choice")


def load_projects(filename):
    projects = []
    with open(filename, 'r') as file:
        reader = csv.reader(file, delimiter='\t')
        next(reader)  # Skip header
        for row in reader:
            projects.append(Project(*row))
    return projects


def save_projects(filename, projects):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file, delimiter='\t')
        writer.writerow(["Name", "Start Date", "Priority", "Cost Estimate", "Completion Percentage"])
        for project in projects:
            writer.writerow(
                [project.name, project.start_date.strftime('%d/%m/%Y'), project.priority, project.cost_estimate,
                 project.completion_percentage])
    print(f"Saved {len(projects)} projects to {filename}")


def display_projects(projects):
    incomplete_projects = [p for p in projects if not p.is_complete()]
    complete_projects = [p for p in projects if p.is_complete()]

    incomplete_projects.sort()
    complete_projects.sort()

    print("Incomplete projects:")
    for project in incomplete_projects:
        print(f"  {project}")

    print("Completed projects:")
    for project in complete_projects:
        print(f"  {project}")


def filter_projects_by_date(projects, date_string):
    filter_date = datetime.strptime(date_string, "%d/%m/%Y").date()
    filtered_projects = [p for p in projects if p.start_date > filter_date]
    filtered_projects.sort(key=lambda p: p.start_date)

    print(f"Projects starting after {date_string}:")
    for project in filtered_projects:
        print(f"  {project}")


def add_new_project(projects):
    print("Let's add a new project")
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yyyy): ")
    priority = input("Priority: ")
    cost_estimate = input("Cost estimate: ")
    completion_percentage = input("Percent complete: ")

    projects.append(Project(name, start_date, priority, cost_estimate, completion_percentage))


def update_project(projects):
    for i, project in enumerate(projects):
        print(f"{i} {project}")

    project_index = int(input("Project choice: "))
    project = projects[project_index]

    print(f"{project}")
    new_percentage = input("New Percentage: ")
    new_priority = input("New Priority: ")

    if new_percentage:
        project.completion_percentage = int(new_percentage)
    if new_priority:
        project.priority = int(new_priority)
    print(f"Updated {project}")


if __name__ == "__main__":
    main()
