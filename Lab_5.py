# №1
class Book():
    def __init__(self, a:str, b:str, c:int):
        self.title = a
        self.author = b
        self.year = c

    def get_info(self):
        return {'title':self.title, 'autor':self.author, 'year':self.year}

a = Book('Лезвие бритвы', 'Иван Антонович Ефремов', 1963)
book = a.get_info()
print(f'Название книги: {book["title"]}, Автор: {book["autor"]}, Год издания: {book["year"]}')



# №2
class Circle():
    def __init__(self):
        self.radius = 20

    def get_radius(self):
        return self.radius

    def set_radius(self, n:int = 20):
        self.radius = n

c = Circle()
print(c.get_radius())

c.set_radius(15)
print(c.get_radius())
