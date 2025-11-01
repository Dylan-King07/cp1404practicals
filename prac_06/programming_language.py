"""
CP1404 Practical 6 programming language exercise
Estimated time: 20 minutes
Actual time: 30 minutes
"""


class ProgrammingLanguage:
    """Represent programming language information."""

    def __init__(self, name, typing, reflection, year):
        """Using available information, build ProgrammingLanguage.

        name: string, language name
        typing: string, if language typing is 'static' or 'dynamic'
        reflection: boolean, if or if not the language has a reflection
        year: integer, the year the language appeared
        """

        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Return formatted string of ProgrammingLanguage values."""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"

    def is_dynamic(self):
        """If language is dynamically typed, return true."""
        return self.typing.lower() == "dynamic"

