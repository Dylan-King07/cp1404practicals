"""
CP1404 prac_07 Project Management Program
Estimated time: 30 minutes
Actual time: 40 minutes
"""

from datetime import date  # Not used yet, but will be used later


class Project:
    """Represent the details of a project being managed."""

    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        """Initialise project qualities."""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        """Return projects as a string."""
        return (f"{self.name}, "
                f"start: {self.start_date.strftime('%d/%m/%Y')}, "
                f"priority {self.priority},"
                f"estimate: {self.cost_estimate:,2f},"
                f"completion: {self.completion_percentage}%")

    def __lt__(self, other):
        """Sort projects by priority."""
        return self.priority < other.priority

    def is_job_complete(self, complete=True):
        """Determine if job is 100% completed or not."""
        return self.completion_percentage if complete else self.completion_percentage != 100


