# """ 1)  Абстрактная фабрика (Abstract factory):
#  создает семейства связанных объектов, не привязываясь к конкретным классам создаваемых объектов.
#  абстрактная фабрика возвращает объект немедленно
# """
#
# import random
#
#
# class PetShop:
#     """A pet shop"""
#
#     def __init__(self, animal_factory=None):
#         """pet_factory is our abstract factory.  We can set it at will."""
#
#         self.pet_factory = animal_factory
#
#     def show_pet(self):
#         """Creates and shows a pet using the abstract factory"""
#
#         pet = self.pet_factory()
#         print(f"We have a lovely {pet}")
#         print(f"It says {pet.speak()}")
#
#
# class Dog:
#     def speak(self):
#         return "woof"
#
#     def __str__(self):
#         return "Dog"
#
#
# class Cat:
#     def speak(self):
#         return "meow"
#
#     def __str__(self):
#         return "Cat"
#
#
# # Additional factories:
#
# # Create a random animal
# def random_animal():
#     """Let's be dynamic!"""
#     return random.choice([Dog, Cat])()
#
#
# # Show pets with various factories
# if __name__ == "__main__":
#
#     # A Shop that sells only cats
#     cat_shop = PetShop(Cat)
#     cat_shop.show_pet()
#     # dog_shop = PetShop(Dog)
#     # dog_shop.show_pet()
#     print("")
#
#     # A shop that sells random animals
#     shop = PetShop(random_animal)
#     for i in range(3):
#         shop.show_pet()
#         print("=" * 20)

# """
# 2)  Строитель (Builder):
#  От абстрактной фабрики отличается тем, что делает акцент на пошаговом конструировании объекта.
#  Строитель возвращает объект на последнем шаге, тогда как абстрактная фабрика возвращает объект немедленно.
#
#  Строитель часто используется для создания паттерна компоновщик.
# """
#
# class Builder(object):
#     def build_body(self):
#         raise NotImplementedError()
#
#     def build_lamp(self):
#         raise NotImplementedError()
#
#     def build_battery(self):
#         raise NotImplementedError()
#
#     def create_flashlight(self):
#         raise NotImplementedError()
#
#
# class Flashlight(object):
#     """Карманный фонарик"""
#     def __init__(self, body, lamp, battery):
#         self._shine = False  # излучать свет
#         self._body = body
#         self._lamp = lamp
#         self._battery = battery
#
#     def on(self):
#         self._shine = True
#
#     def off(self):
#         self._shine = False
#
#     def __str__(self):
#         shine = 'on' if self._shine else 'off'
#         return 'Flashlight [%s]' % shine
#
#
# class Lamp(object):
#     """Лампочка"""
#
#
# class Body(object):
#     """Корпус"""
#
#
# class Battery(object):
#     """Батарея"""
#
#
# class FlashlightBuilder(Builder):
#     def build_body(self):
#         return Body()
#
#     def build_battery(self):
#         return Battery()
#
#     def build_lamp(self):
#         return Lamp()
#
#     def create_flashlight(self):
#         body = self.build_body()
#         lamp = self.build_lamp()
#         battery = self.build_battery()
#         return Flashlight(body, lamp, battery)
#
#
# builder = FlashlightBuilder()
# flashlight = builder.create_flashlight()
# flashlight.on()
# print(flashlight)

