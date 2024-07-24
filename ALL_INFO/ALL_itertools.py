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


--- Модуль itertools в Python, эффективные итераторы для циклов   - сборник полезных итераторов ---

 Эти инструменты и их встроенные аналоги также хорошо работают с высокоскоростными функциями в модуле operator.
 Например, оператор умножения может отображаться на два вектора для формирования эффективного точечного произведения:

 sum(map(operator.mul, vector1, vector2)).

 Но если itertools вам уже не хватает, то вэлкам: more-itertools.
 Тут есть chunked, spy, first, one, only, unique_everseen и прочие прелести. Осторожно, с этой дряни невозможно слезть.

________________________________________________________________________________________________________________________
 --- Бесконечные итераторы   Infinite iterators ---

 Модуль itertools поставляется с тремя итераторами, которые могут повторяться бесконечно. Это означает, что при их
 использовании необходимо понимать, что в конце концов нужно будет как то выходить из этих итераторов, иначе будет бесконечный цикл.
________________________________________________________________________________________________________________________
 itertools.count(start=0, step=1) - Создать бесконечную равномерно распределенную последовательность.

 создает бесконечный итератор, который возвращает равномерно распределенные значения, начиная с номера start с шагом step.

 Часто используется в качестве аргумента функции map() для генерации последовательных значений данных. Также
 используется с функцией zip() для добавления порядковых номеров.


 Функция itertools.count() примерно эквивалентна следующему коду:

 def count(start=0, step=1):
    # count(10) --> 10 11 12 13 14 ...
    # count(2.5, 0.5) -> 2.5 3.0 3.5 ...
    n = start
    while True:
        yield n
        n += step

 Примеры 1:
 from itertools import count

 for i in count(10):
     if i > 15:
         break
     else:
         print(i, end=' ')  #  10 11 12 13 14 15

 Примеры 2:
 from itertools import count
 for i in count(10):
     print(i, end=' ')
     if i > 16:
         print()
         break
 # 10 11 12 13 14 15 16 17


 for i in count(10, 0.5):
     print(i, end=' ')
     if i > 13:
         print()
         break
 # 10 10.5 11.0 11.5 12.0 12.5 13.0 13.5

 Другой способ ограничить вывод этого бесконечного итератора - использовать другую функцию из itertools с именем itertools.islice().

 from itertools import islice, count
 for i in islice(count(10), 5):
    print(i, end=' ')  #  10 11 12 13 14
________________________________________________________________________________________________________________________
 itertools.cycle(iterable) -  Создает бесконечный итератор из значений последовательности.

 создает бесконечный итератор, возвращающий элементы из итерируемой последовательности iterable и сохраняющий копию
 каждого элемента. Когда последовательность iterable исчерпана, начинает возвращать элементы из сохраненной копии.

 Обратите внимание, что этому члену набора инструментов может потребоваться значительный дополнительный объем памяти
 (в зависимости от длины итерации).

 Примерно эквивалентно:

 # аргументу передается итератор
 # как мы знаем - итератор конечен
 def cycle(iterable):
     # cycle('ABCD') --> A B C D A B C D A B C D ...
     saved = []
     for element in iterable:
         yield element
         saved.append(element)
     while saved:
         for element in saved:
               yield element

 Примеры 1:
 from itertools import cycle
 x = list(range(5))
 print(x)  # [0, 1, 2, 3, 4]

 for index, value in enumerate(cycle(x)):
     print(value, end=' ')
     if index > 13:
         print()
         break
 # 0 1 2 3 4 0 1 2 3 4 0 1 2 3 4

 Примеры 2:
 from itertools import cycle
 for index, item in enumerate(cycle('XYZ')):
     if index > 5:
         break
     print(item, end=' ')
 # X Y Z X Y Z

 Примеры 3:
 from itertools import cycle
 polys = ['triangle', 'square', 'pentagon']
 iterator = cycle(polys)
 next(iterator)
 # 'triangle'
 next(iterator)
 # 'square'
 next(iterator)
 # 'pentagon'
 next(iterator)
 # 'triangle'
 next(iterator)
 # 'square'
_________________________________________________________________________________________________________________________
 itertools.repeat(object[, times]) - Ленивое повторение объекта.

 будет возвращать переданный объект (например словарь, список и т.д. ) снова и снова (бесконечно), если НЕ установить
 аргумент times, который отвечает за количество повторений.

 Инвариант - программный объект, не изменяющийся в процессе выполнения. Остающийся неизменным при определённых
 преобразованиях, при переходе к новым условиям.

 Инвариант – это условие или отношение, которое всегда истинно .

 Создает итератор, который возвращает объект снова и снова. Работает бесконечно, если не указан аргумент times.

 Функция используется в качестве аргумента для map() для инвариантных параметров вызываемой функции.
 Также используется с zip() для создания инвариантной части записи кортежа.

 Функция itertools.repeat() примерно эквивалентна следующему коду:

 def repeat(object, times=None):
    # repeat(10, 3) → 10 10 10
    if times is None:
        while True:
            yield object
    else:
        for i in range(times):
            yield object

 Примеры 1:
 from itertools import repeat
 lst = [1, 2]
 # передаем объект списка
 # и устанавливаем 2 повтора
 for list_obj in repeat(lst, 2):
     for i in list_obj:
         print(i, end=' ')
 # 1 2 1 2

 Обычное использование для itertools.repeat() - предоставить поток постоянных значений для map() или zip():
 Примеры 2:
 from itertools import repeat

 # квадраты элементов списка
 list(map(pow, range(10), repeat(2)))
 # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

 # кубы элементов списка
 list(map(pow, range(10), repeat(3)))
 # [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]

_________________________________________________________________________________________________________________________
 --- Конечные итераторы    Iterators terminating on the shortest input sequence ---
 --- Итераторы, оканчивающиеся на самой короткой входной последовательности ---
_________________________________________________________________________________________________________________________
 itertools.accumulate(iterable[, func, *, initial=None]) - Накопление результатов работы функции для элементов списка.

 создает итератор, который возвращает накопленные суммы или накопленные результаты другой функции, которая задается
 с помощью необязательного аргумента func.

 functools.reduce(). аналогичную функцию, которая возвращает только окончательное накопленное значение.

 Функция itertools.accumulate() примерно эквивалентна следующему коду:
 def accumulate(iterable, func=operator.add, *, initial=None):
    'Return running totals'
    # accumulate([1,2,3,4,5]) --> 1 3 6 10 15                            # Пример как работает функция  accumulate()
    # accumulate([1,2,3,4,5], initial=100) --> 100 101 103 106 110 115   # Пример как работает функция  accumulate()
    # accumulate([1,2,3,4,5], operator.mul) --> 1 2 6 24 120             # Пример как работает функция  accumulate()
    it = iter(iterable)
    total = initial
    if initial is None:
        try:
            total = next(it)
        except StopIteration:
            return
    yield total
    for element in it:
        total = func(total, element)
        yield total

 Примеры 1:

 from itertools import accumulate

 print(list(accumulate(range(10))))
 # [0, 1, 3, 6, 10, 15, 21, 28, 36, 45]

 import itertools, operator

 # Таким образом, для каждой итерации - значения умножается (1x1, 1x2, 2x3 и т. д.), а не складывается.
 print(list(itertools.accumulate(range(1, 5), operator.mul)))
 # [1, 2, 6, 24]
 print(list(itertools.accumulate(range(1, 5), operator.mul, initial=100)))
 # [100, 100, 200, 600, 2400]

 Примеры 2:
 Можно установить значение min() для рабочего минимума, max() для рабочего максимума или operator.mul() для работающего продукта:
 from itertools import accumulate
 import operator
 data = [3, 4, 6, 2, 1, 9, 0, 7, 5, 8]
 print(list(accumulate(data, operator.mul)))
 # [3, 12, 72, 144, 144, 1296, 0, 0, 0, 0]
 print(list(accumulate(data, max)))
 # [3, 4, 6, 6, 6, 9, 9, 9, 9, 9]

 Примеры 3:
 Можно построить таблицы амортизации, накапливая проценты и применяя платежи:
 # Амортизация 5%, кредит 1000 с 4 ежегодными платежами по 90
 from itertools import accumulate
 cashflows = [1000, -90, -90, -90, -90]
 print(list(accumulate(cashflows, lambda bal, pmt: bal * 1.05 + pmt)))
 # [1000, 960.0, 918.0, 873.9000000000001, 827.5950000000001]
________________________________________________________________________________________________________________________
 itertools.batched(iterable, n) - Разбивает данные по кортежам определенной длины.     Новое в версии 3.12.

 разбивает пакетные данные из итерируемого объекта iterable на кортежи длиной n. Последняя партия может быть короче n.

 Примерно эквивалентно:
 def batched(iterable, n):
    # batched('ABCDEFG', 3) → ABC DEF G
    if n < 1:
        raise ValueError('n must be at least one')
    it = iter(iterable)
    while batch := tuple(islice(it, n)):
        yield batch

 Примеры 1:
 from itertools import islice, batched

 def batched(iterable, n):
     # batched('ABCDEFG', 3) --> ABC DEF G
     if n < 1:
         raise ValueError('n must be at least one')
     it = iter(iterable)
     while batch := tuple(islice(it, n)):
         yield batch

 flattened_data = ['roses', 'red', 'violets', 'blue', 'sugar', 'sweet']
 unflattened = list(batched(flattened_data, 2))
 print(unflattened)
 # [('roses', 'red'), ('violets', 'blue'), ('sugar', 'sweet')]

 for batch in batched('ABCDEFG', 3):
     print(batch)

 # ('A', 'B', 'C')
 # ('D', 'E', 'F')
 # ('G',)
________________________________________________________________________________________________________________________
 itertools.chain(*iterables) - берет серию итераций и, по сути, "сглаживает" их в одну общую итерацию.
 Объединить несколько списков в один.

 Функция itertools.chain() примерно эквивалентна следующему коду:
 def chain(*iterables):
    # chain('ABC', 'DEF') --> A B C D E F
    for it in iterables:
        for element in it:
            yield element

 Примеры 1:
 from itertools import chain
 it1 = range(1, 6)
 it2 = range(10, 16)
 it3 = {'a': 'new', 'b': 'cool'}
 rez = chain(it1, it2, it3.items())
 print(list(rez))
 # [1, 2, 3, 4, 5, 10, 11, 12, 13, 14, 15, ('a', 'new'), ('b', 'cool')]

 Примеры 2:
 from itertools import chain
 lst = ['foo', 'bar', ['one', 'two']]
 new_list = list(chain(lst, range(5)))
 print(new_list)
 # ['foo', 'bar', ['one', 'two'], 0, 1, 2, 3, 4]

 То же самое можно сделать без использования itertools при помощи оператора сложения или list.extend(),
 но при этом получится НЕ ИТЕРАТОР, а список, который увеличит расход памяти (будет содержать в себе копии списков):

 new_list = ['foo', 'bar', ['one', 'two']]
 new_list += range(5)
 print(new_list)
 # ['foo', 'bar', ['one', 'two'], 0, 1, 2, 3, 4]

 или

 new_list = ['foo', 'bar', ['one', 'two']]
 new_list.extend(range(5))
 print(new_list)
 # ['foo', 'bar', ['one', 'two'], 0, 1, 2, 3, 4]
________________________________________________________________________________________________________________________
 classmethod chain.from_iterable(iterable) - Объединить список списков в единый список
 Он работает немного иначе, чем прямое использование itertools.chain() и принимает в качестве аргумента на серию итераций,
 а список с вложенными списками, которые необходимо сгладить.

 Примеры 1:
 from itertools import chain

 it1 = list(range(1, 6))
 it2 = list(range(10, 16))
 lists_in_list = [it1, it2]
 print(lists_in_list)
 # [[1, 2, 3, 4, 5], [10, 11, 12, 13, 14, 15]]
 print(list(chain(lists_in_list)))
 # [[1, 2, 3, 4, 5], [10, 11, 12, 13, 14, 15]]
 print(list(chain.from_iterable(lists_in_list)))
 # [1, 2, 3, 4, 5, 10, 11, 12, 13, 14, 15]

 Примеры 2:
 from itertools import chain
 lst = ['foo', ['one', 'two', [1, 2]]]
 print(list(chain(lst)))
 # ['foo', ['one', 'two', [1, 2]]]
 print(list(chain.from_iterable(lst)))
 # ['f', 'o', 'o', 'one', 'two', [1, 2]]
________________________________________________________________________________________________________________________
 itertools.compress(data, selectors) - Фильтр элементов на основе списка из False и True

 создает итератор, который фильтрует элементы из данных data, возвращая только те, которые имеют соответствующий элемент,
 равный True или 1 в последовательности selectors.

 Примерно эквивалентно:

 def compress(data, selectors):
    # compress('ABCDEF', [1,0,1,0,1,1]) --> A C E F
    return (d for d, s in zip(data, selectors) if s)

 Бессмысленный пример, зато показывает как работает функция:

 from itertools import compress
 # есть строка
 letters = 'ABCDEFG'
 # нужно получить итерацию из букв
 true_letter = 'AEG'
 # создадим список логических значений
 bools = [x in true_letter for x in letters]
 print(bools)
 # [True, False, False, False, True, False, True]

 # Подставляем
 print(list(compress(letters, bools)))
 # ['A', 'E', 'G']

 Пример 2:
 from itertools import compress
 data = 'ABCDEF'
 selectors = [1, 0, 1, 0, 1, 1]
 rez = compress(data, selectors)
 print(list(rez))
 # ['A', 'C', 'E', 'F']
________________________________________________________________________________________________________________________
 itertools.dropwhile(predicate, iterable) - Последовательно удалять элементы списка пока условие истинно.

 создает итератор, который удаляет элементы из последовательности iterable до тех пор, пока функция
 predicate равна True или 1. Возвращается итератор с отобранными элементами.

 отбрасывает элементы, пока критерий фильтра равен True. Другими словами, он не будет выдавать выходные данные,
 пока предикат не станет ложным. Это может увеличить время запуска, поэтому об этом нужно знать.

 Функция itertools.dropwhile() примерно эквивалентна следующему коду:

 def dropwhile(predicate, iterable):
    # dropwhile(lambda x: x<5, [1,4,6,4,1]) --> 6 4 1
    iterable = iter(iterable)
    for x in iterable:
        if not predicate(x):
            yield x
            break
    for x in iterable:
        yield x

 Пример 1:
 from itertools import dropwhile

 print(list(dropwhile(lambda x: x < 5, [1, 4,           6, 4, 1])))
 # [6, 4, 1]

 Пример 2:
 from itertools import dropwhile
 def trigger_to_five(x):
     return x > 5

 lst = [6, 7, 8, 9, 1, 2, 3, 10]
 print(list(dropwhile(trigger_to_five, lst)))
 # [1, 2, 3, 10]

 Пример 3:
 from itertools import dropwhile
 x = list(range(6))
 y = sorted(x, reverse=True)
 z = x + y
 print(z)
 # [0, 1, 2, 3, 4, 5, 5, 4, 3, 2, 1, 0]

 # например не нужны данные списка до определенного значения.
 rez = dropwhile(lambda x: x < 5, z)
 print(list(rez))
 # [5, 5, 4, 3, 2, 1, 0]

 rez = dropwhile(lambda x: x < 3, z)
 print(list(rez))
 # [3, 4, 5, 5, 4, 3, 2, 1, 0]
________________________________________________________________________________________________________________________
 itertools.takewhile(predicate, iterable) - Последовательно возвращать элементы списка пока условие истинно.

 противоположна итератору itertools.dropwhile(), который рассматривали ранее. Функция itertools.takewhile() создаст итератор,
 который будет возвращать элементы из итерируемого объекта только до тех пор, пока предикат или триггер имеет значение True.

 Функция itertools.takewhile() примерно эквивалентна следующему коду:

 def takewhile(predicate, iterable):
    # takewhile(lambda x: x<5, [1,4,6,4,1]) --> 1 4
    for x in iterable:
        if predicate(x):
            yield x
        else:
            break

 Пример 1:
 from itertools import takewhile, dropwhile

 print(list(takewhile(lambda x: x < 5, [1, 4, 6, 4, 1])))
 # [1, 4]
 print((list(dropwhile(lambda x: x < 5, [1, 4, 6, 4, 1]))))
 # [6, 4, 1]
________________________________________________________________________________________________________________________
 itertools.filterfalse(predicate, iterable) - Удалить элементы списка по условию

 создает итератор, который удаляет элементы из последовательности iterable до тех пор, пока функция predicate
 равна False или 0. Возвращается итератор с отобранными элементами.

 очень похожа на itertools.dropwhile(). Однако вместо триггера, который выводит все значения после его срабатывания,
 itertools.filterfalse() работает как фильтр и возвращает только те значения, которые оцениваются как False.

 Функция itertools.filterfalse() примерно эквивалентна следующему коду:

 def filterfalse(predicate, iterable):
    # filterfalse(lambda x: x%2, range(10)) --> 0 2 4 6 8
    if predicate is None:
        predicate = bool
    for x in iterable:
        if not predicate(x):
            yield x

 Пример 1:
 from itertools import filterfalse
 def greater_than_five(x):
    return x > 5

 print(list(filterfalse(greater_than_five, [6, 7, 8, 9, 1, 2, 3, 10])))
 # [1, 2, 3]
 print(list(filterfalse(lambda x: x > 5, [6, 7, 8, 9, 1, 2, 3, 10])))
 # [1, 2, 3]
 print(list(filterfalse(lambda x: x % 2, [6, 7, 8, 9, 1, 2, 3, 10])))
 print(list(filterfalse(lambda x: x % 2 != 0, [6, 7, 8, 9, 1, 2, 3, 10])))
 # [6, 8, 2, 10]
 print(list(filterfalse(lambda x: x % 2 == 0, [6, 7, 8, 9, 1, 2, 3, 10])))
 print(list(filterfalse(lambda x: not x % 2, [6, 7, 8, 9, 1, 2, 3, 10])))
 # [7, 9, 1, 3]

 Пример 2:
 from itertools import filterfalse

 def greater_than_five(x):
     return x > 5

 print(list(filterfalse(greater_than_five, [6, 7, 8, 9, 1, 2, 3, 10])))
 # [1, 2, 3]
 print(list(filterfalse(lambda x: x > 5, [6, 7, 8, 9, 1, 2, 3, 10])))
 # [1, 2, 3]
________________________________________________________________________________________________________________________
 itertools.groupby(iterable, key=None) - Группировка списка списков по ключу

 Поведение функции отличается от выражения GROUP BY в SQL, который объединяет общие элементы независимо от их порядка ввода.
 создает итератор, который возвращает последовательные ключи и группы из итерируемой последовательности iterable.

 groupby()примерно эквивалентно:

 class groupby:
    # [k for k, g in groupby('AAAABBBCCDAABBB')] → A B C D A B     # -> ['A', 'B', 'C', 'D', 'A', 'B']
    # [list(g) for k, g in groupby('AAAABBBCCD')] → AAAA BBB CC D  # -> [['A', 'A', 'A', 'A'], ['B', 'B', 'B'], ['C', 'C'], ['D']]

    def __init__(self, iterable, key=None):
        if key is None:
            key = lambda x: x
        self.keyfunc = key
        self.it = iter(iterable)
        self.tgtkey = self.currkey = self.currvalue = object()

    def __iter__(self):
        return self

    def __next__(self):
        self.id = object()
        while self.currkey == self.tgtkey:
            self.currvalue = next(self.it)    # Exit on StopIteration
            self.currkey = self.keyfunc(self.currvalue)
        self.tgtkey = self.currkey
        return (self.currkey, self._grouper(self.tgtkey, self.id))

    def _grouper(self, tgtkey, id):
        while self.id is id and self.currkey == tgtkey:
            yield self.currvalue
            try:
                self.currvalue = next(self.it)
            except StopIteration:
                return
            self.currkey = self.keyfunc(self.currvalue)


 Пример 1:  Уникальные и повторяющиеся значения в списке:

 from itertools import groupby

 x = list('AAAABBBCCDAABBB')
 # Удаление повторяющихся значений в списке
 print([k for k, g in groupby(x)])
 # ['A', 'B', 'C', 'D', 'A', 'B']
 print([[k, list(v)] for k, v in groupby(x)])
 # [['A', ['A', 'A', 'A', 'A']], ['B', ['B', 'B', 'B']], ['C', ['C', 'C']], ['D', ['D']], ['A', ['A', 'A']], ['B', ['B', 'B', 'B']]]


 # вывод уникальных значений
 print([k for k, g in groupby(sorted(x))])
 # ['A', 'B', 'C', 'D']

 Пример 2:

 from itertools import groupby
 # список с повторами
 x = list('abc' * 3)
 print(x)
 # ['a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c']

 # сортируем список с повторами
 x.sort()
 print(x)
 # ['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'c']

 for i, j in groupby(x):
     print(i, list(j))

 # a ['a', 'a', 'a']
 # b ['b', 'b', 'b']
 # c ['c', 'c', 'c']
________________________________________________________________________________________________________________________
 itertools.starmap(function, iterable) - Применить функцию для каждого кортежа из списка кортежей

 map   vs   starmap    -  Посмотри Пример 1:

 Используется вместо map(), когда параметры функции уже сгруппированы в кортежи из одной итерации,
 т. е. данные были предварительно упакованы в кортежи.

 Разница между функциями map() и itertools.starmap() заключается в способе передачи аргументов вызываемой функции
 и аналогична разнице между function(a, b) и function(*c)

 Функция itertools.starmap() примерно эквивалентна следующему коду:

 def starmap(function, iterable):
    # starmap(pow, [(2,5), (3,2), (10,3)]) --> 32 9 1000
    for args in iterable:
        yield function(*args)

 Пример 1: Важно Понимать отличие примера     map   vs   starmap
 from itertools import starmap

 def add_plus(a, b):
     return a+b


 for item in starmap(add_plus, [(2, 3), (4, 5)]):
     print(item, end=' ')
 # 5 9
 print()

 for item in map(add_plus, [(2, 3)], [(4, 5)]):
     print(item, end=' ')
 print()
 # (2, 3, 4, 5)
 for item in map(add_plus, [2, 3], [4, 5]):
     print(item, end=' ')
 # 6 8

 Пример 2:

 from itertools import starmap

 def composition(*x):
     # произведение
     for n, i in enumerate(x):
         if n==0:
             rez = i
         else:
             rez = rez * i
     return rez

 # произведение
 x = starmap(composition, [(2,5,3), (3,2,1), (10,10,3)])
 print(list(x))
 # [30, 6, 300]

 # квадраты
 x = starmap(pow, [(2,5), (3,2), (10,3)])
 print(list(x))
 # [32, 9, 1000]

 # max
 x = starmap(max, [(2,5,4), (3,2,1), (10,3,8)])
 print(list(x))
 # [5, 3, 10]

 # min
 x = starmap(min, [(2,5,9,3), (3,2,6,8), (1,0,10,3)])
 print(list(x))
 # [2, 2, 3]
________________________________________________________________________________________________________________________
 itertools.tee(iterable, n=2) - Получить n независимых копий итераторов из одной итерации.

 создает n итераторов из одного итерируемого объекта iter. По умолчанию создается 2 итератора.
 вернет n одинаковых, независимых итераторов из одной итерируемой последовательности.

 Итераторы не являются потокобезопасными. При одновременном использовании итераторов, возвращаемых одним и тем же вызовом
 itertools.tee() может возникать ошибка RuntimeError, даже если исходная итерация является поточно-ориентированной.

 Функция itertools.tee() может потребовать значительной памяти, в зависимости от того, сколько временных данных
 необходимо сохранить. В общем, если один итератор использует большую часть или все данные перед запуском другого
 итератора, быстрее использовать list().

 Следующий код Python помогает объяснить, что делает tee (хотя реальная реализация более сложна и
 использует только одну базовую очередь FIFO ):

 def tee(iterable, n=2):
    it = iter(iterable)
    deques = [collections.deque() for i in range(n)]
    def gen(mydeque):
        while True:
            if not mydeque:             # when the local deque is empty
                try:
                    newval = next(it)   # fetch a new value and
                except StopIteration:
                    return
                for d in deques:        # load it to all the deques
                    d.append(newval)
            yield mydeque.popleft()
    return tuple(gen(d) for d in deques)

 Пример 1:

 from itertools import tee
 x = list(range(9, 15))
 rez = tee(x, 3)

 for l in rez:
    print(list(l))

 # [9, 10, 11, 12, 13, 14]
 # [9, 10, 11, 12, 13, 14]
 # [9, 10, 11, 12, 13, 14]

 Пример 2:   Интересно поиграть с примером =)

 from itertools import tee

 data = 'ABC'
 iter1, iter2 = tee(data)
 for item in iter1:
     print(item)
 print()
 for item in iter2:
     print(item)

 c = deepcopy(iter1)
 print(list(c))
 # print(next(iter1))
 print(list(iter1))
 print(list(c))
________________________________________________________________________________________________________________________
 itertools.zip_longest(*iterables, fillvalue=None) - Объединить несколько списков разной длины в список кортежей

 создает итератор, который объединяет элементы из каждой итерируемой последовательности *iterables в кортежи.

 Отличие функции itertools.zip_longest() от встроенной функции zip() заключается в том, что zip() останавливается по
 исчерпании самой короткой входной последовательности и отбрасывает несопоставимые значения более длинных итераций,
 в то время как itertools.zip_longest() работает пока самая длинная итерация не будет исчерпана, а пропущенные элементы
 заполняются значением fillvalue.

 Если одна из итераций потенциально бесконечна, то zip_longest() функцию следует обернуть чем-то, ограничивающим
 количество вызовов (например islice() или takewhile()). Если не указано, значение fillvalue по умолчанию равно None.

 Примерно эквивалентно:

 def zip_longest(*args, fillvalue=None):
    # zip_longest('ABCD', 'xy', fillvalue='-') → Ax By C- D-
    iterators = [iter(it) for it in args]
    num_active = len(iterators)
    if not num_active:
        return
    while True:
        values = []
        for i, it in enumerate(iterators):
            try:
                value = next(it)
            except StopIteration:
                num_active -= 1
                if not num_active:
                    return
                iterators[i] = repeat(fillvalue)
                value = fillvalue
            values.append(value)
        yield tuple(values)

 Пример 1:
 from itertools import zip_longest

 for item in zip_longest('ABCD', 'xy', fillvalue='BLANK'):
     print (item)

 # ('A', 'x')
 # ('B', 'y')
 # ('C', 'BLANK')
 # ('D', 'BLANK')

 Сравнение с zip:

 from itertools import zip_longest

 a = list(range(5))
 b = list(range(3, 10))
 rez = zip_longest(a, b, fillvalue=100)
 print(list(rez))
 # [(0, 3), (1, 4), (2, 5), (3, 6), (4, 7), (100, 8), (100, 9)]

 # встроенная функция zip()
 rez = zip(a, b)
 print(list(rez))
 # [(0, 3), (1, 4), (2, 5), (3, 6), (4, 7)]
________________________________________________________________________________________________________________________
 itertools.islice(iterable, stop), itertools.islice(iterable, start, stop[, step]) - Получить срез итератора/генератора

 создает итератор, который возвращает выбранные элементы из итератора iterable. Другими словами, получает срез
 итератора/генератора, для которых нельзя получить срез обычными средствами или встроенной функцией slice().

 В отличие от обычных срезов списков или кортежей, функция itertools.islice() не поддерживает отрицательные значения
 для start, stop или step.

 Пример 1:
 a_gen = (i for i in range(10))
 type(a_gen)                             # -> <class 'generator'>
 itertools.islice(a_gen, None, 5)        # -> <itertools.islice object at 0x000001B631C83830>
 a_gen = (i for i in range(10))
 list(itertools.islice(a_gen, None, 5))  # -> [0, 1, 2, 3, 4]
 a_gen = (i for i in range(10))
 list(itertools.islice(a_gen, 2, None))  # -> [2, 3, 4, 5, 6, 7, 8, 9]

 a_iter = iter([i for i in range(10)])
 type(a_iter)                            # -> <class 'list_iterator'>
 list(itertools.islice(a_iter, None, 3)) # -> [0, 1, 2]

 Пример 2:

 from itertools import islice

 # Сравнение с обычным slice vs islice

 print(list(islice([1, 2, 3], None, 2)))
 # [1, 2]
 print(list(islice([1, 2, 3], None, None,  -1)))
 # ValueError: Step for islice() must be a positive integer or None.
 print(list([1, 2, 3][slice(None, 2)]))
 # [1, 2]
 print(list([1, 2, 3][slice(None, None, -1)]))
 # [3, 2, 1]


 print(list(islice('ABCDEFG', 2)))
 # ['A', 'B']
 print(list(islice('ABCDEFG', 2, 4)))
 # ['C', 'D']
 print(list(islice('ABCDEFG', 2, None)))
 # ['C', 'D', 'E', 'F', 'G']
 print(list(islice('ABCDEFG', 0, None, 2)))
 # ['A', 'C', 'E', 'G']
________________________________________________________________________________________________________________________
 itertools.pairwise(iterable) - Возвращает последовательные перекрывающиеся пары, взятые из входного итерируемого объекта .

 Количество кортежей из двух кортежей в выходном итераторе будет на единицу меньше, чем количество входных данных.
 Он будет пустым, если входная итерация имеет менее двух значений.

 Примерно эквивалентно:

 def pairwise(iterable):
    # pairwise('ABCDEFG') → AB BC CD DE EF FG
    iterator = iter(iterable)
    a = next(iterator, None)
    for b in iterator:
        yield a, b
        a = b

 Пример 1:

 import itertools

 letters = ['a', 'b', 1,  'c', 'd', 'e']

 result = itertools.pairwise(letters)

 print(list(result))
 # [('a', 'b'), ('b', 1), (1, 'c'), ('c', 'd'), ('d', 'e')]
________________________________________________________________________________________________________________________
--- Комбинаторные итераторы   Combinatoric iterators ---
________________________________________________________________________________________________________________________
 itertools.combinations(iterable, r) - Генерация сочетаний элементов списка без повторений.

 позволяет создать итератор со всеми возможными комбинациями элементов входной последовательности.

 Код для itertools.combinations() также может быть выражен как подпоследовательность itertools.permutations() после
 фильтрации записей, в которых элементы расположены не в отсортированном порядке, а в соответствии с их положением во входном пуле:

 Функция itertools.combinations() примерно эквивалентна следующему коду:

 def combinations(iterable, r):
    # combinations('ABCD', 2) --> AB AC AD BC BD CD
    # combinations(range(4), 3) --> 012 013 023 123
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indices = list(range(r))
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1
        yield tuple(pool[i] for i in indices)

 Пример 1:

 from itertools import combinations, permutations
 x = [1, 2, 3, 4]
 print(list(combinations(x, 2)))
 # [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
 print(list(permutations(x, 2)))
 # [(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)]
 print(list(combinations(x, 3)))
 # [(1, 2, 3), (1, 2, 4), (1, 3, 4), (2, 3, 4)]
 print(list(permutations(x, 3)))
 # [(1, 2, 3), (1, 2, 4), (1, 3, 2), (1, 3, 4), (1, 4, 2), (1, 4, 3), (2, 1, 3), (2, 1, 4), (2, 3, 1), (2, 3, 4), (2, 4, 1)...

 x = ['a', 'b', 'c', 'd']
 print(list(combinations(x, 3)))
 # [('a', 'b', 'c'), ('a', 'b', 'd'), ('a', 'c', 'd'), ('b', 'c', 'd')]
 print(print(list(permutations(x, 3))))
 # [('a', 'b', 'c'), ('a', 'b', 'd'), ('a', 'c', 'b'), ('a', 'c', 'd'), ('a', 'd', 'b'), ('a', 'd', 'c'), ('b', 'a', 'c')...

 Пример 2:

 from itertools import combinations

 print(list(combinations('WXYZ', 2)))
 # [('W', 'X'), ('W', 'Y'), ('W', 'Z'), ('X', 'Y'), ('X', 'Z'), ('Y', 'Z')]

 for item in combinations('WXYZ', 2):
     print(''.join(item))
________________________________________________________________________________________________________________________
 itertools.combinations_with_replacement(iterable, r) - Генерация сочетаний элементов списка с повторением

 похож на itertools.combinations(). Единственное отличие заключается в том, что он фактически будет создавать комбинации,
 в которых элементы действительно повторяются.

 Функция itertools.combinations_with_replacement() примерно эквивалентна следующему коду:

 def combinations_with_replacement(iterable, r):
    # combinations_with_replacement('ABC', 2) --> AA AB AC BB BC CC
    pool = tuple(iterable)
    n = len(pool)
    if not n and r:
        return
    indices = [0] * r
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != n - 1:
                break
        else:
            return
        indices[i:] = [indices[i] + 1] * (r - i)
        yield tuple(pool[i] for i in indices)

 Код комбинации combinations_with_replacement() также может быть выражен как подпоследовательность itertools.product()
 после фильтрации записей, в которых элементы расположены не в отсортированном порядке, а в соответствии с их положением во входном пуле:

 from itertools import product

 def combinations_with_replacement(iterable, r):
     pool = tuple(iterable)
     n = len(pool)
     for indices in product(range(n), repeat=r):
         if sorted(indices) == list(indices):
             yield tuple(pool[i] for i in indices)

 Пример 1:

 from itertools import combinations, combinations_with_replacement

 print(list(combinations_with_replacement('WXYZ', 2)))

 # [('W', 'W'), ('W', 'X'), ('W', 'Y'), ('W', 'Z'), ('X', 'X'), ('X', 'Y'), ('X', 'Z'), ('Y', 'Y'), ('Y', 'Z'), ('Z', 'Z')]
________________________________________________________________________________________________________________________
 itertools.permutations(iterable, r=None) - Все комбинации элементов списка, включая смену порядка.

 Будет возвращать последовательные перестановки элементов указанной длины из итерации, которая передается в качестве
 аргумента. Подобно функции itertools.combinations(), перестановки выдаются в лексикографическом порядке сортировки.

 Функция itertools.permutations() примерно эквивалентна следующему коду:

 def permutations(iterable, r=None):
    # permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
    # permutations(range(3)) --> 012 021 102 120 201 210
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    if r > n:
        return
    indices = list(range(n))
    cycles = list(range(n, n-r, -1))
    yield tuple(pool[i] for i in indices[:r])
    while n:
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield tuple(pool[i] for i in indices[:r])
                break
        else:
            return

 Код функция itertools.permutations() также может быть выражен в виде подпоследовательности функция itertools.product(),
 отфильтрованной для исключения записей с повторяющимися элементами:

 def permutations(iterable, r=None):
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    for indices in product(range(n), repeat=r):
        if len(set(indices)) == r:
            yield tuple(pool[i] for i in indices)

 Пример 1:
 from itertools import permutations

 print(list(permutations('XYZ', 2)))
 # [('X', 'Y'), ('X', 'Z'), ('Y', 'X'), ('Y', 'Z'), ('Z', 'X'), ('Z', 'Y')]
 for item in permutations('XYZ', 2):
   print(''.join(item))
________________________________________________________________________________________________________________________
 itertools.product(*iterables, repeat=1) - Декартово произведение входных последовательностей.

 Прямое, или Декаартово произведеение двух непустых множеств — множество, элементами которого являются все возможные
 упорядоченные пары элементов исходных множеств.

 Декартово произведение списков — это набор всех возможных комбинаций элементов из каждого списка.

 CROSS JOIN - декартово произведение в SQL запросе.

 Эта функция примерно эквивалентна следующему коду, за исключением того, что фактическая реализация не создает
 промежуточные результаты в памяти:

 def product(*args, repeat=1):
    # product('ABCD', 'xy') --> Ax Ay Bx By Cx Cy Dx Dy
    # product(range(2), repeat=3) --> 000 001 010 011 100 101 110 111
    pools = [tuple(pool) for pool in args] * repeat
    result = [[]]
    for pool in pools:
        result = [x+[y] for x in result for y in pool]
    for prod in result:
        yield tuple(prod)

 Пример 1:

 from itertools import product

 x = ['a', 'b']
 y = [1]
 print(list(product(x, y, repeat=2)))
 # [('a', 1, 'a', 1), ('a', 1, 'b', 1), ('b', 1, 'a', 1), ('b', 1, 'b', 1)]

 print(list(product([1, 2], repeat=2)))
 # [(1, 1), (1, 2), (2, 1), (2, 2)]

 Пример 2:

 from itertools import product
 x = ['a', 'b', 'c']
 y = ['1', '2']
 print(list(product(x, y)))
 # [('a', '1'), ('a', '2'), ('b', '1'), ('b', '2'), ('c', '1'), ('c', '2')]

 Пример 3:
 from itertools import product

 pairs=['Aa','bb','CC','dD']
 gams=list([x for x in product(*pairs)])
 print(gams)
________________________________________________________________________________________________________________________
 --- Отличия    combinations  vs  combinations_with_replacement vs  permutations ---
 Разница между itertools.permutations() и itertools.combinations():
 - itertools.permutations(): Порядок элементов имеет значение.
 - itertools.combinations(): Порядок элементов не имеет значения.

 Разница между itertools.combinations() и itertools.combination_swith_replacement:
 - combinations(): Порядок элементов не имеет значения, и значения не повторяются.
 - combinations_with_replacement(): Порядок элементов не имеет значения, и значения повторяются.

 from itertools import combinations, combinations_with_replacement, permutations
 x = ['a', 'b', 'c']

 print(list(combinations(x, 2)))
 # [('a', 'b'), ('a', 'c'), ('b', 'c')]
 print(list(combinations_with_replacement(x, 2)))
 # [('a', 'a'), ('a', 'b'), ('a', 'c'), ('b', 'b'), ('b', 'c'), ('c', 'c')]
 print(list(permutations(x, 2)))
 # [('a', 'b'), ('a', 'c'), ('b', 'a'), ('b', 'c'), ('c', 'a'), ('c', 'b')]
________________________________________________________________________________________________________________________

 -- Пример работы с бесконечными итераторами:
 from itertools import count, repeat, cycle

 # Итератор, возвращающий равномерно распределенные значения
 i1 = count(start=0, step=.1)
 print(next(i1))  # -> 0
 print(next(i1))  # -> 0.1
 print(next(i1))  # -> 0.2

 # Итератор, циклично и бесконечно возвращающий элементы итерируемого объекта
 i2 = cycle([1, 2])
 print(next(i2))  # -> 1
 print(next(i2))  # -> 2
 print(next(i2))  # -> 1

 # Итератор, возвращающий один и тот же объект бесконечно, если не указано значение аргумента times
 i3 = repeat("Wow!", times=3)
 print(list(i3))  # -> ['Wow!', 'Wow!', 'Wow!']
________________________________________________________________________________________________________________________

 -- Применение некоторых конечных итераторов:
 from itertools import accumulate, chain, compress, dropwhile, takewhile, pairwise
 import operator

 # Итератор, возвращающий накопленный результат выполнения указанной функции (по умолчанию — сложение)
 i1 = accumulate([1, 2, 3, 4])
 i2 = accumulate([1, 2, 3, 4], initial=10)
 print(list(i1), list(i2))  # -> [1, 3, 6, 10]   [10, 11, 13, 16, 20]

 i3 = accumulate([ -3, -2, -1, 1, 2, 3, 4], operator.mul)
 print(list(i3))  # -> [-3, 6, -6, -6, -12, -36, -144]

 # Можно использовать свою функцию
 def myfunc(accumulated, current):
     return accumulated + 2 * current

 i4 = accumulate([1, 2, 3, 4], func=myfunc)
 print(list(i4))  # -> [1, 5, 11, 19]

 # Можно использовать лямбду (подробнее рассмотрены ниже)
 i5 = accumulate([1, 2, 3, 4], lambda accumulated, current: accumulated + 2 * current)
 print(list(i5))  # -> [1, 5, 11, 19]

 # Итератор, возвращающий только те элементы входной последовательности,
 # которые имеют соответствующий элемент, равный True или 1 в последовательности selectors
 i6 = compress("ABCDEF", [1, 1, 1, 0, 0, 1])
 print(list(i6))  # -> ['A', 'B', 'C', 'F']

 # Итератор, отбрасывающий элементы входной последовательности, если результат выполнения функции равен True.
 # Как только предикат становится False, то отбрасывание прекращается (предикат больше не применяется)
 i7 = dropwhile(lambda x: x<5, [1, 4, 6, 4, 1, 1, 1, 0])
 print(list(i7))  # -> [6, 4, 1, 1, 1, 0]

 # takewhile, в отличие от dropwhile, наоборот, возвращает элементы входной последовательности,
 # если результат выполнения функции равен True
 i8 = takewhile(lambda x: x<5, [1, 4, 6, 0, 4, 1, 2, 1])
 print(list(i8))  # -> [1, 4]

 # Итератор, формирующий из нескольких входных последовательностей одну общую
 i2 = chain(["A", "B", "C"],["D", "E", "F"],["G", "H", "I"])
 print(list(i2))  # -> ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
 # Кстати, такой же трюк можно провернуть при помощи обычной sum(), задав ей начальный параметр [] (т. е. пустой список)
 a = sum([["A", "B", "C"],["D", "E", "F"],["G", "H", "I"]], [])
 print(a)         # -> ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']

 # Возвращает элементы входной коллекции попарно
 i6 = pairwise([1, 2, 3, 4, 5])
 print(list(i6))  # -> [(1, 2), (2, 3), (3, 4), (4, 5)]
________________________________________________________________________________________________________________________

 -- Комбинаторика
 from itertools import product, combinations, combinations_with_replacement, permutations

 # Создает множество, содержащее все упорядоченные пары элементов из входных множеств
 a = product("abc", "xyz")
 print(list(a))  # -> [('a', 'x'), ('a', 'y'), ('a', 'z'), ('b', 'x'), ('b', 'y'), ('b', 'z'), ('c', 'x'), ('c', 'y'), ('c', 'z')]

 b = product([0, 1], repeat=3)
 print(list(b))  # -> [(0, 0, 0), (0, 0, 1), (0, 1, 0), (0, 1, 1), (1, 0, 0), (1, 0, 1), (1, 1, 0), (1, 1, 1)]

 # Возвращает подпоследовательности длины r из элементов входного итерируемого объекта, повторяющиеся элементы не допускаются
 c = combinations("abc", r=2)
 print(list(c))  # -> [('a', 'b'), ('a', 'c'), ('b', 'c')]

 # Выдает перестановки элементов итерируемого объекта
 d = permutations("abc", r=2)
 print(list(d))  # -> [('a', 'b'), ('a', 'c'), ('b', 'a'), ('b', 'c'), ('c', 'a'), ('c', 'b')]

 # Возвращает подпоследовательности длины r из элементов входного итерируемого объекта, повторяющиеся элементы допустимы
 e = combinations_with_replacement("abc", r=2)
 print(list(e))  # -> [('a', 'a'), ('a', 'b'), ('a', 'c'), ('b', 'b'), ('b', 'c'), ('c', 'c')]







"""