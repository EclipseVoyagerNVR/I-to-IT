# №1
with open('example.txt', 'r') as file:
    content = file.read()
print(content)

with open('example.txt', 'r') as file:
    for line in file:
        print(line)


# №2
with open('user_input.txt', 'a') as f:
    f.write(input())
print(f)


# №3
def func(file = 'ext'):
    for i in open(file, 'r', encoding='utf-8'):
        print(i)
try:
    func()
except FileNotFoundError:
    print('Такого файла нет')
