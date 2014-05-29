class StudentBase():
    """
    Super class
    Contain student name and current points
    """
    def __init__(self, name, points):
        self.name = name
        self.points = points


class Student(StudentBase):
    """
    This class extends StudentBase class and override __lt__ for sort()
    """
    def __lt__(self, other):
        return self.points > other.points

    def __str__(self):
        return self.name + ' ' + str(self.points)
