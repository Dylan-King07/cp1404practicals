"""
CP1404 Practical 6 languages exercise
Estimated time: 10 minutes
Actual time: 15 minutes
"""

from prac_06.programming_language import ProgrammingLanguage


def main():
    """Main function for displaying ProgrammingLanguage."""
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    # Check to make sure __str__ is working
    print(python)
    print(ruby)
    print(visual_basic)

    languages = [python, ruby, visual_basic]
    print("The dynamically typed languages are: ")
    display_dynamic_languages(languages)


def display_dynamic_languages(languages):
    """Only print languages which are Dynamic."""
    for language in languages:
        if language.is_dynamic():
            print(language.name)


main()
