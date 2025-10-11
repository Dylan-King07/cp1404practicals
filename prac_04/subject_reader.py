"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    """Read from file and display subject details"""
    subjects = load_subject_data(FILENAME)
    display_subject_details(subjects)


def load_subject_data(filename=FILENAME):
    """Load data from file and return list [code, learner, student_count]"""
    subjects = []
    input_file = open(filename)
    for line in input_file:
        line = line.strip()
        parts = line.split(',')
        parts[2] = int(parts[2])
        subjects.append(parts)
    input_file.close()
    return subjects


def display_subject_details(subjects):
    """Display formatted subject details"""
    for subject in subjects:
        print(f"{subject[0]} is taught by {subject[1]} and has {subject[2]} students")


main()
