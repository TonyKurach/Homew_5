class Magic:

    def __init__(self, name, author, publisher, year, num_pages, price, binding):
        self.name = name
        self.author = author
        self.publisher = publisher
        self.year = year
        self.num_pages = num_pages
        self.price = price
        self.binding = binding


# 1. строковое представление объекта
    def __str__(self):
        return "Name: {}, Author: {}, Publisher: {}, Year: {}, Num_pages: {}, Price: {}, Binding: {}".format(self.name,
                                                                                                         self.author,
                                                                                                         self.publisher,
                                                                                                         self.year,
                                                                                                         self.num_pages,
                                                                                                         self.price,
                                                                                                         self.binding)

a = Magic("Запретная дверь", "Олег Синицын", "Аскона", 2013, 150, 32.15, "Плотный переплет")
print(a)

# 2. использование арифметического метода
def __mul__(self, other):
    return self.price * other
print("Новая стоимость книги: ", __mul__(a, 2), " рублей")

# 3. использование магического метода сравнения
def __eq__(self, other):
    if other is None or not isinstance(other, Magic):
        return False
    else: return self.price == other.price
b = Magic("Товарищ жандарм", "Станислав Сергеев", "АСТ", 2015, 205, 27.42, "Мягкий переплет")
print(a == b)

# 4. методы контроля доступа к атрибутам - метод "getattr":
def __getattr__(self, attrname):
    if attrname == "total_sum":
        return self.price * 100
    else: raise AttributeError
print("Выручка от реализации 100 экземпляров книги составила: ", __getattr__(a, "total_sum"), " рублей")

# 5. метод преобразования типов
def __int__(self):
    return int(self.price)
print("Стоимость книги без мелочи составляет: ", __int__(a), " рубля")
