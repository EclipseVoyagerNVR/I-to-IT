class Employee():
    def __init__(self, name, id):
        self.__name = name
        self.__id = id

    def get_info(self):
        return f'Имя: {self.__name}, ID: {self.__id}'


class Manager(Employee):
    def __init__(self, name, id, department):
        Employee.__init__(self, name=name, id=id)
        self.__department = department

    def manage_project(self, department):
        return f'{Employee.get_info(self)}, отдел: {department}'


class Technician(Employee):
    def __init__(self, specialization, name, id):
        Employee.__init__(self, name=name, id=id)
        self.__specialization = specialization

    def perform_maintenance(self, specialization):
        return f'{Employee.get_info(self)}, специализация: {specialization}'


class TechManager(Manager, Technician):
    def __init__(self, name, id, department, specialization):
        Manager.__init__(self, name=name, id=id, department=department)
        Technician.__init__(self, name=name, id=id, specialization=specialization)
        self.lst = []

    def add_employee(self, name):
        self.lst.append(f'{name}')

    def get_team_info(self):
        return [name.get_info() for name in self.lst]

a = TechManager('kjds', 'sgu', 'dfk', 'dfbf')
a.add_employee('srdxfchgvb')
print(a.get_team_info())