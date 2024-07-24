"""

 Самое Важное!!!
 Всегда ДУМАТЬ! перед тем, как что-либо сделать, необходимо всё тщательно обдумать

 Радоваться Жизни  Радоваться разным мелочам

 Ценить:         Ценить то что есть и стремиться к лучшему, Ценить сегодняшний день и брать МАКСИМУМ
 Быть проще:     Ко всему относиться Проще и Спокойнее без Волнения
 Слушать Других: Прислушиваться к мнению других людей они могут быть правы  И делать выводы
 Время:          Тайм-менеджмент   Грамотное распределение времени, Контроль Времени, Правильно раставлять Приоритеты
 Уверенность:    Быть уверенным в себе НО Оценивать свои силы!
 Развития:       Развиваться, Учиться, учиться и ещё раз - учиться, Саморазвитие
 Не Надеяться:   Надеяться только на себя
 Контроль:       Быть менее Эмоциональным, Совладать с Эмоциями, Контролировать свои эмоции в любой ситуации
 Внимательность: Быть Внимательным
 Спокойствие:    Быть Спокойнее, Перестать Нервничать , Быть Расслабленным, Не Злиться на себя и на других
 Режим:          Правильный Сон, Пить Воду
 Зарядка:        Бег, Тренировки, Стойка на Голове
 Тельце в тепле: НЕ переохлаждаться

 Молчание золото:  Лучше промолчать, чем сказать и потом жалеть о том, что сказал
 Соломон:          Все пройдёт, и это тоже пройдёт
 Вообще это замечательный подход: осознать, что проблема не такая уж и проблема, и вполне решаема.
 Кто ищет-тот всегда найдет!
 Искать Другие способы
 Не спеши, а то успеешь...   Успеешь, но не туда куда хотел...
 Подумай, нужно ли тебе ЭТО и для Чего
 Надо принимать вещи такими, как они есть, и пользоваться ими с наибольшей для себя выгодой.
 Если научиться принимать вещи как они есть, страдание исчезнет.
________________________________________________________________________________________________________________________


 --- functools Функции высшего порядка и операции над вызываемыми объектами ---

 Модуль functools предназначен для функций высшего порядка: функций, которые действуют или возвращают другие функции.
 В общем, любой вызываемый объект может рассматриваться как функция для целей этого модуля.

________________________________________________________________________________________________________________________
 --- Кэширование значений ---
 Кэширование результатов представлено тремя функциями (можно использовать в качестве декоратора)
 - functools.lru_cache(),- functools.cache(),- functools.cached_property().
 .cache_info() - информацию о кэше, который показывает количество попаданий и промахов в кэш.
 .clear_cache() - функцию очистки или аннулирования кеша. Для очистки или аннулирования кэшированных результатов.
 .cache_parameters() - проверки параметров.

________________________________________________________________________________________________________________________
 @functools.cache(user_function) - Легкий кеширующий декоратор функций.

 Представляет собой простой легкий неограниченный кеш функций. Иногда называется "memoization",  “memoize”(«запоминание»).


 Возвращает то же самое, что и @lru_cache(maxsize=None), создавая тонкую оболочку вокруг поиска по словарю для
 аргументов функции. Так как ему никогда не нужно удалять старые значения, он меньше и быстрее, чем @functools.lru_cache()
 с ограничением размера.

 import functools

 @functools.cache
 def factorial(n):
     return n * factorial(n-1) if n else 1

 # нет ранее кэшированного результата,
 # выполняет 11 рекурсивных вызовов
 factorial(10)
 # 3628800

 # просто ищет результат кэшированного значения
 factorial(5)
 # 120

 # делает два новых рекурсивных вызова,
 # остальные 10 кэшируются
 factorial(12)
 # 479001600

 factorial.cache_info()  #  CacheInfo(hits=2, misses=13, maxsize=None, currsize=13)
 factorial.cache_parameters() #  {'maxsize': None, 'typed': False}
________________________________________________________________________________________________________________________
 @functools.cached_property(func) - Кешировать метод класса и преобразовать его в свойство.

 Используется для кэширования результатов атрибутов класса. Это очень полезно, если есть свойство, которое дорого вычислять,
 но при этом является неизменяемым. Работает аналогично встроенной функции property() с добавлением кэширования.

 Механика cached_property() несколько отличается от property(). Атрибут обычного свойства блокирует запись, если не
 определен установщик. Напротив, свойство cached_property разрешает запись.

 Кэшированное значение можно очистить, удалив атрибут. Это позволит методу cached_property запуститься снова.

 from functools import cached_property

 class DataSet:

    def __init__(self, sequence_of_numbers):
        self._data = tuple(sequence_of_numbers)

    @cached_property
    def stdev(self):
        return statistics.stdev(self._data)
________________________________________________________________________________________________________________________
 @functools.lru_cache(user_function), @functools.lru_cache(maxsize=128, typed=False) - Кеширование результата выполнения функции

 Декоратор @lru_cache() модуля functools оборачивает функцию с переданными в нее аргументами и запоминает возвращаемый
 результат соответствующий этим аргументам. Такое поведение может сэкономить время и ресурсы, когда дорогая или
 связанная с вводом/выводом функция периодически вызывается с одинаковыми аргументами.

 Позиционные и ключевые аргументы, переданные в функцию должны быть хешируемыми, т.к. для кэширования результатов
 декоратор lru_cache() использует словарь.

 max_size - ограничивает количество кэшированных значений.
 Если для параметра maxsize установлено значение None, функция LRU отключена, и кэш может расти без ограничений.

 Пример 1:
 import functools

 @functools.lru_cache  # НЕ ограничивает количество кэшированных значений.
 def count_vowels(sentence):
     return sum(sentence.count(vowel) for vowel in 'AEIOUaeiou')

 # print(count_vowels({'a', 'b', 'z'})) # TypeError: unhashable type: 'set'
 print(count_vowels('abc')) # 1
 print(count_vowels.cache_info())  # CacheInfo(hits=0, misses=1, maxsize=128, currsize=1)
 # print(count_vowels.cache_clear()) # Очистка кэша
 print(count_vowels.cache_parameters())  # {'maxsize': 128, 'typed': False}

 Пример 2:
 from functools import lru_cache

 @lru_cache(maxsize=32) # ограничивает количество кэшированных значений.
 def count_vowels(sentence):
     return sum(sentence.count(vowel) for vowel in 'AEIOUaeiou')


 print(count_vowels(['a', 'b', 'z'])) # TypeError: unhashable type: 'list'
 print(count_vowels(('a', 'b', 'z'))) # 1
 print(count_vowels.cache_info()) # CacheInfo(hits=0, misses=1, maxsize=32, currsize=1)
 # print(count_vowels.cache_clear()) # Очистка кэша
 print(count_vowels.cache_parameters()) # {'maxsize': 32, 'typed': False}

 Пример эффективного вычисления чисел Фибоначчи с использованием кэша для реализации метода динамического программирования:
 from functools import  lru_cache
 @lru_cache(maxsize=None)
 def fib(n):
     if n < 2:
         return n
     return fib(n-1) + fib(n-2)


 print([fib(n) for n in range(16)])
 # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
 print(fib.cache_info())
 # CacheInfo(hits=28, misses=16, maxsize=None, currsize=16)
________________________________________________________________________________________________________________________
 @functools.total_ordering - Автоматическая реализация операторов сравнения.

 Класс должен определить один из __lt__(), __le__(), __gt__() или __ge__().
 Кроме того, класс должен предоставить __eq__() метод а остальные будут автоматически созданы декоратором:

 from functools import total_ordering

 @total_ordering
 class Number:
     def __init__(self, value):
         self.value = value

     def __lt__(self, other):
         return self.value < other.value

     def __eq__(self, other):
         return self.value == other.value

 print(Number(20) > Number(3))
 # True
 print(Number(1) < Number(5))
 # True
 print(Number(15) >= Number(15))
 # True
 print(Number(10) <= Number(2))
 # False

 Примечание: Хотя этот декоратор позволяет легко создавать полностью упорядоченные типы с хорошим поведением,
 за это приходится платить более медленным выполнением и более сложными трассировками стека для производных методов
 сравнения. Если тесты производительности показывают, что это узкое место для данного приложения, вместо этого реализация
 всех шести расширенных методов сравнения, вероятно, обеспечит легкий прирост скорости.
________________________________________________________________________________________________________________________
 functools.cmp_to_key(func) - преобразует функцию сравнения старого стиля в ключевую функцию сравнения.

 Используется с инструментами, которые принимают в качестве ключа сортировки функцию, такие как:
 sorted(), min(), max(), heapq.nlargest(), heapq.nsmallest(), itertools.groupby(). Эта функция в основном используется
 в качестве инструмента перехода для программ, конвертируемых из Python 2.

 Функция сравнения - это любой вызываемый объект, который принимает два аргумента, сравнивает их и возвращает
 отрицательное число для "меньше чем", ноль для равенства значений и положительное число для "больше чем".

 key function(ключевая функция) - функция, принимающая один аргумент и возвращающая другое значение, определяющее
 положение аргумента при сортировке. Примеры:
 sorted(['ab', 'a', 'c'], key=len) -> ['a', 'c', 'ab'],  max([1, 2, 'a'], key=str) -> 'a'
 sorted(['ab', 'a', 'c', 1]) -> TypeError: '<' not supported between instances of 'int' and 'str'
 sorted(['ab', 'a', 'c', 1], key=str) -> [1, 'a', 'ab', 'c']
 Функция, используемая в качестве ключа - это вызываемый объект, который принимает один аргумент и возвращает другое
 значение, которое будет использоваться в качестве ключа сортировки.

 Ряд инструментов Python поддерживают ключевые функции для управления упорядочением или группировкой элементов.
 К ним относятся min(), max(), sorted(), list.sort(), heapq.merge(), heapq.nsmallest(), heapq.nlargest(), и itertools.groupby().

 from functools import cmp_to_key
 import locale

 # locale-aware sort order
 new_iterable = sorted(iterable, key=cmp_to_key(locale.strcoll))
________________________________________________________________________________________________________________________
 functools.partial(func, /, *args, **keywords) - Заморозить часть аргументов вызываемой функции.

 возвращает partial-объект (частичный объект) (по сути, функцию).
 используется для частичного применения каких то аргументов к вызываемой
 функции func. Другими словами partial() "замораживает" некоторую часть аргументов и/или ключевых слов, в результате
 чего создается новый объект с упрощенной записью аргументов вызываемой функции func.

 Пример 1:
 from functools import partial

 def multiply(x, y):
     return x * y

 doubleNum = partial(multiply, 2)
 tripleNum = partial(multiply, 3)
 res = multiply(10, 2)

 print(res)  # 20
 print(multiply(10, 2))  # 20
 print(doubleNum(20))  # 40
 print(tripleNum(20))  # 60

 Пример 2:
 from functools import partial

 def orderFunc(a, b, c, d):
     return a * 4 + b * 3 + c * 2 + d

 result = partial(orderFunc, 5, 6, 7)

 print(orderFunc(5, 6, 7, 8))   # 60
 print(result(8))               # 60

 Пример 3:
 from functools import partial

 def orderFunc(a, b, c, d):
     return a * 4 + b * 3 + c * 2 + d

 result = partial(orderFunc, c=5, d=6)

 print(orderFunc(8, 4, c=5, d=6)) # 60
 print(result(8, 4))              # 60
________________________________________________________________________________________________________________________
 class functools.partialmethod(func, /, *args, **keywords) - Заморозить часть аргументов метода класса.

 возвращает новый дескриптор метода func, который ведет себя как функция functools.partial(), за исключением того,
 что он предназначен для использования в качестве определения метода, а не для прямого вызова.

 Аргумент func должен быть дескриптором (определяет методы __get__(), __set__() или __delete__() или вызываемым методом класса.

 from functools import partialmethod

 class Cell(object):
     def __init__(self):
         self._alive = False

     @property
     def alive(self):
         return self._alive

     def set_state(self, state):
         self._alive = bool(state)

     set_alive = partialmethod(set_state, True)
     set_dead = partialmethod(set_state, False)


 c = Cell()
 print(c.alive)
 #  False
 c.set_alive()
 print(c.alive)
 #  True
________________________________________________________________________________________________________________________
 functools.reduce(function, iterable[, initializer]) - берет итерируемый объект и уменьшает (или складывает) все его значения в одно.

 кумулятивно применяет функцию function к элементам итерируемой iterable последовательности, сводя её к единственному значению.

 Примените функцию двух аргументов кумулятивно к элементам iterable слева направо, чтобы свести итерируемый объект к одному значению.

 Например reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) вычисляет ((((1 + 2) +3) +4) +5).
 Левый аргумент x - это накопленное значение, а правый аргумент y - это следующий элемент iterable.

 Функция reduce() эквивалентна следующему коду:
 def reduce(function, iterable, initializer=None):
    it = iter(iterable)
    if initializer is None:
        value = next(it)
    else:
        value = initializer
    for element in it:
        value = function(value, element)
    return value

 Пример 1:   Вычисление суммы всех элементов списка при помощи модуля operator и функции functools.reduce():
 from functools import reduce
 import operator
 # допустим имеем список чисел
 numbers = list(range(1, 11))
 print(reduce(operator.add, numbers))
 # 55
 print(reduce(operator.sub, numbers))
 # -53
 print(reduce(operator.mul, numbers))
 # 3628800
 print(reduce(operator.truediv, numbers))
 # 2.7557319223985894e-07

 Пример 2:   Вычисление суммы всех элементов списка при помощи reduce() и lambda-функции:
 from functools import reduce

 itemss = [10, 20, 30, 40, 50]
 print(reduce(lambda x, y: x + y, itemss)) # 150

 Пример 3:  Вычисление наибольшего элемента в списке при помощи reduce():
 from functools import reduce

 itemss = [1, 24, 17, 14, 9, 32, 2]
 print(reduce(lambda a, b: a if (a > b) else b, itemss))
________________________________________________________________________________________________________________________
 Перегрузка методов/функций.
 Всех учили, что перегрузка функций невозможна в Python, но на самом деле есть простой способ реализовать ее,
 используя две функции в модуле functools - это functools.singledispatch() и/или functools.singledispatchmethod().
 Эти функции помогают реализовать то, что называется алгоритмом множественной отправки, который позволяет языкам
 программирования с динамической типизацией, таким как Python, различать типы во время выполнения.

 @functools.singledispatch - Декоратор @singledispatch модуля functools создает из обычной функции - универсальную
 функцию одиночной диспетчеризации.

 Универсальная (generic) функция это функция, составленная из нескольких функций, реализующих одну и ту же операцию
 для различных типов. Нужная реализация при этом определяется алгоритмом диспетчеризации.

 Одиночная (single) диспетчеризация это алгоритм диспетчеризации для универсальных функций, при котором нужная
 реализация выбирается на основе типа одного аргумента.

 Чтобы определить универсальную функцию, оберните ее с помощью декоратора @singledispatch. Обратите внимание,
 что в перегруженные реализации передается тип первого аргумента:

 from functools import singledispatch

 @singledispatch
 def fun(arg, verbose=False):
     if verbose:
         print("Let me just say,", end=" ")
     print(arg)

 fun('Sasya', False) # Sasya
 fun('Sasya', True) # Let me just say, Sasya

 Чтобы добавить перегруженные реализации в функцию, используйте атрибут .register() обобщенной функции fun.
 Выражение fun.register() то же является декоратором. Для функций, аннотированных типами, декоратор @singledispatch
 автоматически выведет тип первого аргумента:

 from functools import singledispatch
 @singledispatch
 def fun(arg, verbose=False):
     if verbose:
         print("Let me just say,", end=" ")
     print(arg)


 @fun.register
 def _(arg: int, verbose=False):
     if verbose:
         print("Strength in numbers, eh?", end=" ")
     print(arg)


 @fun.register
 def _(arg: list, verbose=False):
     if verbose:
         print("Enumerate this:")
     for i, elem in enumerate(arg):
         print(i, elem)

 fun('Sasya', False) # Sasya
 fun('Sasya', True)  # Let me just say, Sasya
________________________________________________________________________________________________________________________
 class functools.singledispatchmethod(func) - Декоратор singledispatchmethod() модуля functools создает из обычного
 метода класса - универсальный метод одиночной диспетчеризации.

 Чтобы определить универсальный метод, оберните его с помощью декоратора @singledispatchmethod. Обратите внимание,
 что в перегруженные реализации передается тип первого аргумента, а не-self или non-cls:

 class Negator:
    @singledispatchmethod
    def neg(self, arg):
        raise NotImplementedError("Cannot negate a")

    @neg.register
    def _(self, arg: int):
        return -arg

    @neg.register
    def _(self, arg: bool):
        return not arg

 Декоратор @singledispatchmethod поддерживает вложение с другими декораторами, такими как @classmethod.
 Обратите внимание, что для использования dispatcher.register, декоратор @singledispatchmethod должен быть внешним.
 Вот класс Negator с методом neg, привязанным к классу:

 class Negator:
    @singledispatchmethod
    @classmethod
    def neg(cls, arg):
        raise NotImplementedError("Cannot negate a")

    @neg.register
    @classmethod
    def _(cls, arg: int):
        return -arg

    @neg.register
    @classmethod
    def _(cls, arg: bool):
        return not arg

 Тот же шаблон может быть использован для других подобных декораторов, например @staticmethod и других.
________________________________________________________________________________________________________________________
 functools.update_wrapper(wrapper, wrapped, assigned=WRAPPER_ASSIGNMENTS, updated=WRAPPER_UPDATES) -
 Заменить атрибуты функции атрибутами другой функции.

 Декоратор @update_wrapper() модуля functools обновляет функцию-обертку wrapped, чтобы она выглядела как исходная
 функция wrapper. Другими словами дополняет функцию-обертку, данными из некоторых атрибутов оборачиваемой функции.

 Основное предназначение @update_wrapper() - функции декоратора, которые оборачивают декорированную функцию
 и возвращают обертку. Если функция декоратора не обновляется, метаданные возвращенной функции будут отражать
 определение оболочки, а не исходное определение функции, которое обычно менее чем полезно.

 from functools import update_wrapper

 def my_func():
     '''Wrapped function. - docstring'''
     return 'This original func'

 def wrapper_func():
     '''Wrapped function.'''
     return 'This wrapper func'


 wrapper_func = update_wrapper(wrapper_func, my_func)
 print(wrapper_func.__name__)
 # 'my_func'
 print(wrapper_func.__doc__)
 # 'Wrapped function.'
 print(wrapper_func())
 # This wrapper func
 print(wrapper_func.__wrapped__())
 # This original func
________________________________________________________________________________________________________________________
 @functools.wraps(wrapped, assigned=WRAPPER_ASSIGNMENTS, updated=WRAPPER_UPDATES) - Сохранение имени и строк документации
 декорированной функции.   Заменить атрибуты декоратора на атрибуты исходной функции.

 Декоратор @wraps() модуля functools это удобная функция для вызова @functools.update_wrapper() в качестве декоратора
 при определении функции-обертки.

 Декоратор @wraps() частично эквивалентно вызову partial(update_wrapper, wrapped=wrapped, assigned=assigned, updated=updated).

 from functools import wraps
 def my_decorator(f):
     @wraps(f)
     def wrapper(*args, **kwds):
         print('Calling decorated function')
         return f(*args, **kwds)
     return wrapper

 @my_decorator
 def example():
     '''Docstring'''
     print('Called example function')

 example()
 # Calling decorated function
 # Called example function
 print(example.__name__)
 'example'
 print(example.__doc__)
 'Docstring'
________________________________________________________________________________________________________________________















"""