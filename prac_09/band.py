class Band:
    """Represent a group of musicians as a band class."""
    def __init__(self, name=""):
        """Initialise a Band with information such as the name and musician list."""
        self.name = name
        self.musicians = []

    def add(self, musician):
        """Add musician to band."""
        self.musicians.append(musician)

    def play(self):
        """Musicians play their instrument."""
        return "\n".join(musician.play() for musician in self.musicians)

    def __str__(self):
        """Return band information as string."""
        musician_string = ", ".join(str(musician) for musician in self.musicians)
        return f"{self.name} ({musician_string})"
