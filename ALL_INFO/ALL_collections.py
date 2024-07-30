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


# OrderedDict нужен для действий со словарем где необходим порядок элементов, например
# сравнение с учетом порядка, перестановки элементов с сохранением порядка. Платим памятью!!!

# ChainMap нужен для логического обьединения словарей для поиска информации, но при изменениях меняется первый словарь

# Counter нужен для подсчета элементов в последовательности, работает только с hashable

# defaultdict нужен для создания словаря по умолчанию. Значение подставляется при обращении к несуществующему ключу

# deque(двунаправленная очередь) потокобезопасна, быстро оперирует с обеими сторонами

# namedtuple нужен для создания структуры данных, нечто среднее между стандартными типами и самописными классом.
# Неизменяемый, позволяет обращаться по имени атрибута, позволяет использовать индексы.


 1) OrderedDict - упорядоченный словарь, несмотря на мнение многих, он все еще актуален, оптимизирован для работы
 с порядком элементов в словаре. Позволяет доставать пары как с конца так и с начала словаря, переставлять
 пары в конец или начало словаря. При сравнении учитывает порядок элементов, а не только их равенство.
 За все это платит большим потреблением памяти.

 Методы объекта OrderedDict():
 - popitem(last=True) - удаляет последний элемент если last=True, и первый, если last=False. # inplace
 - move_to_end(key, last=True) - добавляет ключ в конец если last=True, и в начало, если last=False. # inplace

 2) ChainMap нужен для логического объединения словарей для поиска информации, физического копирования
 словарей не происходит и если изменить один из исходников, то изменении отобразится и в ChainMap.
 Удобен для поиска информации, но при изменениях меняется первый словарь в наборе.

 Объект ChainMap, атрибуты и методы:
 - ChainMap.maps[0], maps[1] - Управление списком отображений через .maps
 - ChainMap.new_child(m=None) - Добавим подконтекст через .new_child()
 - ChainMap.parents - Пропуск подконтекстов с помощью .parents

 3) Counter - удобный инструмент для подсчета элементов в последовательности,
 считает только с hashable типы (строки, числа, кортежи, ...).

 Объект Counter, атрибуты и методы:
 - Counter.elements() возвращает итератор по элементам.
 - Counter.most_common() список наиболее распространенных элементов.
 - Counter.subtract() вычитает элементы счетчика и итерируемой последовательности. # inplace
 - Counter.total() вычисляет сумму значений счетчика.
 - Counter.update() складывает элементы счетчика и итерируемой последовательности. # inplace

 4) defaultdict нужен для создания словаря со значением по умолчанию.
 Значение подставляется при обращении к несуществующему ключу, что позволяет не писать лишней логики.
 В остальном аналогичен обычному словарю.

 5) deque - двунаправленная очередь, быстро вставляет элементы как в конец, так и начало,
 быстро достает с обоих концов. Она потокобезопасна (thread-safe) и может быть использована для многопоточных операций,
 позволяет задать максимальный размер.

 Объект Deque, атрибуты и методы:
 - Deque.append(x) - добавляет x к правой стороне (в конец) контейнера deque(). # inplace
 - Deque.appendleft(x) - добавляет x к левой стороне (в начало) контейнера deque().  # inplace
 - Deque.copy() - создает неглубокую копию контейнера deque().
 - Deque.clear() - удаляет все элементы из контейнера deque(), оставляя его длиной 0. # inplace
 - Deque.count(x) - подсчитывает количество элементов контейнера deque(), равное значению x.
 - Deque.extend(iterable) -  расширяет правую сторону (с конца) контейнера deque(), добавляя элементы из  iterable. # inplace
 - Deque.extendleft(iterable): - расширяет левую сторону (с начала) контейнера deque(), добавляя элементы из iterable. # inplace
 - Deque.index(x[, start[, stop]]) - вернет позицию (индекс) первого совпадения значения аргумента x в контейнере deque()
 - Deque.insert(i, x) - вставляет значение аргумента x в позицию i контейнера deque(). # inplace
 - Deque.pop() - удаляет и возвращает элемент с правой стороны (с конца) контейнера deque(). Не подерживает индекс(агрумент) pop(1) # inplace
 - Deque.popleft() - удаляет и возвращает элемент с левой стороны (с конца) контейнера deque(). Не работает popleft(1) # inplace
 - Deque.remove(value) - удаляет первое вхождение значения value в контейнер deque(). # inplace
 - Deque.reverse() - разворачивает элементы контейнера deque() на месте и возвращает None. # inplace
 - Deque.rotate(n=1) - разворачивает контейнер deque() на n шагов вправо. # inplace
 - Deque.maxlen() - возвращает максимальный размер maxlen контейнера deque(), если параметр maxlen не задан, то возвращает None.

 6) namedtuple нужен для создания структуры данных, нечто среднее между стандартными типами и самописным классом.
 Пригодится когда отдельный класс избыточен или ООП пока неизвестно. Неизменяемый,
 позволяет обращаться по имени атрибута (причем быстро), позволяет использовать индексы.

_______________________________________________________________________________________________________________________
 --- Контейнерные типы данных модуля collections ---

________________________________________________________________________________________________________________________
 --- ChainMap ---

 class collections.ChainMap(*maps) -  Обновляемый, производительный контейнер словарей dict()

 предназначен для быстрого объединения нескольких словарей, чтобы их можно было рассматривать как единое целое. Такой
 контейнер объединяет словари и ищет ключи намного быстрее, чем создание нового словаря и выполнение объединения
 при помощи вызовов dict.update().

 Класс ChainMap() добавляет и хранит словари по ссылкам. Таким образом, если обновляется один из исходных словарей,
 эти изменения будут отражены в ChainMap() и на оборот, все обновления произведенные со словарями через класс ChainMap()
 отразятся на исходных словарях.

 Пример 1:
 from collections import ChainMap

 first = {'two': 22, 'three': 3}
 last = {'one': 1, 'two': 2}
 d = ChainMap(first, last)
 print(d)
 # ChainMap({'two': 22, 'three': 3}, {'one': 1, 'two': 2})

 d['four'] = 4
 print(d)
 # ChainMap({'two': 22, 'three': 3, 'four': 4}, {'one': 1, 'two': 2})
 d.popitem()

 print(d)
 # ChainMap({'two': 22, 'three': 3}, {'one': 1, 'two': 2})

 # попробуем изменить первый элемент второго словаря
 d['one'] = 11
 print(d)
 # ChainMap({'two': 22, 'three': 3, 'one': 11}, {'one': 1, 'two': 2})
 # все изменения происходят только с первым словарем

 # смотрим исходный словарь
 print(first)
 # {'two': 22, 'three': 3, 'one': 11}

 # изменяем исходные словари
 del first['two']
 last['four'] = 4

 # смотрим как изменился 'd' - экземпляр ChainMap()
 print(d)
 # ChainMap({'three': 3, 'one': 11}, {'one': 1, 'two': 2, 'four': 4})
________________________________________________________________________________________________________________________
 --- Объект ChainMap, атрибуты и методы ---
 - ChainMap.maps[0], maps[1] - Управление списком отображений через .maps
 - ChainMap.new_child(m=None) - Добавим подконтекст через .new_child()
 - ChainMap.parents - Пропуск подконтекстов с помощью .parents
________________________________________________________________________________________________________________________
 ChainMap.maps - представляет собой обновляемый пользователем список словарей dict() и должен всегда содержать хотя бы
 один словарь. Список словарей ChainMap.maps упорядочен в порядке их добавления для последовательного поиска по ключам
 от первого до последнего. Это единственное сохраненное состояние, которое можно изменить.

 Примеры:

 from collections import ChainMap

 first = {'three': 3, 'one': 11}
 last = {'one': 1, 'two': 2, 'four': 4}
 d = ChainMap(first, last)
 print(d)
 # ChainMap({'three': 3, 'one': 11}, {'one': 1, 'two': 2, 'four': 4})

 print(d.maps)
 # [{'three': 3, 'one': 11}, {'one': 1, 'two': 2, 'four': 4}]

 Атрибут ChainMap.maps поддерживает все основные операции со списками, следовательно можно добавлять новые словари и
 удалять уже добавленные, а так же изменять их последовательность.

 Обратите внимание, что изменяя последовательность словарей с списке атрибута d.maps, так же меняется последовательность
 поиска ключей и их значений.

 # поиск ключа в экземпляре `ChainMap()`
 print(d['one'])
 # 11

 # меняем последовательность словарей `ChainMap()`
 d.maps.reverse()
 print(d.maps)
 # [{'one': 1, 'two': 2, 'four': 4}, {'three': 3, 'one': 11}]

 # ключ изменился
 print(d['one'])
 # 1

 Через атрибут maps можно изменять ВСЕ словари. Доступ к конкретному словарю осуществляется по индексу в списке атрибута
 d.maps[i], а изменения осуществляются через их методы dict().

 # доступ к словарям
 print(d.maps[0])
 # {'one': 1, 'two': 2, 'four': 4}
 print(d.maps[1]['three'])
 # 3

 # изменяем словари и не забываем, что мы
 # поменяли их местами - 'd.maps.reverse()'
 d.maps[0]['five'] = 5
 del d.maps[0]['four']
 d.maps[1]['four'] = 4
 print(d)
 # ChainMap({'one': 1, 'two': 2, 'five': 5}, {'three': 3, 'one': 11, 'four': 4})

 # исходные словари тоже изменились
 print(first)
 # {'three': 3, 'one': 11, 'four': 4}
 print(last)
 # {'one': 1, 'two': 2, 'five': 5}

 # изменяем список словарей
 d.maps.pop()
 # {'three': 3, 'one': 11, 'four': 4}
 print(d)
 # ChainMap({'one': 1, 'two': 2, 'five': 5})

 # добавляем в экземпляр `ChainMap()` новый словарь
 new_dict = {'a': 10, 'b': 20, 'c': 30}
 d.maps.append(new_dict)
 print(d)
 # ChainMap({'one': 1, 'two': 2, 'five': 5}, {'a': 10, 'b': 20, 'c': 30})
 del d.maps[1]['c']
 d.maps[0]['one'] = 0
 print(d)
 # ChainMap({'one': 0, 'two': 2, 'five': 5}, {'a': 10, 'b': 20})

 # исходные словари
 print(last)
 # {'one': 0, 'two': 2, 'five': 5}
 print(new_dict)
 # {'a': 10, 'b': 20}
________________________________________________________________________________________________________________________
 new_child(m=None, **kwargs) - возвращает новый экземпляр класса ChainMap(), содержащий новый словарь m, за которым
 следуют все словари в текущем экземпляре.

 Этот метод используется для создания подконтекстов, которые могут быть обновлены без изменения значений в любом из родительских словарей.

 Примеры:
 first = {'one': 0, 'two': 2, 'five': 5}
 last = {'a': 10, 'b': 20}
 d = ChainMap(first, last)
 print(d)
 # ChainMap({'one': 0, 'two': 2, 'five': 5}, {'a': 10, 'b': 20})

 d_child = d.new_child()
 print(d_child)
 # ChainMap({}, {'one': 0, 'two': 2, 'five': 5}, {'a': 10, 'b': 20})

 # 'd_child' это новый экземпляр 'ChainMap()'
 d_child = d.new_child({'one': 1, 'a': 1})
 print(d_child)
 # ChainMap({'one': 1, 'a': 1}, {'one': 0, 'two': 2, 'five': 5}, {'a': 10, 'b': 20})

 # Исходный экземпляр `d` класса `ChainMap()` не изменился
 print(d)
 # ChainMap({'one': 0, 'two': 2, 'five': 5}, {'a': 10, 'b': 20})
________________________________________________________________________________________________________________________
 ChainMap.parents - возвращает новый экземпляр класса ChainMap(), содержащий все словари в текущем экземпляре,
 кроме первого. Это полезно для пропуска первого словаря при поиске ключей.

 Варианты использования аналогичны тем, которые используются для оператора nonlocal, используемого во вложенных областях.
 Варианты использования также параллельны для встроенной функции super().

 Ссылка на d.parents эквивалентна вызову ChainMap(*d.maps[1:]).

 Примеры:
 first = {'one': 0, 'two': 2, 'five': 5}
 last = {'a': 10, 'b': 20}
 d = ChainMap(first, last)
 print(d)
 # ChainMap({'one': 0, 'two': 2, 'five': 5}, {'a': 10, 'b': 20})
 d_child = d.new_child()
 print(d_child)
 # ChainMap({}, {'one': 0, 'two': 2, 'five': 5}, {'a': 10, 'b': 20})

 print(d_child.parents)
 # ChainMap({'one': 0, 'two': 2, 'five': 5}, {'a': 10, 'b': 20})

 print(d.parents)
 # ChainMap({'a': 10, 'b': 20})

 # Исходные экземпляры не изменяются
 print(d)
 # ChainMap({'one': 0, 'two': 2, 'five': 5}, {'a': 10, 'b': 20})
 print(d_child)
 # ChainMap({}, {'one': 0, 'two': 2, 'five': 5}, {'a': 10, 'b': 20})
________________________________________________________________________________________________________________________
 --- Counter ---

 class collections.Counter([iterable-or-mapping]) - Подсчет количества повторений элементов в последовательности.

 предназначен для удобных и быстрых подсчетов количества появлений неизменяемых элементов в последовательностях.

 это подкласс словаря dict для подсчета хеш-объектов (неизменяемых, таких как строки, числа, кортежи и т.д.).
 Это коллекция, в которой элементы хранятся в виде словарных ключей, а их счетчики хранятся в виде значений словаря.

 Для объектов collections.Counter() доступны обычные методы словарей, за исключением двух, которые для счетчиков работают по-другому.
 - Counter.fromkeys() не реализован для объектов Counter().
 - Counter.update() Работает подобно методу словаря dict.update(), но складывает количество (значения ключей), а не заменяет их.

 Примеры:

 from collections import Counter

 cnt = Counter()
 for word in ['red', 'blue', 'red', 'green', 'blue', 'blue']:
     cnt[word] += 1
 print(cnt)
 # Counter({'blue': 3, 'red': 2, 'green': 1})

 print(Counter(['red', 'blue', 'red', 'green', 'blue', 'blue']))
 # Counter({'blue': 3, 'red': 2, 'green': 1})



 from collections import Counter

 # новый пустой счетчик
 cnt = Counter()
 print(cnt)
 # Counter()
 # новый счетчик из последовательности
 cnt = Counter('gallahad')
 print(cnt)
 # Counter({'a': 3, 'l': 2, 'g': 1, 'h': 1, 'd': 1})
 # новый счетчик из словаря
 cnt = Counter({'red': 4, 'blue': 2})
 print(cnt)
 Counter({'red': 4, 'blue': 2})
 # новый счетчик из ключевых слов 'args'
 cnt = Counter(cats=4, dogs=8)
 print(cnt)
 # Counter({'dogs': 8, 'cats': 4})
 print(cnt['catss'])
 # 0

 Счетчики collections.Counter() имеют интерфейс словаря, за исключением того, что они возвращают 0 для отсутствующих
 элементов вместо вызова исключения KeyError:

 from collections import Counter

 cnt = Counter(['eggs', 'ham'])
 print(cnt['bacon'])
 # 0

 Установка счетчика в ноль не удаляет элементы из счетчика. Используйте инструкцию del, чтобы полностью удалить ключ счетчика:
________________________________________________________________________________________________________________________
 Объект Counter, атрибуты и методы:
 - Counter.elements() возвращает итератор по элементам.
 - Counter.most_common() список наиболее распространенных элементов.
 - Counter.subtract() вычитает элементы счетчика и итерируемой последовательности. # inplace
 - Counter.total() вычисляет сумму значений счетчика.
 - Counter.update() складывает элементы счетчика и итерируемой последовательности. # inplace
________________________________________________________________________________________________________________________
 elements() - возвращает итератор по элементам, в котором каждый элемент повторяется столько раз, во сколько
 установлено его значение. Элементы возвращаются в порядке их появления. Если количество элементов меньше единицы,
 то метод Counter.elements() просто проигнорирует его.

 from collections import Counter

 cnt = Counter(a=4, b=2, c=0, d=-2)               # создание словаря
 cnt = Counter({'a': 4, 'b': 2, 'c': 0, 'd': -2}) # тоже создание словаря
 print(list(cnt.elements()))
 # ['a', 'a', 'a', 'a', 'b', 'b']
 print(sorted(cnt.elements()))
 # ['a', 'a', 'a', 'a', 'b', 'b']
________________________________________________________________________________________________________________________
 most_common([n]) - возвращает список из n наиболее распространенных элементов и их количество от наиболее
 распространенных до наименее. Если n опущено или None, метод cnt.most_common() возвращает все элементы в счетчике.

 Элементы с равным количеством упорядочены в порядке, в котором они встречаются первыми:

 from collections import Counter

 print(Counter('abracadabra').most_common(3))
 # [('a', 5), ('b', 2), ('r', 2)]
________________________________________________________________________________________________________________________
 subtract([iterable-or-mapping]) - вычитает элементы текущего счетчика cnt и итерируемой последовательности или другого # inplace
 словаря или другого счетчика Counter(). Подобно методу словаря dict.update(), но вычитает количество (значения ключей), а не заменяет их.

 from collections import Counter

 c = Counter(a=4, b=2, c=0, d=-2)
 c = Counter({'a': 4, 'b': 2, 'c': 0, "d": -2})
 d = Counter(a=1, b=2, c=3, d=4)
 d = Counter({'a': 1, 'b': 2, 'c': 3, "d": -4})
 c.subtract(d)
 print(c)
 # Counter({'a': 3, 'd': 2, 'b': 0, 'c': -3})
________________________________________________________________________________________________________________________
 total() - В Python 3.10 появился метод Counter.total(), который вычисляет сумму значений текущего счетчика.

 В Python 3.10 +                           В более ранних версиях Python, этот метод можно заменить выражением:
 from collections import Counter           from collections import Counter

 c = Counter(a=10, b=5, c=0)               c = Counter(a=10, b=5, c=0)
 print(c.total())                          print(sum(c.values()))
 # 15                                      # 15
________________________________________________________________________________________________________________________
 update([iterable-or-mapping]) - Работает подобно методу словаря dict.update(), но складывает количество
 (значения ключей), а не заменяет их. # inplace

 from collections import Counter

 a = {'a': 4, 'b': 2, 'c': 0, "d": -2}
 b = {'a': 1, 'b': 2, 'c': 3, "d": -4}
 a.update(b)
 print(a)
 # {'a': 1, 'b': 2, 'c': 3, 'd': -4}
 c = Counter(a=4, b=2, c=0, d=-2)
 c = Counter({'a': 4, 'b': 2, 'c': 0, "d": -2})
 d = Counter(a=1, b=2, c=3, d=4)
 d = Counter({'a': 1, 'b': 2, 'c': 3, "d": -4})
 c.update(d)
 print(c)
 # Counter({'a': 5, 'b': 4, 'c': 3, 'd': -6})
________________________________________________________________________________________________________________________
 --- deque ---

 class collections.deque([iterable[, maxlen]]) - Двусторонняя очередь в Python

 maxlen - автоматически «выпихивая» старые при добавлении новых.

 возвращает новый объект deque(), инициализированный слева направо данными из итерируемой последовательности iterable.


 from collections import deque

 dq_empty = deque()
 # deque([])
 dq = deque('ABCD')
 # deque(['A', 'B', 'C', 'D'])
 dq_maxlen_1 = deque('ABCD', maxlen=1)
 # deque(['D'], maxlen=1)
 dq_maxlen_2 = deque('ABCD', maxlen=2)
 # deque(['C', 'D'], maxlen=2)
 dq_maxlen_3 = deque('ABCD', maxlen=3)
 # deque(['B', 'C', 'D'], maxlen=3)
________________________________________________________________________________________________________________________
 --- Объект Deque, атрибуты и методы: ---
________________________________________________________________________________________________________________________
 Deque.append(x) - добавляет x к правой стороне (в конец) контейнера deque(). # inplace

 from collections import deque

 dq = deque('ghi')
 dq.append('j')
 print(dq)
 # deque(['g', 'h', 'i', 'j'])
________________________________________________________________________________________________________________________
 Deque.appendleft(x) - добавляет x к левой стороне (в начало) контейнера deque(). # inplace

 dq.appendleft('f')
 print(dq)
 # deque(['f', 'g', 'h', 'i', 'j'])

 Deque.copy() - создает неглубокую копию контейнера deque().

 cp_dq = dq.copy()
 print(cp_dq)
 deque(['f', 'g', 'h', 'i', 'j'])
________________________________________________________________________________________________________________________
 Deque.clear() - удаляет все элементы из контейнера deque(), оставляя его длиной 0. # inplace

 cp_dq.clear()
 print(cp_dq)
 # deque([])
 print(dq)
 # deque(['f', 'g', 'h', 'i', 'j'])
________________________________________________________________________________________________________________________
 Deque.count(x) - подсчитывает количество элементов контейнера deque(), равное значению x.

 dq.append('g')
 print(dq.count('g'))
 # 2
________________________________________________________________________________________________________________________
 Deque.extend(iterable) - расширяет правую сторону (с конца) контейнера deque(), добавляя элементы из итерируемого аргумента iterable.
 # inplace

 dq.extend('jkl')
 print(dq)
 # deque(['f', 'g', 'h', 'i', 'j', 'g', 'j', 'k', 'l'])
________________________________________________________________________________________________________________________
 Deque.extendleft(iterable) - расширяет левую сторону (с начала) контейнера deque(), добавляя элементы из итерируемого аргумента iterable.
 # inplace
 Обратите внимание, что ряд последовательных добавлений в начало контейнера приводит к изменению порядка элементов в аргументе iterable.

 dq.extendleft('ab')
 print(dq)
 # deque(['b', 'a', 'f', 'g', 'h', 'i', 'j', 'g', 'j', 'k', 'l'])
________________________________________________________________________________________________________________________
 Deque.index(x[, start[, stop]]) - вернет позицию (индекс) первого совпадения значения аргумента x в контейнере deque(),
 расположенного после необязательного аргумента start и до необязательного аргумента stop.
 Вызывает исключение ValueError, если значения аргумента x не найдено.

 print(dq.index('g', 2))
 # 3
 dq.index('b', 2)
 # ValueError: 'b' is not in deque
________________________________________________________________________________________________________________________
 Deque.insert(i, x) - вставляет значение аргумента x в позицию i контейнера deque(). Если вставка значение аргумента x
 приведет к тому, что ограниченный контейнер deque() выйдет за пределы maxlen, будет вызвано исключение IndexError. # inplace

 dq.insert(2, 'C')
 print(dq)
 # deque(['b', 'a', 'C', 'f', 'g', 'h', 'i', 'j', 'g', 'j', 'k', 'l'])

 dq_empty = deque()                           a_deque = deque([1, 2,], maxlen=2)
 print(dq_empty)                              print(a_deque)  # -> deque([1, 2], maxlen=2)
 # deque(['A', 'B', 'C'])                     a_deque.insert(100, 4) # -> IndexError: deque already at its maximum size
 print(dq_empty.insert(100, 'd'))
 # deque(['d'])
 print(dq_empty)
 # deque(['d'])
________________________________________________________________________________________________________________________
 Deque.pop() - удаляет и возвращает элемент с правой стороны (с конца) контейнера deque(). # inplace
 Если элементы отсутствуют, возникает ошибка IndexError.

 print(dq.pop())
 # l

 dq_empty = deque()
 print(dq_empty)
 # deque([])
 print(dq_empty.pop(2))
 # TypeError: deque.pop() takes no arguments (1 given)
 print(dq_empty.pop())
 # IndexError: pop from an empty deque

 dq = deque(['A', 'B', 'C'])
 print(dq)
 # deque(['A', 'B', 'C'])
 # print(dq.pop(1))
 # TypeError: deque.pop() takes no arguments (1 given)
 print(dq.pop())
 # C
 print(dq)
 # deque(['A', 'B'])
________________________________________________________________________________________________________________________
 Deque.popleft() - удаляет и возвращает элемент с левой стороны (с начала) контейнера deque(). # inplace
 Если элементы отсутствуют, возникает ошибка IndexError.

 print(dq.popleft())
 # b


 dq_empty = deque()
 print(dq_empty)
 # deque([])
 print(dq_empty.popleft(2))
 # TypeError: deque.popleft() takes no arguments (1 given)
 print(dq_empty.popleft())
 # IndexError: pop from an empty deque

 dq = deque(['A', 'B', 'C'])
 print(dq)
 # deque(['A', 'B', 'C'])
 print(dq.popleft(1))
 # TypeError: deque.popleft() takes no arguments (1 given)
 print(dq.popleft())
 # A
 print(dq)
 # deque(['B', 'C'])

________________________________________________________________________________________________________________________
 Deque.remove(value) - удаляет первое вхождение значения value в контейнер deque(). Если значение value не найдено,
 возникает ошибка ValueError. # inplace

 dq.remove('g')
 dq.remove('z') - ValueError: 'z' is not in deque

 dq = deque([1, 2, 3])
 print(dq)
 #deque([1, 2, 3])
 dq.remove(2)
 print(dq)
 # deque([1, 3])
 dq.remove(4)
 # ValueError: 4 is not in deque
________________________________________________________________________________________________________________________
 Deque.reverse() - разворачивает элементы контейнера deque() на месте и возвращает None. # inplace

 print(dq)
 # deque(['a', 'c', 'f', 'h', 'i', 'j', 'g', 'j', 'k'])
 print(dq.reverse())
 # None
 print(dq)
 # deque(['k', 'j', 'g', 'j', 'i', 'h', 'f', 'c', 'a'])
________________________________________________________________________________________________________________________
 Deque.rotate(n=1) - разворачивает контейнер deque() на n шагов вправо. Если аргумент n имеет отрицательное значение,
 то разворачивает контейнер налево. # inplace

 Когда контейнер не пуст, вращение на один шаг вправо эквивалентно dq.appendleft(d.pop()),
 а вращение на один шаг влево эквивалентно dq.append(d.popleft()).

 from collections import deque

 dq_1 = deque('abcdefgh')
 dq_2 = deque('abcdefgh')
 dq_3 = deque('abcdefgh')

 dq_1.rotate(1)
 print('dq_1', dq_1)
 dq_1 deque(['h', 'a', 'b', 'c', 'd', 'e', 'f', 'g'])
 dq_2.rotate(2)
 print('dq_2', dq_2)
 dq_2 deque(['g', 'h', 'a', 'b', 'c', 'd', 'e', 'f'])
 dq_3.rotate(-4)
 print('dq_3', dq_3)
 dq_3 deque(['e', 'f', 'g', 'h', 'a', 'b', 'c', 'd'])
________________________________________________________________________________________________________________________
 Deque.maxlen - Свойство Deque.maxlen() возвращает максимальный размер maxlen контейнера deque(),
 если параметр maxlen не задан, то возвращает None.

 dq_empty = deque()
 # deque([])
 dq = deque('ABCD')
 # deque(['A', 'B', 'C', 'D'])
 dq_maxlen_1 = deque('ABCD', maxlen=1)
 # deque(['D'], maxlen=1)
 dq_maxlen_2 = deque('ABCD', maxlen=2)
 # deque(['C', 'D'], maxlen=2)
 dq_maxlen_3 = deque('ABCD', maxlen=3)
 # deque(['B', 'C', 'D'], maxlen=3)
________________________________________________________________________________________________________________________
 --- namedtuple  ---

 Collections.namedtuple(typename, field_names, *, rename=False, defaults=None, module=None) - Именованные кортежи в Python

 возвращает новый подкласс кортежа с именем typename.

 Экземпляры именованных кортежей не имеют словарей, поэтому они легковесны и требуют не больше памяти, чем обычные кортежи.

 Именованные кортежи присваивают имя каждому значению элемента в кортеже и тем самым создают более читаемый код.
 Они могут использоваться везде, где используются обычные кортежи и добавляют возможность доступа к полям по имени вместо индекса позиции.

 field_names -  ['x', 'y'],   'x y'  или  'x, y'
 фабричная функция namedtuple вызывает функцию split() со строковым значением
 'цвет пробег'.split()

 # Простой пример
 from collections import namedtuple
 Point = namedtuple('Point', ['x', 'y'])  # Тоже самое
 Point = namedtuple('Point', 'x y')       # Тоже самое
 Point = namedtuple('Point', 'x, y')      # Тоже самое
 # создаем с позиционным или именованным параметром
 p = Point(11, y=22)

 # можно обращаться через точку как в Классах
 print(p.x) # 11
 print(p.y) # 22

 # можно обращаться по индексу
 # как к обычному кортежу
 print(p[0] + p[1])
 # 33

 # распаковать как обычный кортеж
 x, y = p
 print(x, y)
 # (11, 22)

 # поля также доступны по названию
 print(p.x + p.y)
 # 33

 # человеко-читаемый __repr__
 print(p)
 # Point(x=11, y=22)

 # Именованные кортежи поддерживают функцию getattr():
 print(getattr(p, 'x'))
 # 11

 Чтобы преобразовать словарь в именованный кортеж, используйте оператор двойной звезды **
 from collections import namedtuple

 Point = namedtuple('Point', ['x', 'y'])
 d = {'x': 11, 'y': 22}
 print(Point(**d))
 # Point(x=11, y=22)
 print(Point(d))
 # TypeError: Point.__new__() missing 1 required positional argument: 'y'
________________________________________________________________________________________________________________________
 --- defaultdict ---

 class collections.defaultdict(default_factory=None, /[, ...]) - Словарь со значениями по умолчанию.

 ничем не отличается от обычного словаря за исключением того, что по умолчанию всегда вызывается функция, которая возвращает
 значение по умолчанию для новых значений. Другими словами Класс defaultdict() представляет собой словарь со значениями по умолчанию.

 возвращает новый словарь-подобный объект. Defaultdict является подклассом встроенного класса dict(). Он переопределяет
 один метод и добавляет одну доступную для записи переменную экземпляра. Остальная функциональность такая же, как и для класса dict().

 Попробуй пример!!! # Мульти-словарь - когда ключу соответствует список

 from collections import defaultdict

 s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
 d = defaultdict(list)

 d = dict(list)  #   TypeError: 'type' object is not iterable

 for k, v in s:
     d[k].append(v)

 print(sorted(d.items()))
 # [('blue', [2, 4]), ('red', [1]), ('yellow', [1, 3])]

 Этот метод проще и быстрее, чем эквивалентный метод словаря dict.setdefault():


 Пример с dict.setdefault():
 from collections import defaultdict

 s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
 d = {}
 for k, v in s:
     d.setdefault(k, []).append(v)

 print(sorted(d.items()))
 # [('blue', [2, 4]), ('red', [1]), ('yellow', [1, 3])]

 Установка функции int() в качестве функции default_factory, генерирующей значений по умолчанию, делает defaultdict()
 полезным для подсчета чего либо:

 from collections import defaultdict

 s = 'mississippi'
 d = defaultdict(int)
 for k in s:
     d[k] += 1

 print(sorted(d.items()))
 # [('i', 4), ('m', 1), ('p', 2), ('s', 4)]

 Установка значения default_factory делает defaultdict полезным для создания словаря множеств:

 from collections import defaultdict

 s = [('red', 1), ('blue', 2), ('red', 3), ('blue', 4), ('red', 1), ('blue', 4)]
 d = defaultdict(set)
 for k, v in s:
     d[k].add(v)

 print(sorted(d.items()))
 # [('blue', {2, 4}), ('red', {1, 3})]

 # Мульти-словарь - когда ключу соответствует список
 a_dict = defaultdict(list)

 for char in 'hello':
     a_dict[char].append(char)

 print(a_dict)
________________________________________________________________________________________________________________________
 --- OrderedDict ---

 class collections.OrderedDict([items]) - Обеспечивает частые операции переупорядочения ключей словаря.
 Создан для операций с порядком.

 возвращает экземпляр подкласса dict, у которого есть методы, специализированные для изменения порядка словаря.

 Упорядоченные словари похожи на обычные словари, но имеют некоторые дополнительные возможности, связанные с
 операциями упорядочивания. Теперь они стали менее важными, когда встроенный класс dict получил возможность запоминать
 порядок вставки (это новое поведение стало гарантированным в Python 3.7).

 # Встроенный словарь(dict) не проверяет порядок элементов

 first = {1: 1, 2: 2}
 second = {2: 2, 1: 1}
 print(first == second)
 # True

 # упорядоченный словарь(OrderedDict) проверяет порядок элементов

 order1 = OrderedDict(first)
 order2 = OrderedDict(second)
 print(order1 == order2)
 # False

 # Примеры: popitem() - Пары возвращаются с конца словаря, в порядке LIFO (последним пришёл - первым ушёл).
 first = {1: 1, 2: 2, 3: 3}
 second = {2: 2, 1: 1}
 print(first.popitem())
 # (3, 3)

 # упорядоченный словарь(OrderedDict) popitem(last=False),
 order1 = OrderedDict(first)
 order2 = OrderedDict(second)
 print(order1.popitem())
 # (3, 3)
 print(order1.popitem(last=False))
 # (1, 1)
 print(order1.popitem(last=True))
 # (3, 3)

 print(order1)
 # OrderedDict([(1, 1), (2, 2), (3, 3)])
 order1.move_to_end(1)
 order1.move_to_end(key=1)
 print(order1)
 # OrderedDict([(2, 2), (3, 3), (1, 1)])
 order1.move_to_end(3, last=False)
 print(order1)
 OrderedDict([(3, 3), (1, 1), (2, 2)])

________________________________________________________________________________________________________________________
 Методы объекта OrderedDict():

 popitem(last=True) - для упорядоченных словарей возвращает и удаляет пару (key, value). Пары (key, value)
 возвращаются в порядке LIFO, если аргумент last=True или в порядке FIFO, если last=False. # inplace

 a_dict = OrderedDict(dict.fromkeys('abc', 0))
 print(a_dict)
 # {'a': 0, 'b': 0, 'c': 0}
 print(a_dict.popitem(last=False))
 # ('a', 0)
 print(a_dict.popitem(last=True))
 # ('c', 0)
 print(a_dict)
 # OrderedDict([('b', 0)])
________________________________________________________________________________________________________________________
 move_to_end(key, last=True) - перемещает существующий ключ key в начало/конец упорядоченного словаря. Элемент
 перемещается в правый конец, если аргумент last=True (по умолчанию), или в начало, если last=False. # inplace
 Вызывает исключение KeyError, если ключ не существует:

 d = OrderedDict.fromkeys('abcde')
 d.move_to_end('b')
 print(d)
 # OrderedDict([('a', None), ('c', None), ('d', None), ('e', None), ('b', None)])
 print(''.join(d.keys()))
 # 'acdeb'
 # d.move_to_end('z', last=False)
 # KeyError: 'z'
 d.move_to_end('b', last=False)
 print(d)
 # OrderedDict([('b', None), ('a', None), ('c', None), ('d', None), ('e', None)])
 print(''.join(d.keys()))
 # 'bacde'
________________________________________________________________________________________________________________________




________________________________________________________________________________________________________________________




________________________________________________________________________________________________________________________




________________________________________________________________________________________________________________________




________________________________________________________________________________________________________________________







"""