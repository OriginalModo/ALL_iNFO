"""
Приспособленец (Flyweigth)(Легковес , Кэш):

Суть: предназначен для эффективной поддержки множества мелких обьектов в памяти путем разделения общего состояния между ними
и чтобы в этих обьектах не осуществлялось хранения одинаковых данных

в основе лежит Абстракная фабрика


В каких случаях рекомендуется использовать:
1) в приложении используется слишком большое количество обьектов, что увеличивает требования по памяти
2) не хватает памяти для поддержки всех нужных обьектов
3) большую часть состояния (параметров) можно вынести за пределы обьектов

Плюсы:
--- Позволяет экономить оперативную память

Минусы:
--- требует дополнительное время (процессорные ресурсы) на поиск уже существующего или вычисления контекста для создания нового обьекта
--- добавление в кодовую базу системы множества дополнительных классов
"""



class PizzaOrderFlyWeight:

    def __init__(self, shared_state):
        self.shared_state = shared_state

    def __repr__(self):
        return str(self.shared_state)

class PizzaOrderContext:

    def __init__(self, unique_state, flyweight: PizzaOrderFlyWeight):
        self.unique_state = unique_state
        self.flyweight = flyweight

    def __repr__(self):
        return f'уникальное состояние: {self.unique_state} \n' \
               f'разделяемое состояние: {self.flyweight}'

class FlyWeightFactory:

    def __init__(self):
        self.flyweights = []

    def get_flyweight(self, shared_state) -> PizzaOrderFlyWeight:
        flyweights = list(filter(lambda x: x.shared_state == shared_state, self.flyweights))

        if flyweights:
            return flyweights[0]
        else:
            flyweights = PizzaOrderFlyWeight(shared_state)
            self.flyweights.append(flyweights)
            return flyweights

    @property
    def total(self):
        return len(self.flyweights)


class PizzaOrderMaker:

    def __init__(self, flyweight_factory: FlyWeightFactory):
        self.flyweight_factory = flyweight_factory
        self.contexts = []

    def make_pizza_order(self, unique_state, shared_state) -> PizzaOrderFlyWeight:
        flyweight = self.flyweight_factory.get_flyweight(shared_state)
        context = PizzaOrderContext(unique_state, flyweight)
        self.contexts.append(context)
        return context

if __name__ == '__main__':
    flyweight_factory = FlyWeightFactory()
    pizza_maker = PizzaOrderMaker(flyweight_factory)

    shared_states = [(30, 'Большая пицца'),
                     (25, 'Средняя пицца'),
                     (15, 'Маленькая пицца'),]
    unique_states = ['Маргатира','Салями','4 сыра']

    orders = [pizza_maker.make_pizza_order(x, y)
              for x in unique_states
              for y in shared_states]
    print('Количество созданных пицц:', len(orders))
    print('Количество разделенных обьектов:', flyweight_factory.total)
    for index, pizza in enumerate(orders):
        print('-'*50)
        print(f'Номер пиццы в списке: {index}')
        print(pizza)
