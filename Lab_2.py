# №1
def greet(name):
    s = f'Привет {name}'
    return s
print(greet('Vlad'))


def square(number):
    return number**2
print(square(2))


def max_of_two(x, y):
    return max(x, y)
print(max_of_two(2, 3))



# №2
def describe_person(name, age=30):
    return 'Имя ' + name + ', а возраст ' + str(age)
print(describe_person('Vlad', 18))



# №3
def is_prime(number):
    tf = True
    for i in range(2, int(number**0.5)+1):
        if number % i == 0:
            tf = False
            return tf
    return tf
print(is_prime(5), is_prime(6))
