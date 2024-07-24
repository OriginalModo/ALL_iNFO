# Inheritance - Наследование, это механизм получения доступа к данным и поведению своего предка.
# И расширению (изменению поведения) классов не меняя код
# IS-A является (наследование)
# HAS-A содержит (композиция)
# __ сделано для того чтобы при наследовании не переопределить(изменить) атрибут предка

# Поиск атрибутов/методов сначала у текущего класса затем у предка/предков если нету то AttributeError

class Employee:
    def __init__(self, name, salary, bonus):
        self.name = name
        self.salary = salary
        self.bonus = bonus

    def calculate_total_bonus(self):
        return self.salary // 100 * self.bonus

    def __str__(self):
        return f'{self.__class__.__name__} salary={self.salary}, bonus={self.bonus}%, total bonus={self.calculate_total_bonus()} rub'


class Cleaner(Employee):
    def __init__(self, name):
        super().__init__(name, 15000, 1)
    # def __init__(self, name, salary=15000, bonus=1):
    #     super().__init__(name, salary, bonus)


class Manager(Employee):
    def __init__(self, name):
        super().__init__(name, 45000, 15)


class CEO(Employee):
    def __init__(self, name):
        super().__init__(name, 105000, 100)

    def calculate_total_bonus(self):
        return 200_000


if __name__ == '__main__':
    masha = Cleaner('Maria Ivanovna')
    print(masha)
    grisha = Manager('Grigoriy Petrovich')
    print(grisha)
    ivan_palych = CEO('Ivan Pavlovych')
    print(ivan_palych)
