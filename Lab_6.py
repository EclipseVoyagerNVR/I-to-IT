# №1
print('Задание 1')
class UserAccount():
    def __init__(self, username:str, email:str, password:str):
        self.__username = username
        self.__email = email
        self.__password = password

    def set_password(self, new_password):
        self.__password = new_password

    def check_password(self, password):
        if password == self.__password:
            return True
        else:
            return False

a = UserAccount('name', 'email.com', 'password_1')
a.set_password('password_1')
print(a.check_password('password_2'))
print(a.check_password('password_1'))

print('')

# №2
print('Задание 2')
class Vehical():
    def __init__(self, make:str, model:str):
        self.make = make
        self.model = model

    def get_info(self):
        return f'Марка: {self.make}, модель: {self.model}'


class Car(Vehical):
    def __init__(self, make:str, model:str, fuel_type:str):
        Vehical.__init__(self, make=make, model=model)
        self.fuel_type = fuel_type

    def get_info(self):
        return f'{Vehical.get_info(self)}, тип топлива: {self.fuel_type}'

a = Car('Toyota', 'Hilux', 'Diesel')
print(a.get_info())
