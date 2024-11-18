class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):

        if new_floor > self.number_of_floors or new_floor < 1:
            print("Такого этажа не существует")

        else:
            for i in range(1, new_floor + 1):
                print(i)


    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'


    def __eq__(self, other):
       return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors

    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors = self.number_of_floors + value
        return self

    def __radd__(self, value):
        return self.__add__(value)

    def __iadd__(self, value):
        if isinstance(value, int):
            self.number_of_floors = self.number_of_floors + value
        return self

object = House('ЖК "Кошкин дом"', 6)
object2 = House('ЖК "Собачья конура"', 18)

print(str(object))
print(str(object2))

print(object == object2)
print(object < object2)
print(object <= object2)
print(object > object2)
print(object >= object2)
print(object != object2)

print(object.__add__(10))
print(object.__add__('x'))
print(object2.__radd__(12))
print(object.__iadd__(15))

print(object < object2)


