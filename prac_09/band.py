from musician import Musician


class Band:
    """Band class that has a list of Musicians."""

    def __init__(self, name):
        """Initialise a Band with a name and an empty list of musicians."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a string representation of the Band and its musicians."""
        musicians_str = ', '.join(str(musician) for musician in self.musicians)
        return f"{self.name} ({musicians_str})"

    def add(self, musician):
        """Add a musician to the band's list."""
        self.musicians.append(musician)

    def play(self):
        """Return a string showing each musician playing their instrument or needing one."""
        return '\n'.join(musician.play() for musician in self.musicians)
