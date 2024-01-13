import doctest
# TODO Написать 3 класса с документацией и аннотацией типов
class Cat:
    def __int__(self, name: str, colors: list, age: int):

        self.name = "name"
        self.colors = ["color1", "color2"]
        if not isinstance(age, (int)):
            raise TypeError
        if age < 0:
            raise ValueError
        self.age = age

    def age_in_next_year(self):
        ... #Сколько котику будет в следующем году

    def lucky_cat(self):
        ... #Трехцветные коты приносят удачу

class Class:
    def __int__(self, number: int, letter: str, number_of_students: int):

        if not isinstance(number, (int)):
            raise TypeError
        if (number < 1 or number > 11):
            raise ValueError
        self.number = number
        self.letter = "letter"
        if not isinstance(number_of_students, (int)):
            raise TypeError
        if number < 0 :
            raise ValueError
        self.number_of_students = number_of_students

    def new_study_year(self):
        if self.number == 11:
            print (self, "Graduated")
        else:
            self.number+=1
        ... #Переход в новый учебный год

    def add_new_students(self, number_of_new_students : int):
        if not isinstance(number_of_new_students, (int)):
            raise TypeError
        if number_of_new_students <  0 :
            raise ValueError
        self.number_of_students += number_of_new_students
        ... #Добавление новых учеников

class Product:
    def __init__ (self, name: str, amount: int, price: int):

        self.name= "name"
        if not isinstance(amount, (float)):
            raise TypeError
        if (amount < 0):
            raise ValueError
        self.amount = amount
        self.price= None

    def init_price(self, price: float):
        if not isinstance(price, ( float)):
            raise TypeError
        if not price > 0:
            raise ValueError
        self.price = price

    def discount_percent(self, discount_percent):
        if not isinstance(discount_percent, (int)):
            raise TypeError
        if not 0 < discount_percent <100:
            raise ValueError
        self.price = round(self.price*discount_percent/100, 2)




if __name__ == "__main__":
    doctest.testmod()
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
