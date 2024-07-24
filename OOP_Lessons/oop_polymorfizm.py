# Полиморфизм(Много форм) -  это механизм, позволяющий выполнять один и тот же код по-разному
# Ducktyping (утиная типизация) - наличие поведения для использования в полиморфизме

# В ЯП со статической типизацией для полиморфизма важно кто ты (какой тип)
# Для питона важно что ты умеешь (поведение)


class Animal:
    def make_noise(self):
        print('shh')


class Cat(Animal):
    def make_noise(self):
        print('meow')


class Dog(Animal):
    def make_noise(self):
        print('gavv')

class Car:
    def make_noise(self):
        print('bi-bi')



def noise(animal: Animal):
    animal.make_noise()


if __name__ == '__main__':
    noise(Car())
