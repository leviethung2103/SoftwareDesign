from professor import Professor
from enroll import Enroll


class Course:
    def __init__(self, name, code, max, min, professor):
        self.name = name
        self.code = code
        self.max = max
        self.min = min
        self.professors = []
        self.enrollments = []

        # check the instance belongs to Address
        if isinstance(professor, Professor):
            self.professors.append(professor)
        elif isinstance(professor, list):
            for entry in professor:
                if not isinstance(entry, Professor):
                    raise Error("Invalid professor../")
            self.professors = professor
        else:
            raise Error("Invalid address...")

    def add_professor(self, professor):
        if not isinstance(professor, Professor):
            raise Error("Invalid professor")

        self.professors.append(professor)

    def add_enrollment(self, enroll):
        if not isinstance(enroll, Enroll):
            raise Error("Invalid enroll")

        if len(self.enrollments) == self.max:
            raise Error("Cannot enroll, course is full")

        self.enrollments.append(enroll)

    def is_cancelled(self):
        return len(self.enrollments) < self.min
