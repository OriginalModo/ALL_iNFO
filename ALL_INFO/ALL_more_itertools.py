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


--- сторонний модуль more-itertools в Python, Больше процедур для работы с итерируемыми объектами, помимо itertools ---

 Но если itertools вам уже не хватает, то вэлкам: more-itertools.
 Тут есть chunked, spy, first, one, only, unique_everseen и прочие прелести. Осторожно, с этой дряни невозможно слезть.


________________________________________________________________________________________________________________________
 --- Группировка    Grouping ---

 --- Эти инструменты позволяют получить группы элементов из итерируемого источника ---

 --- These tools yield groups of items from a source iterable ---
________________________________________________________________________________________________________________________
 more_itertools.chunked(iterable, n, strict=False) - Разбейте итерацию на списки длины n

 from more_itertools import chunked

 iterable = [1, 2, 3, 4, 5, 6]
 list(chunked(iterable, 1))  # -> [[1], [2], [3], [4], [5], [6]]
 list(chunked(iterable, 2))  # -> [[1, 2], [3, 4], [5, 6]]
 list(chunked(iterable, 3))  # -> [[1, 2, 3], [4, 5, 6]]

 По умолчанию последний полученный список будет содержать менее n элементов, если длина итерируемого объекта не делится на n :
 list(chunked(iterable, 4))  # -> [[1, 2, 3, 4], [5, 6]]
 Чтобы использовать вместо этого заполняемое значение, смотри функцию grouper().

 Если длина итерируемого объекта не делится на n , а strict равен True
 list(chunked([1], 2, strict=True)) # -> ValueError: iterable is not divisible by n.

 Исходник:
 def chunked(iterable, n, strict=False):
    iterator = iter(partial(take, n, iter(iterable)), [])
        if strict:
            if n is None:
                raise ValueError('n must not be None when using strict mode.')

            def ret():
                for chunk in iterator:
                    if len(chunk) != n:
                        raise ValueError('iterable is not divisible by n.')
                    yield chunk

            return iter(ret())
        else:
            return iterator
________________________________________________________________________________________________________________________
 more_itertools.ichunked(iterable, n) - похож на chunked(), но вместо списков выдает итерации.

 Если подитерации читаются по порядку, элементы итерации не будут храниться в памяти. Если они читаются не по порядку,
 itertools.tee() используется для кэширования элементов по мере необходимости.

 from more_itertools import ichunked
 from itertools import count

 all_chunks = ichunked(count(), 2)                     all_chunks = ichunked(count(), 5)
 c_1, c_2 = next(all_chunks), next(all_chunks)         c_1, c_2 = next(all_chunks), next(all_chunks)
 list(c_1)  # -> [0, 1]                                list(c_1)  # -> [0, 1, 2, 3, 4]
 list(c_2)  # -> [2, 3]                                list(c_2)  # -> [5, 6, 7, 8, 9]

 Исходник Не слабый:
 from more_itertools import peekable
 from itertools import islice
 from collections import deque

 class _IChunk:

     def __init__(self, iterable, n):
         self._it = islice(iterable, n)
         self._cache = deque()

     def fill_cache(self):
         self._cache.extend(self._it)

     def __iter__(self):
         return self

     def __next__(self):
         try:
             return next(self._it)
         except StopIteration:
             if self._cache:
                 return self._cache.popleft()
             else:
                 raise

 def ichunked(iterable, n):
     source = peekable(iter(iterable))
     ichunk_marker = object()
     while True:
         # Check to see whether we're at the end of the source iterable
         item = source.peek(ichunk_marker)
         if item is ichunk_marker:
             return

         chunk = _IChunk(source, n)
         yield chunk

         # Advance the source iterable and fill previous chunk's cache
         chunk.fill_cache()

________________________________________________________________________________________________________________________
 more_itertools.chunked_even(iterable, n) - похож на chunked() но длина списков отличается не более чем на 1 элемент.

 from more_itertools import chunked_even, chunked

 iterable = [1, 2, 3, 4, 5, 6, 7]
 list(chunked_even(iterable, 3))  # -> [[1, 2, 3], [4, 5], [6, 7]]
 list(chunked(iterable, 3))       # -> [[1, 2, 3], [4, 5, 6], [7]]

 Исходник Нет Не слабый:
 from itertools import islice

 def chunked_even(iterable, n):
     len_method = getattr(iterable, '__len__', None)

     if len_method is None:
         return _chunked_even_online(iterable, n)
     else:
         return _chunked_even_finite(iterable, len_method(), n)

 def _chunked_even_online(iterable, n):
     buffer = []
     maxbuf = n + (n - 2) * (n - 1)
     for x in iterable:
         buffer.append(x)
         if len(buffer) == maxbuf:
             yield buffer[:n]
             buffer = buffer[n:]
     yield from _chunked_even_finite(buffer, len(buffer), n)

 def _chunked_even_finite(iterable, N, n):
     if N < 1:
         return

     # Lists are either size `full_size <= n` or `partial_size = full_size - 1`
     q, r = divmod(N, n)
     num_lists = q + (1 if r > 0 else 0)
     q, r = divmod(N, num_lists)
     full_size = q + (1 if r > 0 else 0)
     partial_size = full_size - 1
     num_full = N - partial_size * num_lists
     num_partial = num_lists - num_full

     # Yield num_full lists of full_size
     partial_start_idx = num_full * full_size
     if full_size > 0:
         for i in range(0, partial_start_idx, full_size):
             yield list(islice(iterable, i, i + full_size))

     # Yield num_partial lists of partial_size
     if partial_size > 0:
         for i in range(
             partial_start_idx,
             partial_start_idx + (num_partial * partial_size),
             partial_size,
         ):
             yield list(islice(iterable, i, i + partial_size))

________________________________________________________________________________________________________________________
 more_itertools.sliced(seq, n, strict=False) - Получите срезы длины n из последовательности seq .
 Эта функция будет работать только для итераций, поддерживающих нарезку.

 from more_itertools import sliced

 iterable = [1, 2, 3, 4, 5, 6, 7]
 list(sliced(iterable, 3))  # -> [[1, 2, 3], [4, 5, 6], [7]]
 list(sliced(iterable, 2))  # -> [[1, 2], [3, 4], [5, 6], [7]]
 list(sliced([1], 2, strict=True))  # -> ValueError: seq is not divisible by n.

 Исходник:
 from itertools import takewhile

 def sliced(seq, n, strict=False):
     iterator = takewhile(len, (seq[i: i + n] for i in count(0, n)))
     if strict:

         def ret():
             for _slice in iterator:
                 if len(_slice) != n:
                     raise ValueError("seq is not divisible by n.")
                 yield _slice

         return iter(ret())
     else:
         return iterator

________________________________________________________________________________________________________________________
 more_itertools.constrained_batches(iterable, max_size, max_count=None, get_len=len, strict=True)
 Получайте партии элементов из итерируемого объекта с общим размером, ограниченным max_size .
 позвольте отдельным элементам внутри превышать *max_size*

 from more_itertools import constrained_batches

 iterable = [b'12345', b'123', b'12345678', b'1', b'1', b'12', b'1']
 list(constrained_batches(iterable, max_size=10, max_count=2))  # Делить на max_size внутри и количество max_count
 # [(b'12345', b'123'), (b'12345678', b'1'), (b'1', b'12'), (b'1',)]
 list(constrained_batches(iterable, max_size=50, max_count=50)) # Тут всё в одном tuple/кортеже
 # [(b'12345', b'123', b'12345678', b'1', b'1', b'12', b'1')]
 list(constrained_batches(iterable, max_size=1, max_count=5))   # max_size - длина слова/iterable внутри iterable
 # ValueError: item size exceeds maximum size

 Исходник:
 def constrained_batches(
     iterable, max_size, max_count=None, get_len=len, strict=True
 ):
     if max_size <= 0:
         raise ValueError('maximum size must be greater than zero')

     batch = []
     batch_size = 0
     batch_count = 0
     for item in iterable:
         item_len = get_len(item)
         if strict and item_len > max_size:
             raise ValueError('item size exceeds maximum size')

         reached_count = batch_count == max_count
         reached_size = item_len + batch_size > max_size
         if batch_count and (reached_size or reached_count):
             yield tuple(batch)
             batch.clear()
             batch_size = 0
             batch_count = 0

         batch.append(item)
         batch_size += item_len
         batch_count += 1

     if batch:
         yield tuple(batch)

________________________________________________________________________________________________________________________
 more_itertools.distribute(n, iterable) -  Распределите элементы из итерации среди n меньших итераций.
 Эта функция использует itertools.tee()и может потребовать значительный объем памяти. Если вам нужно, чтобы элементы
 порядка в меньших итерациях соответствовали исходной итерации, смотри функцию divide().

 from more_itertools import distribute

 group_1, group_2 = distribute(2, [1, 2, 3, 4, 5, 6])  # Будет брать элементы через n=2 в список
 list(group_1)  # -> [1, 3, 5]
 list(group_2)  # -> [2, 4, 6]

 children = distribute(4, [1, 2, 3, 4, 5, 6, 7])       # Будет брать элементы через n=4 в список
 [list(c) for c in children]  # -> [[1, 5], [2, 6], [3, 7], [4]]

 Если длина итерации не делится на n без остатка , то длина возвращаемых итераций не будет одинаковой:

 children = distribute(3, [1, 2, 3, 4, 5, 6, 7])
 [list(c) for c in children]  # -> [[1, 4, 7], [2, 5], [3, 6]]

 Если длина итерации меньше n , то последние возвращенные итерации будут пустыми:

 children = distribute(5, [1, 2, 3])
 [list(c) for c in children]  # -> [[1], [2], [3], [], []]

 Исходник:
 from itertools import tee, islice

 def distribute(n, iterable):
     if n < 1:
         raise ValueError('n must be at least 1')

     children = tee(iterable, n)
     return [islice(it, index, None, n) for index, it in enumerate(children)]

________________________________________________________________________________________________________________________
 more_itertools.divide(n, iterable) - Разделите элементы из итерируемого объекта на n частей, соблюдая порядок.
 Эта функция исчерпает итерируемый объект перед возвратом и может потребовать значительного объема памяти.
 Если порядок не важен, см. distribute(), где итерируемый объект сначала не загружается в память.

 from more_itertools import divide

 group_1, group_2 = divide(2, [1, 2, 3, 4, 5, 6])  # Будет делить элементы на n=2 частей в списке соблюдая порядок
 list(group_1)  # -> [1, 2, 3]
 list(group_2)  # -> [4, 5, 6]

 children = divide(4, [1, 2, 3, 4, 5, 6, 7])  # Будет брать элементы через n=4 частей в списке соблюдая порядок
 [list(c) for c in children]  # -> [[1, 5], [2, 6], [3, 7], [4]]

 Если длина итерации не делится на n без остатка , то длина возвращаемых итераций не будет одинаковой:

 children = divide(3, [1, 2, 3, 4, 5, 6, 7])
 [list(c) for c in children]  # -> [[1, 2, 3], [4, 5], [6, 7]]

 Если длина итерации меньше n, то последние возвращенные итерации будут пустыми:

 children = divide(5, [1, 2, 3])
 [list(c) for c in children]  # -> [[1], [2], [3], [], []]

 Исходник:
 def divide(n, iterable):
     if n < 1:
         raise ValueError('n must be at least 1')

     try:
         iterable[:0]
     except TypeError:
         seq = tuple(iterable)
     else:
         seq = iterable

     q, r = divmod(len(seq), n)

     ret = []
     stop = 0
     for i in range(1, n + 1):
         start = stop
         stop += q + 1 if i <= r else q
         ret.append(iter(seq[start:stop]))

     return ret

________________________________________________________________________________________________________________________
 more_itertools.split_at(iterable, pred, maxsplit=-1, keep_separator=False) - Получайте списки элементов из iterable
 где каждый список ограничен элементом, где вызываемый pred возвращает значение True.

 from more_itertools import split_at

 list(split_at('abcdcba', lambda x: x == 'b'))    # -> [['a'], ['c', 'd', 'c'], ['a']]
 list(split_at(range(10), lambda n: n % 2 == 1))  # -> [[0], [2], [4], [6], [8], []]

 В большинстве случаев выполняется разделение maxsplit . Если maxsplit не указан или -1,
 то ограничений на количество разбиений нет:

 list(split_at(range(10), lambda n: n % 2 == 1, maxsplit=2))  # -> [[0], [2], [4, 5, 6, 7, 8, 9]]

 По умолчанию элементы-разделители не включаются в выходные данные. Чтобы включить их,
 установите для параметра Keep_separator значение True.

 list(split_at('abcdcba', lambda x: x == 'b', keep_separator=True))  # -> [['a'], ['b'], ['c', 'd', 'c'], ['b'], ['a']]

 Исходник:
 def split_at(iterable, pred, maxsplit=-1, keep_separator=False):
     if maxsplit == 0:
         yield list(iterable)
         return

     buf = []
     it = iter(iterable)
     for item in it:
         if pred(item):
             yield buf
             if keep_separator:
                 yield [item]
             if maxsplit == 1:
                 yield list(it)
                 return
             buf = []
             maxsplit -= 1
         else:
             buf.append(item)
     yield buf

________________________________________________________________________________________________________________________
 more_itertools.split_before(iterable, pred, maxsplit=-1) - Получайте списки элементов из iterable, где каждый список
 заканчивается непосредственно перед элементом, для которого callable pred возвращает True:

 from more_itertools import split_before

 list(split_before('OneTwo', lambda s: s.isupper()))  # -> [['O', 'n', 'e'], ['T', 'w', 'o']]
 list(split_before(range(10), lambda n: n % 3 == 0))  # -> [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9]]

 В большинстве случаев выполняется разделение maxsplit . Если maxsplit не указан или -1,
 то ограничений на количество разбиений нет:

 list(split_before(range(10), lambda n: n % 3 == 0, maxsplit=2))  # -> [[0, 1, 2], [3, 4, 5], [6, 7, 8, 9]]

 Исходник:
 def split_before(iterable, pred, maxsplit=-1):
     if maxsplit == 0:
         yield list(iterable)
         return

     buf = []
     it = iter(iterable)
     for item in it:
         if pred(item) and buf:
             yield buf
             if maxsplit == 1:
                 yield [item] + list(it)
                 return
             buf = []
             maxsplit -= 1
         buf.append(item)
     if buf:
         yield buf

________________________________________________________________________________________________________________________
 more_itertools.split_after(iterable, pred, maxsplit=-1) - Возвращает списки элементов из iterable, где каждый список
 заканчивается элементом, где callable pred возвращает True:

 from more_itertools import split_after

 list(split_after('one1two2', lambda s: s.isdigit()))  # -> [['o', 'n', 'e', '1'], ['t', 'w', 'o', '2']]
 list(split_after(range(10), lambda n: n % 3 == 0))    # -> [[0], [1, 2, 3], [4, 5, 6], [7, 8, 9]]

 В большинстве случаев выполняется разделение maxsplit . Если maxsplit не указан или -1,
 то ограничений на количество разбиений нет:

 list(split_after(range(10), lambda n: n % 3 == 0, maxsplit=2))  # -> [[0], [1, 2, 3], [4, 5, 6, 7, 8, 9]]

 Исходник:
 def split_after(iterable, pred, maxsplit=-1):
     if maxsplit == 0:
         yield list(iterable)
         return

     buf = []
     it = iter(iterable)
     for item in it:
         buf.append(item)
         if pred(item) and buf:
             yield buf
             if maxsplit == 1:
                 buf = list(it)
                 if buf:
                     yield buf
                 return
             buf = []
             maxsplit -= 1
     if buf:
         yield buf

________________________________________________________________________________________________________________________
 more_itertools.split_into(iterable, sizes) - Получите список последовательных элементов из итерации длины «n»
 для каждого целого числа «n» в размерах .

 from more_itertools import split_into

 list(split_into([1, 2, 3, 4, 5, 6], [1, 2, 3]))  # -> [[1], [2, 3], [4, 5, 6]]

 Если сумма размеров меньше длины iterable , то остальные элементы iterable не будут возвращены.

 list(split_into([1, 2, 3, 4, 5, 6], [2, 3]))  # -> [[1, 2], [3, 4, 5]]

 Если сумма размеров больше длины iterable , в итерации, которая переполняет iterable, будет возвращено меньше элементов,
 и дальнейшие списки будут пустыми:

 list(split_into([1, 2, 3, 4], [1, 2, 3, 4]))  # -> [[1], [2, 3], [4], []]

 Когда Noneо бъект встречается в размерах , возвращаемый список будет содержать элементы до конца итерируемого объекта
 так же, как это делает itertools.slice:

 list(split_into([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], [2, 3 ,None]))  # -> [[1, 2], [3, 4, 5], [6, 7, 8, 9, 0]]

 split_into()может быть полезно для группировки ряда элементов, размеры групп которых неодинаковы. Примером может
 служить случай, когда в строке таблицы несколько столбцов представляют элементы одного и того же объекта
 (например, точку, представленную x, y, z), но формат не одинаков для всех столбцов.

 Исходник:
 def split_into(iterable, sizes):
     # convert the iterable argument into an iterator so its contents can
     # be consumed by islice in case it is a generator
     it = iter(iterable)

     for size in sizes:
         if size is None:
             yield list(it)
             return
         else:
             yield list(islice(it, size))

________________________________________________________________________________________________________________________
 more_itertools.split_when(iterable, pred, maxsplit=-1) - Разделите итерацию на части на основе вывода pred .
 pred должен быть функцией, которая принимает последовательные пары элементов и возвращает результат,
 True если итерация должна быть разделена между ними.
 Например, чтобы найти серии возрастающих чисел, разделите итерацию, когда element iбольше element : i + 1

 from more_itertools import split_when

 list(split_when([1, 2, 3, 3, 2, 5, 2, 4, 2], lambda x, y: x > y))  # -> [[1, 2, 3, 3], [2, 5], [2, 4], [2]]

 В большинстве случаев выполняется разделение maxsplit . Если maxsplit не указан или -1,
 то ограничений на количество разбиений нет:

 list(split_when([1, 2, 3, 3, 2, 5, 2, 4, 2],
                 lambda x, y: x > y, maxsplit=2))       # -> [[1, 2, 3, 3], [2, 5], [2, 4, 2]]

 Исходник:
 def split_when(iterable, pred, maxsplit=-1):
     if maxsplit == 0:
         yield list(iterable)
         return

     it = iter(iterable)
     try:
         cur_item = next(it)
     except StopIteration:
         return

     buf = [cur_item]
     for next_item in it:
         if pred(cur_item, next_item):
             yield buf
             if maxsplit == 1:
                 yield [next_item] + list(it)
                 return
             buf = []
             maxsplit -= 1

         buf.append(next_item)
         cur_item = next_item

     yield buf

________________________________________________________________________________________________________________________
 more_itertools.bucket(iterable, key, validator=None) - Оберните итерируемый объект и верните объект,
 который группирует итерируемый объект в дочерние итерации на основе ключевой функции.

 from more_itertools import bucket

 iterable = ['a1', 'b1', 'c1', 'a2', 'b2', 'c2', 'b3']
 s = bucket(iterable, key=lambda x: x[0])  # Bucket by 1st character
 print(sorted(list(s)))  # Get the keys  # -> ['a', 'b', 'c']
 a_iterable = s['a']
 next(a_iterable)  # -> a1
 next(a_iterable)  # -> a2
 list(s['b'])      # -> ['b1', 'b2', 'b3']

 Исходная итерация будет расширена, а ее элементы будут кэшироваться до тех пор, пока они не будут использованы
 дочерними итерациями. Это может потребовать значительного объема памяти.

 По умолчанию попытка выбрать сегмент, которому не принадлежат никакие элементы, приведет к исчерпанию итерации и
 кешированию всех значений. Если вы укажете функцию валидатора , вместо этого выбранные сегменты будут проверяться по ней.

 from itertools import count
 it = count(1, 2)  # Infinite sequence of odd numbers
 key = lambda x: x % 10  # Bucket by last digit
 validator = lambda x: x in {1, 3, 5, 7, 9}  # Odd digits only
 s = bucket(it, key=key, validator=validator)
 2 in s      # -> False
 list(s[2])  # -> []

 Исходник Очень не слабый:
 from collections import defaultdict, deque

 class bucket:
     def __init__(self, iterable, key, validator=None):
         self._it = iter(iterable)
         self._key = key
         self._cache = defaultdict(deque)
         self._validator = validator or (lambda x: True)

     def __contains__(self, value):
         if not self._validator(value):
             return False

         try:
             item = next(self[value])
         except StopIteration:
             return False
         else:
             self._cache[value].appendleft(item)

         return True

     def _get_values(self, value):
         while True:
             # If we've cached some items that match the target value, emit
             # the first one and evict it from the cache.
             if self._cache[value]:
                 yield self._cache[value].popleft()
             # Otherwise we need to advance the parent iterator to search for
             # a matching item, caching the rest.
             else:
                 while True:
                     try:
                         item = next(self._it)
                     except StopIteration:
                         return
                     item_value = self._key(item)
                     if item_value == value:
                         yield item
                         break
                     elif self._validator(item_value):
                         self._cache[item_value].append(item)

     def __iter__(self):
         for item in self._it:
             item_value = self._key(item)
             if self._validator(item_value):
                 self._cache[item_value].append(item)

         yield from self._cache.keys()

     def __getitem__(self, value):
         if not self._validator(value):
             return iter(())

         return self._get_values(value)

________________________________________________________________________________________________________________________
 more_itertools.unzip(iterable) - Обратная функция zip(), эта функция дезагрегирует элементы заархивированной итерации.
 i-я итерация содержит i-й элемент из каждого элемента сжатой итерации. Первый элемент используется для
 определения длины остальных элементов.

 from more_itertools import unzip

 iterable = [('a', 1), ('b', 2), ('c', 3), ('d', 4)]
 letters, numbers = unzip(iterable)
 list(letters)  # -> ['a', 'b', 'c', 'd']
 list(numbers)  # -> [1, 2, 3, 4]

 Это похоже на использование zip(*iterable), но позволяет избежать чтения итерации в память. Однако обратите внимание,
 что эта функция использует itertools.tee()и, следовательно, может потребовать значительного объема памяти.

 Исходник:
 from more_itertools import spy
 from itertools import tee

 def unzip(iterable):
     head, iterable = spy(iter(iterable))
     if not head:
         # empty iterable, e.g. zip([], [], [])
         return ()
     # spy returns a one-length iterable as head
     head = head[0]
     iterables = tee(iterable, len(head))

     def itemgetter(i):
         def getter(obj):
             try:
                 return obj[i]
             except IndexError:
                 raise StopIteration

         return getter

     return tuple(map(itemgetter(i), it) for i, it in enumerate(iterables))

________________________________________________________________________________________________________________________
 Itertools recipes

 more_itertools.batched(iterable, n, *, strict=False) - Пакетная обработка данных в кортежи длины n. Если количество
 элементов в итерации не делится на n: * Последний пакет будет короче, если strict имеет значение False. * ValueError
 будет возникать, если strict имеет значение True.
 В Python 3.13 и более поздних версиях это псевдоним для itertools.batched().

 from more_itertools import batched

 list(batched('ABCDEFG', 3))  # -> [('A', 'B', 'C'), ('D', 'E', 'F'), ('G',)]

 Исходник:
 from itertools import batched as itertools_batched

 def batched(iterable, n, *, strict=False):
     return itertools_batched(iterable, n, strict=strict)

________________________________________________________________________________________________________________________
 more_itertools.grouper(iterable, n, incomplete='fill', fillvalue=None) - Группируйте элементы из итерируемых в группы
 фиксированной длины длины n .

 from more_itertools import grouper

 list(grouper('ABCDEF', 3))  # -> [('A', 'B', 'C'), ('D', 'E', 'F')]

 Аргументы ключевых слов incomplete и fillvalue управляют тем, что происходит с итерациями, длина которых не кратна n .
 Если неполным является 'fill' , последняя группа будет содержать экземпляры fillvalue .

 list(grouper('ABCDEFG', 3, incomplete='fill', fillvalue='x'))  # -> [('A', 'B', 'C'), ('D', 'E', 'F'), ('G', 'x', 'x')]

 Если неполным является «игнорировать» , последняя группа не будет выдана.

 list(grouper('ABCDEFG', 3, incomplete='ignore', fillvalue='x'))  # -> [('A', 'B', 'C'), ('D', 'E', 'F')]

 Если incomplete имеет значение «strict» , будет создан подкласс ValueError .

 it = grouper('ABCDEFG', 3, incomplete='strict')
 list(it)  # -> UnequalIterablesError: Iterables have different lengths

 Исходник Очень нет слабый:
 from itertools import zip_longest

 _marker = object()

 class UnequalIterablesError(ValueError):
     def __init__(self, details=None):
         msg = 'Iterables have different lengths'
         if details is not None:
             msg += (': index 0 has length {}; index {} has length {}').format(
                 *details
             )

         super().__init__(msg)

 def _zip_equal_generator(iterables):
     for combo in zip_longest(*iterables, fillvalue=_marker):
         for val in combo:
             if val is _marker:
                 raise UnequalIterablesError()
         yield combo

 def _zip_equal(*iterables):
     # Check whether the iterables are all the same size.
     try:
         first_size = len(iterables[0])
         for i, it in enumerate(iterables[1:], 1):
             size = len(it)
             if size != first_size:
                 raise UnequalIterablesError(details=(first_size, i, size))
         # All sizes are equal, we can use the built-in zip.
         return zip(*iterables)
     # If any one of the iterables didn't have a length, start reading
     # them until one runs out.
     except TypeError:
         return _zip_equal_generator(iterables)

 def grouper(iterable, n, incomplete='fill', fillvalue=None):
     args = [iter(iterable)] * n
     if incomplete == 'fill':
         return zip_longest(*args, fillvalue=fillvalue)
     if incomplete == 'strict':
         return _zip_equal(*args)
     if incomplete == 'ignore':
         return zip(*args)
     else:
         raise ValueError('Expected fill, strict, or ignore')

________________________________________________________________________________________________________________________
 more_itertools.partition(pred, iterable) - Возвращает кортеж из двух итераций, полученных из входной итерации.
 Первый дает элементы, у которых pred(item) == False. Второй возвращает элементы, у которых pred(item) == True.

 from more_itertools import partition

 is_odd = lambda x: x % 2 != 0
 iterable = range(10)
 even_items, odd_items = partition(is_odd, iterable)
 list(even_items), list(odd_items)
 # ([0, 2, 4, 6, 8], [1, 3, 5, 7, 9])

 Если pred имеет значение None, bool()используется.

 iterable = [0, 1, False, True, '', ' ']
 false_items, true_items = partition(None, iterable)
 list(false_items), list(true_items)
 # ([0, False, ''], [1, True, ' '])

 Исходник:
 from itertools import tee, compress
 import operator

 def partition(pred, iterable):

     if pred is None:
         pred = bool

     t1, t2, p = tee(iterable, 3)
     p1, p2 = tee(map(pred, p))
     return (compress(t1, map(operator.not_, p1)), compress(t2, p2))

________________________________________________________________________________________________________________________
 more_itertools.transpose(it) - Поменяйте местами строки и столбцы входной матрицы.

 from more_itertools import transpose

 list(transpose([(1, 2, 3), (11, 22, 33)]))       # -> [(1, 11), (2, 22), (3, 33)]
 list(transpose([(1, 2, 3), (11, 22, 33, 200)]))  # -> ValueError: zip() argument 2 is longer than argument 1

 Вызывающая сторона должна убедиться, что размеры входных данных совместимы. Если ввод пуст, вывод не будет произведен.

 Исходник:
 import functools
 try:
     zip(strict=True)
 except TypeError:
     _zip_strict = zip
 else:
     _zip_strict = functools.partial(zip, strict=True)

 def transpose(it):
     return _zip_strict(*it)


________________________________________________________________________________________________________________________
 --- Взгляд вперед и назад    Lookahead and lookback ---

 --- Эти инструменты просматривают значения итерируемого объекта, не изменяя его ---

 --- These tools peek at an iterable’s values without advancing it ---
________________________________________________________________________________________________________________________
 more_itertools.spy(iterable, n=1) - Возвращает кортеж из двух элементов со списком, содержащим первые n элементов
 итерируемого объекта, и итератор с теми же элементами, что и итерируемый объект. Это позволяет вам «заглядывать вперед»
 на элементы итерации, не продвигая ее вперед.

 По умолчанию в списке один элемент:
 from more_itertools import spy

 iterable = 'abcdefg'
 head, iterable = spy(iterable)
 head           # -> ['a']
 list(iterable) # -> ['a', 'b', 'c', 'd', 'e', 'f', 'g']

 Вы можете использовать распаковку для извлечения элементов вместо списков:

 (head,), iterable = spy('abcdefg')
 head   # -> a
 (first, second), iterable = spy('abcdefg', 2)
 first  # -> a
 second # -> b

 Количество запрошенных элементов может быть больше, чем количество элементов в итерации:

 iterable = [1, 2, 3, 4, 5]
 head, iterable = spy(iterable, 10)
 head            # -> [1, 2, 3, 4, 5]
 list(iterable)  # -> [1, 2, 3, 4, 5]

 Исходник:
 from itertools import chain
 from more_itertools import take

 def spy(iterable, n=1):
     it = iter(iterable)
     head = take(n, it)

     return head.copy(), chain(head, it)

________________________________________________________________________________________________________________________
 class more_itertools.peekable(iterable) - Оберните итератор, чтобы разрешить просмотр вперед и добавление элементов.

 Вызовите peek() результат, чтобы получить значение, которое будет возвращено next(). Это не будет продвигать итератор:

 from more_itertools import peekable

 p = peekable(['a', 'b'])
 p.peek()  # -> a
 next(p)   # -> a

 Передайте peek()значение по умолчанию, чтобы вернуть его вместо повышения, StopIterationкогда итератор исчерпан.

 p = peekable([])
 p.peek('hi')   # -> hi

 peekables также предлагает prepend() метод, который «вставляет» элементы в начало итерации:

 p = peekable([1, 2, 3])
 p.prepend(10, 11, 12)
 next(p) # -> 10
 p.peek() # -> 11
 list(p) # -> [11, 12, 1, 2, 3]

 Peekables можно индексировать. Индекс 0 — это элемент, который будет возвращен next(), индекс 1 — это элемент после
 него и т. д. Значения до данного индекса будут кэшироваться.


 p = peekable(['a', 'b', 'c', 'd'])
 p[0]    # -> a
 p[1]    # -> b
 next(p) # -> a

 Отрицательные индексы поддерживаются, но имейте в виду, что они будут кэшировать оставшиеся элементы в исходном
 итераторе, что может потребовать значительного объема памяти.

 Чтобы проверить, исчерпан ли просмотренный объект, проверьте его истинное значение:

 p = peekable(['a', 'b'])
 if p:  # peekable has items
     list(p)   # -> ['a', 'b']

 if not p:  # peekable is exhausted
     list(p)   # -> []

 Исходник Очень не Очень слабый:
 from collections import deque
 from itertools import islice

 _marker = object()

 class peekable:

     def __init__(self, iterable):
         self._it = iter(iterable)
         self._cache = deque()

     def __iter__(self):
         return self

     def __bool__(self):
         try:
             self.peek()
         except StopIteration:
             return False
         return True

     def peek(self, default=_marker):
         if not self._cache:
             try:
                 self._cache.append(next(self._it))
             except StopIteration:
                 if default is _marker:
                     raise
                 return default
         return self._cache[0]

     def prepend(self, *items):
         self._cache.extendleft(reversed(items))

     def __next__(self):
         if self._cache:
             return self._cache.popleft()

         return next(self._it)

     def _get_slice(self, index):
         # Normalize the slice's arguments
         step = 1 if (index.step is None) else index.step
         if step > 0:
             start = 0 if (index.start is None) else index.start
             stop = maxsize if (index.stop is None) else index.stop
         elif step < 0:
             start = -1 if (index.start is None) else index.start
             stop = (-maxsize - 1) if (index.stop is None) else index.stop
         else:
             raise ValueError('slice step cannot be zero')

         # If either the start or stop index is negative, we'll need to cache
         # the rest of the iterable in order to slice from the right side.
         if (start < 0) or (stop < 0):
             self._cache.extend(self._it)
         # Otherwise we'll need to find the rightmost index and cache to that
         # point.
         else:
             n = min(max(start, stop) + 1, maxsize)
             cache_len = len(self._cache)
             if n >= cache_len:
                 self._cache.extend(islice(self._it, n - cache_len))

         return list(self._cache)[index]

     def __getitem__(self, index):
         if isinstance(index, slice):
             return self._get_slice(index)

         cache_len = len(self._cache)
         if index < 0:
             self._cache.extend(self._it)
         elif index >= cache_len:
             self._cache.extend(islice(self._it, index + 1 - cache_len))

         return self._cache[index]

________________________________________________________________________________________________________________________
 class more_itertools.seekable(iterable, maxlen=None) - Оберните итератор, чтобы обеспечить поиск вперед и назад.
 Это постепенно кэширует элементы в исходной итерации, чтобы их можно было повторно посетить.

 Вызов seek() с индексом для поиска этой позиции в итерируемом источнике. Чтобы «сбросить» итератор, выполните 0:

 from more_itertools import seekable

 from itertools import count
 it = seekable((str(n) for n in count()))
 next(it), next(it), next(it)  # ->  ('0', '1', '2')
 it.seek(0)
 next(it), next(it), next(it)  # ->  ('0', '1', '2')
 next(it)  # -> '3'

 Вы также можете искать вперед:

 it = seekable((str(n) for n in range(20)))
 it.seek(10)
 next(it)  # -> '10'
 it.relative_seek(-2)  # Seeking relative to the current position
 next(it)  # -> '9'
 it.seek(20)  # Seeking past the end of the source isn't a problem
 list(it)  # -> []
 it.seek(0)  # Resetting works even after hitting the end
 next(it), next(it), next(it)  # -> ('0', '1', '2')

 Вызов peek()для просмотра на один элемент вперед без перемещения итератора:

 it = seekable('1234')
 it.peek()  # -> '1'
 list(it)  # -> ['1', '2', '3', '4']
 it.peek(default='empty')  # -> 'empty'

 Прежде чем итератор достигнет своего конца, вызов bool() его вернет True. После того, как он вернется False:

 it = seekable('5678')
 bool(it)  # -> True
 list(it)  # -> ['5', '6', '7', '8']
 bool(it)  # -> False

 Вы можете просмотреть содержимое кэша с помощью этого elements() метода. Это возвращает SequenceView представление,
 которое обновляется автоматически:

 it = seekable((str(n) for n in range(10)))
 next(it), next(it), next(it) # -> ('0', '1', '2')
 elements = it.elements()
 elements # -> SequenceView(['0', '1', '2'])
 next(it) # -> '3'
 elements # -> SequenceView(['0', '1', '2', '3'])

 По умолчанию кэш увеличивается по мере выполнения исходной итерации, поэтому остерегайтесь переноса очень больших
 или бесконечных итераций. Укажите maxlen , чтобы ограничить размер кеша (это, конечно, ограничивает глубину поиска).

 from itertools import count
 it = seekable((str(n) for n in count()), maxlen=2)
 next(it), next(it), next(it), next(it)  # -> ('0', '1', '2', '3')
 list(it.elements())                     # -> ['2', '3']
 it.seek(0)
 next(it), next(it), next(it), next(it)  # ->('2', '3', '4', '5')
 next(it)                                # -> '6'

 Исходник Очень не не слабый:
 from more_itertools import SequenceView, consume
 from collections import deque

 class seekable:
     def __init__(self, iterable, maxlen=None):
         self._source = iter(iterable)
         if maxlen is None:
             self._cache = []
         else:
             self._cache = deque([], maxlen)
         self._index = None

     def __iter__(self):
         return self

     def __next__(self):
         if self._index is not None:
             try:
                 item = self._cache[self._index]
             except IndexError:
                 self._index = None
             else:
                 self._index += 1
                 return item

         item = next(self._source)
         self._cache.append(item)
         return item

     def __bool__(self):
         try:
             self.peek()
         except StopIteration:
             return False
         return True

     def peek(self, default=_marker):
         try:
             peeked = next(self)
         except StopIteration:
             if default is _marker:
                 raise
             return default
         if self._index is None:
             self._index = len(self._cache)
         self._index -= 1
         return peeked

     def elements(self):
         return SequenceView(self._cache)

     def seek(self, index):
         self._index = index
         remainder = index - len(self._cache)
         if remainder > 0:
             consume(self, remainder)

     def relative_seek(self, count):
         index = len(self._cache)
         self.seek(max(index + count, 0))


________________________________________________________________________________________________________________________
 --- Окно    Windowing ---

 --- Эти инструменты создают окна элементов из итерации ---

 --- These tools yield windows of items from an iterable ---
________________________________________________________________________________________________________________________
 more_itertools.windowed(seq, n, fillvalue=None, step=1) - Возвращает скользящее окно ширины n по заданной итерации.

 from more_itertools import windowed

 all_windows = windowed([1, 2, 3, 4, 5], 3)
 list(all_windows)  # -> [(1, 2, 3), (2, 3, 4), (3, 4, 5)]

 Когда окно больше итерируемого, вместо отсутствующих значений используется значение fillvalue :

 list(windowed([1, 2, 3], 4))  # -> [(1, 2, 3, None)]

 Каждое окно будет продвигаться с шагом :

 list(windowed([1, 2, 3, 4, 5, 6], 3, fillvalue='!', step=2))  # -> [(1, 2, 3), (3, 4, 5), (5, 6, '!')]

 Чтобы перейти к элементам итерации, используйте chain()для добавления элементов-заполнителей слева:

 iterable = [1, 2, 3, 4]
 n = 3
 padding = [None] * (n - 1)
 list(windowed(chain(padding, iterable), 3))  # ->  [(None, None, 1), (None, 1, 2), (1, 2, 3), (2, 3, 4)]

 Исходник:
 from itertools import chain, repeat
 from collections import deque

 def windowed(seq, n, fillvalue=None, step=1):

     if n < 0:
         raise ValueError('n must be >= 0')
     if n == 0:
         yield tuple()
         return
     if step < 1:
         raise ValueError('step must be >= 1')

     window = deque(maxlen=n)
     i = n
     for _ in map(window.append, seq):
         i -= 1
         if not i:
             i = step
             yield tuple(window)

     size = len(window)
     if size == 0:
         return
     elif size < n:
         yield tuple(chain(window, repeat(fillvalue, n - size)))
     elif 0 < i < min(step, n):
         window += (fillvalue,) * i
         yield tuple(window)

________________________________________________________________________________________________________________________
 more_itertools.substrings(iterable) - Выдать все подстроки iterable .

 from more_itertools import substrings

 [''.join(s) for s in substrings('more')]  # -> ['m', 'o', 'r', 'e', 'mo', 'or', 're', 'mor', 'ore', 'more']

 Обратите внимание, что нестроковые итерации также могут быть подразделены.
 list(substrings([0, 1, 2]))  # -> [(0,), (1,), (2,), (0, 1), (1, 2), (0, 1, 2)]

 Исходник:
 def substrings(iterable):
     # The length-1 substrings
     seq = []
     for item in iter(iterable):
         seq.append(item)
         yield (item,)
     seq = tuple(seq)
     item_count = len(seq)

     # And the rest
     for n in range(2, item_count + 1):
         for i in range(item_count - n + 1):
             yield seq[i : i + n]

________________________________________________________________________________________________________________________
 more_itertools.substrings_indexes(seq, reverse=False) - Выдать все подстроки и их позиции в последовательности
 Полученные элементы будут кортежем вида , где .(substr, i, j)substr == seq[i:j]

 Эта функция работает только для итераций, поддерживающих нарезку, например str объектов.
 Установите параметр «reverse» , чтобы Trueполучить те же элементы в противоположном порядке.

 from more_itertools import substrings_indexes

 for item in substrings_indexes('ab'):     for item in substrings_indexes('ab', reverse=True):
     print(item )                              print(item )
 # ('a', 0, 1)                             # ('ab', 0, 2)
 # ('b', 1, 2)                             # ('a', 0, 1)
 # ('ab', 0, 2)                            # ('b', 1, 2)

 Исходник:
 def substrings_indexes(seq, reverse=False):
     r = range(1, len(seq) + 1)
     if reverse:
         r = reversed(r)
     return (
         (seq[i : i + L], i, i + L) for L in r for i in range(len(seq) - L + 1)
     )
________________________________________________________________________________________________________________________
 more_itertools.stagger(iterable, offsets=(-1, 0, 1), longest=False, fillvalue=None) - Получите кортежи, элементы
 которых смещены от iterable. Сумма, на которую смещается i-й элемент в каждом кортеже, определяется i-м элементом в offsets .

 from more_itertools import stagger

 list(stagger([0, 1, 2, 3]))  # ->  [(None, 0, 1), (0, 1, 2), (1, 2, 3)]
 list(stagger(range(8), offsets=(0, 2, 4)))  # -> [(0, 2, 4), (1, 3, 5), (2, 4, 6), (3, 5, 7)]

 По умолчанию последовательность закончится, когда последний элемент кортежа станет последним элементом итерации. Чтобы
 продолжать до тех пор, пока первый элемент кортежа не станет последним элементом в итерации, установите longest равным True:

 list(stagger([0, 1, 2, 3], longest=True))  # -> [(None, 0, 1), (0, 1, 2), (1, 2, 3), (2, 3, None), (3, None, None)]
 list(stagger([0, 1, 2], longest=True, fillvalue='A'))  # -> [('A', 0, 1), (0, 1, 2), (1, 2, 'A'), (2, 'A', 'A')]

 Исходник:
 from more_itertools import stagger, zip_offset
 from itertools import tee

 def stagger(iterable, offsets=(-1, 0, 1), longest=False, fillvalue=None):
     children = tee(iterable, len(offsets))

     return zip_offset(
         *children, offsets=offsets, longest=longest, fillvalue=fillvalue
     )

________________________________________________________________________________________________________________________
 more_itertools.windowed_complete(iterable, n) - Yield (beginning, middle, end) tuples where:
 Выходные кортежи (начало, середина, конец), где:
 - Каждый middle имеет n элементов из итерируемого
 - У каждого beginning есть предметы, предшествующие тем, что в middle
 - В каждом end есть предметы после тех, что в middle

 Обратите внимание, что n должно быть не менее 0 и максимально равно длине итерируемого объекта .
 Эта функция исчерпает итерируемый объект и может потребовать значительного объема памяти.

 from more_itertools import windowed_complete

 iterable = range(7)
 n = 3
 for beginning, middle, end in windowed_complete(iterable, n):
     print(beginning, middle, end)

 # () (0, 1, 2) (3, 4, 5, 6)
 # (0,) (1, 2, 3) (4, 5, 6)
 # (0, 1) (2, 3, 4) (5, 6)
 # (0, 1, 2) (3, 4, 5) (6,)
 # (0, 1, 2, 3) (4, 5, 6) ()

 Исходник:
 def windowed_complete(iterable, n):
     if n < 0:
         raise ValueError('n must be >= 0')

     seq = tuple(iterable)
     size = len(seq)

     if n > size:
         raise ValueError('n must be <= len(seq)')

     for i in range(size - n + 1):
         beginning = seq[:i]
         middle = seq[i : i + n]
         end = seq[i + n :]
         yield beginning, middle, end

________________________________________________________________________________________________________________________
 Itertools recipes
 more_itertools.pairwise(iterable) - Возвращает итератор парных элементов, перекрывающихся из оригинала

 В Python 3.10 и более поздних версиях это псевдоним для itertools.pairwise().

 from more_itertools import pairwise, take

 take(4, pairwise(count())) # -> [(0, 1), (1, 2), (2, 3), (3, 4)]

 Исходник:
 from itertools import tee

 def _pairwise(iterable):
     a, b = tee(iterable)
     next(b, None)
     return zip(a, b)

 try:
     from itertools import pairwise as itertools_pairwise
 except ImportError:
     pairwise = _pairwise
 else:
     def pairwise(iterable):
         return itertools_pairwise(iterable)
     pairwise.__doc__ = _pairwise.__doc__

________________________________________________________________________________________________________________________
 more_itertools.triplewise(iterable) - Возвращает перекрывающиеся тройки из iterable

 from more_itertools import triplewise

 list(triplewise('ABCDE'))           # ->  [('A', 'B', 'C'), ('B', 'C', 'D'), ('C', 'D', 'E')]
 list(triplewise([1, 2, 3, 4, 5]))   # ->  [(1, 2, 3), (2, 3, 4), (3, 4, 5)]

 Исходник:
 from itertools import pairwise

 def triplewise(iterable):
     for (a, _), (b, c) in pairwise(pairwise(iterable)):
         yield a, b, c

________________________________________________________________________________________________________________________
 more_itertools.sliding_window(iterable, n) - Возвращает скользящее окно ширины n над iterable .

from more_itertools import sliding_window

 list(sliding_window(range(6), 4))      # -> [(0, 1, 2, 3), (1, 2, 3, 4), (2, 3, 4, 5)]
 list(sliding_window([1, 2, 3, 4], 2))  # -> [(1, 2), (2, 3), (3, 4)]

 Если в iterable меньше n элементов, ничего не выдается:

 list(sliding_window(range(3), 4)) # -> []

 Исходник:
 from collections import deque
 from itertools import islice

 def sliding_window(iterable, n):
     it = iter(iterable)
     window = deque(islice(it, n - 1), maxlen=n)
     for x in it:
         window.append(x)
         yield tuple(window)

________________________________________________________________________________________________________________________
 more_itertools.subslices(iterable) - Вернуть все смежные непустые фрагменты iterable .
 Это похоже на substrings(), но выдает элементы в другом порядке.

 from more_itertools import subslices

 list(subslices('ABC'))      # -> [['A'], ['A', 'B'], ['A', 'B', 'C'], ['B'], ['B', 'C'], ['C']]
 list(subslices([1, 2, 3]))  # -> [[1], [1, 2], [1, 2, 3], [2], [2, 3], [3]]

 Исходник:
 from itertools import starmap, combinations, repeat
 import operator

 def subslices(iterable):
     seq = list(iterable)
     slices = starmap(slice, combinations(range(len(seq) + 1), 2))
     return map(operator.getitem, repeat(seq), slices)


________________________________________________________________________________________________________________________
 --- Увеличение    Augmenting ---

 --- Эти инструменты позволяют получить элементы из итерации, а также дополнительные данные ---

 --- These tools yield items from an iterable, plus additional data ---
________________________________________________________________________________________________________________________
 more_itertools.count_cycle(iterable, n=None) -  Перебирайте элементы от итерации до n раз, получая количество
 завершенных циклов вместе с каждым элементом. Если n опущено, процесс повторяется БЕСКОНЕЧНО.   <-----

 from more_itertools import count_cycle

 list(count_cycle('AB', 3))  # -> [(0, 'A'), (0, 'B'), (1, 'A'), (1, 'B'), (2, 'A'), (2, 'B')]
 list(count_cycle('A', 5))   # -> [(0, 'A'), (1, 'A'), (2, 'A'), (3, 'A'), (4, 'A')]

 Исходник:
 from itertools import count

 def count_cycle(iterable, n=None):
     iterable = tuple(iterable)
     if not iterable:
         return iter(())
     counter = count() if n is None else range(n)
     return ((i, item) for i in counter for item in iterable)

________________________________________________________________________________________________________________________
 more_itertools.intersperse(e, iterable, n=1) - Вставьте элемент-заполнитель e среди элементов в iterable ,
 оставляя n элементов между каждым элементом-заполнителем.

 from more_itertools import intersperse

 list(intersperse('!', [1, 2, 3, 4, 5]))     # -> [1, '!', 2, '!', 3, '!', 4, '!', 5]
 list(intersperse('COOL', [1, 2, 3, 4, 5]))  # -> [1, 'COOL', 2, 'COOL', 3, 'COOL', 4, 'COOL', 5]

 list(intersperse(None, [1, 2, 3, 4, 5], n=2))  # -> [1, 2, None, 3, 4, None, 5]
 list(intersperse(None, [1, 2, 3, 4, 5], n=3))  # -> [1, 2, 3, None, 4, 5]

 Исходник:
 from more_itertools import interleave, chunked, flatten
 from itertools import islice, repeat

 def intersperse(e, iterable, n=1):
     if n == 0:
         raise ValueError('n must be > 0')
     elif n == 1:
         # interleave(repeat(e), iterable) -> e, x_0, e, x_1, e, x_2...
         # islice(..., 1, None) -> x_0, e, x_1, e, x_2...
         return islice(interleave(repeat(e), iterable), 1, None)
     else:
         # interleave(filler, chunks) -> [e], [x_0, x_1], [e], [x_2, x_3]...
         # islice(..., 1, None) -> [x_0, x_1], [e], [x_2, x_3]...
         # flatten(...) -> x_0, x_1, e, x_2, x_3...
         filler = repeat([e])
         chunks = chunked(iterable, n)
         return flatten(islice(interleave(filler, chunks), 1, None))

________________________________________________________________________________________________________________________
 more_itertools.padded(iterable, fillvalue=None, n=None, next_multiple=False) - Выдайте элементы из iterable ,
 за которыми следует fillvalue , так, чтобы было выдано как минимум n элементов.

 from more_itertools import padded

 list(padded([1, 2, 3], "?", 5))     # ->[1, 2, 3, '?', '?']
 list(padded([1, 2, 3], "COOL", 7))  # -> [1, 2, 3, 'COOL', 'COOL', 'COOL', 'COOL']

 Если next_multiple равен True, fillvalue будет генерироваться до тех пор,
 пока количество созданных элементов не станет кратным n:

 list(padded([1, 2, 3, 4], n=3, next_multiple=True)))  # -> [1, 2, 3, 4, None, None]

 Исходник:
 from itertools import chain, repeat

 def padded(iterable, fillvalue=None, n=None, next_multiple=False):
     it = iter(iterable)
     if n is None:
         yield from chain(it, repeat(fillvalue))
     elif n < 1:
         raise ValueError('n must be at least 1')
     else:
         item_count = 0
         for item in it:
             yield item
             item_count += 1

         remaining = (n - item_count) % n if next_multiple else n - item_count
         for _ in range(remaining):
             yield fillvalue

________________________________________________________________________________________________________________________
 more_itertools.mark_ends(iterable) - Получите 3-кортежи вида .(is_first, is_last, item)

 from more_itertools import mark_ends

 list(mark_ends('ABC'))  # -> [(True, False, 'A'), (False, False, 'B'), (False, True, 'C')]

 Используйте это при циклическом переборе итерации, чтобы выполнить специальное действие
 над ее первым и/или последним элементом:

 iterable = ['Header', 100, 200, 'Footer']
 total = 0
 for is_first, is_last, item in mark_ends(iterable):
     if is_first:
         continue  # Skip the header
     if is_last:
         continue  # Skip the footer
     total += item
 print(total)  # -> 300

 Исходник:
 from itertools import count

 def mark_ends(iterable):
     it = iter(iterable)

     try:
         b = next(it)
     except StopIteration:
         return

     try:
         for i in count():
             a = b
             b = next(it)
             yield i == 0, False, a

     except StopIteration:
         yield i == 0, True, a

________________________________________________________________________________________________________________________
 more_itertools.repeat_each(iterable, n=2) - Повторите каждый элемент в итерации n раз.

 from more_itertools import repeat_each

 list(repeat_each('ABC', 3))  # -> ['A', 'A', 'A', 'B', 'B', 'B', 'C', 'C', 'C']
 list(repeat_each('ABC', 2))  # -> ['A', 'A', 'B', 'B', 'C', 'C']

 Исходник:
 from itertools import chain, repeat

 def repeat_each(iterable, n=2):
     return chain.from_iterable(map(repeat, iterable, repeat(n)))

________________________________________________________________________________________________________________________
 more_itertools.adjacent(predicate, iterable, distance=1) - Возвращает итерируемый кортеж (bool, item) , в котором
 элемент извлекается из итерируемого объекта , а логическое значение указывает, удовлетворяет ли этот элемент предикату
 или является смежным с элементом, который удовлетворяет этому требованию.

 Например, чтобы узнать, соседствуют ли элементы с 3:

 from more_itertools import adjacent

 list(adjacent(lambda x: x == 3, range(6)))  # -> [(False, 0), (False, 1), (True, 2), (True, 3), (True, 4), (False, 5)]

 Установите расстояние , чтобы изменить то, что считается соседним. Например, чтобы узнать, находятся ли элементы
 в двух местах от 3:

 list(adjacent(lambda x: x == 3, range(6), distance=2))
 # [(False, 0), (True, 1), (True, 2), (True, 3), (True, 4), (True, 5)]

 Это полезно для контекстуализации результатов функции поиска. Например, инструмент сравнения кода может захотеть
 идентифицировать строки, которые были изменены, а также окружающие строки, чтобы предоставить зрителю контекст различий.

 Функция предиката будет вызываться только один раз для каждого элемента итерации.

 См. также раздел groupby_transform(), который можно использовать с этой функцией для группировки диапазонов элементов
 с одинаковым логическим значением.

 Исходник:
 from more_itertools import windowed
 from itertools import tee, chain

 def adjacent(predicate, iterable, distance=1):
     # Allow distance=0 mainly for testing that it reproduces results with map()
     if distance < 0:
         raise ValueError('distance must be at least 0')

     i1, i2 = tee(iterable)
     padding = [False] * distance
     selected = chain(padding, map(predicate, i1), padding)
     adjacent_to_selected = map(any, windowed(selected, 2 * distance + 1))
     return zip(adjacent_to_selected, i2)

________________________________________________________________________________________________________________________
 more_itertools.groupby_transform(iterable, keyfunc=None, valuefunc=None, reducefunc=None)
 Расширение этого itertools.groupby() метода позволяет применять преобразования к сгруппированным данным.

 keyfunc    — это функция, вычисляющая значение ключа для каждого элемента в итерации.
 valuefunc  — это функция, которая преобразует отдельные элементы из итерируемых после группировки.
 reducefunc — это функция, которая преобразует каждую группу элементов.

 from more_itertools import groupby_transform

 iterable = 'aAAbBBcCC'
 keyfunc = lambda k: k.upper()
 valuefunc = lambda v: v.lower()
 reducefunc = lambda g: ''.join(g)
 list(groupby_transform(iterable, keyfunc, valuefunc, reducefunc))  # -> [('A', 'aaa'), ('B', 'bbb'), ('C', 'ccc')]

 Каждый необязательный аргумент по умолчанию имеет функцию идентификации, если она не указана.

 groupby_transform()полезно при группировке элементов итерации с использованием отдельной итерации в качестве ключа.
 Для этого zip() необходимо выполнить итерацию и передать функцию keyfunc , которая извлекает первый элемент,
 и функцию valuefunc , которая извлекает второй элемент:

 from operator import itemgetter
 keys = [0, 0, 1, 1, 1, 2, 2, 2, 3]
 values = 'abcdefghi'
 iterable = zip(keys, values)
 grouper = groupby_transform(iterable, itemgetter(0), itemgetter(1))
 [(k, ''.join(g)) for k, g in grouper]  # -> [(0, 'ab'), (1, 'cde'), (2, 'fgh'), (3, 'i')]

 Исходник:
 from itertools import groupby

 def groupby_transform(iterable, keyfunc=None, valuefunc=None, reducefunc=None):
     ret = groupby(iterable, keyfunc)
     if valuefunc:
         ret = ((k, map(valuefunc, g)) for k, g in ret)
     if reducefunc:
         ret = ((k, reducefunc(g)) for k, g in ret)

     return ret
________________________________________________________________________________________________________________________
 more_itertools.pad_none(iterable) - Возвращает последовательность элементов, а затем возвращает None неопределенное время.

 from more_itertools import pad_none

 take(5, pad_none(range(3)))  # -> [0, 1, 2, None, None]

 Полезно для эмуляции поведения встроенной map() функции. Смотрите также padded().

 Исходник:
 from itertools import chain, repeat

 def pad_none(iterable):
     return chain(iterable, repeat(None))

________________________________________________________________________________________________________________________
 more_itertools.ncycles(iterable, n) - Возвращает элементы последовательности n раз

 from more_itertools import ncycles

 list(ncycles(["a", "b"], 3))  # -> ['a', 'b', 'a', 'b', 'a', 'b']

 Исходник:
 from itertools import chain, repeat

 def ncycles(iterable, n):
     return chain.from_iterable(repeat(tuple(iterable), n))


________________________________________________________________________________________________________________________
 --- Объединение    Combining ---

 --- Эти инструменты объединяют несколько итераций ---

--- These tools combine multiple iterables ---
________________________________________________________________________________________________________________________
 more_itertools.collapse(iterable, base_type=None, levels=None) - Сгладить итерируемый объект с несколькими уровнями
 вложенности (например, список списков кортежей) в неитерируемые типы.

 from more_itertools import collapse

 iterable = [(1, 2), ([3, 4], [[5], [6]])]
 list(collapse(iterable))  # -> [1, 2, 3, 4, 5, 6]

 Двоичные и текстовые строки не считаются повторяемыми и не будут свернуты.
 Чтобы избежать свертывания других типов, укажите base_type :

 iterable = ['ab', ('cd', 'ef'), ['gh', 'ij']]
 list(collapse(iterable, base_type=tuple))  # -> ['ab', ('cd', 'ef'), 'gh', 'ij']

 Укажите уровни , чтобы прекратить сглаживание после определенного уровня:

 terable = [('a', ['b']), ('c', ['d'])]
 list(collapse(iterable))  # Fully flattened
 # ['a', 'b', 'c', 'd']
 list(collapse(iterable, levels=1))  # Only one level flattened
 # ['a', ['b'], 'c', ['d']]

 Хорошее сравнение:
 from more_itertools import collapse
 from itertools import chain

 iterable = [(1, 2), [3, 4], {5, 6}, {"A": 10}]
 list(collapse(iterable))                  # -> [1, 2, 3, 4, 5, 6, 'A']  Всё распаковало в один
 list(collapse(iterable, base_type=set))   # -> [1, 2, 3, 4, {5, 6}, 'A']
 list(collapse(iterable, base_type=dict))  # -> [1, 2, 3, 4, 5, 6, {'A': 10}]
 # Список не распаковывает
 list(collapse(iterable, base_type=list))         # -> [[(1, 2), [3, 4], {5, 6}, {'A': 10}]]
 list(collapse(tuple(iterable), base_type=list))  # -> [1, 2, [3, 4], 5, 6, 'A']  Нужно сделать из него tuple
 # И Сравнение с chain.from_iterable
 iterable = [(1, 2), ([3, 4], [[5], [6]])]
 list(chain.from_iterable(iterable))  # -> [1, 2, [3, 4], [[5], [6]]]  Только один уровень вложенности
 list(collapse(iterable, levels=1))   # -> [1, 2, [3, 4], [[5], [6]]]  Можно выбрать level=1

 Исходник:
 def collapse(iterable, base_type=None, levels=None):

     def walk(node, level):
         if (
             ((levels is not None) and (level > levels))
             or isinstance(node, (str, bytes))
             or ((base_type is not None) and isinstance(node, base_type))
         ):
             yield node
             return

         try:
             tree = iter(node)
         except TypeError:
             yield node
             return
         else:
             for child in tree:
                 yield from walk(child, level + 1)

     yield from walk(iterable, 0)

________________________________________________________________________________________________________________________
 more_itertools.interleave(*iterables) - Возвращает новую итерацию, получая по очереди каждую итерацию,
 пока самая короткая не будет исчерпана.
 О версии, которая не завершается после того, как исчерпана самая короткая итерация, см interleave_longest()

 from more_itertools import interleave

 list(interleave([1, 2, 3], [4, 5], [6, 7, 8]))  # -> [1, 4, 6, 2, 5, 7]
 list(interleave([1, 2], [4], [6, 7, 8]))        # -> [1, 4, 6]   Поочередно берет из каждой последовательности

 Исходник:
 from itertools import chain

 def interleave(*iterables):
     return chain.from_iterable(zip(*iterables))

________________________________________________________________________________________________________________________
 more_itertools.interleave_longest(*iterables) - Возвращает новую итерацию, получая по очереди каждую итерацию,
 пропуская все, что исчерпано. Эта функция выдает тот же результат, что и roundrobin(), но может работать лучше для
 некоторых входных данных (в частности, когда количество итераций велико).

 from more_itertools import interleave_longest

 list(interleave_longest([1, 2, 3], [4, 5], [6, 7, 8]))  # -> [1, 4, 6, 2, 5, 7, 3, 8]

 Исходник:
 from itertools import zip_longest, chain

 _marker = object()

 def interleave_longest(*iterables):
     i = chain.from_iterable(zip_longest(*iterables, fillvalue=_marker))
     return (x for x in i if x is not _marker)

________________________________________________________________________________________________________________________
 more_itertools.interleave_evenly(iterables, lengths=None) Чередуйте несколько итераций, чтобы их элементы были
 равномерно распределены по выходной последовательности.  На основе алгоритма Брезенхема.

 from more_itertools import interleave_evenly

 iterables = [1, 2, 3, 4, 5], ['a', 'b']
 list(interleave_evenly(iterables))  # -> [1, 2, 'a', 3, 4, 'b', 5]

 iterables = [[1, 2, 3], [4, 5], [6, 7, 8]]
 list(interleave_evenly(iterables))  # -> [1, 6, 4, 2, 7, 3, 8, 5]

 Эта функция требует итераций известной длины. Итерации без __len__() можно использовать,
 указав длину вручную с помощью lengths :

 from itertools import combinations, repeat
 iterables = [combinations(range(4), 2), ['a', 'b', 'c']]
 lengths = [4 * (4 - 1) // 2, 3]
 list(interleave_evenly(iterables, lengths=lengths)) # -> [(0, 1), (0, 2), 'a', (0, 3), (1, 2), 'b', (1, 3), (2, 3), 'c']

 Исходник:
 def interleave_evenly(iterables, lengths=None):
     if lengths is None:
         try:
             lengths = [len(it) for it in iterables]
         except TypeError:
             raise ValueError(
                 'Iterable lengths could not be determined automatically. '
                 'Specify them with the lengths keyword.'
             )
     elif len(iterables) != len(lengths):
         raise ValueError('Mismatching number of iterables and lengths.')

     dims = len(lengths)

     # sort iterables by length, descending
     lengths_permute = sorted(
         range(dims), key=lambda i: lengths[i], reverse=True
     )
     lengths_desc = [lengths[i] for i in lengths_permute]
     iters_desc = [iter(iterables[i]) for i in lengths_permute]

     # the longest iterable is the primary one (Bresenham: the longest
     # distance along an axis)
     delta_primary, deltas_secondary = lengths_desc[0], lengths_desc[1:]
     iter_primary, iters_secondary = iters_desc[0], iters_desc[1:]
     errors = [delta_primary // dims] * len(deltas_secondary)

     to_yield = sum(lengths)
     while to_yield:
         yield next(iter_primary)
         to_yield -= 1
         # update errors for each secondary iterable
         errors = [e - delta for e, delta in zip(errors, deltas_secondary)]

         # those iterables for which the error is negative are yielded
         # ("diagonal step" in Bresenham)
         for i, e in enumerate(errors):
             if e < 0:
                 yield next(iters_secondary[i])
                 to_yield -= 1
                 errors[i] += delta_primary

________________________________________________________________________________________________________________________
 more_itertools.partial_product(*iterables) - Создает кортежи, содержащие по одному элементу от каждого итератора,
 причем последующие кортежи изменяют по одному элементу за раз, продвигая каждый итератор до тех пор, пока он не будет
 исчерпан. Эта последовательность гарантирует, что каждое значение в каждой итерации выводится хотя бы один раз без
 создания всех возможных комбинаций.
 Это может быть полезно, например, при тестировании дорогостоящей функции.

 from more_itertools import partial_product

 list(partial_product('AB', 'C', 'DEF'))  # -> [('A', 'C', 'D'), ('B', 'C', 'D'), ('B', 'C', 'E'), ('B', 'C', 'F')]

 Исходник:
 def partial_product(*iterables):
     iterators = list(map(iter, iterables))

     try:
         prod = [next(it) for it in iterators]
     except StopIteration:
         return
     yield tuple(prod)

     for i, it in enumerate(iterators):
         for prod[i] in it:
             yield tuple(prod)

________________________________________________________________________________________________________________________
 more_itertools.sort_together(iterables, key_list=(0,), key=None, reverse=False) - Возвращает входные итерации,
 отсортированные вместе, с key_list в качестве приоритета сортировки. Все итерации обрезаются до длины самого короткого.

 Это можно использовать как функцию сортировки в электронной таблице. Если каждая итерация представляет столбец данных,
 список ключей определяет, какие столбцы используются для сортировки.
 По умолчанию все итерации сортируются с использованием 0-th итерации:

 from more_itertools import sort_together

 iterables = [(4, 3, 2, 1), ('a', 'b', 'c', 'd')]
 sort_together(iterables) # -> [(1, 2, 3, 4), ('d', 'c', 'b', 'a')]

 Установите другой список ключей для сортировки по другой итерации. Указание нескольких ключей определяет,
 как разрываются связи:

 iterables = [(3, 1, 2), (0, 1, 0), ('c', 'b', 'a')]
 sort_together(iterables, key_list=(1, 2))  # -> [(2, 3, 1), (0, 0, 1), ('a', 'c', 'b')]

 Чтобы отсортировать элементы итерируемого объекта по функции, передайте ключевую функцию.
 Его аргументами являются элементы итераций, соответствующие списку ключей:

 names = ('a', 'b', 'c')
 lengths = (1, 2, 3)
 widths = (5, 2, 1)
 def area(length, width):
     return length * width
 sort_together([names, lengths, widths], key_list=(1, 2), key=area)  # -> [('c', 'b', 'a'), (3, 2, 1), (1, 2, 5)]

 Установите reverse=True сортировки в порядке убывания.

 sort_together([(1, 2, 3), ('c', 'b', 'a')], reverse=True)  # -> [(3, 2, 1), ('a', 'b', 'c')]

 Исходник:
 from operator import itemgetter

 def sort_together(iterables, key_list=(0,), key=None, reverse=False):
     if key is None:
         # if there is no key function, the key argument to sorted is an
         # itemgetter
         key_argument = itemgetter(*key_list)
     else:
         # if there is a key function, call it with the items at the offsets
         # specified by the key function as arguments
         key_list = list(key_list)
         if len(key_list) == 1:
             # if key_list contains a single item, pass the item at that offset
             # as the only argument to the key function
             key_offset = key_list[0]
             key_argument = lambda zipped_items: key(zipped_items[key_offset])
         else:
             # if key_list contains multiple items, use itemgetter to return a
             # tuple of items, which we pass as *args to the key function
             get_key_items = itemgetter(*key_list)
             key_argument = lambda zipped_items: key(
                 *get_key_items(zipped_items)
             )

     return list(
         zip(*sorted(zip(*iterables), key=key_argument, reverse=reverse))
     )

________________________________________________________________________________________________________________________
 more_itertools.value_chain(*args) - Выдать все аргументы, переданные функции, в том же порядке, в котором они были
 переданы. Если аргумент сам по себе является итеративным, перебирайте его значения.
 Несколько уровней вложенности не выравниваются.

 from more_itertools import value_chain

 list(value_chain(1, 2, 3, [4, 5, 6]))     # -> [1, 2, 3, 4, 5, 6]
 list(value_chain(1, 2, 3, [[4, 5, 6]]))   # -> [1, 2, 3, [4, 5, 6]]

 Двоичные и текстовые строки не считаются итерируемыми и создаются как есть:

 list(value_chain(b'12', '34', ['56', '78']))  # -> [b'12', '34', '56', '78']

 Исходник:
 def value_chain(*args):
     for value in args:
         if isinstance(value, (str, bytes)):
             yield value
             continue
         try:
             yield from value
         except TypeError:
             yield value

________________________________________________________________________________________________________________________
 more_itertools.zip_offset(*iterables, offsets, longest=False, fillvalue=None)
 zipвходные итерации повторяются вместе, но смещают i -ю итерацию на i -й элемент в offsets .

 from more_itertools import zip_offset

 list(zip_offset('0123', 'abcdef', offsets=(0, 1)))  # -> [('0', 'b'), ('1', 'c'), ('2', 'd'), ('3', 'e')]

 Это можно использовать как облегченную альтернативу SciPy или pandas для анализа наборов данных,
 в которых некоторые ряды имеют отношение опережения или отставания.

 По умолчанию последовательность завершится, когда будет исчерпана самая короткая итерация. Чтобы продолжать до тех пор,
 пока не будет исчерпана самая длинная итерация, установите для longest значение True.

 list(zip_offset('0123', 'abcdef', offsets=(0, 1), longest=True))
 # [('0', 'b'), ('1', 'c'), ('2', 'd'), ('3', 'e'), (None, 'f')]
 list(zip_offset('0123', 'abcdef', offsets=(0, 1), longest=True, fillvalue='COOL'))
 [('0', 'b'), ('1', 'c'), ('2', 'd'), ('3', 'e'), ('COOL', 'f')]

 По умолчанию None будет использоваться для замены смещений за пределами последовательности. Укажите fillvalue ,
 чтобы использовать другое значение.

 Исходник:
 from itertools import chain, repeat, islice, zip_longest

 def zip_offset(*iterables, offsets, longest=False, fillvalue=None):
     if len(iterables) != len(offsets):
         raise ValueError("Number of iterables and offsets didn't match")

     staggered = []
     for it, n in zip(iterables, offsets):
         if n < 0:
             staggered.append(chain(repeat(fillvalue, -n), it))
         elif n > 0:
             staggered.append(islice(it, n, None))
         else:
             staggered.append(it)

     if longest:
         return zip_longest(*staggered, fillvalue=fillvalue)

     return zip(*staggered)

________________________________________________________________________________________________________________________
 more_itertools.zip_equal(*iterables) - zipвходные данные повторяются вместе, но увеличиваются,
 UnequalIterablesError если они не имеют одинаковой длины.

 from more_itertools import zip_equal

 it_1 = range(3)
 it_2 = iter('abc')
 list(zip_equal(it_1, it_2))  # -> [(0, 'a'), (1, 'b'), (2, 'c')]

 it_1 = range(3)
 it_2 = iter('abcd')
 list(zip_equal(it_1, it_2))  # -> UnequalIterablesError: Iterables have different lengths

 Исходник:
 from sys import hexversion
 import warnings

 def zip_equal(*iterables):
     if hexversion >= 0x30A00A6:
         warnings.warn(
             (
                 'zip_equal will be removed in a future version of '
                 'more-itertools. Use the builtin zip function with '
                 'strict=True instead.'
             ),
             DeprecationWarning,
         )

     return _zip_equal(*iterables)

________________________________________________________________________________________________________________________
 more_itertools.zip_broadcast(*objects, scalar_types=(str, bytes), strict=False) - Версия, zip() которая «транслирует»
 любые скалярные (т. е. неитерируемые) элементы в выходные кортежи.

 from more_itertools import zip_broadcast

 iterable_1 = [1, 2, 3]
 iterable_2 = ['a', 'b', 'c']
 scalar = '_'
 list(zip_broadcast(iterable_1, iterable_2, scalar))  # -> [(1, 'a', '_'), (2, 'b', '_'), (3, 'c', '_')]

 Аргумент ключевого слова scalar_types определяет, какие типы считаются скалярными. По умолчанию установлено значение
 (str, bytes). Установите значение None, чтобы строки и байтовые строки рассматривались как итеративные:

 list(zip_broadcast('abc', 0, 'xyz', scalar_types=None))  # -> [('a', 0, 'x'), ('b', 0, 'y'), ('c', 0, 'z')]

 Если аргументом strict является True, то UnequalIterablesError, если какая-либо из итераций имеет разную длину.

 iterable_1 = [1, 2, 3]
 iterable_2 = ['a', 'b', 'c', 'd']
 scalar = '_'
 list(zip_broadcast(iterable_1, iterable_2, scalar, strict=False)) # -> Нет ошибки хотя длина разная
 list(zip_broadcast(iterable_1, iterable_2, scalar, strict=True))  # -> UnequalIterablesError: Iterables have different lengths

 Исходник:
 def zip_broadcast(*objects, scalar_types=(str, bytes), strict=False):
     def is_scalar(obj):
         if scalar_types and isinstance(obj, scalar_types):
             return True
         try:
             iter(obj)
         except TypeError:
             return True
         else:
             return False

     size = len(objects)
     if not size:
         return

     new_item = [None] * size
     iterables, iterable_positions = [], []
     for i, obj in enumerate(objects):
         if is_scalar(obj):
             new_item[i] = obj
         else:
             iterables.append(iter(obj))
             iterable_positions.append(i)

     if not iterables:
         yield tuple(objects)
         return

     zipper = _zip_equal if strict else zip
     for item in zipper(*iterables):
         for i, new_item[i] in zip(iterable_positions, item):
             pass
         yield tuple(new_item)

________________________________________________________________________________________________________________________
 Itertools recipes
 more_itertools.dotproduct(vec1, vec2) - Возвращает скалярное произведение двух итераций.
 Скалярное произведение - своими словами:
 первый элемент массива умножается на первый элемент другого массива и в конце всё суммируется:
 a = [1, 2]
 b = [4, 5]
 sum([i*j for i, j in zip(a, b)])  # -> 14

 from more_itertools import dotproduct
 import numpy

 a = [1, 2]
 b = [4, 5]
 print(numpy.dot(a, b))   # -> 14    Вот что происходит внутри 1*4+2*5
 print(dotproduct(a, b))  # -> 14    Вот что происходит внутри 1*4+2*5

 numpy.dot([10, 10], [20, 20])   # -> 400
 dotproduct([10, 10], [20, 20])  # -> 400


 Исходник:
 import operator

 def dotproduct(vec1, vec2):
     return sum(map(operator.mul, vec1, vec2))

________________________________________________________________________________________________________________________
 more_itertools.convolve(signal, kernel) - Сверните итерируемый signal с итерируемым kernel .

 from more_itertools import convolve

 signal = (1, 2, 3, 4, 5)
 kernel = [3, 2, 1]
 list(convolve(signal, kernel))  # -> [3, 8, 14, 20, 26, 14, 5]

 Примечание: входные аргументы не являются взаимозаменяемыми, поскольку ядро/kernel немедленно потребляется и сохраняется.
 math.sumprod(p, q) - Возвращает сумму произведений значений из двух итераций p и q .

 Исходник:
 from more_itertools import dotproduct
 from collections import deque
 import math

 # math.sumprod is available for Python 3.12+
 _sumprod = getattr(math, 'sumprod', lambda x, y: dotproduct(x, y))

 def convolve(signal, kernel):
     # This implementation intentionally doesn't match the one in the itertools
     # documentation.
     kernel = tuple(kernel)[::-1]
     n = len(kernel)
     window = deque([0], maxlen=n) * n
     for x in chain(signal, repeat(0, n - 1)):
         window.append(x)
         yield _sumprod(kernel, window)

________________________________________________________________________________________________________________________
 more_itertools.flatten(listOfLists) - Возвращает итератор, выравнивающий один уровень вложенности в списке списков.

 from more_itertools import flatten

 list(flatten([[0, 1], [2, 3]]))    # -> [0, 1, 2, 3]
 list(flatten([[[0, 1]], [2, 3]]))  # -> [[0, 1], 2, 3]  Только 1 уровень может

 См. также раздел collapse(), который может сгладить несколько уровней вложенности.

 Исходник:
 from itertools import chain

 def flatten(listOfLists):
     return chain.from_iterable(listOfLists)

________________________________________________________________________________________________________________________
 more_itertools.roundrobin(*iterables) - Возвращает элемент из каждой итерации, чередуя их.

 from more_itertools import roundrobin

 list(roundrobin('ABC', 'D', 'EF'))    # -> ['A', 'D', 'E', 'B', 'F', 'C']
 list(roundrobin([1, 2], [10], [20]))  # -> [1, 10, 20, 2]

 Эта функция выдает тот же результат, что и interleave_longest(), но может работать лучше для некоторых входных данных
 (в частности, когда количество итераций невелико).

 Исходник:
 from itertools import cycle, islice

 def roundrobin(*iterables):
     # Recipe credited to George Sakkis
     pending = len(iterables)
     nexts = cycle(iter(it).__next__ for it in iterables)
     while pending:
         try:
             for next in nexts:
                 yield next()
         except StopIteration:
             pending -= 1
             nexts = cycle(islice(nexts, pending))

________________________________________________________________________________________________________________________
 more_itertools.prepend(value, iterator) - Yield value, за которым следуют элементы в итераторе.

 from more_itertools import prepend

 value = '0'
 iterator = ['1', '2', '3']
 list(prepend(value, iterator))  # -> ['0', '1', '2', '3']

 list(prepend({100, 200}, [1, 2, 3]))  # -> [{200, 100}, 1, 2, 3]

 Исходник:
 from itertools import chain

 def prepend(value, iterator):
     return chain([value], iterator)

________________________________________________________________________________________________________________________
--- Подведение итогов     Summarizing ---

--- Эти инструменты возвращают обобщенные или агрегированные данные из итерации ---

--- These tools return summarized or aggregated data from an iterable ---
________________________________________________________________________________________________________________________
 more_itertools.ilen(iterable) - Возвращает количество элементов в iterable .
 Это потребляет итерацию, поэтому обращайтесь с ней осторожно.

 from more_itertools import ilen

 ilen(x for x in range(1000000) if x % 3 == 0)  # -> 333334

 a_gen = (i for i in range(10))
 print(ilen(a_gen))   # -> 10  Генератор/Итератор одноразовый
 print(list(a_gen))   # -> []  <-----                                                            <-----
 print(len(a_gen))    # -> TypeError: object of type 'generator' has no len()     Обычный len()  <-----

 Исходник:
 from collections import deque
 from itertools import count

 def ilen(iterable):
     # This approach was selected because benchmarks showed it's likely the
     # fastest of the known implementations at the time of writing.
     counter = count()
     deque(zip(iterable, counter), maxlen=0)
     return next(counter)

________________________________________________________________________________________________________________________
 more_itertools.unique_to_each(*iterables) - Возвращайте элементы из каждой входной итерации, которых нет в других
 входных итерациях. Например, предположим, что у вас есть набор пакетов, каждый из которых имеет набор зависимостей:

 from more_itertools import unique_to_each

 {'pkg_1': {'A', 'B'}, 'pkg_2': {'B', 'C'}, 'pkg_3': {'B', 'D'}}

 Если вы удалите один пакет, какие зависимости также можно удалить?

 Если pkg_1 удалено, то A больше не нужно — оно не связано с pkg_2 или pkg_3. Аналогично, C
 требуется только для pkg_2 и D требуется только для pkg_3:

 unique_to_each({'A', 'B'}, {'B', 'C'}, {'B', 'D'})       # -> [['A'], ['C'], ['D']]
 unique_to_each({'A', 'B', 'D'}, {'B', 'C'}, {'B', 'D'})  # -> [['A'], ['C'], []]
 unique_to_each([1, 2], [2, 3], [4, 5])                   # -> [[1], [3], [4, 5]]

 Если в одной входной итерации есть дубликаты, которых нет в других, они будут дублироваться в выходных данных.
 Порядок ввода сохраняется:

 unique_to_each("mississippi", "missouri")  # -> [['p', 'p'], ['o', 'u', 'r']]

 Предполагается, что элементы каждой итерации хешируются.

 Исходник:
 from itertools import chain
 from collections import Counter

 def unique_to_each(*iterables):
     pool = [list(it) for it in iterables]
     counts = Counter(chain.from_iterable(map(set, pool)))
     uniques = {element for element in counts if counts[element] == 1}
     return [list(filter(uniques.__contains__, it)) for it in pool]

________________________________________________________________________________________________________________________
 more_itertools.sample(iterable, k=1, weights=None) - Возвращает список элементов длины k , выбранных (без замены)
 из итерируемого объекта . Похож на random.sample(), но работает с итерациями неизвестной длины.
 random.sample() - Случайная выборка нескольких элементов последовательности без замены

 from more_itertools import sample

 iterable = range(100)
 sample(iterable, 5)  # -> [81, 60, 96, 16, 4]

 iterable_1 = (i for i in range(100))
 sample(iterable_1, 5)  # -> [32, 19, 72, 76, 20]
 sample(iterable_1, 1)  # -> []

 Также может быть задана итерация с весами :

 iterable = range(100)
 weights = (i * i + 1 for i in range(100))
 sampled = sample(iterable, 5, weights=weights)  # -> [79, 67, 74, 66, 78]

 Алгоритм также можно использовать для генерации взвешенных случайных перестановок. Относительный вес каждого элемента
 определяет вероятность того, что он появится в перестановке поздно.

 data = "abcdefgh"
 weights = range(1, len(data) + 1)
 sample(data, k=len(data), weights=weights)  # -> ['c', 'a', 'b', 'e', 'g', 'd', 'h', 'f']

 Исходник Классный:
 from math import exp, floor, log
 from more_itertools import take
 from random import random, randrange, uniform
 from heapq import heapify, heappop, heapreplace

 def _sample_unweighted(iterable, k):
     # Implementation of "Algorithm L" from the 1994 paper by Kim-Hung Li:
     # "Reservoir-Sampling Algorithms of Time Complexity O(n(1+log(N/n)))".

     # Fill up the reservoir (collection of samples) with the first `k` samples
     reservoir = take(k, iterable)

     # Generate random number that's the largest in a sample of k U(0,1) numbers
     # Largest order statistic: https://en.wikipedia.org/wiki/Order_statistic
     W = exp(log(random()) / k)

     # The number of elements to skip before changing the reservoir is a random
     # number with a geometric distribution. Sample it using random() and logs.
     next_index = k + floor(log(random()) / log(1 - W))

     for index, element in enumerate(iterable, k):
         if index == next_index:
             reservoir[randrange(k)] = element
             # The new W is the largest in a sample of k U(0, `old_W`) numbers
             W *= exp(log(random()) / k)
             next_index += floor(log(random()) / log(1 - W)) + 1

     return reservoir


 def _sample_weighted(iterable, k, weights):
     # Implementation of "A-ExpJ" from the 2006 paper by Efraimidis et al. :
     # "Weighted random sampling with a reservoir".

     # Log-transform for numerical stability for weights that are small/large
     weight_keys = (log(random()) / weight for weight in weights)

     # Fill up the reservoir (collection of samples) with the first `k`
     # weight-keys and elements, then heapify the list.
     reservoir = take(k, zip(weight_keys, iterable))
     heapify(reservoir)

     # The number of jumps before changing the reservoir is a random variable
     # with an exponential distribution. Sample it using random() and logs.
     smallest_weight_key, _ = reservoir[0]
     weights_to_skip = log(random()) / smallest_weight_key

     for weight, element in zip(weights, iterable):
         if weight >= weights_to_skip:
             # The notation here is consistent with the paper, but we store
             # the weight-keys in log-space for better numerical stability.
             smallest_weight_key, _ = reservoir[0]
             t_w = exp(weight * smallest_weight_key)
             r_2 = uniform(t_w, 1)  # generate U(t_w, 1)
             weight_key = log(r_2) / weight
             heapreplace(reservoir, (weight_key, element))
             smallest_weight_key, _ = reservoir[0]
             weights_to_skip = log(random()) / smallest_weight_key
         else:
             weights_to_skip -= weight

     # Equivalent to [element for weight_key, element in sorted(reservoir)]
     return [heappop(reservoir)[1] for _ in range(k)]

 def sample(iterable, k, weights=None):
     if k == 0:
         return []

     iterable = iter(iterable)
     if weights is None:
         return _sample_unweighted(iterable, k)
     else:
         weights = iter(weights)
         return _sample_weighted(iterable, k, weights)

________________________________________________________________________________________________________________________
 more_itertools.consecutive_groups(iterable, ordering=lambda x: ...) - Получите группы последовательных элементов,
 используя itertools.groupby(). Функция упорядочивания определяет, являются ли два элемента соседними, возвращая их позицию.

 По умолчанию функция упорядочивания является функцией идентификации. Это подходит для поиска серий чисел:

 from more_itertools import consecutive_groups

 iterable = [1, 10, 11, 12, 20, 30, 31, 32, 33, 40]
 for group in consecutive_groups(iterable):
     print(list(group))

 # [1]
 # [10, 11, 12]
 # [20]
 # [30, 31, 32, 33]
 # [40]

 Для поиска последовательностей соседних букв попробуйте использовать index()метод строки букв:

 from string import ascii_lowercase
 iterable = 'abcdfgilmnop'
 ordering = ascii_lowercase.index
 for group in consecutive_groups(iterable, ordering):
     print(list(group))

 # ['a', 'b', 'c', 'd']
 # ['f', 'g']
 # ['i']
 # ['l', 'm', 'n', 'o', 'p']

 Каждая группа последовательных элементов представляет собой итератор, который использует общий источник с iterable. При
 расширении группы вывода предыдущая группа больше не доступна, пока ее элементы не будут скопированы (например, в файл list).

 iterable = [1, 2, 11, 12, 21, 22]
 saved_groups = []
 for group in consecutive_groups(iterable):
     saved_groups.append(list(group))  # Copy group elements
 saved_groups  # -> [[1, 2], [11, 12], [21, 22]]

 Исходник:
 from itertools import groupby
 from operator import itemgetter

 def consecutive_groups(iterable, ordering=lambda x: x):
     for k, g in groupby(
         enumerate(iterable), key=lambda x: x[0] - ordering(x[1])
     ):
         yield map(itemgetter(1), g)

________________________________________________________________________________________________________________________
 class more_itertools.run_length - run_length.encode() сжимает итерацию с кодированием длины серии.
 Он дает группы повторяющихся элементов с подсчетом того, сколько раз они повторялись:

 from more_itertools import run_length

 uncompressed = 'abbcccdddd'
 list(run_length.encode(uncompressed))  # -> [('a', 1), ('b', 2), ('c', 3), ('d', 4)]

 uncompressed = 'abab'
 list(run_length.encode(uncompressed))  # -> [('a', 1), ('b', 1), ('a', 1), ('b', 1)]

 run_length.decode() распаковывает итерацию, которая ранее была сжата с помощью кодирования длины серии.
 Он возвращает элементы распакованной итерации:

 compressed = [('a', 1), ('b', 2), ('c', 3), ('d', 4)]
 list(run_length.decode(compressed))  # -> ['a', 'b', 'b', 'c', 'c', 'c', 'd', 'd', 'd', 'd']

 compressed = [('a', 1), ('b', 2), ('a', 3), ('b', 4)]
 list(run_length.decode(compressed))  # -> ['a', 'b', 'b', 'a', 'a', 'a', 'b', 'b', 'b', 'b']

 Исходник:
 from more_itertools import ilen
 from itertools import groupby, chain, repeat

 class run_length:

     @staticmethod
     def encode(iterable):
         return ((k, ilen(g)) for k, g in groupby(iterable))

     @staticmethod
     def decode(iterable):
         return chain.from_iterable(repeat(k, n) for k, n in iterable)

________________________________________________________________________________________________________________________
 more_itertools.map_reduce(iterable, keyfunc, valuefunc=None, reducefunc=None) - Возвращает словарь, который
 сопоставляет элементы в итерируемом объекте с категориями, определенными keyfunc , преобразует их с помощью valuefunc ,
 а затем суммирует их по категориям с помощью сокращения .

 valuefunc по умолчанию использует функцию идентификации, если она не указана. Если параметр dropfunc не указан,
 суммирование не производится:

 from more_itertools import map_reduce

 keyfunc = lambda x: x.upper()
 result = map_reduce('abbccc', keyfunc)
 sorted(result.items())  # -> [('A', ['a']), ('B', ['b', 'b']), ('C', ['c', 'c', 'c'])]

 Указание valuefunc преобразует категоризированные элементы:

 keyfunc = lambda x: x.upper()
 valuefunc = lambda x: 1
 result = map_reduce('abbccc', keyfunc, valuefunc)
 sorted(result.items())  # -> [('A', [1]), ('B', [1, 1]), ('C', [1, 1, 1])]

 Указание уменьшения функции суммирует элементы по категориям:

 keyfunc = lambda x: x.upper()
 valuefunc = lambda x: 1
 reducefunc = sum
 result = map_reduce('abbccc', keyfunc, valuefunc, reducefunc)
 sorted(result.items())  # -> [('A', 1), ('B', 2), ('C', 3)]

 Возможно, вы захотите отфильтровать итерируемые входные данные перед применением процедуры сопоставления/сокращения:

 all_items = range(30)
 items = [x for x in all_items if 10 <= x <= 20]  # Filter
 keyfunc = lambda x: x % 2  # Evens map to 0; odds to 1
 categories = map_reduce(items, keyfunc=keyfunc)
 sorted(categories.items())  # -> [(0, [10, 12, 14, 16, 18, 20]), (1, [11, 13, 15, 17, 19])]

 summaries = map_reduce(items, keyfunc=keyfunc, reducefunc=sum)
 sorted(summaries.items())   # -> [(0, 90), (1, 75)]

 Обратите внимание, что все элементы итерируемого объекта собираются в список перед этапом суммирования,
 что может потребовать значительного объема памяти.

 Возвращаемый объект — это Collections.defaultdict с параметром default_factory=None , поэтому он ведет себя как обычный словарь.

 Исходник:
 from collections import defaultdict

 def map_reduce(iterable, keyfunc, valuefunc=None, reducefunc=None):
     valuefunc = (lambda x: x) if (valuefunc is None) else valuefunc

     ret = defaultdict(list)
     for item in iterable:
         key = keyfunc(item)
         value = valuefunc(item)
         ret[key].append(value)

     if reducefunc is not None:
         for key, value_list in ret.items():
             ret[key] = reducefunc(value_list)

     ret.default_factory = None
     return ret

________________________________________________________________________________________________________________________
 more_itertools.exactly_n(iterable, n, predicate=bool) - Возвращает значение True, если именно n элементы в итерируемом
 объекте True соответствуют функции предиката . Итерация будет продвигаться вперед до тех пор, пока не встретится n + 1
 истинный элемент, поэтому избегайте вызова ее для бесконечных итераций.

 from more_itertools import exactly_n

 exactly_n([True, True, False], 2)  # -> True

 exactly_n([True, True, False], 1)  # -> False

 exactly_n([0, 1, 2, 3, 4, 5], 3, lambda x: x < 3)  # -> True

 Исходник:
 from more_itertools import take

 def exactly_n(iterable, n, predicate=bool):
     return len(take(n + 1, filter(predicate, iterable))) == n

________________________________________________________________________________________________________________________
 more_itertools.is_sorted(iterable, key=None, reverse=False, strict=False) - Возвращает True, если элементы итерируемого
 объекта находятся в отсортированном порядке, и False в противном случае. key и reverse имеют то же значение,
 что и во встроенной sorted() функции.

 from more_itertools import is_sorted

 is_sorted(['1', '2', '3', '4', '5'], key=int)  # ->  True
 is_sorted([5, 4, 3, 1, 2], reverse=True)       # ->  False

 Если strict , проверяет строгую сортировку, то есть возвращает результат, Falseесли найдены равные элементы:

 is_sorted([1, 2, 2])                 # ->  True
 is_sorted([1, 2, 2], strict=True)    # ->  False

 Функция возвращается False после обнаружения первого элемента, находящегося вне порядка. Если нет элементов,
 выходящих за пределы порядка, итерация исчерпывается.

 Исходник:
 from operator import le, ge, lt, gt
 from itertools import starmap, pairwise

 def is_sorted(iterable, key=None, reverse=False, strict=False):
     compare = (le if reverse else ge) if strict else (lt if reverse else gt)
     it = iterable if key is None else map(key, iterable)
     return not any(starmap(compare, pairwise(it)))

________________________________________________________________________________________________________________________
 more_itertools.all_unique(iterable, key=None) - Возвращает значение True, если все элементы итерируемого объекта
 уникальны (нет двух одинаковых элементов).

 all_unique('ABCB')     # -> False
 all_unique([1, 2, 3])  # -> True

 Если указана ключевая функция, она будет использоваться для сравнения.

 all_unique('ABCb')             # -> True
 all_unique('ABCb', str.lower)  # -> False

 Функция возвращает значение, как только встречается первый неуникальный элемент. Можно использовать итерации со
 смесью хешируемых и нехешируемых элементов, но для нехешируемых элементов функция будет работать медленнее.

 Исходник:
 def all_unique(iterable, key=None):
     seenset = set()
     seenset_add = seenset.add
     seenlist = []
     seenlist_add = seenlist.append
     for element in map(key, iterable) if key else iterable:
         try:
             if element in seenset:
                 return False
             seenset_add(element)
         except TypeError:
             if element in seenlist:
                 return False
             seenlist_add(element)
     return True

________________________________________________________________________________________________________________________
 more_itertools.minmax(iterable, *[, key, default])
 more_itertools.minmax(arg1, arg2, *args[, key])
 Возвращает как самый маленький, так и самый большой элементы в итерации или самый большой из двух или более аргументов.

 from more_itertools import minmax

 minmax([3, 1, 5])  # -> (1, 5)

 minmax(4, 2, 6)    # -> (2, 6)

 Если указана ключевая функция, она будет использоваться для преобразования входных элементов для сравнения.

 minmax([5, 30], key=str)  # '30' sorts before '5'
 # (30, 5)

 Если указано значение по умолчанию , оно будет возвращено, если входных элементов нет. В противном случае ValueError

 minmax([], default=(0, 0))   # -> (0, 0)
 minmax([]) # -> ValueError: `minmax()` argument is an empty iterable. Provide a `default` value to suppress this error.

 Эта функция основана на рецепте Раймонда Хеттингера и старается минимизировать количество выполняемых сравнений.

 Исходник:
 from itertools import zip_longest

 _marker = object()

 def minmax(iterable_or_value, *others, key=None, default=_marker):
     iterable = (iterable_or_value, *others) if others else iterable_or_value

     it = iter(iterable)

     try:
         lo = hi = next(it)
     except StopIteration as e:
         if default is _marker:
             raise ValueError(
                 '`minmax()` argument is an empty iterable. '
                 'Provide a `default` value to suppress this error.'
             ) from e
         return default

     # Different branches depending on the presence of key. This saves a lot
     # of unimportant copies which would slow the "key=None" branch
     # significantly down.
     if key is None:
         for x, y in zip_longest(it, it, fillvalue=lo):
             if y < x:
                 x, y = y, x
             if x < lo:
                 lo = x
             if hi < y:
                 hi = y

     else:
         lo_key = hi_key = key(lo)

         for x, y in zip_longest(it, it, fillvalue=lo):
             x_key, y_key = key(x), key(y)

             if y_key < x_key:
                 x, y, x_key, y_key = y, x, y_key, x_key
             if x_key < lo_key:
                 lo, lo_key = x, x_key
             if hi_key < y_key:
                 hi, hi_key = y, y_key

     return lo, hi

________________________________________________________________________________________________________________________
 more_itertools.iequals(*iterables) - Возврат True, если все заданные итерации равны друг другу, что означает,
 что они содержат одни и те же элементы в одном и том же порядке.

 Функция полезна для сравнения итераций разных типов данных или итераций, которые не поддерживают проверки на равенство.

 from more_itertools import iequals

 iequals("abc", ['a', 'b', 'c'], ('a', 'b', 'c'), iter("abc"))  # -> True

 iequals("abc", "acb")  # -> False

 Не путать с all_equal(), который проверяет, равны ли все элементы итерируемого объекта друг другу.

 Исходник:
 from more_itertools import all_equal
 from itertools import zip_longest

 def iequals(*iterables):
     return all(map(all_equal, zip_longest(*iterables, fillvalue=object())))

________________________________________________________________________________________________________________________
 more_itertools.all_equal(iterable) - Возвращает True, если все элементы равны друг другу.

 from more_itertools import all_equal

 all_equal('aaaa')  # -> True
 all_equal('aaab')  # -> False

 all_equal([1, 1, 1])             # -> True
 all_equal([1, 1, 2])             # -> False
 all_equal([1, 2, 3], [1, 2, 3])  # -> TypeError: all_equal() takes 1 positional argument but 2 were given

 Исходник:
 from itertools import groupby

 def all_equal(iterable):
     g = groupby(iterable)
     return next(g, True) and not next(g, False)

________________________________________________________________________________________________________________________
 more_itertools.first_true(iterable, default=None, pred=None) - Возвращает первое истинное значение в итерируемом объекте.
 Если истинное значение не найдено, возвращается значение по умолчанию. сли pred не None, возвращает первый элемент,
 для которого .pred(item) == True

 from more_itertools import first_true

 first_true(range(10))                                           # ->  1
 first_true(range(10), pred=lambda x: x > 5)                     # ->  6
 first_true(range(10), default='missing', pred=lambda x: x > 9)  # -> 'missing'

 a_list = [False, [], 1, 2, 3, 4]
 first_true(a_list, default='COOL', pred=lambda x: x not in [False, []] and x > 5)  # -> COOL

 a_list = [1, 2, 3, 4]
 first_true(a_list, default='COOL', pred=lambda x: x > 3)  # -> 4

 Исходник:
 def first_true(iterable, default=None, pred=None):
     return next(filter(pred, iterable), default)

________________________________________________________________________________________________________________________
 more_itertools.quantify(iterable, pred=bool) - Возвращает количество раз, когда предикат истинен.

 from more_itertools import quantify

 quantify([True, False, True])      # -> 2
 quantify([1, [], {}, {1, 2}, ()])  # -> 2

 Исходник:
 def quantify(iterable, pred=bool):
     return sum(map(pred, iterable))


________________________________________________________________________________________________________________________
 --- Выбор     Selecting ---

 --- Эти инструменты позволяют получить определенные элементы из итерации ---

 --- These tools yield certain items from an iterable ---
________________________________________________________________________________________________________________________
 class more_itertools.islice_extended(iterable, stop)
 class more_itertools.islice_extended(iterable, start, stop[, step])
 Расширение этого itertools.islice()поддерживает отрицательные значения для stop , start и Step .

 from more_itertools import islice_extended

 iterable = iter('abcdefgh')
 list(islice_extended(iterable, -4, -1))  # -> ['e', 'f', 'g']

 Срезы с отрицательными значениями требуют некоторого кэширования iterable , но эта функция старается минимизировать
 требуемый объем памяти. Например, вы можете использовать отрицательный шаг с бесконечным итератором:

 from itertools import count
 list(islice_extended(count(), 110, 99, -2))  # -> [110, 108, 106, 104, 102, 100]

 Вы также можете использовать обозначение среза напрямую:

 iterable = map(str, count())
 it = islice_extended(iterable)[10:20:2]
 list(it)  # -> ['10', '12', '14', '16', '18']

 Исходник Не хилый:
 class islice_extended:

     def __init__(self, iterable, *args):
         it = iter(iterable)
         if args:
             self._iterable = _islice_helper(it, slice(*args))
         else:
             self._iterable = it

     def __iter__(self):
         return self

     def __next__(self):
         return next(self._iterable)

     def __getitem__(self, key):
         if isinstance(key, slice):
             return islice_extended(_islice_helper(self._iterable, key))

         raise TypeError('islice_extended.__getitem__ argument must be a slice')

 def _islice_helper(it, s):
     start = s.start
     stop = s.stop
     if s.step == 0:
         raise ValueError('step argument must be a non-zero integer or None.')
     step = s.step or 1

     if step > 0:
         start = 0 if (start is None) else start

         if start < 0:
             # Consume all but the last -start items
             cache = deque(enumerate(it, 1), maxlen=-start)
             len_iter = cache[-1][0] if cache else 0

             # Adjust start to be positive
             i = max(len_iter + start, 0)

             # Adjust stop to be positive
             if stop is None:
                 j = len_iter
             elif stop >= 0:
                 j = min(stop, len_iter)
             else:
                 j = max(len_iter + stop, 0)

             # Slice the cache
             n = j - i
             if n <= 0:
                 return

             for index, item in islice(cache, 0, n, step):
                 yield item
         elif (stop is not None) and (stop < 0):
             # Advance to the start position
             next(islice(it, start, start), None)

             # When stop is negative, we have to carry -stop items while
             # iterating
             cache = deque(islice(it, -stop), maxlen=-stop)

             for index, item in enumerate(it):
                 cached_item = cache.popleft()
                 if index % step == 0:
                     yield cached_item
                 cache.append(item)
         else:
             # When both start and stop are positive we have the normal case
             yield from islice(it, start, stop, step)
     else:
         start = -1 if (start is None) else start

         if (stop is not None) and (stop < 0):
             # Consume all but the last items
             n = -stop - 1
             cache = deque(enumerate(it, 1), maxlen=n)
             len_iter = cache[-1][0] if cache else 0

             # If start and stop are both negative they are comparable and
             # we can just slice. Otherwise we can adjust start to be negative
             # and then slice.
             if start < 0:
                 i, j = start, stop
             else:
                 i, j = min(start - len_iter, -1), None

             for index, item in list(cache)[i:j:step]:
                 yield item
         else:
             # Advance to the stop position
             if stop is not None:
                 m = stop + 1
                 next(islice(it, m, m), None)

             # stop is positive, so if start is negative they are not comparable
             # and we need the rest of the items.
             if start < 0:
                 i = start
                 n = None
             # stop is None and start is positive, so we just need items up to
             # the start index.
             elif stop is None:
                 i = None
                 n = start + 1
             # Both stop and start are positive, so they are comparable.
             else:
                 i = None
                 n = start - stop
                 if n <= 0:
                     return

             cache = list(islice(it, n))

             yield from cache[i::step]

________________________________________________________________________________________________________________________
 more_itertools.first(iterable[, default]) - Возвращает первый элемент iterable или значение по умолчанию , если iterable пуст.

 from more_itertools import first

 first([0, 1, 2, 3])        # -> 0
 first([], 'some default')  # -> 'some default'
 first([])  # -> ValueError: first() was called on an empty iterable, and no default value was provided.

 first()полезно, когда у вас есть генератор дорогостоящих для извлечения значений и вам нужен любой произвольный.
 Это немного короче, чем next(iter(iterable), default)

 Исходник:
 _marker = object()

 def first(iterable, default=_marker):
     for item in iterable:
         return item
     if default is _marker:
         raise ValueError(
             'first() was called on an empty iterable, and no '
             'default value was provided.'
         )
     return default

________________________________________________________________________________________________________________________
 more_itertools.last(iterable[, default]) - Возвращает последний элемент iterable или значение по умолчанию ,
 если iterable пуст.

 from more_itertools import last

 last([0, 1, 2, 3])        # -> 3
 last([], 'some default')  # -> 'some default'
 last([])  # -> ValueError: last() was called on an empty iterable, and no default was provided.

 Исходник:
 from collections.abc import Sequence
 from sys import hexversion
 from collections import deque

 _marker = object()

 def last(iterable, default=_marker):
     try:
         if isinstance(iterable, Sequence):
             return iterable[-1]
         # Work around https://bugs.python.org/issue38525
         elif hasattr(iterable, '__reversed__') and (hexversion != 0x030800F0):
             return next(reversed(iterable))
         else:
             return deque(iterable, maxlen=1)[-1]
     except (IndexError, TypeError, StopIteration):
         if default is _marker:
             raise ValueError(
                 'last() was called on an empty iterable, and no default was '
                 'provided.'
             )
         return default

________________________________________________________________________________________________________________________
 more_itertools.one(iterable, too_short=ValueError, too_long=ValueError) - Верните первый элемент из iterable , который,
 как ожидается, будет содержать только этот элемент. Вызовите исключение, если итерируемый объект пуст или содержит
 более одного элемента.

 one() полезен для обеспечения того, чтобы итерация содержала только один элемент. Например, его можно использовать для
 получения результата запроса к базе данных, который, как ожидается, вернет одну строку.

 from more_itertools import one

 it = [1]
 one(it)   # -> 1

 it = 1
 one(it)   # -> TypeError: 'int' object is not iterable

 Если iterable пуст, ValueError будет поднят. Вы можете указать другое исключение с помощью ключевого слова Too_short :

 from more_itertools import one

 it = []
 one(it)                       # -> ValueError: too few items in iterable (expected 1)

 too_short = IndexError('too few items')
 one(it, too_short=too_short)  # -> IndexError: too few items

 Аналогично, если iterable содержит более одного элемента, ValueError будет поднято. Вы можете указать другое исключение
 с помощью ключевого слова Too_long :

 it = ['too', 'many']
 # one(it)   # -> ValueError: Expected exactly one item in iterable, but got 'too', 'many', and perhaps more.

 too_long = RuntimeError
 one(it, too_long=too_long)  # -> RuntimeError

 Обратите внимание, что one() попытки выполнить итерацию выполняются дважды, чтобы гарантировать наличие только одного
 элемента. Посмотрите spy()или, peekable() чтобы проверить итерируемое содержимое менее разрушительно.

 Исходник:
 def one(iterable, too_short=None, too_long=None):
     it = iter(iterable)

     try:
         first_value = next(it)
     except StopIteration as e:
         raise (
             too_short or ValueError('too few items in iterable (expected 1)')
         ) from e

     try:
         second_value = next(it)
     except StopIteration:
         pass
     else:
         msg = (
             'Expected exactly one item in iterable, but got {!r}, {!r}, '
             'and perhaps more.'.format(first_value, second_value)
         )
         raise too_long or ValueError(msg)

     return first_value

________________________________________________________________________________________________________________________
 more_itertools.only(iterable, default=None, too_long=ValueError) - Если в iterable есть только один элемент,
 верните его. Если в нем нет элементов, верните значение по умолчанию . Если у него более одного элемента,
 вызовите исключение, заданное Too_long , которое используется ValueErrorпо умолчанию.

 from more_itertools import only

 only([], default='missing')  # -> 'missing'
 only([1])     # -> 1
 only([1, 2])  # -> ValueError: Expected exactly one item in iterable, but got 1, 2, and perhaps more.
 only([1, 2], too_long=TypeError)  # -> TypeError


 Обратите внимание, что only()попытки выполнить итерацию выполняются дважды, чтобы гарантировать наличие только одного
 элемента. Посмотрите spy() или, peekable() чтобы проверить итерируемое содержимое менее разрушительно.

 Исходник:
 def only(iterable, default=None, too_long=None):
     it = iter(iterable)
     first_value = next(it, default)

     try:
         second_value = next(it)
     except StopIteration:
         pass
     else:
         msg = (
             'Expected exactly one item in iterable, but got {!r}, {!r}, '
             'and perhaps more.'.format(first_value, second_value)
         )
         raise too_long or ValueError(msg)

     return first_value

________________________________________________________________________________________________________________________
 more_itertools.strictly_n(iterable, too_short=None, too_long=None) - Убедитесь, что итерируемый объект содержит
 ровно n элементов, и верните их, если это так. Если в нем меньше n элементов, вызовите функцию Too_short с этими
 элементами. Если в нем более n элементов, вызовите функцию Too_long с первыми n + 1 элементами.

 from more_itertools import strictly_n

 iterable = ['a', 'b', 'c', 'd']
 n = 4
 list(strictly_n(iterable, n))  # -> ['a', 'b', 'c', 'd']

 Обратите внимание, что возвращенная итерация должна быть использована для выполнения проверки.
 По умолчанию Too_short и Too_long — это функции, которые поднимают ValueError.

 list(strictly_n('ab', 3))   # -> ValueError: Too few items in iterable (got 2)
 list(strictly_n('abc', 2))  # -> ValueError: Too many items in iterable (got at least 3)

 Вместо этого вы можете предоставить функции, которые делают что-то другое.
 Too_short будет вызываться с количеством элементов в итерации. Too_long будет вызываться с n + 1.

 def too_short(item_count):
     raise RuntimeError

 it = strictly_n('abcd', 6, too_short=too_short)
 list(it)  # -> RuntimeError

 def too_long(item_count):
     print('The boss is going to hear about this')

 it = strictly_n('abcdef', 4, too_long=too_long)
 list(it)  # -> The boss is going to hear about this

 Исходник:
 from more_itertools import raise_

 def strictly_n(iterable, n, too_short=None, too_long=None):
     if too_short is None:
         too_short = lambda item_count: raise_(
             ValueError,
             'Too few items in iterable (got {})'.format(item_count),
         )

     if too_long is None:
         too_long = lambda item_count: raise_(
             ValueError,
             'Too many items in iterable (got at least {})'.format(item_count),
         )

     it = iter(iterable)
     for i in range(n):
         try:
             item = next(it)
         except StopIteration:
             too_short(i)
             return
         else:
             yield item

     try:
         next(it)
     except StopIteration:
         pass
     else:
         too_long(n + 1)

________________________________________________________________________________________________________________________
 more_itertools.strip(iterable, pred) - Выдавайте элементы из iterable , но удаляйте все элементы с начала и конца,
 для которых возвращается pred True . Эта функция аналогична str.strip().

 Например, чтобы удалить набор элементов с обоих концов итерации:

 from more_itertools import strip

 iterable = (None, False, None, 1, 2, None, 3, False, None)
 pred = lambda x: x in {None, False, ''}
 list(strip(iterable, pred))  # -> [1, 2, None, 3]

 iterable = [1, 2, 5, 4, 5]
 pred = lambda x: x == 1 or x == 5
 list(strip(iterable, pred))  # -> [2, 5, 4]

 Исходник:
 from more_itertools import rstrip, lstrip

 def strip(iterable, pred):
     return rstrip(lstrip(iterable, pred), pred)

________________________________________________________________________________________________________________________
 more_itertools. lstrip ( итеративный , pred ) - Выдавайте элементы из iterable , но удаляйте все с конца, для которого
 возвращается pred True . Эта функция аналогична to str.lstrip() и по сути является оберткой для itertools.dropwhile().

 Например, чтобы удалить набор элементов из конца итерации:

 from more_itertools import lstrip

 iterable = (None, False, None, 1, 2, None, 3, False, None)
 pred = lambda x: x in {None, False, ''}
 list(lstrip(iterable, pred))  # -> [1, 2, None, 3, False, None]

 iterable = [5, 5, 4, 5]
 pred = lambda x: x == 5
 list(lstrip(iterable, pred))  # -> [4, 5]

 Исходник:
 from itertools import dropwhile

 def lstrip(iterable, pred):
     return dropwhile(pred, iterable)
________________________________________________________________________________________________________________
 more_itertools.rstrip(iterable, pred) - Выдавайте элементы из iterable , но удаляйте все с конца, для которого
 возвращается pred True . Эта функция аналогична str.rstrip().

 from more_itertools import rstrip

 iterable = (None, False, None, 1, 2, None, 3, False, None)
 pred = lambda x: x in {None, False, ''}
 list(rstrip(iterable, pred))  # -> [None, False, None, 1, 2, None, 3]

 iterable = [5, 4, 5, 5]
 pred = lambda x: x == 5
 list(rstrip(iterable, pred))  # -> [5, 4]

 Исходник:
 def rstrip(iterable, pred):
     cache = []
     cache_append = cache.append
     cache_clear = cache.clear
     for x in iterable:
         if pred(x):
             cache_append(x)
         else:
             yield from cache
             cache_clear()
             yield x

________________________________________________________________________________________________________________________
 more_itertools.filter_except(validator, iterable, *exceptions) - Выдавайте элементы из итерируемого объекта ,
 для которых функция проверки не вызывает ни одного из указанных исключений .

 Валидатор вызывается для каждого элемента в iterable . Это должна быть функция, которая принимает один аргумент
 и вызывает исключение, если этот элемент недействителен.

 Если валидатор вызывает исключение, отличное от того, которое задано исключениями , оно вызывается как обычно.

 from more_itertools import filter_except

 iterable = ['1', '2', 'three', '4', None]
 list(filter_except(int, iterable, ValueError, TypeError))  # -> ['1', '2', '4']

 iterable = ['1', '2', 'three', '4', None, 1, 20, (30, 40), {"A", "b"}, {1: 'one'}]
 list(filter_except(int, iterable, ValueError, TypeError))  # -> ['1', '2', '4', 1, 20]

 Исходник:
 def filter_except(validator, iterable, *exceptions):
     for item in iterable:
         try:
             validator(item)
         except exceptions:
             pass
         else:
             yield item

________________________________________________________________________________________________________________________
 more_itertools.map_except(function, iterable, *exceptions) - Преобразуйте каждый элемент из итерируемого с помощью
 функции и дайте результат, если только функция не вызовет одно из указанных исключений .

 Функция вызывается для преобразования каждого элемента в iterable . Он должен принять один аргумент.

 from more_itertools import map_except

 iterable = ['1', '2', 'three', '4', None]
 list(map_except(int, iterable, ValueError, TypeError))  # -> [1, 2, 4]

 iterable = ['1', '2', 'three', '4', None, 20, 30, {1: 20}]
 list(map_except(int, iterable, ValueError, TypeError))  # -> [1, 2, 4, 20, 30]

 Исходник:
 def map_except(function, iterable, *exceptions):
     for item in iterable:
         try:
             yield function(item)
         except exceptions:
             pass

________________________________________________________________________________________________________________________
 more_itertools.filter_map(func, iterable) - Примените func к каждому элементу iterable , получая только те, которые
 не являются таковыми None.

 from more_itertools import filter_map

 elems = ['1', 'a', '2', 'b', '3']
 list(filter_map(lambda s: int(s) if s.isnumeric() else None, elems))  # -> [1, 2, 3]

 elems = [10, 20, 30, None, 'A']
 list(filter_map(lambda x: x if type(x) == int else 'Bad', elems))  # -> [10, 20, 30, 'Bad', 'Bad']

 Исходник:
 def filter_map(func, iterable):
     for x in iterable:
         y = func(x)
         if y is not None:
             yield y

________________________________________________________________________________________________________________________
 more_itertools.iter_suppress(iterable, *exceptions) - Выведите каждый из элементов из iterable . Если итерация вызывает
 одно из указанных исключений , это исключение будет подавлено и итерация остановится.

 from more_itertools import iter_suppress

 from itertools import chain
 def breaks_at_five(x):
     while True:
         if x >= 5:
             raise RuntimeError
         yield x
         x += 1
 it_1 = iter_suppress(breaks_at_five(1), RuntimeError)
 it_2 = iter_suppress(breaks_at_five(2), RuntimeError)
 list(chain(it_1, it_2))  # -> [1, 2, 3, 4, 2, 3, 4]

 Исходник:
 def iter_suppress(iterable, *exceptions):
     try:
         yield from iterable
     except exceptions:
         return

________________________________________________________________________________________________________________________
 more_itertools.nth_or_last(iterable, n[, default]) - Возвращает n-й или последний элемент iterable или значение
 по умолчанию , если iterable пуст.

 from more_itertools import nth_or_last

 nth_or_last([0, 1, 2, 3], 2)  # -> 2
 nth_or_last([0, 1], 2)        # -> 1
 nth_or_last([], 0, 'some default')  # -> 'some default'
 nth_or_last([], 0)  # -> ValueError: last() was called on an empty iterable, and no default was provided.

 Исходник:
 from more_itertools import last
 from itertools import islice

 _marker = object()

 def nth_or_last(iterable, n, default=_marker):
     return last(islice(iterable, n + 1), default=default)

________________________________________________________________________________________________________________________
 more_itertools.unique_in_window(iterable, n, key=None) - Выдавайте элементы из итерации , которые в последнее время
 не видели. n — размер окна ретроспективного анализа. Элементы в итерации должны быть хешируемыми.

 from more_itertools import unique_in_window

 iterable = [0, 1, 0, 2, 3, 0]
 n = 3
 list(unique_in_window(iterable, n))  # -> [0, 1, 2, 3, 0]

 iterable = ["A", "A", "B", "B", "C"]
 list(unique_in_window(iterable, 2))  # -> ['A', 'B', 'C']

 iterable = ["A", []]  # -> TypeError: unhashable type: 'list'

 Ключевая функция, если она предусмотрена, будет использоваться для определения уникальности:

 list(unique_in_window('abAcda', 3, key=lambda x: x.lower()))  # -> ['a', 'b', 'c', 'd', 'a']

 Исходник:
 from collections import deque, defaultdict

 def unique_in_window(iterable, n, key=None):
     if n <= 0:
         raise ValueError('n must be greater than 0')

     window = deque(maxlen=n)
     counts = defaultdict(int)
     use_key = key is not None

     for item in iterable:
         if len(window) == n:
             to_discard = window[0]
             if counts[to_discard] == 1:
                 del counts[to_discard]
             else:
                 counts[to_discard] -= 1

         k = key(item) if use_key else item
         if k not in counts:
             yield item
         counts[k] += 1
         window.append(k)

________________________________________________________________________________________________________________________
 more_itertools.duplicates_everseen(iterable, key=None) - Выдавать повторяющиеся элементы после их первого появления.
 Эта функция аналогична unique_everseen() и подчиняется тем же соображениям производительности.

 from more_itertools import duplicates_everseen

 list(duplicates_everseen([1, 2, 2]))                  # -> [2]
 list(duplicates_everseen('mississippi'))              # -> ['s', 'i', 's', 's', 'i', 'p', 'i']
 list(duplicates_everseen('AaaBbbCccAaa', str.lower))  # -> ['a', 'a', 'b', 'b', 'c', 'c', 'A', 'a', 'a']

 Исходник:
 def duplicates_everseen(iterable, key=None):
     seen_set = set()
     seen_list = []
     use_key = key is not None

     for element in iterable:
         k = key(element) if use_key else element
         try:
             if k not in seen_set:
                 seen_set.add(k)
             else:
                 yield element
         except TypeError:
             if k not in seen_list:
                 seen_list.append(k)
             else:
                 yield element

________________________________________________________________________________________________________________________
 more_itertools.duplicates_justseen(iterable, key=None) - Выдает серийно повторяющиеся элементы после их первого появления.
 Эта функция аналогична unique_justseen().

 from more_itertools import duplicates_justseen

 list(duplicates_justseen([1, 1, 1, 2, 1]))            # -> [1, 1]
 list(duplicates_justseen('mississippi'))              # -> ['s', 's', 'p']
 list(duplicates_justseen('AaaBbbCccAaa', str.lower))  # -> ['a', 'a', 'b', 'b', 'c', 'c', 'a', 'a']

 Исходник:
 from more_itertools import flatten
 from itertools import groupby

 def duplicates_justseen(iterable, key=None):
     return flatten(g for _, g in groupby(iterable, key) for _ in g)

________________________________________________________________________________________________________________________
 more_itertools.classify_unique(iterable, key=None) -Классифицируйте каждый элемент с точки зрения его уникальности.
 Эта функция аналогична unique_everseen()и подчиняется тем же соображениям производительности.
 Для каждого элемента во входной итерации верните тройной кортеж, состоящий из:

 - Сам элемент
 - False если элемент равен предыдущему ему во входных данных, Trueв противном случае (т. е. эквивалент unique_justseen())
 - False если этот элемент ранее уже встречался где-либо во входных данных,
 True в противном случае (т. е. эквивалент unique_everseen())

 from more_itertools import classify_unique

 list(classify_unique('otto'))  # -> [('o', True, True), ('t', True, True), ('t', False, False), ('o', True, False)]
 # [('o', True,  True),
    ('t', True,  True),
    ('t', False, False),
    ('o', True,  False)]

 Исходник:
 def classify_unique(iterable, key=None):
     seen_set = set()
     seen_list = []
     use_key = key is not None
     previous = None

     for i, element in enumerate(iterable):
         k = key(element) if use_key else element
         is_unique_justseen = not i or previous != k
         previous = k
         is_unique_everseen = False
         try:
             if k not in seen_set:
                 seen_set.add(k)
                 is_unique_everseen = True
         except TypeError:
             if k not in seen_list:
                 seen_list.append(k)
                 is_unique_everseen = True
         yield element, is_unique_justseen, is_unique_everseen

________________________________________________________________________________________________________________________
 more_itertools.longest_common_prefix(iterables) - Возвращает элементы самого длинного общего префикса среди заданных итераций .

 from more_itertools import longest_common_prefix

 ''.join(longest_common_prefix(['abcd', 'abc', 'abf']))  # -> 'ab'

 Исходник:
 from itertools import takewhile
 from more_itertools import all_equal

 def longest_common_prefix(iterables):
     return (c[0] for c in takewhile(all_equal, zip(*iterables)))

________________________________________________________________________________________________________________________
 more_itertools.takewhile_inclusive(predicate, iterable) - Вариант takewhile(), который возвращает один дополнительный элемент.

 from more_itertools import takewhile_inclusive
 from itertools import takewhile

 list(takewhile_inclusive(lambda x: x < 5, [1, 4, 6, 4, 1]))  # -> [1, 4, 6]       # takewhile_inclusive
 list(takewhile(lambda x: x < 5, [1, 4, 6, 4, 1]))            # -> [1, 4]          # takewhile

 Исходник:
 def takewhile_inclusive(predicate, iterable):
     for x in iterable:
         yield x
         if not predicate(x):
             break

________________________________________________________________________________________________________________________
 Itertools recipes
 more_itertools.nth(iterable, n, default=None) - Возвращает n-й элемент или значение по умолчанию.

 from more_itertools import nth

 l = range(10)
 nth(l, 3)            # ->  3
 nth(l, 8)            # ->  8
 nth(l, 20, "zebra")  # -> 'zebra'
 nth(l, 20)           # -> None


 Исходник:
 from itertools import islice

 def nth(iterable, n, default=None):
     return next(islice(iterable, n, None), default)

________________________________________________________________________________________________________________________
 more_itertools.before_and_after(predicate, it) - Вариант takewhile(), обеспечивающий полный доступ к оставшейся части итератора.
 Обратите внимание, что первый итератор должен быть полностью использован, прежде чем второй итератор сможет
 генерировать действительные результаты.

 from more_itertools import before_and_after

 it = iter('ABCdEfGhI')
 all_upper, remainder = before_and_after(str.isupper, it)
 ''.join(all_upper)  # -> 'ABC'

 ''.join(remainder) # takewhile() would lose the 'd'
 # 'dEfGhI'

 from itertools import takewhile

 iterable = [1, 2, 3, 4]
 firsst, lastt = before_and_after(lambda x: x < 3, iterable)
 list(firsst), list(lastt)                      # ->  [1, 2] [3, 4]   # before_and_after
 list(takewhile(lambda x: x < 3, iterable))     # ->  [1, 2]          # takewhile

 Исходник:
 from itertools import chain

 def before_and_after(predicate, it):
     it = iter(it)
     transition = []

     def true_iterator():
         for elem in it:
             if predicate(elem):
                 yield elem
             else:
                 transition.append(elem)
                 return

     # Note: this is different from itertools recipes to allow nesting
     # before_and_after remainders into before_and_after again. See tests
     # for an example.
     remainder_iterator = chain(transition, it)

     return true_iterator(), remainder_iterator

________________________________________________________________________________________________________________________
 more_itertools.take(n, iterable) - Возвращает первые n элементов итерируемого объекта в виде списка.

 from more_itertools import take

 take(3, range(10))  # -> [0, 1, 2]

 iterable = [1, 2, 3, 4, 5]
 take(2, iterable)  # -> [1, 2]
t ake(4, iterable)  # -> [1, 2, 3, 4]

 Если в итерации меньше n элементов, возвращаются все они.

 take(10, range(3))  # -> [0, 1, 2]

 Исходник:
 from itertools import islice

 def take(n, iterable):
     return list(islice(iterable, n))

________________________________________________________________________________________________________________________
 more_itertools.tail(n, iterable) - Возвращает итератор для последних n элементов iterable .

 from more_itertools import tail

 t = tail(3, 'ABCDEFG')
 list(t)  # -> ['E', 'F', 'G']

 iterable = [1, 2, 3, 4]
 list(tail(2, iterable))  # -> [3, 4]
 list(tail(3, iterable))  # -> [2, 3, 4]

 Исходник:
 from collections.abc import Sized
 from itertools import islice
 from collections import deque

 def tail(n, iterable):
     # If the given iterable has a length, then we can use islice to get its
     # final elements. Note that if the iterable is not actually Iterable,
     # either islice or deque will throw a TypeError. This is why we don't
     # check if it is Iterable.
     if isinstance(iterable, Sized):
         yield from islice(iterable, max(0, len(iterable) - n), None)
     else:
         yield from iter(deque(iterable, maxlen=n))

________________________________________________________________________________________________________________________
 more_itertools.unique_everseen(iterable, key=None) - Создавайте уникальные элементы, сохраняя порядок.

 from more_itertools import unique_everseen

 list(unique_everseen('AAAABBBCCDAABBB'))     # -> ['A', 'B', 'C', 'D']
 list(unique_everseen('ABBCcAD', str.lower))  # -> ['A', 'B', 'C', 'D']

 Можно использовать последовательности со смесью хешируемых и нехэшируемых элементов. Функция будет медленнее
 (т. е. O(n^2) ) для нехэшируемых элементов.

 Помните, что list объекты не хешируются — вы можете использовать параметр key для преобразования списка в кортеж
 (который хешируется), чтобы избежать замедления работы.

 iterable = ([1, 2], [2, 3], [1, 2])
 list(unique_everseen(iterable))  # Slow                <-----
 # [[1, 2], [2, 3]]
 list(unique_everseen(iterable, key=tuple))  # Faster   <-----
 # [[1, 2], [2, 3]]

 В основном tuple самый быстрый, можно самому еще потестить варианты
 a_list = ([1, 2], [2, 3], [1, 2])
 print(timeit('list(unique_everseen(a_list))', globals=globals()))             # ->  3.41782069997862    <-----
 print(timeit('list(unique_everseen(a_list, key=tuple))', globals=globals()))  # ->  1.4006470999447629  <-----

 a_set = ({1, 2}, {2, 3}, {1, 2})
 timeit('list(unique_everseen(a_set))', globals=globals())                 # ->  4.487388600013219   <-----
 timeit('list(unique_everseen(a_set, key=frozenset))', globals=globals())  # ->  1.4916451999451965  <-----

 Аналогичным образом вы можете захотеть преобразовать нехэшируемые set объекты с помощью key=frozenset.
 Для dict объектов можно использовать  key=lambda x: frozenset(x.items())

 Исходник:
 def unique_everseen(iterable, key=None):
     seenset = set()
     seenset_add = seenset.add
     seenlist = []
     seenlist_add = seenlist.append
     use_key = key is not None

     for element in iterable:
         k = key(element) if use_key else element
         try:
             if k not in seenset:
                 seenset_add(k)
                 yield element
         except TypeError:
             if k not in seenlist:
                 seenlist_add(k)
                 yield element

________________________________________________________________________________________________________________________
 more_itertools.unique_justseen(iterable, key=None) - Выдает элементы по порядку, игнорируя серийные дубликаты.

 from more_itertools import unique_justseen

 list(unique_justseen('AAAABBBCCDAABBB'))     # -> ['A', 'B', 'C', 'D', 'A', 'B']
 list(unique_justseen('ABBCcAD', str.lower))  # -> ['A', 'B', 'C', 'A', 'D']

 Исходник:
 import operator
 from itertools import groupby

 def unique_justseen(iterable, key=None):
     if key is None:
         return map(operator.itemgetter(0), groupby(iterable))

     return map(next, map(operator.itemgetter(1), groupby(iterable, key)))


________________________________________________________________________________________________________________________
 --- Комбинаторика     Combinatorics ---

 --- Эти инструменты позволяют создавать комбинаторные расположения элементов из итераций ---

 --- These tools yield combinatorial arrangements of items from iterables. ---
________________________________________________________________________________________________________________________
 more_itertools.distinct_permutations(iterable, r=None) - Получите последовательные различные перестановки элементов в iterable .

 from more_itertools import distinct_permutations

 sorted(distinct_permutations([1, 0, 1]))  # -> [(0, 1, 1), (1, 0, 1), (1, 1, 0)]

 Эквивалентно set(permutations(iterable)), за исключением того, что дубликаты не создаются и не выбрасываются.
 Для больших входных последовательностей это гораздо более эффективно.

 Повторяющиеся перестановки возникают, когда во входной итерации присутствуют повторяющиеся элементы. Количество
 возвращенных товаров равно n! / (x_1! * x_2! * … * x_n!) , где n — общее количество входных элементов,
 а каждый x_i — это количество отдельных элементов во входной последовательности.

 Если задан r , получаются только перестановки длины r .

 sorted(distinct_permutations([1, 0, 1], r=2))  # -> [(0, 1), (1, 0), (1, 1)]
 sorted(distinct_permutations(range(3), r=2))   # -> [(0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1)]

 Исходник:
 def distinct_permutations(iterable, r=None):

     # Algorithm: https://w.wiki/Qai
     def _full(A):
         while True:
             # Yield the permutation we have
             yield tuple(A)

             # Find the largest index i such that A[i] < A[i + 1]
             for i in range(size - 2, -1, -1):
                 if A[i] < A[i + 1]:
                     break
             #  If no such index exists, this permutation is the last one
             else:
                 return

             # Find the largest index j greater than j such that A[i] < A[j]
             for j in range(size - 1, i, -1):
                 if A[i] < A[j]:
                     break

             # Swap the value of A[i] with that of A[j], then reverse the
             # sequence from A[i + 1] to form the new permutation
             A[i], A[j] = A[j], A[i]
             A[i + 1 :] = A[: i - size : -1]  # A[i + 1:][::-1]

     # Algorithm: modified from the above
     def _partial(A, r):
         # Split A into the first r items and the last r items
         head, tail = A[:r], A[r:]
         right_head_indexes = range(r - 1, -1, -1)
         left_tail_indexes = range(len(tail))

         while True:
             # Yield the permutation we have
             yield tuple(head)

             # Starting from the right, find the first index of the head with
             # value smaller than the maximum value of the tail - call it i.
             pivot = tail[-1]
             for i in right_head_indexes:
                 if head[i] < pivot:
                     break
                 pivot = head[i]
             else:
                 return

             # Starting from the left, find the first value of the tail
             # with a value greater than head[i] and swap.
             for j in left_tail_indexes:
                 if tail[j] > head[i]:
                     head[i], tail[j] = tail[j], head[i]
                     break
             # If we didn't find one, start from the right and find the first
             # index of the head with a value greater than head[i] and swap.
             else:
                 for j in right_head_indexes:
                     if head[j] > head[i]:
                         head[i], head[j] = head[j], head[i]
                         break

             # Reverse head[i + 1:] and swap it with tail[:r - (i + 1)]
             tail += head[: i - r : -1]  # head[i + 1:][::-1]
             i += 1
             head[i:], tail[:] = tail[: r - i], tail[r - i :]

     items = sorted(iterable)

     size = len(items)
     if r is None:
         r = size

     if 0 < r <= size:
         return _full(items) if (r == size) else _partial(items, r)

     return iter(() if r else ((),))

________________________________________________________________________________________________________________________
 more_itertools.distinct_combinations(iterable, r) - Получите различные комбинации из r элементов, взятых из iterable .

 from more_itertools import distinct_combinations

 list(distinct_combinations([0, 0, 1], 2))  # -> [(0, 0), (0, 1)]

 Эквивалентно set(combinations(iterable)), за исключением того, что дубликаты не создаются и не выбрасываются.
 Для больших входных последовательностей это гораздо более эффективно.


 Исходник:
 from operator import itemgetter
 from more_itertools import unique_everseen

 def distinct_combinations(iterable, r):
     if r < 0:
         raise ValueError('r must be non-negative')
     elif r == 0:
         yield ()
         return
     pool = tuple(iterable)
     generators = [unique_everseen(enumerate(pool), key=itemgetter(1))]
     current_combo = [None] * r
     level = 0
     while generators:
         try:
             cur_idx, p = next(generators[-1])
         except StopIteration:
             generators.pop()
             level -= 1
             continue
         current_combo[level] = p
         if level + 1 == r:
             yield tuple(current_combo)
         else:
             generators.append(
                 unique_everseen(
                     enumerate(pool[cur_idx + 1 :], cur_idx + 1),
                     key=itemgetter(1),
                 )
             )
             level += 1

________________________________________________________________________________________________________________________
 more_itertools.nth_combination_with_replacement(iterable, r, index) Эквивалентно:

 list(combinations_with_replacement(iterable, r))[index]

 Подпоследовательности с повторением итераций длиной r можно упорядочить лексикографически.
 nth_combination_with_replacement() вычисляет подпоследовательность по индексу позиции сортировки напрямую,
 без вычисления предыдущих подпоследовательностей с заменой.

 from more_itertools import nth_combination_with_replacement

 nth_combination_with_replacement(range(5), 3, 5)   # -> (0, 1, 1)
 nth_combination_with_replacement(range(5), -1, 5)  # -> ValueError

 Исходник:
 from math import comb

 def nth_combination_with_replacement(iterable, r, index):
     pool = tuple(iterable)
     n = len(pool)
     if (r < 0) or (r > n):
         raise ValueError

     c = comb(n + r - 1, r)

     if index < 0:
         index += c

     if (index < 0) or (index >= c):
         raise IndexError

     result = []
     i = 0
     while r:
         r -= 1
         while n >= 0:
             num_combs = comb(n + r - 1, r)
             if index < num_combs:
                 break
             n -= 1
             i += 1
             index -= num_combs
         result.append(pool[i])

     return tuple(result)

________________________________________________________________________________________________________________________
 more_itertools.circular_shifts(iterable) - Возвращает список циклических сдвигов iterable .

 from more_itertools import circular_shifts

 circular_shifts(range(4))  # -> [(0, 1, 2, 3), (1, 2, 3, 0), (2, 3, 0, 1), (3, 0, 1, 2)]
 my_iterable = [1, 2, 3]
 circular_shifts(iterable=my_iterable)  # -> [(1, 2, 3), (2, 3, 1), (3, 1, 2)]

 Исходник:
 from more_itertools import take, windowed
 from itertools import cycle

 def circular_shifts(iterable):
     lst = list(iterable)
     return take(len(lst), windowed(cycle(lst), len(lst)))

________________________________________________________________________________________________________________________
 more_itertools.partitions(iterable) - Выдать все возможные разделы iterable , сохраняющие порядок .
 Это не связано с partition().

 from more_itertools import partitions

 iterable = 'abc'
 for part in partitions(iterable):
     print([''.join(p) for p in part])
 ['abc']
 ['a', 'bc']
 ['ab', 'c']
 ['a', 'b', 'c']

 iterable = [1, 2, 3]
 list(partitions(iterable=iterable))  # -> [[[1, 2, 3]], [[1], [2, 3]], [[1, 2], [3]], [[1], [2], [3]]]

 Исходник:
 from more_itertools import powerset

 def partitions(iterable):
     sequence = list(iterable)
     n = len(sequence)
     for i in powerset(range(1, n)):
         yield [sequence[i:j] for i, j in zip((0,) + i, i + (n,))]

________________________________________________________________________________________________________________________
 more_itertools.set_partitions(iterable, k=None) - Разбейте множество разделов итерируемого объекта на k частей.
 Установленные разделы не сохраняют порядок.

 from more_itertools import set_partitions

 iterable = 'abc'
 for part in set_partitions(iterable, 2):
     print([''.join(p) for p in part])
 ['a', 'bc']
 ['ab', 'c']
 ['b', 'ac']

 Если k не задан, генерируется каждый раздел набора.

 iterable = 'abc'
 for part in set_partitions(iterable):
     print([''.join(p) for p in part])
 ['abc']
 ['a', 'bc']
 ['ab', 'c']
 ['b', 'ac']
 ['a', 'b', 'c']

 Исходник:
 def set_partitions(iterable, k=None):
     L = list(iterable)
     n = len(L)
     if k is not None:
         if k < 1:
             raise ValueError(
                 "Can't partition in a negative or zero number of groups"
             )
         elif k > n:
             return

     def set_partitions_helper(L, k):
         n = len(L)
         if k == 1:
             yield [L]
         elif n == k:
             yield [[s] for s in L]
         else:
             e, *M = L
             for p in set_partitions_helper(M, k - 1):
                 yield [[e], *p]
             for p in set_partitions_helper(M, k):
                 for i in range(len(p)):
                     yield p[:i] + [[e] + p[i]] + p[i + 1 :]

     if k is None:
         for k in range(1, n + 1):
             yield from set_partitions_helper(L, k)
     else:
         yield from set_partitions_helper(L, k)

________________________________________________________________________________________________________________________
 more_itertools.product_index(element, *args) - Эквивалентно:  list(product(*args)).index(element)   Произведения args
 можно упорядочить лексикографически. product_index()вычисляет первый индекс элемента без вычисления предыдущих продуктов.

 from more_itertools import product_index

 product_index([8, 2], range(10), range(5))    # -> 42
 product_index([1, 3], [2, 2], [1, 3])         # -> ValueError: tuple.index(x): x not in tuple

 Исходник:
 from itertools import zip_longest

 _marker = object()

 def product_index(element, *args):
     index = 0

     for x, pool in zip_longest(element, args, fillvalue=_marker):
         if x is _marker or pool is _marker:
             raise ValueError('element is not a product of args')

         pool = tuple(pool)
         index = index * len(pool) + pool.index(x)

     return index

________________________________________________________________________________________________________________________
 more_itertools.combination_index(element, iterable) - Эквивалентно:  list(combinations(iterable, r)).index(element)
 Подпоследовательности итерации длиной r можно упорядочить лексикографически. combination_index() вычисляет индекс
 первого элемента без вычисления предыдущих комбинаций.

 from more_itertools import combination_index

 combination_index('adf', 'abcdefg')  # -> 10
 combination_index('adf', 'abc')      # -> ValueError: element is not a combination of iterable

 Исходник:
 from more_itertools import last
 from math import comb

 def combination_index(element, iterable):
     element = enumerate(element)
     k, y = next(element, (None, None))
     if k is None:
         return 0

     indexes = []
     pool = enumerate(iterable)
     for n, x in pool:
         if x == y:
             indexes.append(n)
             tmp, y = next(element, (None, None))
             if tmp is None:
                 break
             else:
                 k = tmp
     else:
         raise ValueError('element is not a combination of iterable')

     n, _ = last(pool, default=(n, None))

     # Python versions below 3.8 don't have math.comb
     index = 1
     for i, j in enumerate(reversed(indexes), start=1):
         j = n - j
         if i <= j:
             index += comb(j, i)

     return comb(n + 1, k + 1) - index

________________________________________________________________________________________________________________________
 more_itertools.permutation_index(element, iterable) - Эквивалентно:  list(permutations(iterable, r)).index(element)`
 Подпоследовательности итерации длиной r , где порядок важен, можно упорядочить лексикографически. permutation_index()
 вычисляет индекс первого элемента напрямую, без вычисления предыдущих перестановок.

 from more_itertools import permutation_index

 permutation_index([1, 3, 2], range(5))  # -> 19
 permutation_index([1, 3, 2], [1, 2])    # -> ValueError: 3 is not in list

 Исходник:
 def permutation_index(element, iterable):
     index = 0
     pool = list(iterable)
     for i, x in zip(range(len(pool), -1, -1), element):
         r = pool.index(x)
         index = index * i + r
         del pool[r]

     return index

________________________________________________________________________________________________________________________
 more_itertools.combination_with_replacement_index(element, iterable) - Подпоследовательности с повторением итераций
 длиной r можно упорядочить лексикографически. combination_with_replacement_index() вычисляет индекс первого элемента ,
 не вычисляя предыдущие комбинации с заменой.

 from more_itertools import combination_with_replacement_index

 combination_with_replacement_index('adf', 'abcdefg')  # -> 20
 combination_with_replacement_index('adf', 'ac') # -> ValueError: element is not a combination with replacement of iterable

 Исходник:
 from math import comb

 def combination_with_replacement_index(element, iterable):
     element = tuple(element)
     l = len(element)
     element = enumerate(element)

     k, y = next(element, (None, None))
     if k is None:
         return 0

     indexes = []
     pool = tuple(iterable)
     for n, x in enumerate(pool):
         while x == y:
             indexes.append(n)
             tmp, y = next(element, (None, None))
             if tmp is None:
                 break
             else:
                 k = tmp
         if y is None:
             break
     else:
         raise ValueError(
             'element is not a combination with replacement of iterable'
         )

     n = len(pool)
     occupations = [0] * n
     for p in indexes:
         occupations[p] += 1

     index = 0
     cumulative_sum = 0
     for k in range(1, n):
         cumulative_sum += occupations[k - 1]
         j = l + n - 1 - k - cumulative_sum
         i = n - k
         if i <= j:
             index += comb(j, i)

     return index

________________________________________________________________________________________________________________________
 more_itertools.gray_product(*iterables) - Аналогично itertools.product(), но возвращает кортежи в таком порядке,
 что только один элемент в сгенерированном кортеже изменяется от одной итерации к другой.

 from more_itertools import gray_product

 list(gray_product('AB','CD'))  # -> [('A', 'C'), ('B', 'C'), ('B', 'D'), ('A', 'D')]

 Эта функция обрабатывает все входные итерации перед выдачей выходных данных. Если какая-либо из входных итераций
 содержит менее двух элементов, ValueError вызывается.

 list(gray_product([1, 2], [2]))  # -> ValueError: each iterable must have two or more items

 # Сравнение с product
 from itertools import product

 list(gray_product([1, 2], [2, 3]))  # -> [(1, 2), (2, 2), (2, 3), (1, 3)]      gray_product
 list(product([1, 2], [2, 3]))       # -> [(1, 2), (1, 3), (2, 2), (2, 3)]      product

 Информацию об алгоритме можно найти в книге Дональда Кнута  «Искусство компьютерного программирования» .

 Исходник:
 def gray_product(*iterables):
     all_iterables = tuple(tuple(x) for x in iterables)
     iterable_count = len(all_iterables)
     for iterable in all_iterables:
         if len(iterable) < 2:
             raise ValueError("each iterable must have two or more items")

     # This is based on "Algorithm H" from section 7.2.1.1, page 20.
     # a holds the indexes of the source iterables for the n-tuple to be yielded
     # f is the array of "focus pointers"
     # o is the array of "directions"
     a = [0] * iterable_count
     f = list(range(iterable_count + 1))
     o = [1] * iterable_count
     while True:
         yield tuple(all_iterables[i][a[i]] for i in range(iterable_count))
         j = f[0]
         f[0] = 0
         if j == iterable_count:
             break
         a[j] = a[j] + o[j]
         if a[j] == 0 or a[j] == len(all_iterables[j]) - 1:
             o[j] = -o[j]
             f[j] = f[j + 1]
             f[j + 1] = j + 1

________________________________________________________________________________________________________________________
 more_itertools.outer_product(func, xs, ys, *args, **kwargs) - Обобщенный внешний продукт, который применяет бинарную
 функцию ко всем парам элементов. Возвращает двумерную матрицу со len(xs)строками и len(ys) столбцами.
 Также принимает *argsи **kwargsте, которые передаются в func.

 Таблица умножения:

 from more_itertools import outer_product
 from operator import mul

 list(outer_product(mul, range(1, 4), range(1, 6)))  # -> [(1, 2, 3, 4, 5), (2, 4, 6, 8, 10), (3, 6, 9, 12, 15)]

 Кросстабуляция:

 xs = ['A', 'B', 'A', 'A', 'B', 'B', 'A', 'A', 'B', 'B']
 ys = ['X', 'X', 'X', 'Y', 'Z', 'Z', 'Y', 'Y', 'Z', 'Z']
 rows = list(zip(xs, ys))
 count_rows = lambda x, y: rows.count((x, y))
 list(outer_product(count_rows, sorted(set(xs)), sorted(set(ys))))  # -> [(2, 3, 0), (1, 0, 4)]

 Использование с *argsи **kwargs:

 animals = ['cat', 'wolf', 'mouse']
 list(outer_product(min, animals, animals, key=len))
 # [('cat', 'cat', 'cat'), ('cat', 'wolf', 'wolf'), ('cat', 'wolf', 'mouse')]

 Исходник:
 from itertools import starmap
 from more_itertools import batched

 def outer_product(func, xs, ys, *args, **kwargs):
     ys = tuple(ys)
     return batched(
         starmap(lambda x, y: func(x, y, *args, **kwargs), product(xs, ys)),
         n=len(ys),
     )

________________________________________________________________________________________________________________________
 Itertools recipes
 more_itertools.powerset(iterable) - Возвращает все возможные подмножества итерируемого объекта.

 from more_itertools import powerset

 list(powerset([1, 2, 3]))  # -> [(), (1,), (2,), (3,), (1, 2), (1, 3), (2, 3), (1, 2, 3)]

 powerset()будет работать с итерациями, которые не являются set экземплярами, поэтому повторяющиеся элементы на входе
 будут создавать повторяющиеся элементы на выходе. Используйте unique_everseen()на входе, чтобы избежать создания дубликатов:

 seq = [1, 1, 0]
 list(powerset(seq))                   # ->  [(), (1,), (1,), (0,), (1, 1), (1, 0), (1, 0), (1, 1, 0)]

 from more_itertools import unique_everseen
 list(powerset(unique_everseen(seq)))  # -> [(), (1,), (0,), (1, 0)]

 Исходник:
 from itertools import chain, combinations

 def powerset(iterable):
     s = list(iterable)
     return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))

________________________________________________________________________________________________________________________
 more_itertools.random_product(*args, repeat=1) - Нарисуйте случайный элемент из каждой входной итерации.

 from more_itertools import random_product

 random_product('abc', range(4), 'XYZ')  # -> ('c', 3, 'Z')

 Если в качестве аргумента ключевого слова указано повторение , из каждой итерации будет взято такое количество элементов.

 random_product('abcd', range(4), repeat=2)  # -> ('a', 2, 'd', 3)

 Это эквивалентно случайному выбору из  itertools.product(*args, **kwarg)

 Исходник:
 from random import choice

 def random_product(*args, repeat=1):
     pools = [tuple(pool) for pool in args] * repeat
     return tuple(choice(pool) for pool in pools)

________________________________________________________________________________________________________________________
 more_itertools.random_permutation(iterable, r=None) - Возвращает случайную перестановку элементов длины r в iterable .

 Если r не указан или равен None, то по умолчанию r равна длине итерируемого объекта .

 from more_itertools import random_permutation

 random_permutation(range(5))  # -> (3, 4, 0, 1, 2)

 Это эквивалентно случайному выбору из itertools.permutations(iterable, r)

 Исходник:
 from more_itertools import sample

 def random_permutation(iterable, r=None):
     pool = tuple(iterable)
     r = len(pool) if r is None else r
     return tuple(sample(pool, r))

________________________________________________________________________________________________________________________
 more_itertools.random_combination(iterable, r) - Возвращает случайную подпоследовательность элементов длины r в iterable .


 from more_itertools import random_combination

 random_combination(range(5), 3)  # -> (2, 3, 4)

 Это эквивалентно случайному выбору из  itertools.combinations(iterable, r)

 Исходник:
 from more_itertools import sample

 def random_combination(iterable, r):
     pool = tuple(iterable)
     n = len(pool)
     indices = sorted(sample(range(n), r))
     return tuple(pool[i] for i in indices)

________________________________________________________________________________________________________________________
 more_itertools.random_combination_with_replacement(iterable, r) - Возвращает случайную подпоследовательность элементов
 длины r в iterable , позволяя повторять отдельные элементы.

 from more_itertools import random_combination_with_replacement

 random_combination_with_replacement(range(3), 5)  # -> (0, 0, 1, 2, 2)

 Это эквивалентно случайному выбору из  itertools.combinations_with_replacement(iterable, r)

 Исходник:
 from random import randrange

 def random_combination_with_replacement(iterable, r):
     pool = tuple(iterable)
     n = len(pool)
     indices = sorted(randrange(n) for i in range(r))
     return tuple(pool[i] for i in indices)

_______________________________________________________________________________________________________________________
 more_itertools.nth_product(index, *args) - Эквивалентно:  list(product(*args))[index].
 Произведения args можно упорядочить лексикографически. nth_product()вычисляет продукт по индексу позиции сортировки ,
 не вычисляя предыдущие продукты.

 from more_itertools import nth_product

 nth_product(8, range(2), range(2), range(2), range(2))    # -> (1, 0, 0, 0)
 nth_product(888, range(2), range(2), range(2), range(2))  # -> IndexError

 IndexError будет поднят, если данный индекс недействителен.

 Исходник:
 from functools import reduce

 def nth_product(index, *args):
     pools = list(map(tuple, reversed(args)))
     ns = list(map(len, pools))

     c = reduce(mul, ns)

     if index < 0:
         index += c

     if not 0 <= index < c:
         raise IndexError

     result = []
     for pool, n in zip(pools, ns):
         result.append(pool[index % n])
         index //= n

     return tuple(reversed(result))

________________________________________________________________________________________________________________________
 more_itertools.nth_permutation(iterable, r, index) - Эквивалентно:  list(permutations(iterable, r))[index]
 Подпоследовательности итерации длиной r , где порядок важен, можно упорядочить лексикографически. nth_permutation()
 вычисляет подпоследовательность по индексу позиции сортировки напрямую, без вычисления предыдущих подпоследовательностей.

 from more_itertools import nth_permutation

 nth_permutation('ghijk', 2, 5)  # -> ('h', 'i')

 ValueError будет повышен, если r отрицательное значение или больше длины итерируемого объекта .
 IndexError будет поднят, если данный индекс недействителен.

 nth_permutation('ghijk', -2, 5)  # -> ValueError
 nth_permutation('ghijk', 2, 50)  # -> IndexError

 Исходник:
 from math import factorial, perm

 def nth_permutation(iterable, r, index):
     pool = list(iterable)
     n = len(pool)

     if r is None or r == n:
         r, c = n, factorial(n)
     elif not 0 <= r < n:
         raise ValueError
     else:
         c = perm(n, r)

     if index < 0:
         index += c

     if not 0 <= index < c:
         raise IndexError

     if c == 0:
         return tuple()

     result = [0] * r
     q = index * factorial(n) // c if r < n else index
     for d in range(1, n + 1):
         q, i = divmod(q, d)
         if 0 <= n - d < r:
             result[n - d] = i
         if q == 0:
             break

     return tuple(map(pool.pop, result))

________________________________________________________________________________________________________________________
 more_itertools.nth_combination(iterable, r, index) - Эквивалентно:  list(combinations(iterable, r))[index]
 Подпоследовательности итерации длиной r можно упорядочить лексикографически. nth_combination() вычисляет
 подпоследовательность по индексу позиции сортировки напрямую, без вычисления предыдущих подпоследовательностей.

 from more_itertools import nth_combination

 nth_combination(range(5), 3, 5)  # -> (0, 3, 4)

 ValueError будет повышен, если r отрицательное значение или больше длины итерируемого объекта .
 IndexError будет поднят, если данный индекс недействителен.

 nth_combination(range(5), -3, 5)  # -> ValueError
 nth_combination(range(5), 3, 50)  # -> IndexError

 Исходник:
 def nth_combination(iterable, r, index):
     pool = tuple(iterable)
     n = len(pool)
     if (r < 0) or (r > n):
         raise ValueError

     c = 1
     k = min(r, n - r)
     for i in range(1, k + 1):
         c = c * (n - k + i) // i

     if index < 0:
         index += c

     if (index < 0) or (index >= c):
         raise IndexError

     result = []
     while r:
         c, n, r = c * r // n, n - 1, r - 1
         while index >= c:
             index -= c
             c, n = c * (n - r) // n, n - 1
         result.append(pool[-1 - n])

     return tuple(result)


________________________________________________________________________________________________________________________
 --- Оберточная бумага     Wrapping ---

 --- Эти инструменты предоставляют оболочки для облегчения работы с объектами, которые создают или потребляют итерации

 --- These tools provide wrappers to smooth working with objects that produce or consume iterables ---
________________________________________________________________________________________________________________________
 more_itertools.always_iterable(obj, base_type=(<class 'str'>, <class 'bytes'>)) - Если объект obj является итеративным,
 верните итератор по его элементам:

 from more_itertools import always_iterable

 obj = (1, 2, 3)
 list(always_iterable(obj))  # -> [1, 2, 3]

 Если obj не является итеративным, верните итерируемый объект из одного элемента, содержащий obj :

 obj = 1
 list(always_iterable(obj))  # -> [1]

 Если obj равен None, верните пустую итерацию:

 obj = None
 list(always_iterable(None))  # -> []

 По умолчанию двоичные и текстовые строки не считаются итерируемыми:

 obj = 'foo'
 list(always_iterable(obj))  # -> ['foo']

 Если установлен base_type, объекты, для которых isinstance(obj, base_type) возвращает True, не будут считаться итерируемыми.

 bj = {'a': 1}
 list(always_iterable(obj))  # Iterate over the dict's keys   Перебираем ключи dict
 ['a']
 list(always_iterable(obj, base_type=dict))  # Treat dicts as a unit    Рассматривать дикты как единое целое
 [{'a': 1}]

 Установите base_type во Noneизбежание какой-либо специальной обработки и рассматривайте объекты,
 которые Python считает итерируемыми, как итерируемые:

 obj = 'foo'
 list(always_iterable(obj, base_type=None))  # -> ['f', 'o', 'o']


 Исходник:
 def always_iterable(obj, base_type=(str, bytes)):
     if obj is None:
         return iter(())

     if (base_type is not None) and isinstance(obj, base_type):
         return iter((obj,))

     try:
         return iter(obj)
     except TypeError:
         return iter((obj,))

________________________________________________________________________________________________________________________
 more_itertools.always_reversible(iterable) - Расширение этого reversed() поддерживает все итерации,
 а не только те, которые реализуют протоколы Reversible или Sequence.

 from more_itertools import always_reversible

 print(*always_reversible(x for x in range(3)))  # -> 2 1 0

 Если итерация уже обратима, эта функция возвращает результат reversed(). Если итерация необратима,
 эта функция будет кэшировать оставшиеся элементы в итерации и возвращать их в обратном порядке,
 что может потребовать значительного объема памяти.

 Исходник:
 def always_reversible(iterable):
     try:
         return reversed(iterable)
     except TypeError:
         return reversed(list(iterable))

________________________________________________________________________________________________________________________
 more_itertools.countable(iterable) - Оберните итерацию и подсчитайте, сколько элементов было израсходовано.
 Атрибут items_seenначинается с 0и увеличивается по мере использования итерируемого объекта:

 from more_itertools import countable

 iterable = map(str, range(10))
 it = countable(iterable)
 it.items_seen  # -> 0
 next(it), next(it)
 ('0', '1')
 list(it)  # -> ['2', '3', '4', '5', '6', '7', '8', '9']
 it.items_seen  # -> 10

 Исходник:
 class countable:

     def __init__(self, iterable):
         self._it = iter(iterable)
         self.items_seen = 0

     def __iter__(self):
         return self

     def __next__(self):
         item = next(self._it)
         self.items_seen += 1

         return item

________________________________________________________________________________________________________________________
 more_itertools.consumer(func) - Декоратор, который автоматически перемещает «обратный итератор» в стиле PEP-342
 к его первой точке текучести, поэтому вам не придется вызывать для него next() вручную.

 from more_itertools import consumer

 @consumer
 def tally():
     i = 0
     while True:
         print('Thing number %s is %s.' % (i, (yield)))
         i += 1

 t = tally()
 t.send('red')    # ->  Thing number 0 is red.
 t.send('fish')   # ->  Thing number 1 is fish.

 Без декоратора вам пришлось бы вызвать, next(t) прежде чем можно было бы использовать t.send().

 Исходник:
 from functools import wraps

 def consumer(func):

     @wraps(func)
     def wrapper(*args, **kwargs):
         gen = func(*args, **kwargs)
         next(gen)
         return gen

     return wrapper

________________________________________________________________________________________________________________________
 more_itertools.with_iter(context_manager) - Оберните итерацию в withоператор, чтобы она закрывалась после исчерпания.
 Например, это закроет файл, когда итератор будет исчерпан:

 from more_itertools import with_iter

 upper_lines = (line.upper() for line in with_iter(open('foo')))

 Любой контекстный менеджер, который возвращает итерируемый объект, является кандидатом на использование with_iter.

 Исходник:
 def with_iter(context_manager):
     with context_manager as iterable:
         yield from iterable

________________________________________________________________________________________________________________________
 classmore_itertools.callback_iter(func, callback_kwd='callback', wait_seconds=0.1) - Преобразуйте функцию,
 использующую обратные вызовы, в итератор.
 Пусть func — это функция, которая принимает аргумент ключевого слова обратного вызова . Например:

 from more_itertools import callback_iter

 ef func(callback=None):
    for i, c in [(1, 'a'), (2, 'b'), (3, 'c')]:
        if callback:
            callback(i, c)
    return 4

 Используйте с callback_iter(func), чтобы получить итератор для параметров, которые доставляются в обратный вызов.

 with callback_iter(func) as it:
     for args, kwargs in it:
         print(args)
 (1, 'a')
 (2, 'b')
 (3, 'c')

 Функция будет вызываться в фоновом потоке. Свойство doneуказывает, завершилось ли выполнение.

 it.done  # -> True

 Если оно завершится успешно, его возвращаемое значение будет доступно в result свойстве.

 it.result  # -> 4

 Примечания:
 - Если функция помимо обратного вызова использует какой-либо аргумент ключевого слова, укажите callback_kwd.
 - Если он завершил выполнение, но вызвал исключение, доступ к свойству result вызовет то же исключение.
 - Если выполнение еще не завершено, доступ к свойству result из блока with вызовет ошибку RuntimeError.
 - Если выполнение еще не завершено, доступ к свойству result извне блока with вызовет исключение more_itertools.AbortThread.
 - Укажите wait_секунды, чтобы настроить частоту опроса вывода.

 Исходник Нее Он слабый:
 from queue import Queue, Empty

 class AbortThread(BaseException):
     pass

 class callback_iter:

     def __init__(self, func, callback_kwd='callback', wait_seconds=0.1):
         self._func = func
         self._callback_kwd = callback_kwd
         self._aborted = False
         self._future = None
         self._wait_seconds = wait_seconds
         # Lazily import concurrent.future
         self._executor = __import__(
             'concurrent.futures'
         ).futures.ThreadPoolExecutor(max_workers=1)
         self._iterator = self._reader()

     def __enter__(self):
         return self

     def __exit__(self, exc_type, exc_value, traceback):
         self._aborted = True
         self._executor.shutdown()

     def __iter__(self):
         return self

     def __next__(self):
         return next(self._iterator)

     @property
     def done(self):
         if self._future is None:
             return False
         return self._future.done()

     @property
     def result(self):
         if not self.done:
             raise RuntimeError('Function has not yet completed')

         return self._future.result()

     def _reader(self):
         q = Queue()

         def callback(*args, **kwargs):
             if self._aborted:
                 raise AbortThread('canceled by user')

             q.put((args, kwargs))

         self._future = self._executor.submit(
             self._func, **{self._callback_kwd: callback}
         )

         while True:
             try:
                 item = q.get(timeout=self._wait_seconds)
             except Empty:
                 pass
             else:
                 q.task_done()
                 yield item

             if self._future.done():
                 break

         remaining = []
         while True:
             try:
                 item = q.get_nowait()
             except Empty:
                 break
             else:
                 q.task_done()
                 remaining.append(item)
         q.join()
         yield from remaining

________________________________________________________________________________________________________________________
 Itertools recipes





  # ->

 Исходник:


________________________________________________________________________________________________________________________
 more_itertools.iter_except(func, exception, first=None) - Возвращает результаты функции неоднократно,
 пока не возникнет исключение. Преобразует интерфейс вызова до исключения в интерфейс итератора.
 Похож на iter(func, Sentinel), но для завершения цикла вместо дозорного используется исключение.

 from more_itertools import iter_except

 l = [0, 1, 2]
 list(iter_except(l.pop, IndexError))  # -> [2, 1, 0]

 l = [1, 2, 3, '...', 4, 5, 6]
 list(iter_except(lambda: 1 + l.pop(), (IndexError, TypeError)))  # -> [7, 6, 5]
 list(iter_except(lambda: 1 + l.pop(), (IndexError, TypeError)))  # -> [4, 3, 2]
 list(iter_except(lambda: 1 + l.pop(), (IndexError, TypeError)))  # -> []

 В качестве условия остановки можно указать несколько исключений:

 Исходник:
 def iter_except(func, exception, first=None):
     try:
         if first is not None:
             yield first()
         while 1:
             yield func()
     except exception:
         pass


________________________________________________________________________________________________________________________
 --- Другие     Others ---


________________________________________________________________________________________________________________________
 more_itertools.locate(iterable, pred=bool, window_size=None) - Возвращает индекс каждого элемента в итерируемом объекте,
 для которого возвращается pred True . По умолчанию pred использует bool(), который будет выбирать правдивые элементы:

 from more_itertools import locate

 list(locate([0, 1, 1, 0, 1, 0, 0]))[1, 2, 4]

 Установите для pred пользовательскую функцию, например, для поиска индексов для определенного элемента.

 list(locate(['a', 'b', 'c', 'b'], lambda x: x == 'b'))  # -> [1, 3]

 Если указан размер окна , то функция pred будет вызываться с таким количеством элементов.
 Это позволяет осуществлять поиск подпоследовательностей:

 iterable = [0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3]
 pred = lambda *args: args == (1, 2, 3)
 list(locate(iterable, pred=pred, window_size=3))  # -> [1, 5, 9]

 Используйте вместе с seekable() для поиска индексов и последующего извлечения связанных элементов:

 from itertools import count
 from more_itertools import seekable
 source = (3 * n + 1 if (n % 2) else n // 2 for n in count())
 it = seekable(source)
 pred = lambda x: x > 100
 indexes = locate(it, pred=pred)
 i = next(indexes)
 it.seek(i)
 next(it)  # -> 106

 Исходник:
 from more_itertools import windowed
 from itertools import compress, count, starmap

 _marker = object()

 def locate(iterable, pred=bool, window_size=None):
     if window_size is None:
         return compress(count(), map(pred, iterable))

     if window_size < 1:
         raise ValueError('window size must be at least 1')

     it = windowed(iterable, window_size, fillvalue=_marker)
     return compress(count(), starmap(pred, it))

________________________________________________________________________________________________________________________
 more_itertools.rlocate(iterable, pred=bool, window_size=None) - Получите индекс каждого элемента в итерации ,
 для которого pred возвращает значение True, начиная справа и двигаясь влево.

 По умолчанию pred использует bool(), который будет выбирать правдивые элементы:

 from more_itertools import rlocate

 list(rlocate([0, 1, 1, 0, 1, 0, 0]))  # Truthy at 1, 2, and 4

 Установите pred в пользовательскую функцию, например, для поиска индексов для определенного элемента:

 iterable = iter('abcb')
 pred = lambda x: x == 'b'
 list(rlocate(iterable, pred))  # -> [3, 1]

 Если указан размер окна , то функция pred будет вызываться с таким количеством элементов.
 Это позволяет осуществлять поиск подпоследовательностей:

 iterable = [0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3]
 pred = lambda *args: args == (1, 2, 3)
 list(rlocate(iterable, pred=pred, window_size=3))  # -> [9, 5, 1]

 Будьте осторожны: эта функция ничего не вернет для бесконечных итераций. Если итерация обратима, rlocate  перевернет ее
 и начнет искать справа. В противном случае он будет искать слева и возвращать результаты в обратном порядке.

 Исходник:
 from more_itertools import locate

 def rlocate(iterable, pred=bool, window_size=None):
     if window_size is None:
         try:
             len_iter = len(iterable)
             return (len_iter - i - 1 for i in locate(reversed(iterable), pred))
         except TypeError:
             pass

     return reversed(list(locate(iterable, pred, window_size)))

________________________________________________________________________________________________________________________
 more_itertools.replace(iterable, pred, substitutes, count=None, window_size=1) - Возвращает элементы из iterable ,
 заменяя элементы, для которых возвращается pred True , элементами из итерируемых заменителей .

 from more_itertools import replace

 iterable = [1, 1, 0, 1, 1, 0, 1, 1]
 pred = lambda x: x == 0
 substitutes = (2, 3)
 list(replace(iterable, pred, substitutes))  # -> [1, 1, 2, 3, 1, 1, 2, 3, 1, 1]

 Если задан счетчик , количество замен будет ограничено:

 iterable = [1, 1, 0, 1, 1, 0, 1, 1, 0]
 pred = lambda x: x == 0
 substitutes = [None]
 list(replace(iterable, pred, substitutes, count=2))  # -> [1, 1, None, 1, 1, None, 1, 1, 0]

 Используйте window_size для управления количеством элементов, передаваемых в качестве аргументов pred .
 Это позволяет находить и заменять подпоследовательности.

 iterable = [0, 1, 2, 5, 0, 1, 2, 5]
 window_size = 3
 pred = lambda *args: args == (0, 1, 2)  # 3 items passed to pred
 substitutes = [3, 4] # Splice in these items
 list(replace(iterable, pred, substitutes, window_size=window_size))  # -> [3, 4, 5, 3, 4, 5]

 Исходник:
 from more_itertools import windowed
 from itertools import chain

 _marker = object()

 def replace(iterable, pred, substitutes, count=None, window_size=1):
     if window_size < 1:
         raise ValueError('window_size must be at least 1')

     # Save the substitutes iterable, since it's used more than once
     substitutes = tuple(substitutes)

     # Add padding such that the number of windows matches the length of the
     # iterable
     it = chain(iterable, [_marker] * (window_size - 1))
     windows = windowed(it, window_size)

     n = 0
     for w in windows:
         # If the current window matches our predicate (and we haven't hit
         # our maximum number of replacements), splice in the substitutes
         # and then consume the following windows that overlap with this one.
         # For example, if the iterable is (0, 1, 2, 3, 4...)
         # and the window size is 2, we have (0, 1), (1, 2), (2, 3)...
         # If the predicate matches on (0, 1), we need to zap (0, 1) and (1, 2)
         if pred(*w):
             if (count is None) or (n < count):
                 n += 1
                 yield from substitutes
                 consume(windows, window_size - 1)
                 continue

         # If there was no match (or we've reached the replacement limit),
         # yield the first item from the window.
         if w and (w[0] is not _marker):
             yield w[0]

________________________________________________________________________________________________________________________
 more_itertools.numeric_range(stop)
 more_itertools.numeric_range(start, stop[, step]) - Расширение встроенной range() функции,
 аргументы которой могут быть любого упорядочиваемого числового типа.

 Если указана только остановка , значение по умолчанию для начала0 и значение по умолчанию для шага 1 .
 Выходные элементы будут соответствовать типу остановки :

 from more_itertools import numeric_range

 list(numeric_range(3.5))  # -> [0.0, 1.0, 2.0, 3.0]

 Если указаны только начало и остановка , шаг по умолчанию равен 1. Выходные элементы будут соответствовать типу start :

 from decimal import Decimal
 start = Decimal('2.1')
 stop = Decimal('5.1')
 list(numeric_range(start, stop))  # -> [Decimal('2.1'), Decimal('3.1'), Decimal('4.1')]

 Если указаны start , stop и step , выходные элементы будут соответствовать типу: start + step

 from fractions import Fraction
 start = Fraction(1, 2)  # Start at 1/2
 stop = Fraction(5, 2)  # End at 5/2
 step = Fraction(1, 2)  # Count by 1/2
 list(numeric_range(start, stop, step))  # -> [Fraction(1, 2), Fraction(1, 1), Fraction(3, 2), Fraction(2, 1)]

 Если шаг равен нулю, ValueError повышается. Поддерживаются отрицательные шаги:

 list(numeric_range(3, -1, -1.0))  # -> [3.0, 2.0, 1.0, 0.0]
 list(numeric_range(3, -1, 0))     # -> ValueError: numeric_range() arg 3 must not be zero

 Помните об ограничениях чисел с плавающей запятой; представление полученных чисел может быть неожиданным.

 datetime.datetimeо бъекты могут использоваться для запуска и остановки , если шаг является datetime.timedeltaобъектом:

 import datetime
 start = datetime.datetime(2019, 1, 1)
 stop = datetime.datetime(2019, 1, 3)
 step = datetime.timedelta(days=1)
 items = iter(numeric_range(start, stop, step))
 next(items)  # -> datetime.datetime(2019, 1, 1, 0, 0)
 next(items)  # -> datetime.datetime(2019, 1, 2, 0, 0)

 Исходник Самый слабый:
 import abc
 from itertools import takewhile, count
 from functools import partial, cached_property
 from operator import lt, gt

 class numeric_range(abc.Sequence, abc.Hashable):

     _EMPTY_HASH = hash(range(0, 0))

     def __init__(self, *args):
         argc = len(args)
         if argc == 1:
             (self._stop,) = args
             self._start = type(self._stop)(0)
             self._step = type(self._stop - self._start)(1)
         elif argc == 2:
             self._start, self._stop = args
             self._step = type(self._stop - self._start)(1)
         elif argc == 3:
             self._start, self._stop, self._step = args
         elif argc == 0:
             raise TypeError(
                 'numeric_range expected at least '
                 '1 argument, got {}'.format(argc)
             )
         else:
             raise TypeError(
                 'numeric_range expected at most '
                 '3 arguments, got {}'.format(argc)
             )

         self._zero = type(self._step)(0)
         if self._step == self._zero:
             raise ValueError('numeric_range() arg 3 must not be zero')
         self._growing = self._step > self._zero

     def __bool__(self):
         if self._growing:
             return self._start < self._stop
         else:
             return self._start > self._stop

     def __contains__(self, elem):
         if self._growing:
             if self._start <= elem < self._stop:
                 return (elem - self._start) % self._step == self._zero
         else:
             if self._start >= elem > self._stop:
                 return (self._start - elem) % (-self._step) == self._zero

         return False

     def __eq__(self, other):
         if isinstance(other, numeric_range):
             empty_self = not bool(self)
             empty_other = not bool(other)
             if empty_self or empty_other:
                 return empty_self and empty_other  # True if both empty
             else:
                 return (
                     self._start == other._start
                     and self._step == other._step
                     and self._get_by_index(-1) == other._get_by_index(-1)
                 )
         else:
             return False

     def __getitem__(self, key):
         if isinstance(key, int):
             return self._get_by_index(key)
         elif isinstance(key, slice):
             step = self._step if key.step is None else key.step * self._step

             if key.start is None or key.start <= -self._len:
                 start = self._start
             elif key.start >= self._len:
                 start = self._stop
             else:  # -self._len < key.start < self._len
                 start = self._get_by_index(key.start)

             if key.stop is None or key.stop >= self._len:
                 stop = self._stop
             elif key.stop <= -self._len:
                 stop = self._start
             else:  # -self._len < key.stop < self._len
                 stop = self._get_by_index(key.stop)

             return numeric_range(start, stop, step)
         else:
             raise TypeError(
                 'numeric range indices must be '
                 'integers or slices, not {}'.format(type(key).__name__)
             )

     def __hash__(self):
         if self:
             return hash((self._start, self._get_by_index(-1), self._step))
         else:
             return self._EMPTY_HASH

     def __iter__(self):
         values = (self._start + (n * self._step) for n in count())
         if self._growing:
             return takewhile(partial(gt, self._stop), values)
         else:
             return takewhile(partial(lt, self._stop), values)

     def __len__(self):
         return self._len

     @cached_property
     def _len(self):
         if self._growing:
             start = self._start
             stop = self._stop
             step = self._step
         else:
             start = self._stop
             stop = self._start
             step = -self._step
         distance = stop - start
         if distance <= self._zero:
             return 0
         else:  # distance > 0 and step > 0: regular euclidean division
             q, r = divmod(distance, step)
             return int(q) + int(r != self._zero)

     def __reduce__(self):
         return numeric_range, (self._start, self._stop, self._step)

     def __repr__(self):
         if self._step == 1:
             return "numeric_range({}, {})".format(
                 repr(self._start), repr(self._stop)
             )
         else:
             return "numeric_range({}, {}, {})".format(
                 repr(self._start), repr(self._stop), repr(self._step)
             )

     def __reversed__(self):
         return iter(
             numeric_range(
                 self._get_by_index(-1), self._start - self._step, -self._step
             )
         )

     def count(self, value):
         return int(value in self)

     def index(self, value):
         if self._growing:
             if self._start <= value < self._stop:
                 q, r = divmod(value - self._start, self._step)
                 if r == self._zero:
                     return int(q)
         else:
             if self._start >= value > self._stop:
                 q, r = divmod(self._start - value, -self._step)
                 if r == self._zero:
                     return int(q)

         raise ValueError("{} is not in numeric range".format(value))

     def _get_by_index(self, i):
         if i < 0:
             i += self._len
         if i < 0 or i >= self._len:
             raise IndexError("numeric range object index out of range")
         return self._start + i * self._step

________________________________________________________________________________________________________________________
 more_itertools.side_effect(func, iterable, chunk_size=None, before=None, after=None) - Вызовите func
 для каждого элемента в итерации (или для каждой группы элементов chunk_size ) перед получением элемента.

 func должна быть функцией, принимающей один аргумент. Его возвращаемое значение будет отброшено.

 до и после — необязательные функции, не принимающие аргументов. Они будут выполнены до начала итерации и после
 ее окончания соответственно.

 Side_effect можно использовать для ведения журнала, обновления индикаторов выполнения или чего-либо еще,
 что не является функционально «чистым».

 Отправка сообщения о состоянии:

 from more_itertools import side_effect

 from more_itertools import consume
 func = lambda item: print('Received {}'.format(item))
 consume(side_effect(func, range(2)))

 Received 0
 Received 1

 Работа с фрагментами элементов:

 pair_sums = []
 func = lambda chunk: pair_sums.append(sum(chunk))
 list(side_effect(func, [0, 1, 2, 3, 4, 5], 2))  # -> [0, 1, 2, 3, 4, 5]
 list(pair_sums)  # -> [1, 5, 9]

 Запись в файлоподобный объект:

 from io import StringIO
 from more_itertools import consume
 f = StringIO()
 func = lambda x: print(x, file=f)
 before = lambda: print(u'HEADER', file=f)
 after = f.close
 it = [u'a', u'b', u'c']
 consume(side_effect(func, it, before=before, after=after))
 f.closed  # -> True

 Исходник:
 from more_itertools import chunked

 def side_effect(func, iterable, chunk_size=None, before=None, after=None):
     try:
         if before is not None:
             before()

         if chunk_size is None:
             for item in iterable:
                 func(item)
                 yield item
         else:
             for chunk in chunked(iterable, chunk_size):
                 func(chunk)
                 yield from chunk
     finally:
         if after is not None:
             after()

________________________________________________________________________________________________________________________
 more_itertools.iterate(func, start) - Возвращаться start, func(start), func(func(start)), ...

 from more_itertools import iterate

 from itertools import islice
 list(islice(iterate(lambda x: 2*x, 1), 10))  # -> [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]

 Исходник:
 def iterate(func, start):
     while True:
         yield start
         try:
             start = func(start)
         except StopIteration:
             break

________________________________________________________________________________________________________________________
 more_itertools.difference(iterable, func=operator.sub, *, initial=None) - Эта функция является обратной
 itertools.accumulate(). По умолчанию он вычисляет первую разницу итерируемого значения , используя operator.sub():

 from more_itertools import difference

 from itertools import accumulate
 iterable = accumulate([0, 1, 2, 3, 4])  # produces 0, 1, 3, 6, 10
 list(difference(iterable))                 # -> [0, 1, 2, 3, 4]
 list(accumulate([0, 1, 2, 3, 4]))          # -> [0, 1, 3, 6, 10]

 По умолчанию func имеет значение operator.sub(), но можно указать и другие функции. Они будут применяться следующим образом:

 A, B, C, D, ... --> A, func(B, A), func(C, B), func(D, C), ...

 Например, чтобы выполнить прогрессивное деление:

 iterable = [1, 2, 6, 24, 120]
 func = lambda x, y: x // y
 list(difference(iterable, func))  # -> [1, 2, 3, 4, 5]

 Если задано начальное ключевое слово, первый элемент будет пропущен при вычислении последовательных разностей.

 it = [10, 11, 13, 16]  # from accumulate([1, 2, 3], initial=10)
 list(difference(it, initial=10))  # -> [1, 2, 3]

 Исходник:
 from operator import sub
 from itertools import tee, chain

 def difference(iterable, func=sub, *, initial=None):
     a, b = tee(iterable)
     try:
         first = [next(b)]
     except StopIteration:
         return iter([])

     if initial is not None:
         first = []

     return chain(first, map(func, b, a))

________________________________________________________________________________________________________________________
 more_itertools.make_decorator(wrapping_func, result_index=0) - Возвращает декораторную версию wrapping_func , которая
 представляет собой функцию, изменяющую итерируемый объект. result_index — это позиция в сигнатуре этой функции, где идет итерация.

 Это позволяет вам использовать itertools на «производственной стороне», то есть при определении функции.
 Это может расширить то, что возвращает функция, без изменения кода функции.

 Например, чтобы создать версию декоратора chunked():

 from more_itertools import make_decorator

 from more_itertools import chunked
 chunker = make_decorator(chunked, result_index=0)
 @chunker(3)
 def iter_range(n):
     return iter(range(n))

 list(iter_range(9))  # -> [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

 Чтобы разрешить возврат только правдивых товаров:

 truth_serum = make_decorator(filter, result_index=1)
 @truth_serum(bool)
 def boolean_test():
     return [0, 1, '', ' ', False, True]

 list(boolean_test())  # -> [1, ' ', True]

 Обертки peekable() и seekable() подходят для практичных декораторов:

 from more_itertools import peekable
 peekable_function = make_decorator(peekable)
 @peekable_function()
 def str_range(*args):
     return (str(x) for x in range(*args))

 it = str_range(1, 20, 2)
 next(it), next(it), next(it)
 ('1', '3', '5')
 it.peek()
 '7'
 next(it)
 '7'

 Исходник:
 def make_decorator(wrapping_func, result_index=0):

     # See https://sites.google.com/site/bbayles/index/decorator_factory for
     # notes on how this works.
     def decorator(*wrapping_args, **wrapping_kwargs):
         def outer_wrapper(f):
             def inner_wrapper(*args, **kwargs):
                 result = f(*args, **kwargs)
                 wrapping_args_ = list(wrapping_args)
                 wrapping_args_.insert(result_index, result)
                 return wrapping_func(*wrapping_args_, **wrapping_kwargs)

             return inner_wrapper

         return outer_wrapper

     return decorator

________________________________________________________________________________________________________________________
 classmore_itertools.SequenceView(target) - Возвращает доступное только для чтения
 представление объекта последовательности target .

 SequenceViewобъекты аналогичны встроенным типам «представлений словаря» Python. Они обеспечивают динамическое
 представление элементов последовательности, а это означает, что при обновлении последовательности обновляется и представление.

 from more_itertools import SequenceView

 seq = ['0', '1', '2']
 view = SequenceView(seq)
 view  # -> SequenceView(['0', '1', '2'])
 seq.append('3')
 view  # -> SequenceView(['0', '1', '2', '3'])

 Представления последовательностей поддерживают запросы индексирования, нарезки и определения длины. Они действуют
 как базовая последовательность, за исключением того, что не допускают присваивания:

 view[1]     # -> '1'
 view[1:-1]  # -> ['1', '2']
 len(view)   # -> 4

 Представления последовательности полезны в качестве альтернативы копированию,
 поскольку они не требуют (много) дополнительного хранилища.

 Исходник:
 from collections.abc import Sequence

 class SequenceView(Sequence):

     def __init__(self, target):
         if not isinstance(target, Sequence):
             raise TypeError
         self._target = target

     def __getitem__(self, index):
         return self._target[index]

     def __len__(self):
         return len(self._target)

     def __repr__(self):
         return '{}({})'.format(self.__class__.__name__, repr(self._target))

________________________________________________________________________________________________________________________
 more_itertools.time_limited(limit_seconds, iterable) - Выдавать элементы из итерируемого объекта до тех пор,
 пока не пройдет limit_seconds . Если лимит времени истечет до того, как все элементы будут переданы,
 параметру timed_out будет присвоено значение True.

 from more_itertools import time_limited

 from time import sleep
 def generator():
     yield 1
     yield 2
     sleep(0.2)
     yield 3
 iterable = time_limited(0.1, generator())
 list(iterable)      # -> [1, 2]
 iterable.timed_out  # -> True

 Обратите внимание, что время проверяется перед получением каждого элемента, и итерация останавливается, если прошедшее
 время превышает лимит_секунд . Если ваш лимит времени составляет 1 секунду, но для создания первого элемента
 из итерируемого объекта требуется 2 секунды, функция будет работать в течение 2 секунд и ничего не даст.
 В частном случае, когда limit_секунды равны нулю, итератор никогда ничего не возвращает.

 Исходник:
 from time import monotonic

 class time_limited:

     def __init__(self, limit_seconds, iterable):
         if limit_seconds < 0:
             raise ValueError('limit_seconds must be positive')
         self.limit_seconds = limit_seconds
         self._iterable = iter(iterable)
         self._start_time = monotonic()
         self.timed_out = False

     def __iter__(self):
         return self

     def __next__(self):
         if self.limit_seconds == 0:
             self.timed_out = True
             raise StopIteration
         item = next(self._iterable)
         if monotonic() - self._start_time > self.limit_seconds:
             self.timed_out = True
             raise StopIteration

         return item

________________________________________________________________________________________________________________________
 more_itertools.map_if(iterable, pred, func, func_else=lambda x: ...) - Оцените каждый элемент итерируемого объекта
 с помощью pred . Если результат эквивалентен True, преобразуйте элемент с помощью func и верните его.
 В противном случае преобразуйте элемент с помощью func_else и верните его.

 pred , func и func_else должны быть функциями, принимающими один аргумент. По умолчанию func_else — это функция идентификации.

 from more_itertools import map_if

 from math import sqrt
 iterable = list(range(-5, 5))
 iterable  # -> [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4]
 list(map_if(iterable, lambda x: x > 3, lambda x: 'toobig'))  # -> [-5, -4, -3, -2, -1, 0, 1, 2, 3, 'toobig']
 list(map_if(iterable, lambda x: x >= 0,
 lambda x: f'{sqrt(x):.2f}', lambda x: None)) # -> [None, None, None, None, None, '0.00', '1.00', '1.41', '1.73', '2.00']

 Исходник:
 def map_if(iterable, pred, func, func_else=lambda x: x):
     for item in iterable:
         yield func(item) if pred(item) else func_else(item)

________________________________________________________________________________________________________________________
 Itertools recipes
 more_itertools.iter_index(iterable, value, start=0, stop=None) - Возвращает индекс каждого места в итерации ,
 где встречается значение , начиная с индекса start и заканчивая индексом stop .

 См. locate()более общие способы поиска индексов, связанных с конкретными значениями.

 from more_itertools import iter_index

 list(iter_index('AABCADEAF', 'A'))
 [0, 1, 4, 7]
 list(iter_index('AABCADEAF', 'A', 1))  # start index is inclusive
 [1, 4, 7]
 list(iter_index('AABCADEAF', 'A', 1, 7))  # stop index is not inclusive
 [1, 4]

 Исходник:
 from itertools import islice

 def iter_index(iterable, value, start=0, stop=None):
     seq_index = getattr(iterable, 'index', None)
     if seq_index is None:
         # Slow path for general iterables
         it = islice(iterable, start, stop)
         for i, element in enumerate(it, start):
             if element is value or element == value:
                 yield i
     else:
         # Fast path for sequences
         stop = len(iterable) if stop is None else stop
         i = start - 1
         try:
             while True:
                 yield (i := seq_index(value, i + 1, stop))
         except ValueError:
             pass

________________________________________________________________________________________________________________________
 more_itertools.consume(iterator, n=None) - Предварительная итерация на n шагов. Если n равно None, использовать его полностью.
 Эффективно исчерпывает итератор без возврата значений. По умолчанию используется весь итератор,
 но для ограничения потребления можно указать необязательный второй аргумент.

 from more_itertools import consume

 i = (x for x in range(10))
 next(i)  # -> 0
 consume(i, 3)
 next(i)  # -> 4
 consume(i)
 next(i)  # -> StopIteration

 Если в итераторе осталось меньше элементов, чем заданный предел, будет использован весь итератор.
 i = (x for x in range(3))
 consume(i, 5)
 next(i)  # -> StopIteration

 Исходник:
 from collections import deque
 from itertools import islice

 def consume(iterator, n=None):
     # Use functions that consume iterators at C speed.
     if n is None:
         # feed the entire iterator into a zero-length deque
         deque(iterator, maxlen=0)
     else:
         # advance to the empty slice starting at position n
         next(islice(iterator, n, n), None)

________________________________________________________________________________________________________________________
 more_itertools.tabulate(function, start=0) - Возвращает итератор по результатам func(start), func(start + 1), func(start + 2)…
 func должна быть функцией, которая принимает один целочисленный аргумент. Если параметр start не указан,
 по умолчанию он равен 0. Он будет увеличиваться при каждом перемещении итератора.

 from more_itertools import tabulate

 square = lambda x: x ** 2
 iterator = tabulate(square, -3)
 take(4, iterator)  # -> [9, 4, 1, 0]

 Исходник:
 from itertools import count

 def tabulate(function, start=0):
     return map(function, count(start))

________________________________________________________________________________________________________________________
 more_itertools.repeatfunc(func, times=None, *args) - Вызывайте func с аргументами несколько раз, возвращая итерацию результатов.
 Если указано время , итерация завершится после такого количества повторений:

 from more_itertools import repeatfunc

 from operator import add
 times = 4
 args = 3, 5
 list(repeatfunc(add, times, *args))  # -> [8, 8, 8, 8]

 Если times is None итерация не завершится:

 from random import randrange
 times = None
 args = 1, 11
 take(6, repeatfunc(randrange, times, *args))  # -> [2, 4, 8, 1, 8, 4]

 Исходник:
 from itertools import starmap, repeat

 def repeatfunc(func, times=None, *args):
     if times is None:
         return starmap(func, repeat(args))
     return starmap(func, repeat(args, times))

________________________________________________________________________________________________________________________
 more_itertools.polynomial_from_roots(roots) - Вычислите коэффициенты многочлена по его корням.

 from more_itertools import polynomial_from_roots

 roots = [5, -4, 3]  # (x - 5) * (x + 4) * (x - 3)
 polynomial_from_roots(roots)  # x^3 - 4 * x^2 - 17 * x + 60

 Исходник:
 import operator
 from itertools import repeat
 from functools import reduce
 from more_itertools import convolve

 def polynomial_from_roots(roots):
     factors = zip(repeat(1), map(operator.neg, roots))
     return list(reduce(convolve, factors, [1]))

________________________________________________________________________________________________________________________
 more_itertools.polynomial_eval(coefficients, x) - Оцените полином по определенному значению.
 Пример: оценка x^3 - 4 * x^2 - 17 * x + 60 at x = 2.5:

 from more_itertools import polynomial_eval

 coefficients = [1, -4, -17, 60]
 x = 2.5
 polynomial_eval(coefficients, x)  # -> 8.125

 Исходник:
 import math
 from itertools import repeat

 # math.sumprod is available for Python 3.12+
 _sumprod = getattr(math, 'sumprod', lambda x, y: dotproduct(x, y))

 def polynomial_eval(coefficients, x):
     n = len(coefficients)
     if n == 0:
         return x * 0  # coerce zero to the type of x
     powers = map(pow, repeat(x), reversed(range(n)))
     return _sumprod(coefficients, powers)

________________________________________________________________________________________________________________________
 more_itertools.polynomial_derivative(coefficients) - Вычислите первую производную многочлена.
 Пример: вычисление производной x^3 - 4 * x^2 - 17 * x + 60

 from more_itertools import polynomial_derivative

 coefficients = [1, -4, -17, 60]
 derivative_coefficients = polynomial_derivative(coefficients)
 derivative_coefficients  # -> [3, -8, -17]

 Исходник:
 import operator

 def polynomial_derivative(coefficients):
     n = len(coefficients)
     powers = reversed(range(1, n))
     return list(map(operator.mul, coefficients, powers))

________________________________________________________________________________________________________________________
 more_itertools.sieve(n) - Выведите простые числа меньше n.

 from more_itertools import sieve

 list(sieve(30))  # -> [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

 Исходник:
 import math
 from more_itertools import iter_index

 def sieve(n):
     if n > 2:
         yield 2
     start = 3
     data = bytearray((0, 1)) * (n // 2)
     limit = math.isqrt(n) + 1
     for p in iter_index(data, 1, start, limit):
         yield from iter_index(data, 1, start, p * p)
         data[p * p : n : p + p] = bytes(len(range(p * p, n, p + p)))
         start = p * p
     yield from iter_index(data, 1, start)

________________________________________________________________________________________________________________________
 more_itertools.factor(n) - Выведите простые множители числа n.

 from more_itertools import factor

 list(factor(360))  # -> [2, 2, 2, 3, 3, 5]

 Исходник:
 import math
 from more_itertools import sieve

 def factor(n):
     for prime in sieve(math.isqrt(n) + 1):
         while not n % prime:
             yield prime
             n //= prime
             if n == 1:
                 return
     if n > 1:
         yield n

________________________________________________________________________________________________________________________
 more_itertools.matmul(m1, m2) - Умножьте две матрицы.

 from more_itertools import matmul

 list(matmul([(7, 5), (3, 5)], [(2, 5), (7, 9)]))  # -> [(49, 80), (41, 60)]

 Исходник:
 import math
 from more_itertools import batched, transpose, dotproduct
 from itertools import product, starmap

 # math.sumprod is available for Python 3.12+
 _sumprod = getattr(math, 'sumprod', lambda x, y: dotproduct(x, y))

 def matmul(m1, m2):
     n = len(m2[0])
     return batched(starmap(_sumprod, product(m1, transpose(m2))), n)

________________________________________________________________________________________________________________________
 more_itertools.sum_of_squares(it) - Возвращает сумму квадратов входных значений.

 from more_itertools import sum_of_squares

 sum_of_squares([10, 20, 30])  # -> 1400

 Исходник:
 import math
 from more_itertools import dotproduct
 from itertools import tee

 # math.sumprod is available for Python 3.12+
 _sumprod = getattr(math, 'sumprod', lambda x, y: dotproduct(x, y))

 def sum_of_squares(it):
     return _sumprod(*tee(it))

________________________________________________________________________________________________________________________
 more_itertools.totient(n) - Возвращает количество натуральных чисел до n , взаимно простых с n .

 from more_itertools import totient

 totient(9)   # -> 6
 totient(12)  # -> 4

 Исходник:
 from more_itertools import unique_justseen, factor

 def totient(n):
     for p in unique_justseen(factor(n)):
         n = n // p * (p - 1)

     return n

________________________________________________________________________________________________________________________
 more_itertools.reshape(matrix, cols) - Измените форму двумерной входной матрицы , чтобы количество столбцов было задано cols .

 from more_itertools import reshape

 matrix = [(0, 1), (2, 3), (4, 5)]
 cols = 3
 list(reshape(matrix, cols))  # -> [(0, 1, 2), (3, 4, 5)]

 Исходник:
 from more_itertools import batched
 from itertools import chain

 def reshape(matrix, cols):
     return batched(chain.from_iterable(matrix), cols)

________________________________________________________________________________________________________________________

"""