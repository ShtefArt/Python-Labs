from datetime import date
from Person import Person


class Programmer(Person):
    company = "company"
    spec = "spec"
    position = "position"
    salary = 1
    project = "project"

    def __init__(self, name, surname, father_name, birth_date, comp, spec, pos, sal, proj):

        self.company = comp
        self.spec = spec
        self.position = pos
        self.salary = int(sal)
        self.project = proj
        Person.__init__(self, name, surname, father_name, birth_date)

    def get_salary(self):
        return self.salary

    def print_prog(self):
        print(self.last_name, ' ', self.first_name, ' ', self.position, ' ', self.salary)