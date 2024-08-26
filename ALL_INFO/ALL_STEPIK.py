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

 # Yandex-Маркет Задача Отсортировать по двум параметрам. Как я сделал я не знаю

 xs = [
     '1_a.txt',
     '2_b.txt',
     '1_c.txt',
     '3_d.txt',
     '1_e.txt',
 ]

 def sub_fun(x):
     return -int(re.sub(r'[^\d]+', '', x)), re.search(r'(?<=_)[a-z]+(?=\.)', x, flags=re.I).group()

 def my_func(lst: list) -> list:
     return sorted(lst, key=sub_fun)

 print(my_func(xs))  # -> ['3_d.txt', '2_b.txt', '1_a.txt', '1_c.txt', '1_e.txt']

 print(sorted(xs, key=lambda x: (-int(x[0]), x[1])))
 print(sorted(xs, key=lambda x: (-int(re.sub(r'[^\d]+', '', x)), re.search(r'(?<=_)[a-z]+(?=\.)', x, flags=re.I).group())))
 print(sorted(xs, key=sub_fun))
 # ['3_d.txt', '2_b.txt', '1_a.txt', '1_c.txt', '1_e.txt']
 # ['3_d.txt', '2_b.txt', '1_a.txt', '1_c.txt', '1_e.txt']
 # ['3_d.txt', '2_b.txt', '1_a.txt', '1_c.txt', '1_e.txt']

 # Через split() хз как улучшить
 print(sorted(xs, key=lambda x: (-int(''.join(x.split('.')).split('_')[0]), ''.join(x.split('.')).split('_')[1])))
________________________________________________________________________________________________________________________



 # Задача "Правильная скобочная последовательность"    Valid Braces  Codewars

 # Первый Вариант
 def is_correct_brackets(text):
     while '()' in text or '[]' in text or '{}' in text:
         text = text.replace('()', '')
         text = text.replace('[]', '')
         text = text.replace('{}', '')

     # Возвращаем True, если text с пустой строкой
     return not text

 print(is_correct_brackets('(((())))'))          # True
 print(is_correct_brackets('(((())'))            # False
 print(is_correct_brackets('())))'))             # False
 print(is_correct_brackets('((((){}[]{}[])))'))  # True
 print(is_correct_brackets('(){}[]{}[])))'))     # False
 print(is_correct_brackets('(){}[]{}[]'))        # True


 # Второй Вариант
 def validBraces(string):
     braces = {"(": ")", "[": "]", "{": "}"}
     stack = []
     for character in string:
         if character in braces.keys():
             stack.append(character)
         else:
             if len(stack) == 0 or braces[stack.pop()] != character:
                 return False
     return len(stack) == 0

 print(validBraces('(((())))'))          # True
 print(validBraces('(((())'))            # False
 print(validBraces('())))'))             # False
 print(validBraces('((((){}[]{}[])))'))  # True
 print(validBraces('(){}[]{}[])))'))     # False
 print(validBraces('(){}[]{}[]'))        # True


 # Третий Вариант
 def validBraces(string):
     for _ in string:
         string = string.replace('{}', '').replace('()', '').replace('[]', '')
     return not string

 print(validBraces('(((())))'))          # True
 print(validBraces('(((())'))            # False
 print(validBraces('())))'))             # False
 print(validBraces('((((){}[]{}[])))'))  # True
 print(validBraces('(){}[]{}[])))'))     # False
 print(validBraces('(){}[]{}[]'))        # True


 # Ответ ChatGPT
 def is_valid(s: str) -> bool:
     # Создаем стек для хранения открывающих скобок
     stack = []
     # Словарь для сопоставления открывающих и закрывающих скобок
     mapping = {')': '(', '}': '{', ']': '['}

     for char in s:
         # Если символ — закрывающая скобка
         if char in mapping:
             # Извлекаем верхнюю скобку из стека, если стек не пуст
             # В противном случае используем символ-знак
             top_element = stack.pop() if stack else '#'
             # Проверяем, соответствует ли открывающая скобка закрывающей
             if mapping[char] != top_element:
                 return False
         else:
             # Если это открывающая скобка, добавляем её в стек
             stack.append(char)

     # Если стек пуст, значит все скобки корректны
     return not stack


 # Примеры использования
 print(is_valid("()"))  # True
 print(is_valid("()[]{}"))  # True
 print(is_valid("(]"))  # False
 print(is_valid("([)]"))  # False
 print(is_valid("{[]}"))  # True
________________________________________________________________________________________________________________________

 # Задача "Расстановка скобок в коде"
 def validBraces(string):
     braces = {')': '(', '}': '{', ']': '['}
     stack = []
     for i, v in enumerate(string, start=1):
         if v in braces.values():
             stack.append((v, i))
         if v in braces and (not stack or braces[v] != stack.pop()[0]):
             return i
     return stack.pop()[1] if stack else 'Success'

 print(validBraces('([](){([])})'))  # Success
 print(validBraces('()[]}'))         # 5


 # Вроде правильный вариант но не проходил все Тесты
 def validBraces(string):
     s = string
     for _ in string:
         string = string.replace('{}', '').replace('()', '').replace('[]', '')
     return 'Success' if not string else len(s)

 print(validBraces('([](){([])})'))  # Success
 print(validBraces('()[]}'))         # 5
 print(validBraces('{{[()]]'))       # 5
________________________________________________________________________________________________________________________

 # Задача "Высота дерева"

 # Вариант 1
 from functools import lru_cache

 @lru_cache(maxsize=None)
 def count(data, i):
     return (data[i] == -1 and 1 or count(data, data[i]) + 1)

 num, data = 10, (9, 7, 5, 5, 2, 9, 9, 9, 2, -1)
 print(max(count(data, i) for i in range(num)))   # -> 4


 # Вариант 2
 n = 10
 s = [9, 7, 5, 5, 2, 9, 9, 9, 2, -1]

 def countd(i):
     if d[i] == - 1:
         d[i] = countd(s[i]) + 1
     return d[i]

 d = [-1] * (len(s)) + [0]
 [countd(i) for i in range(len(s))]
 print(max(d))                                      # -> 4

________________________________________________________________________________________________________________________

 # Максимум в скользящем окне    # Sliding Window Maximum

 # Вариант с exec
 exec('''def convert(iterable, m):
     t = [iterable[x:] for x in range(m)]
     result = [max(i) for i in zip(*t)]
     return result

 print(convert([2, 7, 3, 1, 5, 2, 6, 2], 3))  # -> [7, 7, 5, 5, 6, 6]
 ''')

 # Вариант zip
 def convert(iterable, m):
     t = [iterable[x:] for x in range(m)]
     result = [max(i) for i in zip(*t)]
     return result

 print(convert([2, 7, 3, 1, 5, 2, 6, 2], 3))   # -> [7, 7, 5, 5, 6, 6]


 # Вариант Обычный
 def convert2(listi, m):
     listo = []
     n = len(listi)
     for i in range(n-m+1):
         listo.append(max(listi[i:3+i]))
     return listo

 print(convert2([2, 7, 3, 1, 5, 2, 6, 2], 3))  # -> [7, 7, 5, 5, 6, 6]
________________________________________________________________________________________________________________________

 Задача на программирование: небольшое число Фибоначчи    Посмотри тесты в конце!!!    Важно!!! <-----    <-----

 # Скорость O(1)                      # Скорость O(1)
 def fibonacci__1(n):                 import math
     if n == 0:
         return 0                     def fibonacci__2(n):
     elif n == 1:                         phi = (1 + math.sqrt(5)) / 2
         return 1                         return round((phi**n - (1 - phi)**n) / math.sqrt(5))

     a, b = 0, 1
     for _ in range(2, n + 1):
         a, b = b, a + b
     return b

 n = 7                                 n = 7
 print(fibonacci__1(n))  # -> 13       print(fibonacci__2(n))   # -> 13


 # Решения с мемоизацией КЭШ  Скорость O(n)   НО С ОЧЕНЬ БОЛЬШИМИ ЧИСЛАМИ НЕ БУДЕТ РАБОТАТЬ!!! ЛУЧШЕ ВЫБРАТЬ fibonacci__1
 # @__import__('functools').lru_cache(maxsize=None)  #  Так тоже можно импортировать
 @functools.lru_cache(maxsize=None)
 def fibonacci__3(n):
     if n < 2:
         return n
     else:
         return fibonacci__3(n - 1) + fibonacci__3(n - 2)

 n = 7
 print(fibonacci__3(n))  # -> 13


 # Простая функция  if/else                               # Простая функция  match/case     <-----  Посмотри тесты в конце!!!
 def fibonacci__0(n):                                     def fib(n):
     if n < 2:                                                match n:
         return n                                                 case 0 | 1:
     else:                                                            return n
         return fibonacci__0(n - 1) + fibonacci__0(n - 2)         case _:
                                                                    return fib(n - 1) + fib(n - 2)
 n = 7                                                    n = 7
 print(fibonacci__0(n))  # -> 13                          print(fibonacci__0(n))  # -> 13


 # Замеры с параметром 50!!!
 print(timeit.timeit('fibonacci__1(50)', globals=globals()))                          # -> 2.737594800069928
 print(timeit.timeit('fibonacci__2(50)', globals=globals()))                          # -> 1.235288399970159
 print(timeit.timeit('fibonacci__3(50)', globals=globals()))                          # -> 0.10358340013772249

 # Замер простой функции с параметром ТОЛЬКО 10!!!
 print(timeit.timeit('fibonacci__0(10)', globals=globals()))                          # -> 16.955934199970216
 # Замер match case простой функции с параметром ТОЛЬКО 10!!!
 print(timeit.timeit('fib(10)', globals=globals()))                                   # -> 24.523009299999103


 # Тоже самое но с setup()
 print(timeit.timeit('fibonacci__1(50)', setup="from __main__ import fibonacci__1"))  # -> 2.7405860000289977
 print(timeit.timeit('fibonacci__2(50)', setup="from __main__ import fibonacci__2"))  # -> 1.2412337001878768
 print(timeit.timeit('fibonacci__3(50)', setup="from __main__ import fibonacci__3"))  # -> 0.09871609997935593

 # Замер простой функции с параметром ТОЛЬКО 10!!!
 print(timeit.timeit('fibonacci__0(10)', setup="from __main__ import fibonacci__0"))  # -> 16.960932299960405

 # Замер match case простой функции с параметром ТОЛЬКО 10!!!
 print(timeit.timeit('fib(10)', setup="from __main__ import fib"))                    # -> 24.574260200140998


 times = {
     'fibonacci__1': round(timeit.timeit('fibonacci__1(50)', globals=globals()), 3),
     'fibonacci__2': round(timeit.timeit('fibonacci__2(50)', globals=globals()), 3),
     'fibonacci__3': round(timeit.timeit('fibonacci__3(50)', globals=globals()), 3),
     'Default': round(timeit.timeit('fibonacci__0(10)', globals=globals()), 3),
     'Default match case': round(timeit.timeit('round(fib(10), 2)', globals=globals()), 3),
 }

 # Оценим время, за которое они завершили исполнение!   Странно match case очень долго работает
 print(sorted(times.items(), key=lambda x: x[1]))
 # [('fibonacci__3', 0.104), ('fibonacci__2', 1.225), ('fibonacci__1', 2.692), ('Default', 17.286), ('Default match case', 25.659)]
________________________________________________________________________________________________________________________


________________________________________________________________________________________________________________________


________________________________________________________________________________________________________________________


________________________________________________________________________________________________________________________


________________________________________________________________________________________________________________________


 --- Интересные решения ---

 На вход подается 5 чисел, что нам нужно с ними сделать, запоминаем:
 - Первое число умножить на второе число
 - К результату прибавить третье число
 - Из результата вычесть четвертое число
 - То что получилось поделить на пятое число

 # Входные данные [a = 5, b = 14, c = 8.0, d = 6, e = 3]

  # Тоже самое
 a = float(input())  # 5
 b = float(input())  # 14
 c = float(input())  # 8.0
 d = float(input())  # 6
 e = float(input())  # 3
 print((((a*b)+c)-d)/e)                                     # -> 24.0


 # Тоже самое
 res = float(input())
 for op in ('mul', 'add', 'sub', 'truediv'):
     res = getattr(res, f'__{op}__')(float(input()))
 print(res)                                                 # -> 24.0


 # Тоже самое
 n1, n2, n3, n4, n5 = (float(input()) for _ in range(5))
 print((n1 * n2 + n3 - n4) / n5)                            # -> 24.0
 -----------------------------------------------------------------------------------------------------------------------

 # Сумма чисел
 total = 0
 while (number := input()) != 'конец':
     total += int(number)
 print(total)
 -----------------------------------------------------------------------------------------------------------------------

 # На вход программе подается некоторое количество слов, а далее текст "сколько" и слово, количество которого считаем
 res = []
 while True:
     m = input()
     if m == 'сколько':
         print(res.count(input()))
         break
     else:
         res.append(m)
 -----------------------------------------------------------------------------------------------------------------------

 # Моржа :=  Можно оборачивать с скобки () и Лучше всегда его оборачивать

 # str.format
 print('Если перевернуть слово "{0}", получится "{1}".'.format((s := 'Hello'), s[::-1]))  # Тут смотри моржа
 # f-строка
 print(f'Если перевернуть слово "{(s:="Hello")}", получится "{s[::-1]}".')                # Тут смотри моржа
 # -> Если перевернуть слово "Hello", получится "olleH".
 -----------------------------------------------------------------------------------------------------------------------

 # Сразу применить в ф-строке несколько +_  можно без ()
 s = 5000                                  s = 345
 s1 = 756                                  s1 = 786
 print(f'{(s-s1):+_}')  # -> +4_244        print(f'{s-s1:+_}')  # -> -441
 -----------------------------------------------------------------------------------------------------------------------

 # Поменяйте местами минимальный и максимальный элемент
 lst = [1, 2, 3, 4, 5]
 mx, mn = lst.index(max(lst)), lst.index(min(lst))
 lst[mx], lst[mn] = lst[mn], lst[mx]
 print(*lst)  # -> 5 2 3 4 1
 -----------------------------------------------------------------------------------------------------------------------

 # Ход ладьи   может ли ладья попасть с первой клетки на вторую одним ходом.
 x1, y1, x2, y2 = [3, 5, 7, 2]
 if (-1 <= x1 - x2 <= 1) and (-1 <= y1 - y2 <= 1):
     print(f'ДА')
 else:
     print(f'НЕТ')
 -----------------------------------------------------------------------------------------------------------------------

 # Необходимо сравнить первое число со вторым и вывести <=>
 a, b = [4, 6]
 print('>' if a > b else '<' if a < b else '=')  # -> <
 -----------------------------------------------------------------------------------------------------------------------

 # Калькулятор
 # lst = input().split()
 # x, y = input().split()
 # symbol = input()

 x, y = '7.0', '0'
 symbol = '/'
 try:
     print(float(eval(x + symbol + y)))
 except:
     print("Некорректная операция")  # -> Некорректная операция
 -----------------------------------------------------------------------------------------------------------------------

 # Классный пример c моржом и pass внутри

 psw = 'Password'                                      psw = 'Password'
 while (enter := input('Введите пароль: ')) != psw:    for i in iter(input, psw):
     pass                                                  pass
 print('Вход в систему')                               print('Вход в систему')


 # Можно через ; делать
 # Тоже самое           # Тоже самое
 a, b = 15, 45          a, b = 15, 45
 c = 0                  c = 0
 while a <= b:          while a <= b:
     a *= 3                 a *= 3; b *= 2; c += 1   # Вот тут ;
     b *= 2             print(c)  # -> 3
     c += 1
 print(c)  # -> 3
 -----------------------------------------------------------------------------------------------------------------------



 --- else в Циклах while и for ---
 # Важно else в циклах while и for!!!  <-----                                      <-----

 # else НЕ срабатывает в цикле while           # else срабатывает в цикле while    <-----           <-----
 c = 0                                         c = 0
 while c < 5:                                  while c < 5:
     c += 1                                        c += 1
     if c == 4:                                    if c == 100:
         break                                         break
 else:                                         else:
     print('Цикл while отработал полностью')        print('Цикл while отработал полностью')  # -> Цикл while отработал полностью



 # else НЕ срабатывает в цикле for            # else срабатывает в цикле for       <-----           <-----
 c = 0                                        c = 0
 for i in range(5):                           for i in range(5):
     c += 1                                       c += 1
     if c == 4:                                   if c == 100:
         break                                        break
 else:                                        else:
     print('Цикл for отработал полностью')        print('Цикл for отработал полностью')  # -> Цикл for отработал полностью
 -----------------------------------------------------------------------------------------------------------------------


 # Необходимо реализовать игру в "Города"  Следующее слово начинается на букву, которой оканчивалось предыдущее.
 lst = ['Гжижевск', 'Королевыьъ', 'Вайфаеград']

 res = []
 for i, v in enumerate(lst):
     if i == 0:
         continue
     if lst[i-1][-1].lower() in "ыьъ":
         if lst[i-1][-2].lower() == lst[i][0].lower():
             res.append(True)
             continue
     if lst[i-1][-1].lower() == lst[i][0].lower():
         res.append(True)
         continue
     else:
         res.append(False)

 print('ДА' if all(res) else 'НЕТ')  # -> НЕТ
 -----------------------------------------------------------------------------------------------------------------------

 -- enumerate vs range(len(lst)) --

 # Тоже самое                       # Тоже самое                           # Внутри enumerate Кортежи (индекс, значение)
 lst = ['a', 'b', 'c', 'd']         lst = ['a', 'b', 'c', 'd']             lst = ['a', 'b', 'c', 'd']

 for i, v in enumerate(lst):        for i in range(len(lst)):              for i in enumerate(lst):
     print(f'{i}={v}', end='  ')        print(f'{i}={lst[i]}', end='  ')       print(f'{i}', end='  ')
 # -> 0=a  1=b  2=c  3=d            # -> 0=a  1=b  2=c  3=d                # -> (0, 'a')  (1, 'b')  (2, 'c')  (3, 'd')
 -----------------------------------------------------------------------------------------------------------------------

 # Лесенка из чисел и выводится на экран.            # Вывод
 n = 3
 for i in range(1, n+1):                             # 1
     a = ''                                          # 1 2
     for j in range(1, i+1):                         # 1 2 3
         a += str(j)+' '
     print(a.strip())
 -----------------------------------------------------------------------------------------------------------------------


 # За раз можно взять только одну гантель.                        # За раз можно взять только одну гантель.
 l, target = sorted([1, 2, 4, 8, 16, 32, 64], reverse=True), 255  target = 255
 arr = []                                                         res = []
 res = target                                                     for x in [64, 32, 16, 8, 4, 2, 1]:
 while target != 0:                                                   while 1 <= x <= target: target -= x; res.append(x)
     for el in l:                                                 print(res)  # -> [64, 64, 64, 32, 16, 8, 4, 2, 1]
         if el <= target:
             res -= el
             arr.append(el)
             break
     target -= el
 print(arr)  # -> [64, 64, 64, 32, 16, 8, 4, 2, 1]


 # Моё решение
 # За раз можно взять только одну гантель.
 target = 255
 dumbbells = (1, 2, 4, 8, 16, 32, 64)

 res = []
 c = 0
 for i in dumbbells[::-1]:
     while sum(res) < target or i < target:
         if c + i <= target:
             res.append(i)
             c += i
             continue
         else:
             break
 print(res)  # -> [64, 64, 64, 32, 16, 8, 4, 2, 1]
 -----------------------------------------------------------------------------------------------------------------------

 # Сколько дней в каком-нибудь месяце.

 from calendar import monthrange
 days = monthrange(2023, 4)[1]
 print(days)  # -> 30
 days = monthrange(2023, 4)
 print(days)  # -> (5, 30)
 -----------------------------------------------------------------------------------------------------------------------

 # Достать значения
 lst = [
     {
      'id': 1, 'name': 'fruits',
      'list': ['apples', 'bananas', 'oranges']
     },
 ]

 print([list(i.items())[-1][-1] for i in lst])  # -> [['apples', 'bananas', 'oranges']]
 print([list(s.items())[2][1] for s in lst])    # -> [['apples', 'bananas', 'oranges']]
 -----------------------------------------------------------------------------------------------------------------------

 # Интересный момент с fromkeys При создании можно указать любой словарь даже НЕ пустой
 a_dict = dict.fromkeys('abc', 1)
 print(a_dict)  # -> {'a': 1, 'b': 1, 'c': 1}

 a_dict = {}.fromkeys('abc', 1)
 print(a_dict)  # -> {'a': 1, 'b': 1, 'c': 1}

 a_dict = {1: 2}.fromkeys('abc', 1)
 print(a_dict)  # -> {'a': 1, 'b': 1, 'c': 1}
 -----------------------------------------------------------------------------------------------------------------------

 # dict comprehensions только key
 a_dict = {k: k*2 for k in range(5)}
 print(a_dict)  # -> {0: 0, 1: 2, 2: 4, 3: 6, 4: 8}
 -----------------------------------------------------------------------------------------------------------------------

 # Необходимо вывести все индексы неуникальных слов(встречающихся более 1-го раза)
 lst = ['к', 'п', 'р', 'н', 'г', 'о', 'л', 'о', 'к', 'а', 'п', 'н',]
 print([i for i, v in enumerate(lst) if lst.count(v) > 1])  # -> [0, 1, 3, 5, 7, 8, 10, 11]
-----------------------------------------------------------------------------------------------------------------------

 # Объединить все элементы Разные способы
 lst = [{1, 2}, frozenset({3, 4}), {5, 6}, frozenset({8, 7}), {9, 10}, frozenset({11, 12})]
 print(frozenset(chain.from_iterable(lst)))           # -> frozenset({1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12})
 print(frozenset(set.union(*lst)))                    # -> frozenset({1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12})
 print(frozenset({elem for i in lst for elem in i}))  # -> frozenset({1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12})
 -----------------------------------------------------------------------------------------------------------------------

 # Несколько Переменных и проверок сразу  match  case

 # Срабатывает                           # Срабатывает                           # НЕ Срабатывает
 a, b = 1, '1'                           a, b = 1, '1'                           a, b = 1, 1000

 match a, b:                             match a, b:                             match a, b:
     case int() as x, str() as y:            case int(a), str(b):                    case int(a), str(b):
         print('Integer and String')             print('Integer and String')             print('Integer and String')
     case _:                                 case _:                                 case _:
         print('a != int or b != str')           print('a != int or b != str')           print('a != int or b != str')

 # -> Integer and String                 # -> Integer and String                 # -> a != int or b != str
 -----------------------------------------------------------------------------------------------------------------------

 # Вам необходимо перебрать его и для каждого типа данных, кроме str
 lst = [1, 5.6, '3', [1, 2], (4, 7), {'a': 4}, True]

 for e in lst:
     match e:
         case str():
             continue                                                       # Можно даже так        <-----
         case _:
             print(f'{type(e)}', end=' ')

 # -> <class 'int'> <class 'float'> <class 'list'> <class 'tuple'> <class 'dict'> <class 'bool'>
 -----------------------------------------------------------------------------------------------------------------------

 # отвечает тем же сообщением, что написали ему или s1
 s = 'Как дела?'                                   s = 'Как дела?'
 s1 = 'Пока не родила'                             s1 = 'Пока не родила'

 match s, s1:                                      match s == s1:
     case x, y if x == y:                              case True:
         print('полное соответствие')                      print('полное соответствие')
     case _:                                           case _:
         print(s1)                                         print(s1)
 -----------------------------------------------------------------------------------------------------------------------

 # 2 новых списка. В первом 'облачность' =  'ясно' и 'температура' не менее 25 градусов. Во втором остальное
 lst = [{'номер': 1, 'облачность': 'ясно', 'температура': 26},
        {'номер': 2, 'облачность': 'облачно', 'температура': 18},
        ]

 lst1, lst2 = [], []
 for line in lst:
     match line:
         case {'облачность': 'ясно', 'температура': int(n)} if n >= 25:
             lst1.append(line)
         case _:
             lst2.append(line)
 print(lst1); print(lst2)
 # -> [{'номер': 1, 'облачность': 'ясно', 'температура': 26}]
 # -> [{'номер': 2, 'облачность': 'облачно', 'температура': 18}]


 # Тоже самое
 good, bad = [], []
 for el in lst:
     match el:
         case {'номер': num, 'облачность': cloudy as cl, 'температура': temp as t} if cl == 'ясно' and t >= 25:
             good.append(el)
         case _:
             bad.append(el)
 print(good, bad, sep='\n')
 # -> [{'номер': 1, 'облачность': 'ясно', 'температура': 26}]
 # -> [{'номер': 2, 'облачность': 'облачно', 'температура': 18}]
 -----------------------------------------------------------------------------------------------------------------------

 # Необходимо на основе него создать список lst со вложенными списками   Думаю вспомнишь что надо было сделать)
 tpl = (
     ['name - Побег из Шоушенка', 'year - 1994', 'genre - драма',
      'director - Фрэнк Дарабонт', 'rating - 9.1'],
     ['name: Властелин колец: Возв к', 'year: 2003', 'genre: фэнтези, прик, дра, бое',
      'director: Пит Дже', 'rating: 8.7'],
     {'name': 'Властелин колец: Две крепости', 'year': '2002', 'genre': 'фэнтези, приключения, драма, боевик',
      'director': 'Питер Джексон', 'rating': '8.6'},
     ('name: Иван Васильевич меняет профессию', 'year: 1973', 'genre: комедия, фант, прикл',
      'director: Леонид Гайдай', 'rating: 8.8'),
 )

 def sub_fun(m):
     if m[0] == '{':
         return '['
     if m[0] == '}':
         return ']'

 lst = []
 for i in tpl:
     match i:
         case tuple():
             pass
         case {'name': name, 'rating': rating, **kwargs} if len(kwargs) >= 2 and float(rating) > 8.6:
             lst.append(re.sub(r'[{}]|\'(?=:)|(?<=: )\'', sub_fun, str(i)))
         # case {'name': name, 'rating': rating, **kwargs} if len(kwargs) >= 2 and float(rating) > 8.6:
         #     lst.append([': '.join(j) for j in i.items()])
         case name1, _, _, _, rating1 if 'name' in name1 and 'rating' in rating1 and float(rating1.split()[-1]) > 8.6:
             lst.append([j.replace(' -', ':') for j in i])

 print(*lst, sep='\n')

 # ['name: Побег из Шоушенка', 'year: 1994', 'genre: драма', 'director: Фрэнк Дарабонт', 'rating: 9.1']
 # ['name: Властелин колец: Возв к', 'year: 2003', 'genre: фэнтези, прик, дра, бое', 'director: Пит Дже', 'rating: 8.7']
 -----------------------------------------------------------------------------------------------------------------------

 # возвращает первое уникальное число
 lst = [3, 2, 4, 6, 5, 4, 3, 2, 6, 8, 7, 5, 3]

 def func(a_list):                  def func(nums: list) -> int:
     for i in a_list:                   '''Принимает список и возвращает первое уникальное. Если такое отсутствует, то -1'''
         if a_list.count(i) == 1:       return next((i for i in nums if nums.count(i) == 1), -1)
             return i
     return -1

 print(func(lst))  # -> 8           print(func(lst))  # -> 8
 -----------------------------------------------------------------------------------------------------------------------

 # Запаковка/Распаковка Двапаковка  в список *
 lst = [1, 2, 3, *[4, 5, 6]]
 print(lst)                          # -> [1, 2, 3, 4, 5, 6]
 print(*lst)                         # -> 1 2 3 4 5 6

 *x, y, z = 1, 2, 3, 4, 5
 print(f'{x=}   {y=}   {z=}')        # -> x=[1, 2, 3]   y=4   z=5
 x, *y, z = 1, 2, 3, 4, 5
 print(f'{x=}   {y=}   {z=}')        # -> x=1   y=[2, 3, 4]   z=5
 x, y, *z = 1, 2, 3, 4, 5
 print(f'{x=}   {y=}   {z=}')        # -> x=1   y=2   z=[3, 4, 5]

 d = {1: 'one', 2: 'two'}
 print(*d.items())                   # -> (1, 'one') (2, 'two')


 # Распаковка Двапаковка ** Работает только Внутри словарей
 d = {1: 'one', 2: 'two'}
 print({**d})                         # -> {1: 'one', 2: 'two'}
 print({**d, 3: 'three', 4: 'four'})  # -> {1: 'one', 2: 'two', 3: 'three', 4: 'four'}


 # Хороший пример с игнорированием значений
 lst = [6, 3, 4, 7, 8, 4]

 _, *x, _, = lst
 print(x)  # -> [3, 4, 7, 8]
 -----------------------------------------------------------------------------------------------------------------------

 # Как можно использовать функции!!!
 a = 17

 lst = [bin, oct, hex]
 print(*[i(a) for i in lst])  # -> 0b10001 0o21 0x11
 # Моржик
 print(*[i(b := 17) for i in lst])
 -----------------------------------------------------------------------------------------------------------------------

 # Как работает Моржик Посмотри :=

 # Без Моржика                                          # 1 раз обьявляем Моржика := и потом используем
 n = 10
 print(5 <= n < 10 or 101 < n < 201)  # -> # False      print(5 <= (n := 10) < 10 or 101 < n < 201)
 -----------------------------------------------------------------------------------------------------------------------

 # Моржика в условии нельзя
 print((n := 10)+10 if n % 2 == 0 else n-10)  # -> NameError: name 'n' is not defined
 print(n+10 if (n := 10) % 2 == 0 else n-10)  # -> 20
 -----------------------------------------------------------------------------------------------------------------------
 # Шифр Цезаря     # Шифер Цезаря

 s = "zzzbbb"
 shift = 1
 res = ''

 # Вариант 1
 for el in s:
     res+=chr((((ord(el)-97)+shift) % 26) + 97)
 print(res)                                                                                                 # -> aaaccc

 # Вариант 2
 print(*[chr((ord(c)-ord('a')+n)%26+ord('a')) for s,n in [["zzzbbb", 1]] for c in s], sep='')               # -> aaaccc

 # Вариант 3
 s, shift = "zzzbbb", 1 % 26                                                                                # -> aaaccc
 print(''.join([chr(((ord(char) - ord('a') + shift) % 26) + ord('a')) if char.islower() else char for char in s]))


 # Напишите программу-дешифратор шифра цезаря меняем +shift на -shift

 for el in s:
     res+=chr((((ord(el)-97)-shift) % 26) + 97)
 print(res)                                                                                                 # -> yyyaaa

 -----------------------------------------------------------------------------------------------------------------------

 # наибольшее количество подряд идущих одинаковых символов. Если таких несколько – выведите последнюю.
 from itertools import groupby

 s = "aaabbccccaaaab"
 print(*max(((k, len(list(g))) for k, g in groupby(s[::-1])), key=lambda x: x[1]), sep='=')  # -> a=4
 -----------------------------------------------------------------------------------------------------------------------

 # А вот метод format содержит в себе одно важное преимущество.
 # Дело в том, что в модульных проектах не всегда бывает так, что переменная находится в том же окружении, что и строка-шаблон.

 # у нас нет переменной name
 s = f"Моё имя - {name}"          # -> NameError: name 'name' is not defined

 # у нас нет переменной name
 s = "Моё имя - {name}"
 print(s.format(name='Антон'))    # -> Моё имя - Антон   ошибки уже не будет



 #  Можно использовать * и **    в format()
 a_dict = {'A': '1', 'B': '2'}
 a_list = ['C', 2, 'D']

 print('Coordinates: {A} , {B} '.format(**a_dict))       # ->   Coordinates: 1 , 2
 print('Coordinates: {1} , {2} , {0} '.format(*a_list))  # ->   Coordinates: 2 , D , C
 -----------------------------------------------------------------------------------------------------------------------

 # все нули в нем оказались в конце массива, сохранив при этом порядок чисел.
 lst = [10, 0, 3, 0, 4, 0, 0, 5, 6, 7, 8]

 print(sorted(lst, key=lambda x: x == 0))  # -> [10, 3, 4, 5, 6, 7, 8, 0, 0, 0, 0]
 -----------------------------------------------------------------------------------------------------------------------

 # Реализуйте кучу с максимумом в вершине для этого списка.   maxheap   Добавляем к числам минус -
 # Обрати внимание на match case и второй for

 numbers = [1, 5, 2, 6, 3, 7, 4, 8]
 numbers = [-i for i in numbers]
 heapq.heapify(numbers)

 numbers2 = ['insert 20', 'pop', 'insert 0', 'pop', 'insert 4', 'pop', 'end']

 for i in numbers2:
 # for i in iter(input, 'end'):                         # пока не будет слово end
     match i.split():
         case "insert", n:                              # тут интересно
             heapq.heappush(numbers, -int(n))
         case "pop",:
             print(-heapq.heappop(numbers), end=' ')  # -> 20 8 7


 # Тоже самое но с _heapify_max      но нужно каждый раз нужно делать  heapq._heapify_max(numbers)
 numbers = [1, 5, 2, 6, 3, 7, 4, 8]
 heapq._heapify_max(numbers)

 numbers2 = ['insert 20', 'pop', 'insert 0', 'pop', 'insert 4', 'pop', 'end']

 for i in numbers2:
 # for i in iter(input, 'end'):
     match i.split():
         case "insert", n:
             heapq.heappush(numbers, int(n))
             heapq._heapify_max(numbers)
         case "pop",:
             print(heapq._heappop_max(numbers), end=' ')  # -> 20 8 7
 -----------------------------------------------------------------------------------------------------------------------

 # Посчитайте количество високосных годов между ними включительно.

 from calendar import leapdays, isleap

 year1, year2 = int('2020'), int('2028')

 print(len([i for i in range(year1, year2+1) if isleap(i)]))                             # -> 3
 print(leapdays(year1, year2+1))                                                         # -> 3
 print(len([i for i in range(year1, year2 + 1) if __import__('calendar').isleap(i)]))    # -> 3
 -----------------------------------------------------------------------------------------------------------------------

 # Определите количество дней между двумя годами.
 a, b = 2020, 2024

 year1 = datetime.date(a, 1, 1)
 year2 = datetime.date(b, 1, 1)

 print(*re.findall(r'\d+(?= )', str(year2 - year1)))  # -> 1461
 print(abs(year2 - year1).days)                       # -> 1461
 -----------------------------------------------------------------------------------------------------------------------

 # Вывести на экран произведение цифр.
 a = 1984
 from functools import reduce

 lst = [int(i) for i in str(a)]
 print(reduce(lambda x, y: x * y, lst))  # -> 288

 # Классное решение через eval()
 print('*'.join(str(a)))           # -> 1*9*8*4
 print(eval('*'.join(str(a))))     # -> 288


 # Другой Пример
 # Можно через math.prod()
 a = [1, 2, 3, 4]
 print(__import__('math').prod(a))         # -> 24

 # Если пустой, то возвращает 1
 print(__import__('math').prod([]))        # -> 1
 print(reduce(lambda x, y: x * y, [], 1))  # -> 1
 -----------------------------------------------------------------------------------------------------------------------

 # Общее количество секунд перевести в   часы, минуты и секунды
 a = 129700

 import time
 res = time.gmtime(a)
 print(time.strftime("%H:%M:%S", res))         # -> 12:01:40         # f-строки  не работают с time.struct_time

 from datetime import timedelta
 print(str(timedelta(seconds=a)).split()[-1])  # -> 12:01:40
 print(timedelta(seconds=a))                   # -> 1 day, 12:01:40
 -----------------------------------------------------------------------------------------------------------------------

 # Определить, содержится ли в этом числе хотя бы одна цифра 1
 a = 256

 print('Да' if '1' in str(a) else 'Нет')                      # -> Нет
 print(('Нет', 'Да')[str(a).count('1') >= 1])                 # -> Нет

 # Классные решения Пойми почему!
 print(('Нет', 'Да')['1' in str(a)])                          # -> Нет
 print(("Нет", "Да")[any(digit == '1' for digit in str(a))])  # -> Нет
 -----------------------------------------------------------------------------------------------------------------------

 # s = 'aaaabbсaa' преобразуется в 'a4b2с1a2'  Считаем символы которые идут подряд
 a = 'aaaabbcaa'

 # Придумал сам)
 print(re.sub(r'(\w)\1+|\w', lambda x: f'{x[0][0]}{len(x[0])}', a))  # -> a4b2c1a2

 # Первый способ с groupby
 from itertools import groupby

 for k, g in groupby(a):
     print(k, len(list(g)), sep='', end='')  # -> a4b2c1a2


 # Второй способ руками
 a = 'aaaabbcaa'
 genome = a+' '
 s = 0
 n=genome[0]
 for i in genome:
     if n!=i:
         print(n + str(s), end = '')         # -> a4b2c1a2
         s=0
         n=i
     s+=1


 # Тоже руками
 s='aaaabbcaa'
 last_word=s[0]
 last_count=1
 res=''

 for el in s[1:]:
     if el==last_word:
         last_count+=1
     else:
         res+=f'{last_word}{last_count}'
         last_count=1
         last_word=el

 res+=f'{last_word}{last_count}'
 print(res)                                 # -> a4b2c1a2
 -----------------------------------------------------------------------------------------------------------------------

 # Определить, сколько раз в этом списке два одинаковых элемента стоят рядом.
 lst = [1, 2, 2, 3, 4, 4, 5, 6, 6, 6, 7]
 print(sum(lst[i] == lst[i - 1] for i in range(1, len(lst))))  # -> 4

 # Тоже самое
 c=0
 for i in range(len(lst)-1):
     if lst[i]==lst[i+1]:
         c+=1
 print(c)                                                      # -> 4
 -----------------------------------------------------------------------------------------------------------------------

 # Найти все слова длиной не менее 5 символов и содержащие не менее 2 гласных
 s = 'The candle light will burn the whole night'.split()

 for i in s:
     x = sum([1 for l in i if l in 'aeiouy'])
     if len(i) >= 5 and x >= 2:
         print(i, end=' ')                              # ->  candle whole

 # Тоже самое
 for i in s.split():
    if len(i) > 4 and sum(w.lower() in 'aeiouy' for w in i) > 1:
        print(i)                                        # ->  candle whole

 -----------------------------------------------------------------------------------------------------------------------
 Валидация пароля  длина пароля не менее 8 символов   1 строчная, 1  прописная буква и хотя бы 1 цифра

 s = 'hGjk67_sdfkl56'
 print('-+'[bool(re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d_]{8,}$', s))])    # -> +


 # Тоже самое
 answer = '-'

 if bool(re.match('^[a-zA-Z0-9_]{8,}$', s)):
     a = bool(re.search('[a-z]', s))
     b = bool(re.search('[A-Z]', s))
     c = bool(re.search('[0-9]', s))
     answer = ('-+')[a * b * c]

 print(answer)                                                                          # -> +
 -----------------------------------------------------------------------------------------------------------------------

 # Определить количество пар соседних чисел, сумма которых кратна 5.
 c, lst = 0, [1, 7, 3, 2, 6, 8, 12]

 # Вариант 1
 from itertools import pairwise
 print(list(pairwise(lst)))                                      # -> [(1, 7), (7, 3), (3, 2), (2, 6), (6, 8), (8, 12)]

 for i in list(pairwise(lst)):
     if sum(i) % 5 == 0:
         c += 1
 print(c)                                                        # -> 3


 # Вариант 2
 print([(x, y)for x, y in zip(lst, lst[1:])])                    # -> [(1, 7), (7, 3), (3, 2), (2, 6), (6, 8), (8, 12)]
 print(sum(not (x + y) % 5 for x, y in zip(lst, lst[1:])))       # -> 3
 print(sum(not (a + b) % 5 for a, b in zip(lst[:-1], lst[1:])))  # -> 3


 # Вариант 3
 c=0
 for i in range(len(lst)-1):
     if (lst[i]+lst[i+1]) % 5==0:
         c+=1
 print(c)                                                        # -> 3
 -----------------------------------------------------------------------------------------------------------------------

 # Вывести задом-наперёд все слова, состоящие менее, чем из 6 букв, и не содержащие подряд идущих букв o или O.
 s = 'Temperature hehe rising too man'

 res = [i[::-1] for i in s.split() if len(i) < 6 and 'oo' not in i.lower()]
 print(*res)  # -> eheh nam
 -----------------------------------------------------------------------------------------------------------------------

 Разница между if  vs  elif   Важно!!!!                 <-----                               <-----

 # Программа должна определить, какой тип треугольника образуется по длинам введенных сторон:
 # Равнобедренный (два равных)  Равносторонний (все стороны равны) Разносторонний (все стороны разные).
 # Блок elif это тот же if, но только следующая проверка.   elif - Это можно перевести как "иначе если"

 a = 5
 b = 5
 c = 5

 # Без elif    2 Вывода              # С   elif  1 Вывод

 if a == b == c:                     if a == b == c:
     print("Равносторонний")             print("Равносторонний")
 if a == b or b == c or a == c:      elif a == b or b == c or a == c:
     print("Равнобедренный")             print("Равнобедренный")
 else:                               else:
     print("Разносторонний")             print("Разносторонний")

 # -> Равносторонний                 # -> Равносторонний                       # <-----
 # -> Равнобедренный                                                           # <-----


 # Тоже самое
 s = '5 5 5'
 print(['Равносторонний', 'Равнобедренный', 'Разносторонний'][len(set(s.split()))-1])  # -> Равносторонний
 -----------------------------------------------------------------------------------------------------------------------

 Используйте следующие правила:

 если каждое из трех измерений менее или равно 15 сантиметрам, то выведите на экран "Коробка №1";
 если хотя бы одно из измерений больше 2 метров, то выводите "Упаковка для лыж";
 если хотя бы одно из измерений больше 15 сантиметров, но менее 50 сантиметров, то выводите "Коробка №2";
 во всех остальных случаях выводите "Коробка №3".

 a = 15     # a = int(input())
 b = 55     # b = int(input())
 c = 15     # c = int(input())

 def is_valid(*args):
     if all(i <= 15 for i in args):
         return "Коробка №1"
     elif any(i > 200 for i in args):
         return "Упаковка для лыж"
     elif any(15 < i < 50 for i in args):
         return "Коробка №2"
     return "Коробка №3"

 print(is_valid(a, b, c))  # -> Коробка №3
 -----------------------------------------------------------------------------------------------------------------------

 # match case и Моржик и несколько переменных сразу
 a, b = 7, 4

 match (a:= 7), (b:= 4):
     case 7, 4:
         print(6)    # -> 6
     case 10, 5:
         print(10)
     case 6, 3:
         print(4)
 -----------------------------------------------------------------------------------------------------------------------

 # Использование __import__   Найти цифры длиной 5 символов
 s = '752f78'

 print(bool(__import__('re').search(r'\d{5}', s)))  # -> False

 -----------------------------------------------------------------------------------------------------------------------

 # Дано число секунд. Вычислите сколько это часов, минут и секунд.

 # Первый вариант не лучший!
 import time
 t = time.gmtime(4000)
 h, m, s = time.strftime("%H:%M:%S", t).split(':')
 print(f'{int(h)} часов {m} минут {s} секунд')                  # -> 1 часов 06 минут 40 секунд


 # Второй вариант Лучший!!!
 from datetime import timedelta, datetime
 dt = datetime(year=1, month=1, day=1, minute=0, second=0)  # Создали дату
 print(dt)                 # -> 0001-01-01 00:00:00

 delta = timedelta(seconds=4000)  # Создали делту
 print(delta)              # -> 1:06:40

 # Можно даже Много плюсов использовать ошибки не будет + == +++++++ == + +             <-----            <-----
 print((dt ++++ delta).strftime('%H часов %M минут %S секунд'))  # -> 01 часов 06 минут 40 секунд

 # Или еще лучше через ф-строку
 print(f"{(dt + +++ delta):%H часов %M минут %S секунд}")        # -> 01 часов 06 минут 40 секунд

 -----------------------------------------------------------------------------------------------------------------------

 Как написать if else if else в тернарном операторе     И ПОСМОТРИ ВТОРОЙ ВАРИАНТ!                        <-----

 # Даны два числа определить какое из них больше.

 # Первый варинт
 a, b = [int(i) for i in '5 6'.split()]
 print('Первое больше' if a > b else 'Второе больше' if b > a else 'Равны')  # -> Второе больше

 # Второй варинт                                                             # -> Второе больше          <-----
 (lambda a, b: print(('Равны', 'Первое больше', 'Второе больше')[(a > b) - (b > a)]))(*map(int, '5 6'.split()))
 -----------------------------------------------------------------------------------------------------------------------

 # выигрыш=3/проигрыш=0/ничья=1 если другое ничего ''
 a = 3

 print('выигрыш' if a == 3 else 'проигрыш' if a == 0 else 'ничья' if a == 1 else '')   # -> выигрыш
 print({3: 'выигрыш', 1: 'ничья', 0: 'проигрыш'}.get(a, ''))                           # -> выигрыш
 -----------------------------------------------------------------------------------------------------------------------

 # Выведите на экран в одну строку числа от 5 до -5 включительно.
 [print(i, end=' ') for i in range(-5, 5+1)[::-1]]   # -> 5 4 3 2 1 0 -1 -2 -3 -4 -5
 print()
 [print(i, end=' ') for i in range(5, -6, -1)]       # -> 5 4 3 2 1 0 -1 -2 -3 -4 -5
 -----------------------------------------------------------------------------------------------------------------------

 # находит сумму и количество чисел, кратных 17 или выводит NO    Посмотри как можно в кортеже указывать  NO

 res = [int(i) for i in iter(input, '0') if int(i) % 17 == 0]
 print(*[sum(res), len(res)] if res else ('NO', ))

 # ИЛИ ТАК
 data = [*filter(lambda x: not x % 17, map(int, iter(input, '0')))]
 print(*(sum(data), len(data)) if data else ('NO', ))
 -----------------------------------------------------------------------------------------------------------------------

 # Распаковка сразу нескольких iterable *
 s = '-5 5 1 3 8 -1'
 res = [int(i) for i in s.split()]
 print(*[i for i in res if i > 0], *[i for i in res if i < 0])        # -> 5 1 3 8 -5 -1
 print(*filter(lambda x: x > 0, res), *filter(lambda x: x < 0, res))  # -> 5 1 3 8 -5 -1

 # Умный вариант
 print(*sorted(map(int, s.split()), key=lambda x: x <= 0))            # -> 5 1 3 8 -5 -1
 -----------------------------------------------------------------------------------------------------------------------

 # Упорядочите элементы по возрастанию их модуля (абсолютного значения).
 res = ['-5', '10', '-1', '2', '6', '4', '-9', '8', '40', '-15']

 print(sorted([int(i) for i in res], key=abs))               # -> [-1, 2, 4, -5, 6, 8, -9, 10, -15, 40]
 print(sorted([i for i in res], key=lambda x: abs(int(x))))  # -> ['-1', '2', '4', '-5', '6', '8', '-9', '10', '-15', '40']
 -----------------------------------------------------------------------------------------------------------------------

 # Упорядочить слова по убыванию их длин. Можно через добавление - сортировать
 res = 'слон бродит по джунглям'.split()

 print(*sorted(res, key=lambda x: -len(x)))  # -> джунглям бродит слон по
 print(*sorted(res, key=len, reverse=True))  # -> джунглям бродит слон по
 -----------------------------------------------------------------------------------------------------------------------

 # Поиск трех последовательных элементов, сумма которых максимальна, Вывести только первую   Как можно сделать 3 группы!
 res = [40, 500, 6, 8, 6, 7, 5, 56, 45]

 res = [i for i in zip(res, res[1:], res[2:])]
 print(res)               # ->[(40, 500, 6), (500, 6, 8), (6, 8, 6), (8, 6, 7), (6, 7, 5), (7, 5, 56), (5, 56, 45)]
 a_max = 0
 for i in res:
     if sum(i) > a_max:
         a_max = sum(i)

 for i in res:
     if sum(i) == a_max:
         print(*i)                          # -> 40 500 6
         break



 # Очень крутое решение!!!  Тоже самое

 from collections import deque

 res = [40, 500, 6, 8, 6, 7, 5, 56, 45]

 q, res2 = deque('', 3), (0,)
 for n in res:
     q.append(n)
     res2 = max(res2, tuple(q), key=sum)
 print(*res2)                               # -> 40 500 6
 -----------------------------------------------------------------------------------------------------------------------

 # Минимальное значение среди трёхзначных элементов массива, делящихся на 7.  В min/max можно задавать default!!!
 res = [40, 500, 6, 8, 6, 7, 5, 56, 45]

 res = [int(i) for i in res]
 res = [i for i in res if len(str(i)) == 3 and i % 7 == 0]

 print(min(res))                           # -> ValueError: min() arg is an empty sequence
 print(min(res) if res else 'Не найдено')  # -> Не найдено
 print(min(res, default='Не найдено'))     # -> Не найдено

 # Тоже самое
 print(min(filter(lambda x: (not int(x) % 7) and len(x.strip()) == 3, res), key=int, default='Не найдено'))  # -> Не найдено
 -----------------------------------------------------------------------------------------------------------------------

 # Определите максимальную длину цепочки вида ABCABCABC    фрагмент цепочки может быть неполным
 n = 'CCCCABCABCABCACCCC'

 # Асимптотика - поведение функции при стремлении аргумента к бесконечности
 # Асимптотический анализ — метод описания предельного поведения функций.

 print(max((len(s) for s in re.findall(r"A(?:BCA)*(?:BC?)?", n)), default=0))  # -> 10

 # Хз почему не проходил все тесты
 res = re.search(r'(ABC)+(AB?)*', n).group()
 print(len(res))                                                               # -> 10
 -----------------------------------------------------------------------------------------------------------------------

 # Количество 7-буквенные коды перестановкой букв слова КОННЕКТ. При этом нельзя ставить рядом две гласные.
 from itertools import permutations

 s = map(lambda x: ''.join(x), set(permutations('КОННЕКТ')))
 print(len([x for x in s if 'ОЕ' not in x and 'ЕО' not in x]))                                           # -> 900

 # Тоже самое
 res = sum(not any(x in ''.join(perm) for x in ("ОЕ", "ЕО")) for perm in set(permutations("КОННЕКТ")))
 print(res)                                                                                              # -> 900

 # Тоже самое
 print(sum(not ('ОЕ' in w or 'ЕО' in w) for w in {''.join(p) for p in permutations('КОННЕКТ')}))         # -> 900
 -----------------------------------------------------------------------------------------------------------------------

 # Количество 4-буквенные слова, в которых есть только буквы A, B, C, D, X, причём буква X появляется ровно 1 раз.
 import itertools                                         from itertools import product

 a = 0                                                    cnt = 0
 for word in itertools.product('ABCDX', repeat = 4):      for text in product('abcdx', repeat=4):
     t = word[0] + word[1] + word[2] + word[3]                if text.count('x') == 1:
     if t.count('X') == 1:                                        cnt += 1
         a += 1

 print(a)  # -> 256                                       print(cnt)  # -> 256

 # Тоже самое
 print(sum(1 for t in product('ABCDX', repeat=4) if t.count('X') == 1))  # -> 256
 print(sum(i.count('X') == 1 for i in product('ABCDX', repeat=4)))       # -> 256
 -----------------------------------------------------------------------------------------------------------------------

 # Все 5-буквенные слова, составленные из букв К, О, Р    Запишите слово, которое стоит под номером 237.
 from itertools import product

 for index, text in enumerate(product('КОР', repeat=5), start=1):
     if index == 237:
         print(''.join(text))  # -> РРРКР
         break

 # Тоже самое
 for i, el in enumerate(sorted(set(permutations('КОР' * 5, 5))), 1):
     if i == 237:
         print(''.join(el))    # -> РРРКР
         break
 -----------------------------------------------------------------------------------------------------------------------

 # Все четырёхбуквенные слова, составленные из букв А, Л, Г, О, Р, И, Т, М  Под каким номером начинается с букв ИГ?
 # Алгоритм нужна запускать по набору слов "АГИЛМОРТ", а не "АЛГОРИТМ".  - алфавитный порядок

 from itertools import product
 import re

 for index, text in enumerate(product('АГИЛМОРТ', repeat=4), start=1):
     if re.match(r'ИГ', ''.join(text)):
         print(index, ''.join(text))  # -> 1089 ИГАА
         break
 -----------------------------------------------------------------------------------------------------------------------

 # Классный пример
 a, b = 10, 15                      a, b = 10, 15
 print(-min(-a, -b))  # -> 15       print(-max(-a, -b))  # -> 10
 print(min(-a, -b))   # -> -15      print(max(-a, -b))   # -> -10
 print(min(a, b))     # -> 10       print(max(a, b))     # -> 15
 -----------------------------------------------------------------------------------------------------------------------

 # Интересные примеры с range()
 for i in range(0):
     print("Не забудь написать здесь что-нибудь")  # Ничего Не выведет Без Ошибки

 for i in range(-1):
    print("Не забудь написать здесь что-нибудь")   # Ничего Не выведет Без Ошибки

 for i in range(0, 5, 0):
     print(i, end=" ")     # -> ValueError: range() arg 3 must not be zero

 for i in range(0, 5, 15):
     print(i, end=" ")     # -> 0

 a, b, c = 1, 7, 2
 print(range(a, b, c))   # -> range(1, 7, 2)
 print(*range(a, b, c))  # -> 1 3 5

 -----------------------------------------------------------------------------------------------------------------------

 # Интересные примеры с break/continue

 # то есть, когда i будет 4, она подпадает под это условие, и выполнится continue
 for i in range(10):
    if i % 2 == 0:
        continue
    if i == 4:
        break
    print(i, end=" ")  # -> 1 3 5 7 9


 # else Отработал потому что цикл завершился в Штатном режиме
 for i in range(10):
     if i == 5:
         continue
     print(i, end="")
 else:
     print(5)   # -> 0123467895
 -----------------------------------------------------------------------------------------------------------------------

 # Вывести последний символ
 s = "Hello world"

 print(s[-1])                               # -> d
 print(s[slice(None, None, -1)][slice(1)])  # -> d
 print(s[~0])                               # -> d

 # ~0 == -1
 print(~0)                                  # -> -1
 print(~1)                                  # -> -2


 # Интересные примеры slice
 # Без первых двух и последних двух символов.
 s = "1234567890"

 print(f"{s[slice(2, -2, None)]}")  # -> 345678
 print(s[2:-2])                     # -> 345678
 -----------------------------------------------------------------------------------------------------------------------

 # Пример islower()/isupper()

 # Цифры всегда lower? нет, только если в строке есть хотя бы один символ в нижнем регистре
 print('1234'.islower())                           # -> False
 print('hello 1234'.islower())                     # -> True
 print('_hello'.islower())                         # -> True
 print("my password is \"miku1234\"".islower())    # -> True

 # Тоже самое для isupper()
 print('1234'.isupper())                           # -> False
 print('HELLO 1234'.isupper())                     # -> True
 print('_HELLO'.isupper())                         # -> True
 print("MY PASSWORD IS \"MIKU1234\"".isupper())    # -> True
 -----------------------------------------------------------------------------------------------------------------------

 # Что выводит m и вообще что такое m  Используем  m[0] или m.group(0) или m.group()

 def sub_fun(m):                def sub_fun(m):                      def sub_fun(m):
     print(m)                       print(m)                             print(m)
     if m[0] == 'Ё':                if m.group(0) == 'Ё':                if m.group() == 'Ё':
         return 'Е'                     return 'Е'                           return 'Е'
     if m[0] == 'ё':                if m.group(0) == 'ё':                if m.group() == 'ё':
         return 'е'                     return 'е'                           return 'е'

 # -> <re.Match object; span=(1, 2), match='ё'>
 # -> <re.Match object; span=(9, 10), match='Ё'>
 # -> <re.Match object; span=(16, 17), match='ё'>

 # match case  Bывод что такое m[0]   m.group()
 def sub_fun(m):
     print(f"{m},       ---{m[0]=}   ---  {m.group()=}")
     match m[0]:
         case 'ё':
             return 'е'
         case _:
             return 'Е'

 # -> <re.Match object; span=(1, 2), match='ё'>,       ---m[0]='ё'   ---  m.group()='ё'
 # -> <re.Match object; span=(9, 10), match='Ё'>,       ---m[0]='Ё'   ---  m.group()='Ё'
 # -> <re.Match object; span=(16, 17), match='ё'>,       ---m[0]='ё'   ---  m.group()='ё'


 # Ё нужно заменить Е   ё нужно заменить е
 s = "Чёрный, жЁлтый, ёжик"

 print(__import__('re').sub(r'ё|Ё', sub_fun, s))   # -> Черный, жЕлтый, ежик
 print(__import__('re').sub(r'[ёЁ]', sub_fun, s))  # -> Черный, жЕлтый, ежик
 -----------------------------------------------------------------------------------------------------------------------

 # Если вы хотите добавить строку к списку, можете использовать метод append() или оператор +=.
 lst = ['hello']
 lst += 'world'
 print(lst)                 # -> ['hello', 'w', 'o', 'r', 'l', 'd']

 lst = ['hello'] + 'world'  # -> TypeError: can only concatenate list (not "str") to list
 -----------------------------------------------------------------------------------------------------------------------

 # Преобразует список в одномерный.
 # То есть, за основу берётся пустой список, куда мы "прибавляем" прочие списки из многомерности)

 nested_list = [[1, 2], [3, 4], [5, 6]]
 flattened_list = sum(nested_list, [])
 print(flattened_list)                   # -> [1, 2, 3, 4, 5, 6]

 # Пример с start
 print(sum([1, 2, 3, 4], start=-10))  # -> 0
 -----------------------------------------------------------------------------------------------------------------------

 # Пример split()
 s = "---"
 print(s.split("-"))  # -> ['', '', '', '']
 -----------------------------------------------------------------------------------------------------------------------

 # Для map  list внутри genexp можно НЕ писать тоже будет работать
 s = '1 2 3 4 5 6 7 8 39'
 print([i for i in map(int, s.split()) if i % 2 == 0])           # -> [2, 4, 6, 8]   # map(int, s.split())
 print([i for i in list(map(int, s.split())) if i % 2 == 0])     # -> [2, 4, 6, 8]   # list(map(int, s.split()))

 # Тоже самое
 print(list(filter(lambda x: not x % 2, map(int, s.split()))))           # -> [2, 4, 6, 8]
 print(list(filter(lambda x: not x % 2, [int(i) for i in s.split()])))   # -> [2, 4, 6, 8]

 # Тоже самое без map
 print([i for i in [int(i) for i in s.split()] if i % 2 == 0])           # -> [2, 4, 6, 8]



 # class map(object):   возвращает итератор map object

 # Интересный пример с map                                                                      <-----      <-----
 # Работает как обычный итератор
 a = [-1, 2, -3]
 result = map(abs, a)
 print(result)        # -> <map object at 0x00000228C5CFE230>
 print(next(result))  # -> 1
 print(next(result))  # -> 2
 print(next(result))  # -> 3
 print(next(result))  # -> StopIteration


 # Можно обходить итератор map object сразу в цикле for
 a = [-1, 2, -3, 4, -5]
 for value in map(abs, a):
     print(value, end=' ')  # -> 1 2 3 4 5

 # Для повторного итерирования нужно будет создавать новый итератор при помощи map.
 a = [-1, 2, -3, 4, -5]
 iterator = map(abs, a)
 print(max(iterator))  # -> 5
 print(max(iterator))  # -> ValueError: max() arg is an empty sequence


 # Использование функций
 str_nums = ['-1', '4232', '-33', '312', '12']
 nums = list(map(int, str_nums))
 print(nums)                            # -> [-1, 4232, -33, 312, 12]

 a = ['hello', 'hi', 'good morning']
 b = list(map(len, a))
 print(b)                               # -> [5, 2, 12]

 # В качестве функции в map можно передавать не только встроенные и пользовательские функции, но и методы объектов.
 a = ['hello', 'hi', 'good morning']
 b = list(map(str.upper, a))
 print(b)                               # -> ['HELLO', 'HI', 'GOOD MORNING']


 list_strings = ['hello', 'hi']
 b = list(map(list, list_strings))
 print(b)                               # -> [['h', 'e', 'l', 'l', 'o'], ['h', 'i']]

 words = list(map(sorted, b))
 print(words)                           # -> [['e', 'h', 'l', 'l', 'o'], ['h', 'i']]


 # Всё тоже самое можно делать без map при помощи Генераторов

 list_strings = ['hello', 'hi', 'good morning']
 print(list(map(lambda x: x[::-1], list_strings)))  # -> ['olleh', 'ih', 'gninrom doog']
 print([i[::-1] for i in list_strings])             # -> ['olleh', 'ih', 'gninrom doog']

 # Главное примечание про map и filter и zip
 map представляет собой класс   class map(object):  тоже классы      class filter(object):      class zip(object):

 # Может принимать несколько последовательностей
 # class map(object)
 #    map(func, *iterables) --> map object

 nums1 = [1, 2, 3]
 nums2 = [4, 5, 6]
 nums3 = [7, 8, 9]

 result = map(lambda x, y, z: x + y + z, nums1, nums2, nums3)
 print(list(result))  # -> [12, 15, 18]


 # Что увидим на экране после запуска следующего кода?
 nums1 = [10, 20, 30, 40]
 nums2 = [20, 30, 40, 50]

 result = map(lambda x, y, w=0: x - y - w, nums2, nums1)
 print(sum(result))                                          # -> 40


 # Пример class filter(object):  является функцией/классом высшего порядка,   возвращает итератор filter object

 # Результат получается идентичным. Но filter Возвращает итератор а в нем физически не хранятся все элементы.
 def is_two_digit(x: int) -> bool:
     return x > 9 and x < 100

 numbers = [14, 0, 5, -79, 645, 7952, 18, 0, -192, 471]
 num_filters = list(filter(is_two_digit, numbers)) # фильтруем через filter
 print(num_filters)                  # -> [14, 18]

 # фильтруем через генератор списка
 num_list_comp = [n for n in numbers if is_two_digit(n)]
 print(num_list_comp)                # -> [14, 18]



 # Пример class zip(object):   возвращает итератор zip object

 # Посмотри все примеры!!!
 words = ['approach', 'monstrous', 'mobile']
 numbers = [100, 200, 300]
 s = 'AB'

 result_zip = zip(words, numbers, s)
 print(list(result_zip))                 # -> [('approach', 100, 'A'), ('monstrous', 200, 'B')]

 # Нужно создать новый итератор
 print(list(zip(*result_zip)))           # -> []

 # Создаем новый итератор потому что он закончился
 result_zip = zip(words, numbers, s)
 print(list(zip(*result_zip)))           # -> [('approach', 'monstrous'), (100, 200), ('A', 'B')]

 # Интересный вариант Распаковка
 result_zip = zip(words, numbers, s)
 col1, col2, col3 = zip(*result_zip)

 print(col1)  # -> ('approach', 'monstrous')
 print(col2)  # -> (100, 200)
 print(col3)  # -> ('A', 'B')


 # Все возвращают итератор
 print(zip([1, 2], [2, 3]))                # -> <zip object at 0x000002EEF0F0A700>
 print(map(str, [1, 2]))                   # -> <map object at 0x000002EEF26BE200>
 print(filter(lambda x: x > 2, [1, 2]))    # -> <filter object at 0x000002EEF26BE200>
 -----------------------------------------------------------------------------------------------------------------------

 # Циклическая ссылка  Рекурсия
 l = [1, 2, 3]
 l.append(l)
 print(l)    # -> [1, 2, 3, [...]]

 # Обьяснение
 Этот код создает список l с элементами 1, 2 и 3, а затем добавляет сам список l в конец этого списка.
 Это приводит к циклической ссылке внутри списка l.

 Когда вы выводите список l с помощью print(l), Python пытается представить этот список, и он обнаруживает
 циклическую ссылку. Результатом будет [1, 2, 3, [...]], где ... указывает на циклическую ссылку на сам список.

 Когда вы видите ... в выводе, это означает, что есть циклическая ссылка, и Python избегает бесконечной рекурсии
 при попытке представить всю структуру. Вместо этого он показывает ... для указания на циклическую ссылку.


 # Поскольку между пробелами нет других символов, результат split(' ') будет список
 print(len((' ' * 10).split(' ')))  # -> 11
 print(len((' ' * 10).split()))     # -> 0

 print((' ' * 10).split(' '))       # -> ['', '', '', '', '', '', '', '', '', '', '']
 print((' ' * 10).split())          # -> []
 -----------------------------------------------------------------------------------------------------------------------

 # Реализуйте программу, которая будет вычислять количество различных объектов в списке.    Очень круто!!!
 objects = [1, 2, 1, 5, True, False, True, 'false', [], [1,2], [1,2]]

 print(len(set(map(id, objects))))         # -> 9
 print(len(set(id(i) for i in objects)))   # -> 9

 # Так не работает!
 print(len(set(objects)))                  # -> TypeError: unhashable type: 'list'


 # Тоже самое

 n = len(objects)
 ans = n
 for i in range(n):
     for j in range(i):
         if id(objects[i]) == id(objects[j]):
             ans -= 1
             break

 print(ans)                                 # -> 9
 -----------------------------------------------------------------------------------------------------------------------

 # Приоритет с более высокой точностью (float).
 print(5 + 2.0)  # -> 7.0
 print(5 - 2.0)  # -> 3.0
 print(5 / 2)    # -> 2.5

 # Интересные примеры
 print(int(-2.8))         # -> -2
 print(int(4.9))          # -> 4
 print(round(-2.375, 2))  # -> -2.38
 -----------------------------------------------------------------------------------------------------------------------

 # Напечатайте индекс наименьшего числа в списке.
 lst = [5, 8, 3, 2, 7, 4, 9]

 print(abs(lst.index(min(lst))))                        # -> 3
 print((arr := [5, 8, 3, 2, 7, 4, 9]).index(min(arr)))  # -> 3  # Морж классный  <-----
 print(min(range(len(lst)), key=lst.__getitem__))       # -> 3
 -----------------------------------------------------------------------------------------------------------------------

 # Найти индекс последнего вхождения этого числа в список   ИЩЕМ ЧИСЛО 5
 lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 5]
 res = []
 for i, v in enumerate(lst):
     if v == 5:
         res.append([i, v])

 print(res[-1][0] if res else 'Числа нет!')                                                # -> 9


 # Тоже самое
 a, b = ''.join('1 2 3 4 5 6 7 8 9 5'.split()), '5'
 c = a.rfind(b)
 print(c if c >= 0 else "Числа нет!")                                                      # -> 9


 # Тоже самое
 a, b = ''.join('1 2 3 4 5 6 7 8 9 5'.split()), '5'
 print(["Числа нет!", a.rfind(b)][b in a])                                                 # -> 9


 # Тоже самое  Через словарь
 lst = '1 2 3 4 5 6 7 8 9 5'
 print({value: index for index, value in enumerate(lst.split())}.get('5', "Числа нет!"))   # -> 9


 # Тоже самое
 l, n = '1 2 3 4 5 6 7 8 9 5'.split(), '5'
 l.reverse()
 try:
     print(len(l) - l.index(n) - 1)                                                        # -> 9
 except:
     print('Числа нет!')


 # Тоже самое
 data, num = [*map(int, '1 2 3 4 5 6 7 8 9 5'.split())], 5
 idx = len(data)
 while (idx := idx - 1) >= 0:
     if num == data[idx]:
         print(idx)
         break
 else:
     print('Числа нет!')                                                                    # -> 9
 -----------------------------------------------------------------------------------------------------------------------

 # Заменить запятые на Одну запятую
 s = '1, 2, , , , 3, 4, 5'

 print(__import__('re').sub(r'(, )+', ', ', s))          # -> 1, 2, 3, 4, 5
 print(*__import__('re').findall(r'\w+', s), sep=', ')   # -> 1, 2, 3, 4, 5
 -----------------------------------------------------------------------------------------------------------------------

 # Убрать лишние пробелы
 s = 'Алгоритмы     это основа    программирования'
 
 print(*s.split())               # -> Алгоритмы это основа программирования
 print(' '.join(s.split()))      # -> Алгоритмы это основа программирования
 print(re.sub(r'\s+', r' ', s))  # -> Алгоритмы это основа программирования
 -----------------------------------------------------------------------------------------------------------------------

 # Наибольший общий делитель двух чисел  math.gcd
 print(__import__('math').gcd(30, 18))   # -> 6
 -----------------------------------------------------------------------------------------------------------------------

 # Выведите True, если последовательность возрастающая и False, если нет.

 lst = [-6, -3, 1, 4, 6, 10]
 for i, j in zip(lst, lst[1:]):
     if i > j:
         print(False)
         break
 else:
     print(True)                                                                                 # -> True

 # Тоже самое
 print(lst == sorted(lst) and len(lst) == len(set(lst)))                                         # -> True
 print((lst:='-6 -3 1 4 6 10'.split()) == sorted(lst, key=int) and len(lst) == len(set(lst)))    # -> True
 print((lambda *arr: all(a < b for a, b in zip(arr, arr[1:])))(lst))                             # -> True
 -----------------------------------------------------------------------------------------------------------------------

 # Обновить словарь
 students = {"Alice": {"English": 85}, "Bob": {"English": 92}}
 additional_scores = {"Alice": {"History": 87, "Geography": 76}, "Bob": {"History": 91,    "Geography": 83}}
 # print(eagles | beavers)

 # Создать новый словарь
 a_dict = {}
 for k, v in zip(additional_scores.items(), students.items()):
     # a_dict[k[0]] = v[1] | k[1]
     a_dict[k[0]] = {**v[1], **k[1]}
 print(a_dict)
 # {'Alice': {'English': 85, 'History': 87, 'Geography': 76}, 'Bob': {'English': 92, 'History': 91, 'Geography': 83}}

 # Обновить текущий
 for k, v in students.items():
     v.update(additional_scores[k])
 print(students)
 # {'Alice': {'English': 85, 'History': 87, 'Geography': 76}, 'Bob': {'English': 92, 'History': 91, 'Geography': 83}}

 # Обновить текущий
 students['Alice'].update(additional_scores['Alice'])
 students["Bob"].update(additional_scores["Bob"])
 print(students)
 # {'Alice': {'English': 85, 'History': 87, 'Geography': 76}, 'Bob': {'English': 92, 'History': 91, 'Geography': 83}}
 -----------------------------------------------------------------------------------------------------------------------

 #  Определите, какое слово в тексте встречается чаще всего и напечатайте, сколько раз оно встретилось в тексте.
 s = 'The cat sat on the mat'.lower().split()

 # Простой вариант
 print(s.count(max(s, key=lambda x: s.count(x))))                                    # -> 2

 # Варинт Counter
 from collections import Counter
 print(max(Counter(s).values()))                                                     # -> 2

 # Варинт Counter и регулярка
 import re
 from collections import Counter

 s = 'The cat sat on the mat'
 print(Counter(re.findall('\w+', s.lower())).most_common(1)[0][1])                   # -> 2
 print(Counter(re.findall('\w+', s.lower())).most_common(1))                         # -> [('the', 2)]

 # Интерсный вариант
 from collections import Counter
 from string import punctuation
 import re

 print(max(Counter(re.sub(fr'[{punctuation}]', '', s).lower().split()).values()))    # -> 2
 -----------------------------------------------------------------------------------------------------------------------

 # Пример с Без распаковки *  Общие элементы есть
 s = set('John, Mary, David, Alice, Charlie'.split(', '))
 s1 = set('Mary, Kate, Peter, Emily, Frank'.split(', '))
 res = s & s1

 print(', '.join(sorted(res)) if res else 'Общих друзей нет!', sep=', ')  # -> Mary


 # Пример с распаковкой *  Общих элементов нет
 s = set('John, David, Alice, Charlie'.split(', '))
 s1 = 'Kate, Peter, Emily, Frank'.split(', ')
 res = s.intersection(s1)

 # При использование * в print Распаковка для всего Посмотри пример
 print(*sorted(res)if res else ['Общих друзей нет!'], sep=', ')  # -> Общих друзей нет!
 print(*sorted(res)if res else 'Общих друзей нет!', sep=', ')    # -> О, б, щ, и, х,  , д, р, у, з, е, й,  , н, е, т, !
 -----------------------------------------------------------------------------------------------------------------------

 # Найти пересечение
 lst = [{'Salad', 'Fries', 'Pizza'}, {'Steak', 'Salad', 'Pizza'}, {'Salad', 'Pizza', 'Fries'}]

 res = set.intersection(*lst)
 print(*sorted(res) if res else ["Общих вкусов нет!"], sep=', ')  # -> Pizza, Salad
 -----------------------------------------------------------------------------------------------------------------------

 # Проверьте, что все значения этого словаря являются непустыми строками.
 profile = {'name': 'John', 'age': '30', 'occupation': '', 'location': 'London'}
 print(all(profile.values()))  # -> False

 profile = {'name': 'Alice ', 'occupation': 'programmer'}
 print(all(profile.values()))  # -> True
 -----------------------------------------------------------------------------------------------------------------------

 # Выведите строки, содержащие слово, состоящее из двух одинаковых частей (тандемный повтор).
 s = '123123 is good too'

 print(re.search(r"\b(\w+)\1\b", s).group())            # -> 123123
 print(__import__('re').search(r'(\b\w+)\1\b', s)[0])   # -> 123123

 s = 'aaa'
 print(re.search(r"\b(\w+)\1\b", s))                    # -> None
 print(__import__('re').search(r'(\b\w+)\1\b', s))      # -> None
 -----------------------------------------------------------------------------------------------------------------------

 # Нельзя пользоваться встроенными сортировками в Python
 lst = [19, 4, 5, 17, 1]

 def quick_sort(lst):
     no_sorted = sorted
     return no_sorted(lst)

 print(quick_sort(lst))  # -> [1, 4, 5, 17, 19]
 -----------------------------------------------------------------------------------------------------------------------

 # Часть последовательности 1 2 2 3 3 3 4 4 4 4 5 5 5 5 5 ... (число повторяется столько раз, чему равно)
 # Например, если n = 7, то программа должна вывести 1 2 2 3 3 3 4.

 from itertools import chain
 number = 7

 res = list(chain.from_iterable([[i]*i for i in range(1, number+1)]))
 print(*res[:number])                                                  # -> 1 2 2 3 3 3 4


 # Тоже самое
 from itertools import islice, count
 print(*islice((n for n in count() for _ in range(1, n+1)), number))   # -> 1 2 2 3 3 3 4
 -----------------------------------------------------------------------------------------------------------------------

 # Выведите его дробную часть.
 a = 17.9

 print(a - int(a))  # -> 0.8999999999999986
 print(a % 1)       # -> 0.8999999999999986
 -----------------------------------------------------------------------------------------------------------------------

 # Дано 10 целых чисел. Вычислите их сумму.     Вывод сразу всех чисел из Консоли
 print(sum(map(int, __import__('sys').stdin)))
 print(sum(map(int, open(0))))
 print(sum(int(input()) for _ in range(10)))
 print(sum(map(int, __import__('sys').stdin.readlines())))
 -----------------------------------------------------------------------------------------------------------------------

 # Если бы мы вводили такие цифры подряд:
 # 5
 # 0
 # 700
 # 0
 # 200
 # 2

 #  Вывод был бы таким:
 res = [i for i in __import__('sys').stdin]
 print(res)                                  # -> ['5\n', '0\n', '700\n', '0\n', '200\n', '2']
 -----------------------------------------------------------------------------------------------------------------------

 # Задача «Максимальное число идущих подряд равных элементов»
 lst = [1, 7, 7, 9, 1]                        # Или пока не введут 0            # Или пока не введут 0
                                                                                max_n, count = 1, 1
 count, max_count = 1, 1                      prev = rep = mc = c = 0           prev_num = int(input())
 for i in range(1, len(lst)):                 while (e := int(input())):        while (num := int(input())) != 0:
     if lst[i] == lst[i - 1]:                     if e == prev:                     if num == prev_num:
         count += 1                                   c += 1                            count += 1
         if max_count < count:                    else:                                 max_n = max(max_n, count)
             max_count = count                        mc = max(c, mc)               else:
     else:                                            prev, c = e, 1                    count = 1
         count = 1                            print(max(c, mc))                     prev_num = num
 print(max_count)  # -> 2                                                       print(max_n)

 -----------------------------------------------------------------------------------------------------------------------

 # Задача «Стандартное отклонение»
 lst = [1, 7, 9]

 from statistics import stdev
 print(stdev(lst, sum(lst) / len(lst)))  # -> 4.163331998932265
 -----------------------------------------------------------------------------------------------------------------------

 # Удалите из этой строки первое и последнее вхождение буквы h,а также все символы, находящиеся между ними.
 s = 'In the hole in the ground there lived a hobbit'

 print(__import__('re').sub(r'h.*h', '', s))  # -> In tobbit
 -----------------------------------------------------------------------------------------------------------------------

 # Дана строка. Замените в этой строке все появления буквы h на букву H, кроме первого и последнего вхождения.
 s = 'In the hole in the ground there lived a hobbit'

 n = s.count("h")
 s1 = s.replace("h", "H", n-1)

 print(s1.replace("H", "h", 1))  # -> In the Hole in tHe ground tHere lived a hobbit
 -----------------------------------------------------------------------------------------------------------------------

 # Задача «Пингвины»

 # Первый вариант                           # Второй вариант                            # Мой вариант
 n = 3                                      n = 3                                       n = 3
 penguin = ['''   _~_                       '''\                                        a = r'   _~_    '
   (o o)                                       _~_                                      b = r'  (o o)   '
  /  V  \\                                    (o o)                                     c = r' /  V  \  '
 /(  _  )\\                                  /  V  \                                    d = r'/(  _  )\ '
   ^^ ^^   '''.split("\n")]                 /(  _  )\\                                  e = r'  ^^ ^^   '
                                              ^^ ^^  '''                                res = [a, b, c, d, e]
 penguins = zip(*penguin * n)                                                           [print(i*n) for i in res]
 print("\n".join(map("".join, penguins)))   n = int(input())
                                            for row in __doc__.split('\n'):
   _~_       _~_       _~_                      print(' '.join([row] * n), end=' \n')
  (o o)     (o o)     (o o)
 /  V  \   /  V  \   /  V  \
/(  _  )\ /(  _  )\ /(  _  )\
  ^^ ^^     ^^ ^^     ^^ ^^
 -----------------------------------------------------------------------------------------------------------------------

 # Задача «Больше предыдущего»  Дан список чисел. Выведите все элементы списка, которые больше предыдущего элемента.
 res = [1, 5, 2, 4, 3]

 print(*[res[i] for i in range(1, len(res)) if res[i] > res[i-1]])  # -> 5 4
 -----------------------------------------------------------------------------------------------------------------------

 # Задача «Больше своих соседей»
 res = [1, 2, 3, 4, 5]

 print(sum(res[i - 1] < res[i] > res[i + 1] for i in range(1, len(res) - 1)))   # -> 0
 -----------------------------------------------------------------------------------------------------------------------

 # Простое число — это число, которое делится только на 1 и на себя.
 # Проверка числа на простоту в Python

 # SymPy — это библиотека Python для выполнения символьных вычислений. Это система компьютерной алгебры
 import sympy

 print(sympy.isprime(5))  # -> True
 print(sympy.isprime(4))  # -> False


 # Найдите все простые числа в диапазоне от 2 до n включительно.
 n = 6

 print(*[i for i in range(2, n + 1) if __import__('sympy').isprime(i)])  # -> 2 3 5
 -----------------------------------------------------------------------------------------------------------------------

 # В нижний регистр первый символ, а все остальные — в верхний регистр.
 s = 'Hello World'

 print(*[f"{i[0].lower()}{i[1:].upper()}" for i in s.split()])  # -> hELLO wORLD
 print(s.title().swapcase())                                    # -> hELLO wORLD
 -----------------------------------------------------------------------------------------------------------------------

 # Интересный Пример
 print(f"Python {3 + .2}")  # -> Python 3.2
 -----------------------------------------------------------------------------------------------------------------------

 # Интересный Пример
 x1 = {"jack": 30, "john": 35}
 x2 = {"jack": 355, "john": 35}

 print(x1 > x2)  # -> TypeError: '>' not supported between instances of 'dict' and 'dict'
 -----------------------------------------------------------------------------------------------------------------------

 # ВАЖНО !!! eval vs ast.literal_eval()                                             <-----                  <-----

 # Функции eval() и ast.literal_eval() интерпретируют строки как код Python.
 # ast.literal_eval() - обрабатывает только строки, представляющие литералы, более безопасный в применении.
 # eval()             - функция способна выполнить любые команды. Более Производительный

 import ast
 s = '[4, 2, 5, 9, 1]'

 print(ast.literal_eval(s))           # -> [4, 2, 5, 9, 1]  # Создание безопасного аналога eval()
 print(eval(s))                       # -> [4, 2, 5, 9, 1]  # eval() Более Производительный

 print(ast.literal_eval('{"a":10}'))  # -> {'a': 10}  # Из строки сделали словарь
 print(eval('{"a":10}'))              # -> {'a': 10}  # Из строки сделали словарь


 # Наглядный пример                                                                 <-----                  <-----
 s = "deque([1, 2, 3])"

 print(eval(s))              # -> deque([1, 2, 3])
 print(ast.literal_eval(s))  # -> ValueError: malformed node or string on line 1: <ast.Call object at 0x00000252CC0DA6E0>

 -----------------------------------------------------------------------------------------------------------------------

 # Как обрезать вручную
 s = '1234567'
 i = 0
 while i < len(s):
     print(s[i:i + 3])
     i = i + 3

 # 123
 # 456
 # 7
 -----------------------------------------------------------------------------------------------------------------------

 # Roman number to decimal  # В римской системе счисления   print(__import__('roman').fromRoman('MCMLXXXIV')) # -> 1984
 import roman
 res = roman.fromRoman("MCMLXXXIV")
 res1 = roman.fromRoman("IX")

 print(res)   # -> 1984
 print(res1)  # -> 9
 -----------------------------------------------------------------------------------------------------------------------
 # Наоборот сделать                                         print(__import__('roman').toRoman(1984))     # -> MCMLXXXIV

 import roman
 res = roman.toRoman(1984)
 res1 = roman.toRoman(9)

 print(res)   # -> MCMLXXXIV
 print(res1)  # -> IX
 -----------------------------------------------------------------------------------------------------------------------

 # Интересные примеры  exec   eval    Разница между   exec  vs   eval                    <-----               <-----

 exec("print(f'{a+b}')", globals(), {'a': 8, 'b': 11})  # -> 19

 exec('''print(f'10*2')''')  # -> 10*2
 eval('''print(f'10*2')''')  # -> 10*2

 exec("print(a)", globals(), {'a': 42})  # -> 42
 eval("print(a)", globals(), {'a': 42})  # -> 42

 exec(f"print([i for i in range(3) if i > 0])")  # -> [0, 1, 2]
 eval(f"print([i for i in range(3) if i > 0])")  # -> [0, 1, 2]

 a = exec(f"print(eval('+'.join('111')))")  # -> 3
 print(a)  # -> None


 a = 5
 # Возвращает Результат
 print(eval('37 + a'))  # -> 42
 # Возвращает None
 print(exec('37 + a'))  # -> None


 # exec Может создать переменную
 print(exec('a = 47'))  # -> 47
 # eval НЕ Может создать переменную
 print(eval('a = 47'))  # -> SyntaxError: invalid syntax


 # Выполняет блок кода exec()      # Ошибка eval()
 program = '''                     program = '''
 for i in range(2):                for i in range(2):
     print("Python, sep=' '")          print("Python, sep=' '")
 '''                               '''

 exec(program)                     eval(program)  # -> SyntaxError: invalid syntax

 # Python, sep=' '
 # Python, sep=' '

 Функция eval() делает то же самое для одного выражения и возвращает значение выражения:
 a = 2
 print(eval('42 * a'))  # -> 84


 # eval vs exec

 exec('print(5)')            # -> 5
 exec('print(5)\nprint(6)')
 # -> 5
 # -> 6
 exec('if True: print(6)')   # -> 6
 exec('5')                   # -> Ничего не возвращает


 # eval vs exec

 x = eval('5')
 print(x)                    # -> 5
 x = eval('%d + 6' % x)
 print(x)                    # -> 11
 x = eval('abs(%d)' % -100)
 print(x)                    # -> 100


 # eval() НЕ Будет работать!
 x = eval('x = 5')          # INVALID; assignment is not an expression.
 x = eval('if 1: x = 4')    # INVALID; if is a statement, not an expression.

 # exec() Будет работать!
 exec('x = 5')
 print(x)                 # -> 5
 x = exec('if 1: x = 4')
 print(x)                 # -> None
 -----------------------------------------------------------------------------------------------------------------------

 # Число  удваивается
 print([10 * 2**i for i in range(12)])  # -> [10, 20, 40, 80, 160, 320, 640, 1280, 2560, 5120, 10240, 20480]
 print([10 << i for i in range(12)])    # -> [10, 20, 40, 80, 160, 320, 640, 1280, 2560, 5120, 10240, 20480]
 -----------------------------------------------------------------------------------------------------------------------

 # Обновить словарь  Через defaultdict
 from collections import defaultdict

 a_dict = defaultdict(dict)

 res = ['Ivanov paper 10', 'Petrov pens 5', 'Ivanov marker 3', 'Ivanov paper 7', 'Petrov envelope 20', 'Ivanov envelope 5']

 for i in res:
     a, b, c = i.split()
     a_dict[a].setdefault(b, 0)
     a_dict[a][b] += int(c)

 print(a_dict)
 # defaultdict(<class 'dict'>, {'Ivanov': {'paper': 17, 'marker': 3, 'envelope': 5}, 'Petrov': {'pens': 5, 'envelope': 20}})


 # Через обычный словарь
 res = ['Ivanov paper 10', 'Petrov pens 5', 'Ivanov marker 3', 'Ivanov paper 7', 'Petrov envelope 20', 'Ivanov envelope 5']

 a_dict = {}
 for line in res:
     a, b, c = line.strip().split(' ')
     a_dict.setdefault(a, {}).setdefault(b, 0)
     a_dict[a][b] += int(c)

 print(a_dict)  # -> {'Ivanov': {'paper': 17, 'marker': 3, 'envelope': 5}, 'Petrov': {'pens': 5, 'envelope': 20}}
 -----------------------------------------------------------------------------------------------------------------------

 # Напишите код, который использует метод .get() вместо операторов if/else
 books = {"Life of Pi": "Adventure Fiction", "Good Omens": "Comedy"}
 s = 'Good Omens'

 print(books.get(s, 'Книга не найдена'))                       # -> Comedy
 print(books[s] if s in books.keys() else 'Книга не найдена')  # -> Comedy

 books = {"Life of Pi": "Adventure Fiction"}
 print(books.get(s, 'Книга не найдена'))                       # -> Книга не найдена
 print(books[s] if s in books.keys() else 'Книга не найдена')  # -> Книга не найдена
 -----------------------------------------------------------------------------------------------------------------------

 # Получить значение через get()/if-else                Важно Посмотри вариант с -1
 contacts = {"David": ["123-321-88", "david@test.com"]}

 s = 'David'
 print(contacts.get(s)[1] if s in contacts.keys() else 'Не найден')  # -> david@test.com
 print(contacts.get(s, ['Не найден'])[-1])                           # -> david@test.com    # Интересный Вариант

 s = 'Ivan'
 print(contacts.get(s)[1] if s in contacts.keys() else 'Не найден')  # -> Не найден
 print(contacts.get(s, ['Не найден'])[-1])                           # -> Не найден         # Интересный Вариант
 -----------------------------------------------------------------------------------------------------------------------

 # Какого цвета клетка?
 d = {'a': '2468', 'b': '1357', 'c': '2468', 'd': '1357', 'e': '2468', 'f': '1357', 'g': '2468', 'h': '1357'}
 a, b = 'b2'
 print('Белая' if b in d.get(a) else 'Чёрная')                     # -> Чёрная

 # Тоже самое
 a = 'b2'
 print('Чёрная' if (ord(a[0]) - int(a[1])) % 2 == 0 else 'Белая')  # -> Чёрная
 -----------------------------------------------------------------------------------------------------------------------

 # Сначало пользователь вводит число, а потом процент, который нужно от него посчитать.
 #  Как можно Сразу Вызывать lambda с аргументами                <-----                              <-----
 a, b = 128, 42
 print((lambda x, y: x / 100 * y)(a, b))  # -> 53.76
 print((lambda x, y: (x*y) / 100)(a, b))  # -> 53.76

 # Или посчитать % от числа
 print(f"{a / b:.2%}")                    # -> 304.76%
 -----------------------------------------------------------------------------------------------------------------------

 # lambda выводит минимальное число

 print((lambda *args: min(*args))([8, 13, 4, 42, 120, 7]))  # -> 4
 -----------------------------------------------------------------------------------------------------------------------

 # Нужно, чтобы номера телефонов, которые начинаются с "00", заменялись на "+"
 s = '0014860098'

 print(s.replace('00', '+', 1) if s.startswith('00') else s)     # -> +14860098
 print(__import__('re').sub(r'^00', sub_fun, s))                 # -> +14860098
 -----------------------------------------------------------------------------------------------------------------------

 # модуль предлагает универсальный парсер строк даты/времени   <----     <----     <----   Крутой модуль dateutil
 from dateutil import parser

 # Поменять местами или заменить Текст на число
 s = '7/26/2019'
 res = parser.parse(s, dayfirst=True)
 print(f"{res.day}/{res.month}/{res.year}")  # -> 26/7/2019

 s = 'January 1, 2021'
 res = parser.parse(s, dayfirst=True)
 print(f"{res.day}/{res.month}/{res.year}")  # -> 1/1/2021
 -----------------------------------------------------------------------------------------------------------------------

 # Аналог chunked из more_itertools Но строку не разбивает

 # Первый Вариант
 chunker = lambda data, chunk: (data[x:x + chunk] for x in range(0, len(data), chunk))

 # Второй Вариант
 def chunker(sequence, size):
     for i in range(0, len(sequence), size):
         yield sequence[i:i + size]

 print(list(chunker([1, 2, 3, 4, 5], 2)))  # -> [[1, 2], [3, 4], [5]]
 print(list(chunker(['abcde'], 2)))        # -> [['abcde']]
 -----------------------------------------------------------------------------------------------------------------------

 # от 6 до 11 включительно, программа выводит сообщение "Доброе утро!"
 # от 12 до 17 включительно, программа выводит сообщение "Добрый день!"
 # от 18 до 23 включительно, программа выводит сообщение "Добрый вечер!"
 # от 0 до 5 включительно, программа выводит сообщение "Доброй ночи!"

 print(["Доброй ночи!", "Доброе утро!", "Добрый день!", "Добрый вечер!"][int(input())//6])
 -----------------------------------------------------------------------------------------------------------------------

 # Требуется вывести одно число - количество различных типов данных в строке.
 a = '1, 2.5, "hello", [1, 2, 3], "world", 5'

 # Моё решение
 res = [type(i) for i in re.findall(r'(\[.*])|(\(.*\))', a)]
 res1 = re.sub(r'(\[.*])|(\(.*\))', '', a)
 res2 = [type(eval(i)) for i in res1.split(', ') if i]+res
 print(len(set(res2)))   # -> 4


 # Лучше варианты
 a = '1, 2.5, "hello", [1, 2, 3], "world", 5'

 # Посмотри что будет в eval()
 print(eval(a))  # -> (1, 2.5, 'hello', [1, 2, 3], 'world', 5)


 # Хороший вариант
 try:
     s = set(map(type, eval(a)))
     print(len(s))
 except:
     print(1)
 # -> 4

 # В качестве безопасной альтернативы для eval можно использовать ast.literal_eval:

 # from ast import literal_eval as eval
 # однако, literal_eval парсить только очень ограниченное подмножество элементов языка Python.

 print(len(set(map(type, eval(a.join('[]'))))))  # -> 4

 # Простой вариант
 a = eval('1, 2.5, "hello", [1, 2, 3], "world", 5')
 print(len(set(type(i) for i in a)) if type(a) == tuple else 1)  # -> 4
 print(len({type(i) for i in a}) if type(a) == tuple else 1)     # -> 4
 -----------------------------------------------------------------------------------------------------------------------

 # Дублирование фрагмента
 # Дана строка, в которой буква h встречается как минимум два раза. Повторите последовательность символов,
 # заключенную между первым и последнием появлением буквы h два раза, сами буквы h повторять не надо.

 s ='qwertyhasdfghzxcvb'.lower()
 res = s[:s.rfind('h')]+s[s.find('h')+1:]
 print(s[:s.rfind('h')]+s[s.find('h')+1:])  # -> qwertyhasdfgasdfghzxcvb

 assert res == 'qwertyhasdfgasdfghzxcvb'
 -----------------------------------------------------------------------------------------------------------------------

 # Суммирует все кубические значения от 1 до n (включительно) и возвращает эту сумму.

 # Можно перед range НЕ ставить list               # Тоже самое
 def sum_cubes(n):                                 def sum_cubes(n):
     return sum(map(lambda x: x**3, range(n+1)))       return sum(i**3 for i in range(n+1))

 print(sum_cubes(10), 3025)  # -> 3025 3025


 # Интересный вариант!!!
 def sum_cubes(n):
     res = iter(list(range(n+1)))
     return sum([next(res)**3 for _ in range(n+1)])

 print(sum_cubes(10), 3025)  # -> 3025 3025
 -----------------------------------------------------------------------------------------------------------------------

 # "Even" для четных чисел или "Odd" для нечетных чисел.
 # Функция также должна возвращать "Even" или "Odd" при доступе к значению по целочисленному индексу.

 # Тоже самое                                        # Тоже самое
 class EvenOrOdd:                                    class EvenOrOdd:
     def __call__(self, num):                            def __call__(self, number):
         return "Even" if num % 2 == 0 else "Odd"            return ['Even', 'Odd'][number % 2]

     def __getitem__(self, num):                         def __getitem__(self, number):
         return self(num)                                    return self.__call__(number)

 even_or_odd = EvenOrOdd()

 print(even_or_odd(10))  # -> Even
 print(even_or_odd(9))   # -> Odd

 # Можно вызывать через []
 print(even_or_odd[10])  # -> Even
 print(even_or_odd[9])   # -> Odd

 # Тоже самое
 class Obj:
     __call__ = __getitem__ = lambda self, n: "Even" if not n % 2 else "Odd"

 even_or_odd = Obj()

 # Тоже самое
 even_or_odd = type('', (), {'__call__': (f:=lambda _, n: 'EOvdedn'[n%2::2]), '__getitem__': f})()
 -----------------------------------------------------------------------------------------------------------------------

 # Найти индекс в списке две заглавные буквы О, с как минимум одним тире между ними!

 find_glasses = lambda x: next(i for i, v in enumerate(x) if re.search(r'O-+O', v))

 print(find_glasses(["O-O"]), 0)           # -> 0 0
 print(find_glasses(['o-o', "O---O"]), 1)  # -> 1 1
 -----------------------------------------------------------------------------------------------------------------------

 # JavaScript предоставляет встроенный метод parseInt. Его можно использовать следующим образом:
 # parseInt("10")              возвращается 10
 # parseInt("10 apples") также возвращается 10

 # Мы хотели бы, чтобы он возвращался "NaN"(в виде строки) во втором случае, поскольку входная строка не является допустимым числом.

 def my_parse_int(strn):
     return int(s.group()) if (s:=re.fullmatch(r'\s*\d+\s*', strn)) else 'NaN'

 print(my_parse_int("1"), 1)              # -> 1 1
 print(my_parse_int("  1 "), 1)           # -> 1 1
 print(my_parse_int("08"), 8)             # -> 8 8
 print(my_parse_int("5 friends"), "NaN")  # -> NaN NaN
 print(my_parse_int("16.5"), "NaN")       # -> NaN NaN


 # Тоже самое
 my_parse_int = lambda s: int(s) if s.strip().isdigit() else "NaN"


 # Хитрый вариант
 def my_parse_int(s):
     try:
         return int(s)
     except ValueError:
         return 'NaN'

 -----------------------------------------------------------------------------------------------------------------------

 # Реализуйте функцию createTemplate, которая принимает строку с тегами, упакованными {{brackets}}в качестве входных
 # данных, и возвращает замыкание, которое может заполнять строку данными (плоский объект, где ключами являются имена тегов).

 # Пример что должно быть на выходе:

 # template = create_template("{{name}} likes {{animalType}}")
 # template(name="John", animalType="dogs")  # ->  John likes dogs

 # Первый вариант
 from jinja2 import Template

 def create_template(template):
     return lambda **vals: Template(template).render(vals)


 # Второй вариант
 def create_template(template):
     return lambda **kwargs: re.sub(r'{{(.*?)}}', lambda m: kwargs.get(m.group(1), ''), template)


 # Третий вариант
 def create_template(template):
    def closure(**kwargs):
        return re.sub(r"{{(\w+)}}", lambda x: kwargs.get(x.group(1)) ,template)

    return closure


 template = create_template("{{firstName}} {{lastName}} likes {{interests}}")
 print(template(firstName="John", lastName="Smith", interests="sport"), "John Smith likes sport")
 print(template(firstName="Albert", lastName="Einstein", occuptation="physicist"), "Albert Einstein likes ")
 -----------------------------------------------------------------------------------------------------------------------

 Валидация пароля  длина пароля От 8 до 20 символов  1 заглавная, 1 строчная, 1 цифра, специальные символы из!@#$%^&*?

 # Первый вариант
 def check_password(s):
     if re.search('^(?=.*?[a-z])(?=.*?[A-Z])(?=.*?\d)(?=.*?[!@#$%^&*?])[a-zA-Z\d!@#$%^&*?]{8,20}$', s):
         return 'valid'
     else:
         return 'not valid'


 # Второй вариант
 PATTERN = re.compile(
 '^'                   # begin string
 '(?=.*?[A-Z])'        # at least one uppercase letter
 '(?=.*?[a-z])'        # at least one lowercase letter
 '(?=.*?\d)'           # at least one digit
 '(?=.*?[!@#$%^&*?])'  # at least one special character
 '[A-Za-z\d!@#$%^&*?]' # only the given characters
 '{8,20}'              # between 8 and 20 characters long
 '$'                   # end string
 )

 def check_password(s):
     return "valid" if PATTERN.match(s) else "not valid"

 print(check_password("P1@p"), "not valid")  # -> not valid not valid
 print(check_password("P1@pP1@p"), "valid")  # -> valid valid
 -----------------------------------------------------------------------------------------------------------------------

 # Ваша задача — удалить все последовательные дубликаты
 def remove_consecutive_duplicates(s):
     res = []
     for i in s.split():
         if i not in res:
             res.append(i)
         if i != res[-1]:
             res.append(i)
     return ' '.join(res)


 # Тоже самое
 from itertools import groupby

 def remove_consecutive_duplicates(s):
     return ' '.join(k for k,_ in groupby(s.split()))

 # Тоже самое
 def remove_consecutive_duplicates(s):
     return re.sub(r'\b(\w+)(?:\s\1)+\b', r'\1', s)


 print(remove_consecutive_duplicates('alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta'))
 # alpha beta gamma delta alpha beta gamma delta

 print(remove_consecutive_duplicates('1 2 2 2 2 3 3 3 3 3 3 3 3 3'))  # -> 1 2 3
 -----------------------------------------------------------------------------------------------------------------------

 # Создайте регулярное выражение, которое соответствует строке со строчными символами в алфавитном порядке,
 # включая любое количество пробелов. Между группами одинаковых букв НЕ может быть пробелов. Начальные и конечные пробелы
 # также разрешены. Должна соответствовать пустая строка.

 REGEX = r'^ *a* *b* *c* *d* *e* *f* *g* *h* *i* *j* *k* *l* *m* *n* *o* *p* *q* *r* *s* *t* *u* *v* *w* *x* *y* *z* *\Z'
 REGEX = fr"\A *{'* *'.join('abcdefghijklmnopqrstuvwxyz')}* *\Z"
 -----------------------------------------------------------------------------------------------------------------------

 # Вам будет дан массив строк. Слова в массиве должны сцепляться вместе, где одна или несколько букв в конце одного слова
 # будут иметь те же буквы (в том же порядке), что и следующее слово в массиве.

 # Моё решение
 import re
 from itertools import pairwise

 def word_mesh(words):
     res = []
     for i in pairwise(words):
         for j in range(len(i[0])):
             if re.match(rf'{i[0][j:]}', i[1]):
                 res.append(i[0][j:])
                 break
     return ''.join(res) if len(res)+1 == len(words) else "failed to mesh"


 # Тоже самое
 def word_mesh(arr):
     common = re.findall(r'(.+) (?=\1)',' '.join(arr))
     return ''.join(common) if len(common) + 1 == len(arr) else 'failed to mesh'

 print(word_mesh(["beacon", "condominium", "umbilical", "california"]), "conumcal")               # -> conumcal conumcal
 print(word_mesh(["allow", "lowering", "ringmaster", "terror"]), "lowringter")                    # -> lowringter lowringter
 print(word_mesh(['muchbetter', 'terriblestorm', 'stormwarning', 'greatlymissed']), 'terstormg')  # -> terstormg terstormg
 -----------------------------------------------------------------------------------------------------------------------

 # Верните общий балл в виде целого числа.
 def eval_parentheses(s):
     return eval(s.replace(')(', ')+(').replace('()', '1').replace('(', '2*('))


 # Тоже самое
 from re import compile

 REGEX = compile(r"\(\)|[\(\)]").finditer

 def eval_parentheses(s):
     level = result = 0
     for x in REGEX(s):
         match x.group(0):
             case "(": level += 1
             case ")": level -= 1
             case _:  result += 1 << level
     return result

 print(eval_parentheses("()"), 1)         # -> 1 1
 print(eval_parentheses("(())"), 2)       # -> 2 2
 print(eval_parentheses("()()"), 2)       # -> 2 2
 print(eval_parentheses("((())())"), 6)   # -> 6 6
 print(eval_parentheses("(()(()))"), 6)   # -> 6 6
 print(eval_parentheses("()(())"), 3)     # -> 3 3
 print(eval_parentheses("()((()))"), 5)   # -> 5 5
 -----------------------------------------------------------------------------------------------------------------------

 # Если строка может рассматриваться как повторение более простого/короткого подшаблона или нет.

 def has_subpattern(strng):
     return bool(re.fullmatch(r'(.+)\1+', strng))                     <-----        \1+

 print(has_subpattern("a"), False)          # -> False False
 print(has_subpattern("aaaa"), True)        # -> True True
 print(has_subpattern("abcd"), False)       # -> False False
 print(has_subpattern("abababab"), True)    # -> True True
 print(has_subpattern("ababababa"), False)  # -> False False
 -----------------------------------------------------------------------------------------------------------------------

 # Есть два кортежа, получить третий как объединение уникальных элементов первых двух кортежей, НЕ встречающихся
 # одновременно в обоих кортежах  >>> (1, 2, 3, 4, 5)

 a = (1, 2, 3)
 b = (3, 4, 5)

 print(tuple({*a, *b}))         # ->  (1, 2, 3, 4, 5)
 print(tuple(set(a) + set(b)))  # ->  TypeError: unsupported operand type(s) for +: 'set' and 'set'
 print(set(tuple(a + b)))       # ->  {1, 2, 3, 4, 5}
 print((a + b).unique())        # ->  AttributeError: 'tuple' object has no attribute 'unique'
 -----------------------------------------------------------------------------------------------------------------------

 # Какие обозначения не стоит использовать при именовании с точки зрения рекомендаций PEP 8?

 [X] 1. l
 [X] 2. O
 [ ] 3. i
 [X] 4. L
 [ ] 5. a
 [X] 6. I
 [ ] 7. bad_name

 # Обьяснение
 1. `l` (маленькая буква "l") - может быть спутана с цифрой "1".
 2. `O` (большая буква "O")   - может быть спутана с цифрой "0".
 3. `I` (большая буква "I")   - может быть спутана с цифрой "1".
 4. `L` (большая буква "L")   - может быть спутана с цифрой "1".
 -----------------------------------------------------------------------------------------------------------------------

 # По рекомендации PEP 8 каким должен быть единичный отступ?

 4 пробела
 -----------------------------------------------------------------------------------------------------------------------

 # Для чего используется пустой слайс [:] списка?

 # Для получения всех элементов коллекции
 print([1, 2, 3][:])  # -> [1, 2, 3]
 -----------------------------------------------------------------------------------------------------------------------

 # Отметьте верные способы создать список (list) с элементами [1, 2, 3, 4]

 print([i + 1 for i in range(4)])       # ->  [1, 2, 3, 4]
 print([i for i in range(4)],)          # ->  [0, 1, 2, 3]
 print([i for i in range(5)][1:])       # ->  [1, 2, 3, 4]
 print(list(i + 1 for i in range(4)))   # ->  [1, 2, 3, 4]
 -----------------------------------------------------------------------------------------------------------------------

 Необходимо обменять значение двух переменных, не применяя других переменных. Отметьте верный способ.

 a = 1
 b = 'q'

 print(swap(a, b))  # -> NameError: name 'swap' is not defined
 print(a.swap(b))   # -> AttributeError: 'int' object has no attribute 'swap'
 {a, b} = {b, a}    # -> SyntaxError: cannot assign to set display here. Maybe you meant '==' instead of '='?

 a, b = b, a
 print(a, b)  # -> q 1
 -----------------------------------------------------------------------------------------------------------------------

 # Необходимо обменять значение двух переменных, не применяя других переменных. Отметьте верный способ.
 # >>> {'John': 1, 'Peter': 2}

 a = ('John', 'Peter')
 b = (1, 2)

 print({key: value for key, value in zip(a, b)})  # -> {'John': 1, 'Peter': 2}
 print({key: value for key, value in (a, b)})     # -> {'John': 'Peter', 1: 2}
 print(dict(keys=a, values=b))                    # -> {'keys': ('John', 'Peter'), 'values': (1, 2)}
 print({key: b[i] for i, key in enumerate(a)})    # -> {'John': 1, 'Peter': 2}

 print(dict(zip(a, b)))                           # -> {'John': 1, 'Peter': 2}
 -----------------------------------------------------------------------------------------------------------------------

 # Интересный пример
 a = [[]] * 3
 a[1].append(1)
 print(a)        # -> [[1], [1], [1]]
 -----------------------------------------------------------------------------------------------------------------------

 # Создать функцию которая убирает дубликаты           Задача с Live Coding Собеседования

 # Первый вариант
 def clean_duplicates(lst: list[dict]) -> list[dict]:
     res = []
     for i in lst:
         if i not in res:
             res.append(i)
     return res

 print(clean_duplicates([{1: 2}, {1: 2}, {1: 2}]))  # -> [{1: 2}]

 # Второй вариант
 def clean_duplicates(lst: list[dict]) -> list[dict]:
     res = []
     [res.append(i) for i in lst if i not in res]
     return res

 print(clean_duplicates([{1: 2}, {1: 2}, {1: 2}]))  # -> [{1: 2}]

 # Третий вариант
 def clean_duplicates(lst: list[dict]) -> list[dict]:
     return list([eval(i) for i in set(tuple([str(i) for i in lst]))])

 print(clean_duplicates([{1: 2}, {1: 2}, {1: 2}]))  # -> [{1: 2}]
 -----------------------------------------------------------------------------------------------------------------------

 Важно !!! \1+
 # Если в строке встречаются дубликаты более двух буквенных символов, возвращать строку со всеми лишними символами в скобках.


 # Первый Вариант
 def string_parse(s):
     if isinstance(s, str):
         return re.sub(r"(.)\1(\1+)", r"\1\1[\2]", s)
     return "Please enter a valid string"

 print(string_parse("aaaabbcdefffffffg"), "aa[aa]bbcdeff[fffff]g")  # -> aa[aa]bbcdeff[fffff]g aa[aa]bbcdeff[fffff]g

 assert string_parse("aaaabbcdefffffffg") == "aa[aa]bbcdeff[fffff]g"


 # Второй Вариант
 def string_parse(string):
     return re.sub(r'(.)\1(\1+)', r'\1\1[\2]', string) if isinstance(string, str) else 'Please enter a valid string'



 # Моё решение!!!   Важно (\w)\1+
 def string_parse(strng):
     c = strng
     if type(strng) != str:
         return "Please enter a valid string"
     if not strng:
         return strng
     res = []
     while strng:
         if res_2 := re.match(r'(\w)\1+', strng):               #  (\w)\1+   <-----   <-----
             res.append(res_2.group())
             strng = strng.replace(res_2.group(), '', 1)
             continue
         if res_3 := re.match(r'\w', strng):
             res.append(res_3.group())
             strng = strng.replace(res_3.group(), '', 1)
     res_res = ''.join([f'{i[:2]}[{i[2:]}]' if len(i) > 2 else i for i in res])
     return c if all([len(i) <= 2 for i in res]) else res_res
 -----------------------------------------------------------------------------------------------------------------------

 # is_audio , соответствует 1 или + заглавным/строчным буквам (возможны комбинации), с расширением .mp3, .flac, .alac или .aac.
 # is_image , соответствует 1 или + заглавным/строчным буквам (возможны комбинации), с расширением .jpg, .jpeg, .png, .bmp или .gif.

 # Первый вариант
 def is_audio(filename):
     name, ext = filename.split('.')
     return name.isalpha() and ext in {'mp3', 'flac', 'alac', 'aac'}

 def is_image(filename):
     name, ext = filename.split('.')
     return name.isalpha() and ext in {'jpg', 'jpeg', 'png', 'bmp', 'gif'}


 # Второй вариант
 def is_audio(file_name):
     return bool(re.match(r'^[A-Za-z]+\.(mp3|flac|alac|aac)$', file_name))

 def is_image(file_name):
     return bool(re.search(r'^[A-Za-z]+\.(jpg|jpeg|png|bmp|gif)$', file_name))


 print(is_audio("Nothing Else Matters.mp3"), False)    # -> False False
 print(is_audio("NothingElseMatters.mp3"), True)       # -> True True
 -----------------------------------------------------------------------------------------------------------------------

 # Если с первой строчки написать/ Вначале файла/модуля

 '''Hello World!'''
 print(__doc__)  # -> Hello World!
 -----------------------------------------------------------------------------------------------------------------------

 # Изменится ли значение a?
 a = 10
 B = [a for a in range(20, 30)]
 print(a)  # -> 10
 -----------------------------------------------------------------------------------------------------------------------

 # Возвращает сумму элементов переданного списка.  Учитывать нужно и отрицательные числа

 def sum_eval(value: int) -> int:
     return eval('+'.join(re.sub(r'[^-\d+]', '', str(value))))

 print(sum_eval([1, 2, 3]))  # -> 6
 -----------------------------------------------------------------------------------------------------------------------

 # Создать полную копию встроенного объекта range. Он может быть вызван от одного, двух или трех аргументов.
 # P.S. И да, функцией range пользоваться нельзя, можете конечно попробовать, но у вас ничего не получится

 def my_range_gen(*args):
     try:
         return vars(__builtins__)['range'](*args)
     except:
         return iter('')

 for i in my_range_gen(5):
     print(i, end=' ')     # -> 0 1 2 3 4
 -----------------------------------------------------------------------------------------------------------------------

 Интересные Возможности!!!

 # Можно использовать все строенные функции
 print(vars(__builtins__)['max'](1, 2))                   # -> 2
 print(vars(__builtins__)['min'](['a', 'ab'], key=len))   # -> a
 print(vars(__builtins__)['sum']([1, 2]))                 # -> 3

 # Можно использовать все строенные функции через точку .
 print(__builtins__.min(1, 2))                            # -> 1
 print(__builtins__.max(['a', 'ab'], key=len))            # -> ab
 print(__builtins__.sorted([1, 2, 1]))                    # -> [1, 1, 2]

 # Посмотреть все возможные атрибуты
 print(__builtins__.globals())   # -> {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__':...
 print(__builtins__.locals())    # -> {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__':...
 print(__builtins__.vars())      # -> {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__':...
 -----------------------------------------------------------------------------------------------------------------------

 # Напишите функцию, которая будет брать ключ X и помещать его в середину Y, повторяя N раз.
 # Внутри f-строки можно использовать {} Внимательно посмотри пример
 def middle_me(N, X, Y):
     if N % 2 == 0:
         return f'{Y}{X:{Y}^{N}}'
     return X

 print(middle_me(18, 'z', '#'), '#########z#########')  # ->  #########z######### #########z#########
 print(middle_me(19, 'z', '#'), 'z')                    # ->  z z
 -----------------------------------------------------------------------------------------------------------------------

 # Remove Duplicates from Sorted Array/Удалить дубликаты из отсортированного массива    Можно просто использовать [:]

 # Мой Вариант
 def removeDuplicates(nums: List[int]) -> int:
     while len(nums) != len(set(nums)):
         for i in nums:
             if nums.count(i) > 1:
                 nums.remove(i)
     return len(nums)

 nums = [0,0,1,1,1,2,2,3,3,4]

 print(removeDuplicates(nums))  # 5
 print(nums)                    # [0, 1, 2, 3, 4]


 # Хороший варинт    Можно просто использовать [:]
 def removeDuplicates(nums: list[int]) -> int:
     nums[:] = sorted(set(nums))
     return len(nums)

 nums = [0,0,1,1,1,2,2,3,3,4]

 print(removeDuplicates(nums))  # [0, 1, 2, 3, 4]
 print(nums)                    # [0, 1, 2, 3, 4]
 -----------------------------------------------------------------------------------------------------------------------

 # Проверить совпадают типы или нет.
 def type_validation(variable, _type):
     return type(variable).__name__ == _type

 print(type_validation(42, "int"), True)     # -> True True
 print(type_validation("42", "int"), False)  # -> False False


 def type_validation(variable, _type):
     return _type in str(type(variable))

 print(type_validation(42, "int"), True)     # -> True True
 print(type_validation("42", "int"), False)  # -> False False
 -----------------------------------------------------------------------------------------------------------------------

 # Интересный момент

 print(type(42).__name__)  # -> int
 print(type(42))           # -> <class 'int'>
 -----------------------------------------------------------------------------------------------------------------------

 # Простая функция Фибоначчи с assert внутри   Лучше использовать functools lru_cache  Но с большим число НЕ будет Работать

 cache = {}

 def fib1(n):
     assert n >= 0
     if n not in cache:
         cache[n] = n if n <= 1 else fib1(n - 1) + fib1(n - 2)
     return cache[n]

 print(fib1(8))   # -> 21
 print(fib1(-1))  # -> AssertionError
 -----------------------------------------------------------------------------------------------------------------------

 # Вернуть элемент, следующий сразу за указанным элементом.
 def next_item(xs, item):
     xs = iter(xs)
     try:
         for i in xs:
             if i == item:
                 return next(xs)
     except:
         pass

 print(next_item([1, 2, 3, 4, 5, 6, 7, 8], 5), 6)  # -> 6 6
 print(next_item(['a', 'b', 'c'], 'd'), None)      # -> None None
 print(next_item(['a', 'b', 'c'], 'c'), None)      # -> None None
 print(next_item('testing', 't'), 'e')             # -> e e
 print(next_item(iter(range(1, 30000)), 12), 13)   # -> 13 13
 -----------------------------------------------------------------------------------------------------------------------

 # Логический оператор «исключающее или» (xor)    Разные варианты ответа
 def xor(a, b):
     return a != b

 def xor(a, b):
     return a ^ b

 def xor(a,b):
     return a is not b

 from operator import xor


 print(xor(False, False), False, "False xor False == False")
 print(xor(True, False), True, "True xor False == True")
 print(xor(False, True), True, "False xor True == True")
 print(xor(True, True), False, "True xor True == False")
 -----------------------------------------------------------------------------------------------------------------------

 # Отформатируйте любое предоставленное целое число в строку, расставив «,» (запятые) в нужных местах.    f'{100:,}'
 # Пример 100000 == '100,000'   5678545 == '5,678,545'   -420902 == '-420,902'
 # print(f'{1000000:,}')  # -> 1,000,000

 def number_format(n):
     return f'{n:,}'

 print(number_format(100000), "100,000")      # -> 100,000 100,000
 print(number_format(5678545), "5,678,545")   # -> 5,678,545 5,678,545
 print(number_format(-420902), "-420,902")    # -> -420,902 -420,902
 print(number_format(-3), "-3")               # -> -3 -3
 print(number_format(-1003), "-1,003")        # -> -1,003 -1,003
 -----------------------------------------------------------------------------------------------------------------------

 # Разделить по Нулям(0) и получить сумму   Merge Nodes in Between Zeros

 def mergeNodes(head):
     res = re.sub(r'[,\s\]\[]', '', str(head))
     return [eval('+'.join(i)) for i in re.split(r'0', res) if i]

 # Тоже самое но с map
 def mergeNodes(head):
     res = ''.join([*map(str, head)]).split('0')
     return [sum(map(int, ' '.join(i).split())) for i in res if i]

 head = [0,3,1,0,4,5,2,0]
 print(mergeNodes(head))  # -> [4, 11]
 head = [0,1,0,3,0,2,2,0]
 print(mergeNodes(head))  # -> [1, 3, 4]
 -----------------------------------------------------------------------------------------------------------------------

 # Проверяет, находятся ли гласные (a, e, i, o, u) и согласные в чередующемся порядке.
 def is_alt(s):
     return re.search(r'[aeiou]{2}|[^aeiou]{2}', s)

 print(is_alt("amazon"), True)   # -> None True
 print(is_alt("apple"), False)   # -> <re.Match object; span=(1, 3), match='pp'> False
 print(is_alt("banana"), True)   # -> None True
 print(is_alt("orange"), False)  # -> <re.Match object; span=(3, 5), match='ng'> False
 -----------------------------------------------------------------------------------------------------------------------


 -----------------------------------------------------------------------------------------------------------------------


 -----------------------------------------------------------------------------------------------------------------------


 -----------------------------------------------------------------------------------------------------------------------


 -----------------------------------------------------------------------------------------------------------------------


 -----------------------------------------------------------------------------------------------------------------------


 -----------------------------------------------------------------------------------------------------------------------


 -----------------------------------------------------------------------------------------------------------------------


 -----------------------------------------------------------------------------------------------------------------------


 -----------------------------------------------------------------------------------------------------------------------


 -----------------------------------------------------------------------------------------------------------------------


 -----------------------------------------------------------------------------------------------------------------------


 -----------------------------------------------------------------------------------------------------------------------


 -----------------------------------------------------------------------------------------------------------------------


 -----------------------------------------------------------------------------------------------------------------------


 -----------------------------------------------------------------------------------------------------------------------


 -----------------------------------------------------------------------------------------------------------------------


 -----------------------------------------------------------------------------------------------------------------------


 -----------------------------------------------------------------------------------------------------------------------


 -----------------------------------------------------------------------------------------------------------------------


 -----------------------------------------------------------------------------------------------------------------------


 -----------------------------------------------------------------------------------------------------------------------


 -----------------------------------------------------------------------------------------------------------------------


 -----------------------------------------------------------------------------------------------------------------------


 -----------------------------------------------------------------------------------------------------------------------


 -----------------------------------------------------------------------------------------------------------------------


 -----------------------------------------------------------------------------------------------------------------------


 -----------------------------------------------------------------------------------------------------------------------


 -----------------------------------------------------------------------------------------------------------------------


 -----------------------------------------------------------------------------------------------------------------------


 -----------------------------------------------------------------------------------------------------------------------


 -----------------------------------------------------------------------------------------------------------------------


 -----------------------------------------------------------------------------------------------------------------------


 -----------------------------------------------------------------------------------------------------------------------


 -----------------------------------------------------------------------------------------------------------------------


 -----------------------------------------------------------------------------------------------------------------------


 -----------------------------------------------------------------------------------------------------------------------


 -----------------------------------------------------------------------------------------------------------------------


 -----------------------------------------------------------------------------------------------------------------------


  --- Функциональное программирование на Python ---

 def repeat_phrase_n_times(phrase, n) -> str:
     print(f"{phrase}\n"*n)                       # Можно \n перенос так использовать

 repeat_phrase_n_times('Белье надевают под одежду', 2)
 # -> Белье надевают под одежду
 # -> Белье надевают под одежду

 -----------------------------------------------------------------------------------------------------------------------

 # Проверка на ВИСОКОСНОСТЬ

 # Разные варианты
 from calendar import isleap         def is_leap(year):
 def is_leap(year):                     return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
     return isleap(year)

 print(is_leap(1900))  # -> False

 # Или lambda
 is_leap = lambda x: __import__('calendar').isleap(x)


 # Список ВИСОКОСНЫХ лет
 get_leap_years = lambda x, y: [i for i in range(x, y) if __import__('calendar').isleap(i)]

 print(get_leap_years(2000, 2018))  # -> [2000, 2004, 2008, 2012, 2016]


 -----------------------------------------------------------------------------------------------------------------------

 from functools import reduce
 import operator

 # принимает список чисел и находит их произведение и start - начальное значение произведения
 def my_product(lst, start=1):                 def my_product(nums: list[int], start: int = 1) -> int:
     return reduce(operator.mul, lst, start)      return __import__('functools').reduce(lambda x, y: x * y, nums, start)

 print(my_product([1, 2, 3]))      # -> 6
 print(my_product([1, 2, 3], 10))  # -> 60


 -----------------------------------------------------------------------------------------------------------------------

 # Если include_quantities = True, вы вывeсти {количество}x{имя_товара}   иначе выводите только имя.
 shopping_list = {'Bread': 13, 'Potato': 5}

 Только регуляркой!!!
 # Вариант с  match case                                    # Вариант с  if
 def sub_fun(m):                                            def sub_fun(m):
     match m[0]:                                                if m[0] in ["'", '[', ']', ' ', '"']:
         case x if x in ["'", '[', ']', ' ', '"']:                  return ''
             return ''                                          if m[0] == ':':
         case ':':                                                  return 'x'
             return 'x'                                         if m[0] == ',':
         case ',':                                                  return '\n'
             return '\n'

 def show_list(include_quantities=True):
     shop = re.findall(r'(?i)\'\w+\': \d+', str(shopping_list))
     shop_sub = re.sub(r'[\'\]\[ :,"]', sub_fun, str(shop))
     if include_quantities:
         print(re.sub(r'(\w+)(x)(\d+)', r'\3\2\1', shop_sub))
     else:
         print(re.sub(r'[\dx]', r'', shop_sub))


 # А вот решения без регулярки!!!
 def show_list(include_quantities=True):           def show_list(include_quantities: bool =True) -> None:
    for key, value in shopping_list.items():           for i, quantity in shopping_list.items():
        if include_quantities:                             print(f'{quantity}x' * int(include_quantities) + i)
            print(f"{value}x{key}")
        else:
            print(f"{key}")

 show_list(include_quantities=False)
 # -> Bread
 # -> Potato
 show_list()
 # -> 13xBread
 # -> 5xPotato


 -----------------------------------------------------------------------------------------------------------------------

 # Что увидим на экране после выполнения следующего кода?

 def do_it_something(lst):
     lst[0] = "Гавайская"
     lst[1] = "пицца"
     return lst

 values = ['Ребрышки', 'гриль', 'это', 'очень', 'вкусно']
 new_values = do_it_something(values)
 print(values)
 print(new_values)


 -----------------------------------------------------------------------------------------------------------------------

 # Простая функция но как написать с lambda?            # А ВОТ ТАК!
 def truncate_sentences(a, *args):                      truncate_sentences = lambda a, *x: [print(i[:a]) for i in x]
     for i in args:
         print(i[:a], end='  ')    # -> ABC  DEF  GHI
 truncate_sentences(3, "ABC","DEF","GHI")


 -----------------------------------------------------------------------------------------------------------------------

 # Обменный пункт.  делим одно на другое и умножаем на количество
 # у тебя есть 100 долларов, тебе нужно поменять эту сумму на евро Сколько ты получишь евро если курс 0.861775 за 1 дол
 exchange_rates = {
     "USD": 1.0,
     "EUR": 0.861775,
 }
 def convert(value, value_2, n):
     return round((exchange_rates[value_2]/exchange_rates[value]) * n, 2)

 currency = convert("USD", "EUR", 100)
 print(currency)  # -> 86.18

 convert = lambda c1, c2, n: round(float.__truediv__(*map(exchange_rates.get, (c2, c1))) * n, 2)
 currency = convert("EUR", "USD", 100)
 print(currency)  # -> 116.04


 -----------------------------------------------------------------------------------------------------------------------

 --- sys.stdin,  open(0) ---

 0 - это дискриптора стандартного потока ввода, соответственно open(0) открывает поток ввода. Более универсальный
 надежный подход к считыванию всех данных одной строкой - через модуль sys
 -- Другими словами, с помощью функции open мы считываем все данные и потом работаем с ними (построчно). --

 Поток ввода (sys.stdin) — это специальный объект в программе, куда попадает весь текст, который ввёл пользователь.
 Потоком его называют потому, что данные хранятся в нем до тех пор, пока программа их не прочитала.

 Поток ввода (sys.stdin) — является итератором, который невозможно перезапустить. Как и любой итератор,
 он может двигаться только вперёд. Как только данные прочитаны, они удаляются из потока ввода безвозвратно.

 # Примеры Посмотри как написан код и else:    <-----


 import re                                     import re, sys

 for i, line in enumerate(open(0), 1):         for i, line in enumerate(sys.stdin, 1):
     if res := re.search(r'[Кк]од', line):         if s := re.search('[Кк]од', line):
         print(i, res.start())                         print(i, s.start())
         break                                         break
 else:                                         else:
     print('код не найден')                        print('код не найден')

 # Тоже самое но установили сколько будет введего строк

 lst = ['Как мне такое? Не знаю', 'Paypal это круто', 'Код запуска: ИлонМаксим2007', 'A']   # Пример что было введено

                                                # Варинт с использованием lst и ответ в конце
 import re                                      import re

 for i in range(4):                             for i, v in enumerate(lst):
     s = input()                                    result = re.search("[кК]од", v)
     result = re.search("[кК]од", s)                if result:
     if result:                                         print(i + 1, result.span()[0])
         print(i + 1, result.span()[0])                 break
         break
 else:                                          else:
     print('код не найден')                         print('код не найден')
                                                # -> 3 0

 sys.stdin вроде в Пичарме не получится использовать, т.к. он не умеет прерывать поток ввода.   <-----

 Обычно я просто копирую в отдельную переменную то, что необходимо и потом с этим работаю (каким угодно способом),
 либо копирую ввод в файл и работаю с файлом через менеджер контекста, в принципе, одно и тоже получается.   <-----
 -----------------------------------------------------------------------------------------------------------------------


 --- Comprehensions: list, dict, set ---
 Работают быстрее цикла for или    цикпа while!                                                 <-----

 Существует 4 генератора (не функций):
 1. list comprehension   - генератор списков   [выражение for переменная in последовательность if условие]          []
 2. set comprehension    - генератор множеств  {выражение for переменная in последовательность if условие}          {}
 3. dict comprehension   - генератор словарей  {ключ: значение for ключ, значение in последовательность if условие} {k:v}
 4. generator expression - выражение-генератор (выражение for переменная in последовательность if условие)          ()

 -- List Comprehensions         Listcomps --

 # Сравнение с обычным for

 # Квадраты чисел ** 2                                        # list comp   Работает быстрее                 <-----
 squares = []                                                 squares = [i**2 for i in range(10)]
 for i in range(10):
     squares.append(i**2)
 print(squares)  # -> [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]    print(squares)  # -> [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

 # Тоже сомое но с lambda
 squares = list(map(lambda x: x**2, range(10)))
 print(squares)  # -> [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

 # Внутри может быть любой iterable
 print([i*5 for i in 'hello'])     # -> ['hhhhh', 'eeeee', 'lllll', 'lllll', 'ooooo']
 print([ord(i) for i in 'hello'])  # -> [104, 101, 108, 108, 111]

 # 10 случайных чисел
 import random
 print([random.randrange(1, 10) for i in range(10)])  # -> [6, 3, 8, 2, 9, 4, 8, 5, 5, 7]
 print([random.randint(1, 10) for i in range(10)])    # -> [7, 3, 3, 5, 7, 3, 7, 10, 3, 1]

 -----------------------------------------------------------------------------------------------------------------------

 Условие внутри:

 a_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]   # list(range(10)) Тоже самое
 # Числа больше 5
 print([i for i in range(10) if i > 5])                         # -> [6, 7, 8, 9]
 # Числа больше 5  не 6, 9
 print([i for i in range(10) if i > 5 and i != 6 and i != 9])   # -> [7, 8]

 # Объединяет элементы двух списков, если они не равны
 combs = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
 print(lst)  # -> [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

 # Тоже самое но с циклом for
 combs = []
 for x in [1,2,3]:
     for y in [3,1,4]:
         if x != y:
             combs.append((x, y))
 print(lst)  # -> [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]


 # if else  Прописывается вначале!!                                                                             <-----
 print([i if i > 7 else 'A' for i in range(10)])  # -> ['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 8, 9]
 # Условия работают как в тернарном операторе
 value = 123
 print('even' if value % 2 == 0 else 'odd')                  # -> odd
 print(['even' if i % 2 == 0 else 'odd' for i in range(3)])  # -> ['even', 'odd', 'even']

 -----------------------------------------------------------------------------------------------------------------------

 vec = [-4, -2, 0, 2, 4]

 # Умножить каждый элемент на 2
 print([x * 2 for x in vec])   # -> [-8, -4, 0, 4, 8]
 # Применить функцию к каждому элементу
 print([abs(x) for x in vec])  # -> [4, 2, 0, 2, 4]

 freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
 # Применить метод к каждому элементу
 print([weapon.strip() for weapon in freshfruit])  # -> ['banana', 'loganberry', 'passion fruit']

 # Создать список из двух кортежей типа (число, квадрат)
 print([(x, x**2) for x in range(6)])  # -> [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]

 # Похожий пример
 print([(i, j) for i in 'ab' for j in [1, 2]])  # -> [('a', 1), ('a', 2), ('b', 1), ('b', 2)]

 # Понимания списков могут содержать сложные выражения и вложенные функции:
 print([str(round(i*0.344, i)) for i in range(1, 6)])  # ->['0.3', '0.69', '1.032', '1.376', '1.72']

 -----------------------------------------------------------------------------------------------------------------------

 -- Nested List Comprehensions     Понимание вложенных списков --

 matrix = [
     [1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12],
 ]
 # Сравни их
 print([i for row in matrix for i in row])     # -> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
 print([[i for i in row] for row in matrix])   # -> [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
 -----------------------------------------------------------------------------------------------------------------------

 matrix = [
     [1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12],
 ]

 # Все результаты будут одинаковые!!!

 # Следующее понимание списка будет транспонировать строки и столбцы:
 transposed = [[row[i] for row in matrix] for i in range(4)]
 print(transposed)          # -> [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

 # Тоже самое
 transposed = []
 for i in range(4):
     transposed.append([row[i] for row in matrix])
 print(transposed)          # -> [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

 # что, в свою очередь, аналогично:
 transposed = []
 for i in range(4):
     # следующие 3 строки реализуют вложенный listcomp
     transposed_row = []
     for row in matrix:
         transposed_row.append(row[i])
     transposed.append(transposed_row)
 print(transposed)          # -> [(1, 5, 9), (2, 6, 10), (3, 7, 11), (4, 8, 12)]

 # В реальном мире вам следует предпочесть встроенные функции
 print(list(zip(*matrix)))  # -> [(1, 5, 9), (2, 6, 10), (3, 7, 11), (4, 8, 12)]
 print(list(zip(matrix)))   # -> [([1, 2, 3, 4],), ([5, 6, 7, 8],), ([9, 10, 11, 12],)]  # Без распаковки *  исходный

 -----------------------------------------------------------------------------------------------------------------------
 Примеры интересные!

 # Обход Списка кортежей
 a = [
     ("Sidorov", 1995),
     ("Lukov", 2002),
     ]

 print([i for i in a])                       # -> [('Sidorov', 1995), ('Lukov', 2002)]
 print([i[0] for i in a])                    # -> ['Sidorov', 'Lukov']
 print([i[0] for i in a if i[1] > 1995])     # -> ['Lukov']
 print([i[0][2] for i in a if i[1] > 1995])  # -> ['k']

 # Обход Словаря
 a = {
     'Sidor': {'age': 1995, 'hob': 'soc', 'car': 'BMW'},
     'Lukov': {'age': 2002, 'hob': 'bas', 'car': 'Opel'},
 }
 print([i for i in a])     # -> ['Sidor', 'Lukov']  # Ключи Словаря
 print([a[i] for i in a])  # -> [{'age': 1995, 'hob': 'soc', 'car': 'BMW'}, {'age': 2002, 'hob': 'bas', 'car': 'Opel'}]
 print([a[i]['car'] for i in a])                             # -> ['BMW', 'Opel']     # Определенный ключ
 print([a[i]['hob'] for i in a])                             # -> ['soc', 'bas']      # Определенный ключ
 print([a[i]['car'] for i in a if a[i]['age'] > 1995])       # -> ['Opel']            # Определенный ключ по условию
 print([(i, a[i]['car']) for i in a])                        # -> [('Sidor', 'BMW'), ('Lukov', 'Opel')] #  Все
 print([(i, a[i]['car']) for i in a if a[i]['age'] > 1995])  # -> [('Lukov', 'Opel')] # Ключ значение в кортеже Условие

 -----------------------------------------------------------------------------------------------------------------------


 -- Set Comprehensions         Set comps --

 squares = {i ** 2 for i in range(10)}
 cubes = {i ** 3 for i in range(10, 21)}
 chars = {c for c in 'abcdefg'}
 print(squares)  # -> {0, 1, 64, 4, 36, 9, 16, 49, 81, 25}
 print(cubes)    # -> {1728, 4096, 8000, 1000, 5832, 6859, 3375, 4913, 1331, 2197, 2744}
 print(chars)    # -> {'d', 'e', 'a', 'g', 'c', 'f', 'b'}

 Сравнение с циклом for

 d = [1, 2, 3, '1', '2', -4, 3, 5]       d = [1, 2, 3, '1', '2', -4, 3, 5]

 # Цикл for                              # set comp   Работает быстрее                                  <-----
 set_d = set()                           a_set = {int(i) for i in d}
 for i in d:
     set_d.add(int(i))
 print(set_d)  # -> {1, 2, 3, 5, -4}     print(a_set)  # -> {1, 2, 3, 5, -4}

 -----------------------------------------------------------------------------------------------------------------------


 -- Dict Comprehensions         Dict comps --

 Сравнение с циклом for

 # Цикл for                                        # dict comp   Работает быстрее                       <-----
 squares = {}                                      squares = {i: i**2 for i in range(5) if i % 2 == 0}
 for i in range(5):
     if i % 2 == 0:
         squares[i] = i**2
 print(squares)  # -> {0: 0, 2: 4, 4: 16}         print(squares)  # -> {0: 0, 2: 4, 4: 16}

 # Генераторы вложенных словарей
 squares = {i: {j: j**2 for j in range(i + 1)} for i in range(3)}
 print(squares)  # -> {0: {0: 0}, 1: {0: 0, 1: 1}, 2: {0: 0, 1: 1, 2: 4}}
 -----------------------------------------------------------------------------------------------------------------------

 Примеры интересные!

 Пример 1
 a = {word:len(word) for word in ['hi', 'hello', 'www']}
 print(a)  # -> {'hi': 2, 'hello': 5, 'www': 3}

 Пример 2
 data = {
     'A_a': '2',
     'b_b': '1',
 }
 new_data = {key.title(): int(value) for key, value in data.items()}
 print(new_data)  # -> {'A_A': 2, 'B_B': 1}

 Пример 3
 from pprint import pprint
 users = [
     [0, 'Bob', 'password'],
     [1, 'code', 'python'],
     [51, 'qwerty', '1234']
 ]
 new_users = {user[0]: user for user in users}
 pprint(new_users)
 print('*'*15)
 pprint(new_users[1])
 pprint(new_users[51])

 # Красивый Вывод pprint
 # {0: [0, 'Bob', 'password'],
 #  1: [1, 'code', 'python'],
 #  51: [51, 'qwerty', '1234']}
 # ***************
 # [1, 'code', 'python']
 # [51, 'qwerty', '1234']

 -----------------------------------------------------------------------------------------------------------------------


 -- Generator expressions         Gen exp --
 Чистый Итератор

 a_gen = (i for i in range(2))
 print(a_gen)             # -> <generator object <genexpr> at 0x0000022CF49B9A40>
 print(next(a_gen))       # -> 0
 print(a_gen.__next__())  # -> 2
 print(a_gen.__next__())  # -> StopIteration

 # Получили ссылку на генератор
 a_gen = [(i for i in range(10))]
 print(a_gen)     # -> [<generator object <genexpr> at 0x00000241E6CF9A40>]
 print(a_gen[0])  # -> <generator object <genexpr> at 0x0000027C7C1E9A40>

 # Интересныe примеры
 a = [1, 2, 3]
 # print(next(a))     # -> TypeError: 'list' object is not an iterator

 d = iter(a)
 print(next(d))       # ->  1
 print(next(d))       # ->  2
 print(d.__next__())  # ->  3
 print(d.__next__())  # ->  StopIteration

 # Одноразовый
 a_gen = (i for i in range(5))
 print(list(a_gen))  # -> [0, 1, 2, 3, 4]
 print(list(a_gen))  # -> []

 -----------------------------------------------------------------------------------------------------------------------

 --- lambda ---

 # Вторичный критерий сортировки указываем в кортеже
 people = [{"name": "B", "country": "AA", "age": 50}, {"name": "A", "country": "AA", "age": 50}]
 sorted(people, key=lambda x: x['age'])
 sorted(people, key=lambda x: (x['age'], x['name']))  # Вторичный критерий сортировки указываем в кортеже     <-----

 # Или просто пишем x без ничего
 people = ["CA", "BA", "DA", "AA", "FD"]
 sorted(people, key=lambda x: (len(x), x))  # ['AA', 'BA', 'CA', 'DA', 'FD']
 sorted(people, key=len)                    # ['CA', 'BA', 'DA', 'AA', 'FD']

 Сортировать одновременно и по значениям, и по ключам, а не сначала по-одному, потом по-другому. Унарный минус <-----
 # Унарный минус работает только с числами!!!  Минус  -   Работает как  reverse=True  Но к элементу            <-----
 a = [('ФФФ', 5), ('Укк', 4), ('Бил', 4)]
 print(sorted(a))                               # -> [('Бил', 4), ('Укк', 4), ('ФФФ', 5)]
 print(sorted(a, key=lambda x: (-x[1], x[0])))  # -> [('ФФФ', 5), ('Бил', 4), ('Укк', 4)]   <----- Унарный минус - Числа



 ---  В отличие от обычной функции, лямбда-функция — это одно выражение. ---

 # НЕЛЬЗЯ использовать  return и pass
 Bad = lambda x: pass       # -> SyntaxError: invalid syntax
 Bad = lambda x: return x   # -> SyntaxError: invalid syntax

 # НЕЛЬЗЯ реализовать аналоги функций, содержащих ЦИКЛЫ.  while/for
 # Условия if else через Тернарный оператор   get_sign = lambda x: 'positive' if x>0 else 'negative or 0'

 # МОЖНО использовать анонимную функцию без параметров
 h = lambda: 'hello'
 print(h())

 # Тоже самое              # Тоже самое
 def surprise():           surprise = lambda: print('surprise')
     print('surprise')     print(surprise())
     return None


 # Хорошее решение                                                                                  <-----       <-----
 # хозяйке на заметку - str.startswith и str.endswith вполне умеют принимать кортежи и проверять каждую букву отдельно
 check_word = lambda x: x.upper().startswith(('Q', 'R')) and x.upper().endswith(tuple('AEIUO'))
 print(check_word.__name__)  # -> <lambda>
 print(check_word('radio'))  # -> True

 check_word = lambda x: x[0].upper() in 'QR' and x[-1].upper() in 'AEIUO'
 print(check_word.__name__)  # -> <lambda>
 print(check_word('radio'))  # -> True

 # Тоже самое
 check_word = lambda x: bool(__import__('re').match(r'(?i)[QR].*[AEIUO]$', x))


 # Интересные решения Тоже самое
 sale_lambda = lambda x: x * 0.9 if x > 50 else x
 sale_lambda = lambda x: (x, x * 0.9)[x > 50]
 print(sale_lambda.__name__)  # -> <lambda>
 print(sale_lambda(50.0))     # -> 50.0


 # Среднее арифметическое. Avg
 average = lambda *args: sum(args) / len(args)
 print(average.__name__)  # -> <lambda>
 print(average(4, 5, 6))  # -> 5.0


 -----------------------------------------------------------------------------------------------------------------------

 --- Вложенные функции ---
 Внутренняя функция (Inner function), также известная как вложенная (nested function), — это функция,
 которая определена внутри другой функций.

 # Увеличивает значение на 1
 def wrap_increment(value):
     def _inc(value):
         return value + 1
     return _inc(value)

 print(wrap_increment(41))  # -> 42


 # Интересный
 def get_extensions(file_list):
     _get_extension = lambda x: x.split(".")[-1] if "." in x else  ""
     return [_get_extension(i) for i in file_list]

 print(get_extensions(["foo.txt", "bar.mp4", "python3"]))  # -> ['txt', 'mp4', '']

 # Тоже самое
 def get_extensions(file_list: list[str]) -> list[str]:
     def _get_extension(filename: str) -> str:
         return ('', filename[filename.rfind('.') + 1:])['.' in filename]
     return [_get_extension(filename) for filename in file_list]

 print(get_extensions(["foo.txt", "bar.mp4", "python3"]))  # -> ['txt', 'mp4', '']

  # Тоже самое
 from pathlib import Path

 def get_extensions(file_list):
     def _get_ext(f_name):
         return Path(f_name).suffix.lstrip('.')
     return [*map(_get_ext, file_list)]

 print(get_extensions(["foo.txt", "bar.mp4", "python3"]))  # -> ['txt', 'mp4', '']



 # Внимательно посмотри как работают
 # double, увеличивающая число в два раза   is_odd, проверяющая на нечетность
 def double_odd_numbers(numbers):
     def double(num):
         return num * 2

     def is_odd(num):
         if num % 2:
             return num
     return [double(num) for num in numbers if is_odd(num)]

 print(double_odd_numbers([1, 2, 3, 4, 5]))  # -> [2, 6, 10]

 # Тоже самое!
 def double_odd_numbers(numbers):
     double = lambda x: x * 2
     is_odd = lambda x: x % 2 != 0
     return [double(num) for num in numbers if is_odd(num)]

 # Тоже самое!                                                                                      <-----       <-----
 def double_odd_numbers(numbers, double=lambda x: x * 2, is_odd=lambda x: x % 2):
     return [double(num) for num in numbers if is_odd(num)]


 -----------------------------------------------------------------------------------------------------------------------

 --- Функция высшего порядка (аббревиатура ФВП) ---

 # Функция-применитель  Посмотри ВСЕ Варианты
 def apply(func, lst):
     return [func(i) for i in lst]

 def square(num):
     return num ** 2

 print(apply(square, [5, 7, 0, 3]))  # -> [25, 49, 0, 9]


 # Тоже самое
 def apply(func, x): return list(map(func, x))

 # Тоже самое
 apply = lambda *args: [*map(*args)]


 # Применить каждую функцию к Каждому значению
 def compute(funcs, *args):
     return [func(arg) for func in funcs for arg in args]

 def square(num):
     return num ** 2

 def inc(num):
     return num + 1

 print(compute([square, inc], 10))  # -> [100, 11]

 # Тоже самое
 compute = lambda f, *args: [el(j) for el in f for j in args]


 # Применить каждую функцию к Одному значению   # Очень хороший пример Разбери как работает
 def compute(funcs, *args):
     res = []
     for arg in args:
         for func in funcs:
             arg = func(arg)
         res.append(arg)
     return res

 def square(num):
     return num ** 2

 def inc(num):
     return num + 1

 print(compute([square, inc], 10))  # -> [101]


 # Интересно как работает Тоже самое ----->                 Тоже самое  Разбери попробуй!
 def filter_collection(f, lst):                             def filter_collection(f, seq):
    match lst:                                                  data = filter(f, seq)
        case str():                                             if isinstance(seq, str):
            return ''.join([i for i in lst if f(i)])                return ''.join(data)
        case list():                                            return type(seq)(data)
            return [i for i in lst if f(i)]
        case _:
             return tuple([i for i in lst if f(i)])

 print(filter_collection(lambda x: x not in 'aeiou', 'I never heard those lyrics before'))  # -> I nvr hrd ths lyrcs bfr


 -----------------------------------------------------------------------------------------------------------------------

 --- Замыкания (Closure) ---

 # Замыкание для умножения Посмотри  как можно вызывать Замыкание в print
 def multiply(a):
     def inner(x):
         return a*x
     return inner

 print(multiply(4)(3))    # -> 12
 print(multiply(400)(5))  # -> 2000

 f_2 = multiply(4)
 print(f_2(3))            # -> 12
 f_3 = multiply(400)
 print(f_3(5))            # -> 2000


 # Присвоение значений Нужно использовать nonlocal Иначе будет ошибка
 # UnboundLocalError: cannot access local variable 'total' where it is not associated with a value
 def create_accumulator():
     total = 0
     def inner(n):
         nonlocal total
         total += n
         return total
     return inner

 summator_1 = create_accumulator()
 print(summator_1(5))  # -> summator_1 = create_accumulator()

 summator_2 = create_accumulator()
 print(summator_2(3))  # -> print(summator_1(5))


 # функцию-замыкание count_calls, которая подсчитывает сколько раз она была вызвана.
 # Особенность этого замыкания заключается в том, что количество вызовов должно хранится в атрибуте total_calls.

 def count_calls():
     def inner():
         inner.total_calls += 1
     inner.total_calls = 0
     return inner

 counter = count_calls()
 counter()
 counter()
 print(counter.total_calls)  # -> 2
 counter()
 print(counter.total_calls)  # -> 3



 # Только функцию-замыкание count_calls, которая подсчитывает сколько раз она была вызвана.
 def count_calls():
     count = 0
     def inner():
         nonlocal count
         count += 1
         return count
     return inner

 counter = count_calls()

 print(counter())  # -> 1
 print(counter())  # -> 2
 -----------------------------------------------------------------------------------------------------------------------

 --- Декораторы ---   return None - Закрывает декоратор

 # return None    # Закрывает декоратор    Посмотри внамательно пример особенно как можно использовать ;
 def validate_all_args_str(func):
     def wrapper(*args, **kwargs):
         if all(type(el) == str for el in args): return func(*args, **kwargs)
         else: print('Все аргументы должны быть строками'); return None         # Закрывает декоратор
     return wrapper

 @validate_all_args_str
 def concatenate(**kwargs):
     result = ""
     for arg in kwargs.values():
         result += str(arg)
     return result
 print(concatenate(a="Я", b="Выучу", c="Этот", d="Питон", e="!"))  # -> ЯВыучуЭтотПитон!


 # В dict comprehension прописывать условие k: v Посмотри
 def uppercase_elements(func):
     def wrapper(*args, **kwargs):
         res = func(*args, **kwargs)
         if isinstance(res, list):
             return [i.upper() if isinstance(i, str) else i for i in res]
         return {k.upper() if isinstance(k, str) else k: v for k, v in res.items()}   # Тут условие
     return wrapper

 @uppercase_elements
 def my_func(**kwargs):
     return {1: 'one', 2: 'store', 'three': 3, 'four': 4} | kwargs

 print(my_func(**{'Five': 5, 'sIx': 6}))  # -> {1: 'one', 2: 'store', 'THREE': 3, 'FOUR': 4, 'FIVE': 5, 'SIX': 6}



 # Классные решения!!!
 # Фильтрация аргументов  Ваша задача создать два декоратора

 from functools import wraps
 from typing import Collection

 def filter_even(func):
     @wraps(func)
     def inner(*args, **kwargs):
         check = lambda x: (isinstance(x, Collection) and not len(x) % 2) or (isinstance(x, int) and not x % 2)
         return func(*filter(check, args), **kwargs)

     return inner


 def delete_short(func):
     @wraps(func)
     def inner(*args, **kwargs):
         return func(*args, **{k: kwargs[k] for k in filter(lambda x: len(x) > 4, kwargs)})

     return inner


 @filter_even
 @delete_short
 def concatenate(*args, **kwargs):
     result = ""
     for arg in args + tuple(kwargs.values()):
         result += str(arg)
     return result

 print(concatenate("Я", "хочу", "Выучить", "Питон", a="За", qwerty=10, c="Месяцев"))  # -> хочу10


 # Тоже самое
 def filter_even(func):
     def wrapper(*args, **kwargs):
         return func(*[el for el in args if el == False or
                       (isinstance(el, (str, list, tuple, dict)) and len(el) % 2 == 0) or
                       (isinstance(el, int) and int(el) % 2 == 0)], **kwargs)
     return wrapper

 def delete_short(func):
     def wrapper(*args, **kwargs):
         return func(*args, **{k:v for k, v in kwargs.items() if len(str(k)) > 4})
     return wrapper

 @filter_even
 def concatenate(*args):
     result = ""
     for arg in args:
         result += arg
     return result

 print(concatenate("Ну", "Когда", "Уже", "Я", "Выучу", "Питон?"))  # -> НуПитон?


 # проверяет количество переданных аргументов. 
 from functools import update_wrapper

 class check_count_args:
     def __init__(self, func):
         update_wrapper(self, func)
         self.func = func

     def __call__(self, *args, **kwargs):
         match sum(map(len, (args, kwargs))):
             case 1 | 0:
                 return print('Not enough arguments')
             case 2:
                 return self.func(*args, **kwargs)
             case _:
                 return print('Too many arguments')


 -----------------------------------------------------------------------------------------------------------------------

 --- Декораторы с параметрами ---

 # Умножает результат декорированной функции на N
 from functools import wraps

 def multiply_result_by(N):
     def my_decor(func):
         @wraps(func)
         def inner(*args, **kwargs):
             return func(*args, **kwargs) * N

         return inner
     return my_decor

 @multiply_result_by(2)
 def my_function(x, y):
     return x + y

 print(my_function(5, 6))  # -> 22


 # Декоратор monkey_patching - 2
 from functools import wraps

 def monkey_patching(arg='Monkey', kwarg='patching'):
     def my_decor(func):
         @wraps(func)
         def inner(*args, **kwargs):
             return func(*[arg for _ in args], **{k:kwarg for k, v in kwargs.items()})

         return inner
     return my_decor

 @monkey_patching(arg='Super')
 def print_args_kwargs(*args, **kwargs):
     for i, value in enumerate(args):
         print(i, value, end='   ')
     for k, v in sorted(kwargs.items()):
         print(f'{k} = {v}', end='   ')

 print_args_kwargs(1, 2, b=300, w=40)  # -> 0 Super   1 Super   b = patching   w = patching


 # Пробрасывает Аргументы декоратора дополнительно к аргументам которые передаются при вызове оригинальной функции
 from functools import wraps
                                                        # Тоже самое
 def pass_arguments(*args, **kwargs):                   def pass_arguments(*args_ext, **kwargs_ext):
     arg = args                                             def wrapper(func):
     kwarg = kwargs                                             @wraps(func)
     def my_decor(func):                                        def inner(*args, **kwargs):
         @wraps(func)                                               return func(*args + args_ext, **kwargs | kwargs_ext)
         def inner(*args, **kwargs):                            return inner
             return func(*args, *arg, **kwargs, **kwarg)    return wrapper

         return inner
     return my_decor

 @pass_arguments(s='Когда', w='-', r='нибудь!')
 def concatenate(**kwargs):
     result = ""
     for arg in kwargs.values():
         result += str(arg)
     return result

 print(concatenate(a="Я", b="Выучу", c="Этот", d="Питон", e="!"))  # -> ЯВыучуЭтотПитон!Когда-нибудь!


 # Разбери как работает!!!
 from functools import wraps

 def compose(*funcs):
     def wrapper(func):
         @wraps(func)
         def inner(*args, **kwargs):
             res = func(*args, **kwargs)
             for f in funcs:
                 res = f(res)
             return res
         return inner
     return wrapper

 def double_it(a):
     return a * 2

 def increment(a):
     return a + 1

 @compose(double_it, increment)
 def get_sum(*args):
     return sum(args)

 print(get_sum(5))          # -> 11
 print(get_sum(20, 10))     # -> 61
 print(get_sum(5, 15, 25))  # -> 91

 -----------------------------------------------------------------------------------------------------------------------

  --- iterator ---

 Как в python реализован цикл for

 # Тоже самое                   # Тоже самое
 s = 'Python'                   s = 'Python'

 it = iter(s)                   for letter in s:
 while True:                        print(letter)
     try:
         print(next(it))
     except StopIteration:
         del it
         break


 # Занимаемая память

 from sys import getsizeof

 numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
 iterator = iter(numbers)
 print(getsizeof(numbers), getsizeof(iterator))           # -> 136 48

 # Чем больше список, тем будет заметнее разница
 too_much_numbers = list(range(1000000))
 iterator = iter(numbers)
 print(getsizeof(too_much_numbers), getsizeof(iterator))  # -> 8000056 48



 -----------------------------------------------------------------------------------------------------------------------
 --- all zip ---

 # Сравнение внутри создадим пары
 lst = [7, 6, 5, 4, 3, 2, 1]
 print(list(zip(lst, lst[1:])))   # -> [(7, 6), (6, 5), (5, 4), (4, 3), (3, 2), (2, 1)]
 print(all([a > b for a, b in zip(lst, lst[1::])]))  # -> True  # Сравнение!  Тоже самое
 print(all(map(lambda x, y: x > y, lst, lst[1:])))   # -> True  # Сравнение!  Тоже самое

 # Создадим словарь
 a_str = 'abc'
 a_list = [1, 2, 3]
 print(dict(zip(a_list, a_str)))  # -> {'a': 1, 'b': 2, 'c': 3}   # Создали словарь   dict(zip(a_list, a_str))

 # Как Зипануть     Легко но всё же
 def read_csv():
     with open('data.csv', encoding='utf-8') as file:
         data = file.readline().replace('\n', '').split(',')
         lst = [i.replace('\n', '').split(',') for i in file.readlines()]
         lst_1 = [dict(zip(data, i)) for i in lst]                              <-----
         return lst_1

 # Тоже самое
 def read_csv():
     with open('data.csv') as file:
         keys = file.readline().strip().split(',')
         return [dict(zip(keys, line.strip().split(','))) for line in file]     <-----

 -----------------------------------------------------------------------------------------------------------------------

 --- with ---

 # Был долгий тупняк!!!                                                                             <-----
 with open('data.txt', encoding='utf-8') as file, open('forbidden_words.txt') as file_2:
     text, lst = file.read(), file_2.read().split()
     for i in lst:
         text = re.sub(i, '*' *len(i), text, flags=re.IGNORECASE)     # Тупняк был тут!   <-----
     print(text)


 # В print Можно использовать параметр file=   Запись в файл
 # Классный параметр  file=                                                                         <-----       <-----
 with open('output1.txt', 'w', encoding='utf-8') as file, open('logfile1.txt', encoding='utf-8') as file_2:
     for i in file_2.read().split('\n'):
         c, a, b = i.split(', ')
         d = datetime.datetime.strptime(b, "%H:%M") - datetime.datetime.strptime(a, "%H:%M")
         if d.seconds >= 3600:
             print(c, file=file)  #  file - Выбор куда записывать                                   <-----       <-----



 # Файл считывается 1 раз                                 # Файл считывается 1 раз
 with open('file.txt', encoding='utf-8') as file:         with open('file.txt', encoding='utf-8') as file:
     data = file.read()                                       # data = file.read()                     # Закоментили
     lst = [i.split() for i in file]                          lst = [i.split() for i in file]
     print(f'{len(lst)} lines')  # -> 0 lines                 print(f'{len(lst)} lines')  # -> 12 lines
     print(len(data))            # -> 1340                    # print(len(data))     # -> 0            # Закоментили

 # Записываем из одного файла в другой с помощью словаря
 d = {'а': 'a', 'к': 'k', 'х': 'h', 'б': 'b'}
 with open('file_1.txt', encoding='utf-8') as file, open('file_2.txt', 'w+') as file_2:
     for i in file.read():
         if i in d:
             print(d[i], file=file_2, end='')                # Выбор куда запись Параметр  file=
         else:
             print(i, file=file_2, end='')                   # Выбор куда запись Параметр  file=

 -----------------------------------------------------------------------------------------------------------------------

 --- json ---

 # Классное решение  Внутри цикла переменные посмотри как делать

 first = ''
 last = ''
 max_total = 0

 with open('manager_sales.json') as file:
     data = json.load(file)
     for element in data:
         name = element['manager']['first_name']
         lastname = element['manager']['last_name']
         total = 0                                    # Обнуляется каждый раз считаем заново
         for car in element['cars']:
             total += car['price']
         if total > max_total:
             max_total = total
             max_name = name
             max_lastname = lastname
         print(first, last, max_total)

 # Создал словарь всех
 import json

 with open('manager_sales.json') as file:
     data = json.load(file)
     a = {}
     for i in data:
         totals = 0
         for j in i['cars']:
             totals += j['price']
             if totals > 0:
                 a[f"{i['manager']['first_name']} {i['manager']['last_name']}"] = totals
     print(*sorted(a.items(), key=lambda x: x[1], reverse=True)[0])

 # Тоже самое с match case
 with open('manager_sales.json') as file:
     data = json.load(file)
     a = {}
     for i in data:
         totals = 0
         for j in i['cars']:
             totals += j['price']
             match totals:                                                                       # match case <-----
                 case totals if totals > 0:
                     a[f"{i['manager']['first_name']} {i['manager']['last_name']}"] = totals
     print(*sorted(a.items(), key=lambda x: x[1], reverse=True)[0])

 -----------------------------------------------------------------------------------------------------------------------

 # Похожий пример
 import json

 with open('group_people.json') as file:
     data = json.load(file)
     maximum = 0
     max_group = None
     for group in data:
         id_group = group['id_group']
         count = 0
         for person in group['people']:
             if person['gender'] == 'Female' and person['year'] > 1977:
                 count += 1
         if count > maximum:
             maximum = count
             max_group = id_group
     print(max_group, maximum)

 # Создал словарь всех
 with open('group_people.json') as file:
     data = json.load(file)
     a = {}
     for i in data:
         count = 0
         for j in i['people']:
             if j['gender'] == 'Female' and j['year'] > 1977:
                 count += 1
                 a[i['id_group']] = count
     print(*sorted(a.items(), key=lambda x: x[1], reverse=True)[0])

 # Тоже самое match case

 with open('group_people.json') as file:
     data = json.load(file)
     a = {}
     for i in data:
         count = 0
         for j in i['people']:
             match j:                                                                             # match case <-----
                 case {'gender': male, 'year': year} if year > 1977 and male == 'Female':
                     count += 1
                     a[i['id_group']] = count
     print(*sorted(a.items(), key=lambda x: x[1], reverse=True)[0])
 -----------------------------------------------------------------------------------------------------------------------

 Открыть сразу 2 и более файлов в одном with

 import json

 with open('Alphabet.json') as file, open('Abracadabra__1_.txt') as file_2:
     file = json.load(file)
     file_2 = file_2.read()
     a_str = ''
     for i in file_2:
         if i in file:
             a_str += file[i]
         else:
             a_str += i
     print(a_str.strip())

 # Тоже самое с match case

 with open('Alphabet.json.json') as file_json, open('Abracadabra__1_.txt.txt') as file_text:
     data_json = json.load(file_json)
     data_text = file_text.read()
     a_str = ''
     for i in data_text:
         match i:                                                                                 # match case <-----
             case i if i in data_json:
                 a_str += data_json[i]
             case _:
                 a_str += i
 print(a_str.strip())

 -----------------------------------------------------------------------------------------------------------------------
 # Открытие файлов разные способы!
 Через запятую ,
 with open('first_file.json') as file_1, open('second_file.txt') as file_2:                               <-----
    ...

 Вариант 2!
 with open(''first_file.txt', 'r') as file_1:
    ...
    with open('second_file.txt', 'r') as file_2:
        ...

 Можно отдельными блоками!
 with open(''first_file.txt', 'r') as file_1:
    ...
 with open('second_file.txt', 'r') as file_2:
    ...

 -----------------------------------------------------------------------------------------------------------------------

 --- Разные Подсчеты Руками ---

 # Метод Подсчета Руками
 a = [2, 1, 2, 3, 2, 1, 2, 3, 3, 2, 0, 3, 5, 3, 2]
 count = [0]*6

 for i in a:
     count[i] += 1
 print(count)                                   # -> [1, 2, 6, 5, 0, 1]

 for i in range(6):
     if count[i] > 0:
         print((str(i)+' ') *count[i], end='')  # -> 0 1 1 2 2 2 2 2 2 3 3 3 3 3 5

 -----------------------------------------------------------------------------------------------------------------------

 # Подсчет букв классно можно расчитать диапазон букв

 s = 'abcdefghigklmnopqrstuvwxyzsdhasd ASDKASD asdasd 543 *(^!*&@#'

 letters = [0] * 26

 for i in s.lower():
     if i >= 'a' and i <= 'z':             # -> Сделали Диапазон
         number = ord(i) - 97
         letters[number] += 1
         print(f"{i}: {number} ", end='')  # -> a: 0 b: 1 c: 2 d: 3 e: 4 f: 5 g: 6 h: 7 i: 8 g: 6 k: 10.......
 print('--'*50)
 for i in range(26):
     if letters[i] > 0:
         print(chr(i+97)*letters[i], end='')  # -> aaaaaabcdddddddefgghhikklmnopqrssssssstuvwxyz
 -----------------------------------------------------------------------------------------------------------------------


 --- Вложенные циклы ---

 # Разбор как работает

 Для Одного Внешнего цикла будет выполнятся 5 раз внутренний
                                                              # Выводим i                   # Выводим j
 for i in range(3):            #  1 Раз Внешний цикл          for i in range(3):            for i in range(3):
    for j in range(5):         #  5 Раз Внутренний                for j in range(5):            for j in range(5):
        print('*', end='')                                            print(i, end='')              print(j, end='')
    print()                    # Перенос строки                   print()                       print()

 # *****                                                      # 00000                       # 01234
 # *****                                                      # 11111                       # 01234
 # *****                                                      # 22222                       # 01234
 -----------------------------------------------------------------------------------------------------------------------

 Еще пример Работы Вложенного цикла

 for i in range(1, 3):            for i in 'ab':
     for j in range(10, 12):          for j in 'cd':
         print(i, j)                      print(i, j)

 # 1 10                           # a c
 # 1 11                           # a d
 # 2 10                           # b c
 # 2 11                           # b d

 -----------------------------------------------------------------------------------------------------------------------
 a = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]]
 b = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3]]
 c = []

 # Складываем a+b списки
 for i, v in enumerate(a):
     for j, k in enumerate(v):
         c.append(k + b[i][j])

 print(c)  # -> [2, 3, 4, 5, 4, 5, 6, 7, 6, 7, 8, 9]
 -----------------------------------------------------------------------------------------------------------------------
 M, N = 2, 3
 zeros = []

 for i in range(M):
     zeros.append([0]* N)

 # Создали список списков из 0
 print(zeros)  # -> [[0, 0], [0, 0], [0, 0]]

 for i in range(M):
     for j in range(N):
         zeros[i][j] = 1
 # Все 0 заменили на 1
 print(zeros)  # -> [[1, 1], [1, 1], [1, 1]]
 -----------------------------------------------------------------------------------------------------------------------
 Строки заменить на столбцы - Транспонированная матрица

 A = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

 for i in range(len(A)):
     for j in range(i+1, len(A)):
         A[i][j], A[j][i] = A[j][i], A[i][j]

 for r in A:                        #  1    5    9     13
     for x in r:                    #  2    6    10    14
         print(x, end='\t')         #  3    7    11    15
     print()                        #  4    8    12    16

 -----------------------------------------------------------------------------------------------------------------------
 Важно посмотри!!!

 n = 4

 # Если создавать список так:
 lst = [[1] * n] * n
 # То просто копируется ссылка на один и тот же список.
 print(lst)  # -> [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]
 lst[0][n-1] = 5
 print(lst)  # -> [[1, 1, 1, 5], [1, 1, 1, 5], [1, 1, 1, 5], [1, 1, 1, 5]]  # Заменили ВСЕ последние элементы на 5

 # Если так:
 lst2 = [[1] * n for _ in range(n)]
 # То создаются отдельные списки
 print(lst2)  # -> [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]
 lst2[0][n-1] = 5
 print(lst2)  # -> [[1, 1, 1, 5], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]  # Заменили Только 1 последний элемент на 5

 # Или делаем руками
 n = 4

 lst = [[1]*n]*n
 print(lst)  # -> [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]
 for i, v in enumerate(lst):
     for j, k in enumerate(v):
         lst[i][-1] = 5

 print(lst)  # -> [[1, 1, 1, 5], [1, 1, 1, 5], [1, 1, 1, 5], [1, 1, 1, 5]]


 Копируется ссылка на один и тот же список.              <-----

 # Хороший пример
                    A = [[1]*N]*N              A[0][N-1] = 5         for i in range(4):
 N = 4              Был такой                  Сделали таким             for j in range(3):      Тоже самое
 A = [[1]*N]*N      #  1 1 1 1                 #  1 1 1 5                    print(1, end=' ')   # 1 1 1 5
 A[0][N-1] = 5      #  1 1 1 1                 #  1 1 1 5                print(5)                # 1 1 1 5
 for i in A:        #  1 1 1 1                 #  1 1 1 5                                        # 1 1 1 5
     print(*i)      #  1 1 1 1                 #  1 1 1 5                                        # 1 1 1 5

 -----------------------------------------------------------------------------------------------------------------------
 n = 4                                                     [print(*[i]*n) for i in range(n)]   # Хитрый вывод
 lst = [[i]*n for i in range(n)]     #  0 0 0 0            #  0 0 0 0
                                     #  1 1 1 1            #  1 1 1 1
 for i in lst:                       #  2 2 2 2            #  2 2 2 2
     print(*i)                       #  3 3 3 3            #  3 3 3 3


 -----------------------------------------------------------------------------------------------------------------------


 --- Вложенные Списки  Nested lists ---

 Элементы матрицы мы можем обходит в любом порядке

 # Обращение по индексам во вложенных списках Nested lists                # Матрица или Таблица  Добавил переносы в a_list
 a_list = [[0, 2, 4, 6], [1, 5, 9, 13], [3, 10, [4, 5, 7, 11], 17, 19]]
                                                                          a_list = [
 print(len(a_list))       # -> 3    # Длина всего списка                      [0, 2, 4, 6],
 print(a_list[2][3])      # -> 17                                             [1, 5, 9, 13],
 print(a_list[0][3])      # -> 6                                              [3, 10, 17, 19]
 print(a_list[0][1])      # -> 2                                          ]
 print(a_list[2][2][1])   # -> 5
 -----------------------------------------------------------------------------------------------------------------------

 # Строка(str) внутри Списка(list) считается вложенным элементом
 b = ['hello', 'hi', 'world']

 print(b[2])      # -> world
 print(b[2][4])   # -> d
 print(b[2][-1])  # -> d

 -----------------------------------------------------------------------------------------------------------------------

 -- Как Работают переменные внутри цилка! Посмотри обязательно!                    <-----   <-----

 1 Вариант обхода Просмотри в Дебаге!

 a_list = [[0, 2, 4, 6], [1, 5, 9, 13], [3, 10, 17, 19]]
 for i in a_list:                                                   # Вывод Внутри
     for j in i:                                                    # 10 12 14 16
         j += 10            # Не изменяет a_list                    # 11 15 19 23
         print(j, end=' ')  # Но выводит Измененный результат       # 13 20 27 29
         b_list = j+10      # Но мы можем создать Переменную
     print()
 print(a_list)  # -> [[0, 2, 4, 6], [1, 5, 9, 13], [3, 10, 17, 19]]      #  a_list Такой же как и был
 print(b_list)  # -> 39                                                  #  Создали перменную b_list
 -----------------------------------------------------------------------------------------------------------------------

 2 Вариант обхода!  Обход по индексам  Изменяет Исходник

 a_list = [[0, 2, 4, 6], [1, 5, 9, 13], [3, 10, 17, 19]]

 for i in range(3):                                                 # Вывод Внутри  Такой же
     for j in range(4):                                             # 10 12 14 16
         a_list[i][j] += 10            # ИЗМЕНЯЕТ a_list            # 11 15 19 23
         print(a_list[i][j], end=' ')                               # 13 20 27 29
     print()
 print(a_list) # -> [[10, 12, 14, 16], [11, 15, 19, 23], [13, 20, 27, 29]]  #  a_list Изменился

 # Если нужен другой  вывод меняем местами Циклы:  j i
 a_list = [[0, 2, 4, 6], [1, 5, 9, 13], [3, 10, 17, 19]]
                                                                    # Вывод Внутри
 for j in range(4):                                                 # 0 1 3
     for i in range(3):                                             # 2 5 10
         print(a_list[i][j], end=' ')                               # 4 9 17
     print()                                                        # 6 13 19

 # Обход в Обратном порядке
 for i in range(2, -1, -1):                                         # 19 17 10 3
     for j in range(3, -1, -1):                                     # 13 9 5 1
         print(a_list[i][j], end=' ')                               # 6 4 2 0
     print()

 # Сумма строк                                                                      Посмотри где переменная   <-----
 a_list = [[0, 2, 4, 6], [1, 5, 9, 13], [3, 10, 17, 19]]
 for i in range(3):                                                 # 12
     s = 0               # Каждый раз сумма обнуляется!!!           # 28
     for j in range(4):                                             # 49
         s += a_list[i][j]
     print(s)

 # Сумма Столбцов                                                                                             <-----
 for j in range(4):                                                 # 4
     s = 0               # Каждый раз сумма обнуляется!!!           # 17
     for i in range(3):                                             # 30
         s += a_list[i][j]                                          # 38
     print(s)

 -----------------------------------------------------------------------------------------------------------------------
 Как устроены матрицы!                                                                                        <-----

 # i < j    # Выше главной диагонали                                                                    <-----
 # i == j   # Главная диагональ                                                                         <-----
 # i > j    # Ниже главной диагонали                                                                    <-----

 a = []
 for i in range(3):
     a.append([0]*3)        #    Создаем Список(list)
 print(a)                   # -> [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

 for i in range(3):
     for j in range(3):
         if i == j:         # i == j   # Главная диагональ
             a[i][j] = 10
         elif i > j:        # i > j    # Ниже главной диагонали
             a[i][j] = 3
         elif i < j:        # i < j    # Выше главной диагонали
             a[i][j] = 5

 print(a)                   # -> [[10, 5, 5], [3, 10, 5], [3, 3, 10]]

 for i in a:
     print(i)

 # [10, 5, 5]
 # [3, 10, 5]
 # [3, 3, 10]
 -----------------------------------------------------------------------------------------------------------------------

 # Несколько примеров для закрепления!

 # Создание и вывод матрицы                n = 2                                   n = 2
 n = 2                                     a = []                                  a = []
 a = []
 for i in range(n):                        for i in range(n):                      for i in range(n):
     a.append([5, 2, 1])                       a.append([5, 2, 1])                     a.append([5, 2, 1])

 print(a)  # -> [[5, 2, 1], [5, 2, 1]]     print(a)  # -> [[5, 2, 1], [5, 2, 1]]   print(a)  # -> [[5, 2, 1], [5, 2, 1]]

                                           # Поменяли местами i j                  # i j  Отрицательные индексы!
 for i in range(n):                        for j in range(n+1):                    for j in range(n, -1, -1):
     for j in range(n+1):                      for i in range(n):                      for i in range(n-1, -1, -1):
         print(a[i][j], end=' ')                   print(a[i][j], end=' ')                 print(a[i][j], end=' ')
     print()                                   print()                                 print()

 # 5 2 1                                   # 5 5                                   # 1 1
 # 5 2 1                                   # 2 2                                   # 2 2
                                           # 1 1                                   # 5 5
 -----------------------------------------------------------------------------------------------------------------------

 Работа Матриц/Матрицы/матриц/матрицы/МАТРИЦ/МАТРИЦЫ/!!! Посмотри интересно                <-----              <-----


 m = [['a', 'a', 'b', 'b'], ['a', 'a', 'b', 'b'], ['c', 'c', 'd', 'd'], ['c', 'c', 'd', 'd']]

 Вот матрица m:
 a a b b
 a a b b
 c c d d
 c c d d

 # m[i][j] распечатает матрицу как она есть:    # m[j][i] отразит матрицу по главной диагонали:

 for i in range(4):                             for i in range(4):
     for j in range(4):                             for j in range(4):
         print(m[i][j], end=' ')                        print(m[j][i], end=' ')
     print()                                        print()

 # a a b b                                      # a a c c
 # a a b b                                      # a a c c
 # c c d d                                      # b b d d
 # c c d d                                      # b b d d


 Вот матрица m:
 a a b b
 a a b b
 c c d d
 c c d d

 # m[~i][j] отразит верх и низ:   # m[i][~j] отразит лево и право:   # m[~j][~i] отразит относительно побочной диагонали:

 for i in range(4):               for i in range(4):                 for i in range(4):
     for j in range(4):               for j in range(4):                 for j in range(4):
        print(m[~i][j], end=' ')         print(m[i][~j], end=' ')          print(m[~j][~i], end=' ')
     print()                          print()                            print()

 # c c d d                        # b b a a                          # d d b b
 # c c d d                        # b b a a                          # d d b b
 # a a b b                        # d d c c                          # c c a a
 # a a b b                        # d d c c                          # c c a a


 Вот матрица m:
 a a b b
 a a b b
 c c d d
 c c d d

 # Тоже самое с enumerate()  Лучше использовать enumerate()

 # m[~j][i] - поворот вправо на 90°     # m[j][~i] - поворот на 90° влево

 for i, v in enumerate(m):              for i, v in enumerate(m):
     for j, k in enumerate(m):              for j, k in enumerate(m):
         print(m[~j][i], end=' ')               print(m[j][~i], end=' ')
     print()                                print()

 # c c a a                              # b b d d
 # c c a a                              # b b d d
 # d d b b                              # a a c c
 # d d b b                              # a a c c

 -----------------------------------------------------------------------------------------------------------------------
 Как работает интересно!
 n = 2
 a_str = 'a b c d e f'

 def chunked(a_str, n):
     a_str = a_str.split()
     a = []
     while len(a_str) != 0:
         c = a_str[:n]
         a.append(c)
         a_str = a_str[n:]
     return a
 print(chunked(a_str, n))  # -> [['a', 'b'], ['c', 'd'], ['e', 'f']]

 -----------------------------------------------------------------------------------------------------------------------

 --- Словарь(dict) ---
 # классный пример   Cоздать словарь из iterable     используем - dict.update()

 persons= [
     ('All H.', 3, 'M', '1'),
     ('Meg M.', 1, 'F', '2'),
 ]
 a_dict = {}
 for i in persons:
     a_dict.update({i[0]: {'salary': i[1], 'gender': i[2], 'passport': i[3]}})

 [a_dict.update({i[0]: {'salary': i[1], 'gender': i[2], 'passport': i[3]}}) for i in persons]  # Тоже работает
 print(a_dict)
 # -> {'All H.': {'salary': 3, 'gender': 'M', 'passport': '1'}, 'Meg M.': {'salary': 1, 'gender': 'F', 'passport': '2'}}

 -----------------------------------------------------------------------------------------------------------------------

 Побитовые операторы: Тильда ~
 # Тильда побитовый оператор ~  Инверсия - противоположное состояние
 a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
 print([[~i for i in i] for i in a])  # -> [[-2, -3, -4], [-5, -6, -7], [-8, -9, -10]]

 print(max((input().split()[~i] for i in range(int(input()))), key=int)) # Интересное решение с вводом матриц
 -----------------------------------------------------------------------------------------------------------------------


 --- match case  Тоже самое что  if...elif...else  но более гибкий ---                 <-----     <-----


 СРАЗУ НЮАНСЫ match case!

 # Нельзя использовать Глобальные переменные
 CMD_3 = 3
 CMD_5 = 5

 cmd = 5
 match cmd:
     case CMD_3:
         print('3')
     case CMD_5:
         print('5')

 # -> SyntaxError: name capture 'CMD_3' makes remaining patterns unreachable
 -----------------------------------------------------------------------------------------------------------------------
 Хитрости чтобы Работало!!!                                                  <-----            <-----
                                      через . переменные из другого модуля         class Consts:    # Можно через Класс
 CMD_3 = 3                                                                             CMD_3 = 3
 CMD_5 = 5                            import my_module                                 CMD_5 = 5

 cmd = 5                              cmd = 5                                      cmd = 5
 match cmd:                           match cmd:                                   match cmd:
     case int() as x if x == CMD_3:       case my_module.CMD_3:  #  через точку .      case Consts.CMD_3:    # точка .
         print('3')                           print('3')                                   print('3')
     case int() as x if x == CMD_5:       case my_module.CMD_5:  #  через точку .      case Consts.CMD_5:    # точка .
         print('5')                           print('5')                                   print('5')

 # -> 5                               # -> 5                                       # -> 5

 -----------------------------------------------------------------------------------------------------------------------

 В блоке case должен быть хоть 1 оператор:

 def connect_db(connect: dict) -> str:
     match connect:
         case {'server': host, 'login': login, 'password': psw, 'port': port}:
             pass
         case {'server': host, 'login': login, 'password': psw}:
             port = 22
         case _:  # wildcard
             return 'error connection'
     return f'connection: {host}@{login}.{psw}:{port}'

 request = {'server': '127.0.0.1', 'login': 'root', 'password': '1234'}

 result = connect_db(request)
 print(result)  # -> connection: 127.0.0.1@root.1234:22

 -----------------------------------------------------------------------------------------------------------------------
 # case _  Тоже самое  else
 # Пример простой    _ wildcard - отрабатывает всегда:

 cmd = 'bottom'                           cmd = 'top'                             cmd = 'MATCH CASE'

 match cmd:                               match cmd:                              match cmd:
     case 'bottom':                           case 'bottom':                          case 'bottom':
         print(f'Команда bottom')                 print(f'Команда bottom')                print(f'Команда bottom')
     case 'top':                              case 'top':                             case 'top':
         print(f'Команда top')                    print(f'Команда top')                   print(f'Команда top')
     case _:                                  case _:                                 case _:
         print('Неверная команда')                print('Неверная команда')               print('Неверная команда')

 # -> Команда bottom                      # -> Команда top                        # -> Неверная команда
 -----------------------------------------------------------------------------------------------------------------------

 # Пример '|' ИЛИ:

 cmd = 'top'                              cmd = 'MATCH CASE'

 match cmd:                               match cmd:
     case 'bottom' | 'top':                   case 'bottom' | 'top':
         print(f'Команда {cmd}')                  print(f'Команда {cmd}')
     case _:                                  case _:
         print('Неверная команда')                print('Неверная команда')

 # -> Команда top                         # -> Неверная команда
 -----------------------------------------------------------------------------------------------------------------------

 # Пример if...else и создание переменной:

 cmd = 'right'                                                  cmd = 'COOL'

 # Тоже самое что и if else Нельзя менять местами if else       # Создает перменную
 match cmd:                                                     match cmd:
     case 'bottom' | 'top':               # if                      case command:
         print(f'Команда {cmd}')                                        print(f'Команда {command}')
     case command:                        # else
         print(f'Команда {command}')

 # -> Команда right                                             # -> Команда COOL
 -----------------------------------------------------------------------------------------------------------------------

 # Пример Проверки типа и создание переменной:
                                                                  # Создание перменной          # Или через 'as'
 cmd = 10000                    cmd = 'STRING'                    cmd = 'NEW VARIABLE'          cmd = 'NEW VARIABLE'

 match cmd:                     match cmd:                        match cmd:                    match cmd:
     case str(cmd):                 case str(cmd):                    case str(new):                case str() as new:
         print(f'{cmd} Строка')         print(f'{cmd} Строка')            print(f'{new}')               print(f'{new}')
     case int(cmd):                 case int(cmd):                    case int(new):                case int() as new:
         print(f'{cmd} Число')          print(f'{cmd} Число')             print(f'{new}')               print(f'{new}')
     case _:                        case _:                           case _:                       case _:
         print('Другое')                print('Другое')                   print('Другое')               print('Другое')

 # ->  10000 Число              # -> STRING Строка                # ->  NEW VARIABLE            # ->  NEW VARIABLE


 # Тоже самое но с isinstance    if...elif...else

 cmd = 10000                    cmd = 'STRING'                    cmd = 'NEW VARIABLE'        cmd = 'NEW VARIABLE'

 if isinstance(cmd, str):       if isinstance(cmd, str):          if isinstance(cmd, str):    if isinstance(cmd, str):
     print(f'{cmd} Строка')         print(f'{cmd} Строка')            print(f'{cmd}')             print(f'{cmd}')
 elif isinstance(cmd, int):     elif isinstance(cmd, int):        elif isinstance(cmd, int):  elif isinstance(cmd, int):
     print(f'{cmd} Число')          print(f'{cmd} Число')             print(f'{cmd}')             print(f'{cmd}')
 else:                          else:                             else:                       else:
     print('Другое')                print('Другое')                   print('Другое')             print('Другое')

 # ->  10000 Число              # -> STRING Строка                # -> NEW VARIABLE           # -> NEW VARIABLE


 -----------------------------------------------------------------------------------------------------------------------

 # Дополнильные проверки if - guard(защитник)           # Не Прошло Проверку
 cmd = 1                                                cmd = 100000

 match cmd:                                             match cmd:
     case int() as new if 0 <= new <= 1000:                 case int() as new if 0 <= new <= 1000:    # guard(защитник)
         print(f'Число Прошло проверку {new}')                  print(f'Число Прошло проверку {new}')
     case _:                                                case _:
         print(f'Число НЕ Прошло проверку {cmd}')               print(f'Число НЕ Прошло проверку {cmd}')

 # ->  Число Прошло проверку 1                          # ->  Число НЕ Прошло проверку 100000
 -----------------------------------------------------------------------------------------------------------------------

 # Несколько проверок сразу
                                                      # Создание перменной  variables
 cmd = 1                                              cmd = 1
 match cmd:                                           match cmd:
     case int() | float() | list():                       case int() | float() | list() as variables:
         print(f'Число Прошло проверку {cmd}')                print(f'Число Прошло проверку {variables} {cmd}')
     case _:                                              case _:
         print(f'Число НЕ Прошло проверку {cmd}')             print(f'Число НЕ Прошло проверку {cmd}')

 # ->  Число Прошло проверку 1                        # ->  Число Прошло проверку 1 1

 -----------------------------------------------------------------------------------------------------------------------
 # Пример с Функцией

 def get_data(value):                                     def get_data(value):
     match value:                                             match value:
         case int(value) if value > 0:                            case int() | float() | str() as v_1:
             return value                                             return v_1
         case float(value) if -100 <= value <= 100:               case list() | tuple() as v_2:
             return value                                             return v_2
         case str(value):                                         case dict() | set() as v_3:
             return f'{value}'                                        return v_3
         case _:                                                  case _:
             return f"Другой Вариант"                                 return 'ВВедите другое'

 print(get_data(10))               # -> 10                print(get_data('hello'))          # ->  hello
 print(get_data('Hello'))          # -> Hello             print(get_data([10, 20]))         # ->  [10, 20]
 print(get_data(10.000))           # -> 10.0              print(get_data({'A': [30, 40]}))  # ->  {'A': [30, 40]}
 print(get_data([1000, 'Hello']))  # -> Другой Вариант    print(get_data(b'Hello'))         # ->  ВВедите другое

 -----------------------------------------------------------------------------------------------------------------------

 -- Работа с Списками(list) и Кортежами(tuple)                                                        <-----    <-----
 Sequence Types в match case - list, tuple, range

 cmd = ("Learning", "Python", 2000.78)  # 3 Элемента         cmd = ("Learning", "Python", 2000.78, 5, 3)  # 5 Элементов
 author, title, price = cmd   # Распаковка аналогичная ниже  author, title, price = cmd  # ValueError: too many values..
 print(author, title, price)  # -> Learning Python 2000.78   author, title, price
                                                             # ValueError: too many values to unpack (expected 3)
 # Будет работать если Кортеж содержить ровно 3 элемента!    # Кортеж содержить 5 Элементов!
 match cmd:                                                  match cmd:
     case author, title, price:               # Распаковка       case author, title, price:
         print(f'Кортеж: {author} {title} {price}')                  print(f'Кортеж: {author} {title} {price}')
     case _:  # wildcard                                         case _:  # wildcard
         print(f'Непонятный формат данных')                          print(f'Непонятный формат данных')

 # -> Кортеж: Learning Python 2000.78                        # -> Непонятный формат данных
 -----------------------------------------------------------------------------------------------------------------------

 -- Всё Работает так же как и при обычной распаковке '*'

 cmd = ["Learning", "Python", 2000.78, 5, 3, 5, 10]  # 7 Элементов Список
 author, title, price, *_ = cmd   # Так будет работать используем *    *_
 author, title, price = cmd       # -> ValueError: too many values to unpack (expected 3)
 print(author, title, price)      # -> Learning Python 2000.78

 # Список содержить 7 элементов и всё Работает!   *_    # Ограничить Размер Кортежа/Списка используем guard if
 match cmd:                                             match cmd:
     case author, title, price, *_:  #  *_                  case author, title, price, *_ if len(cmd) < 7:   # guard
         print(f'Список: {author} {title} {price}')             print(f'Список: {author} {title} {price}')
     case _:  # wildcard                                    case _:  # wildcard
         print(f'Непонятный формат данных')                     print(f'Непонятный формат данных')

 # -> Список: Learning Python 2000.78                   # -> Непонятный формат данных
 -----------------------------------------------------------------------------------------------------------------------

 -- Можно использовать группирующие скобки () или []  НЕ Создают Список ИЛИ Кортеж  Нет разница с () [] или без   <-----
 Говорит Python что будет Последовательность(Sequence) из определенного количества элементов
 Sequence Types в match case - list, tuple, range

 cmd = ("Learning", "Python", 2000.78, 5, 3, 5, 10)  # 7 Элементов Список

 # () - Просто группирующие скобки                           # [] - Просто группирующие скобки
 match cmd:                                                  match cmd:
     case (author, title, price, *_) if len(cmd) < 8: # ()       case [author, title, price, *_] if len(cmd) < 8:
         print(f'Кортеж: {author} {title} {price}')                  print(f'Кортеж: {author} {title} {price}')
     case _:  # wildcard                                         case _:  # wildcard
         print(f'Непонятный формат данных')                          print(f'Непонятный формат данных')

 # -> Кортеж: Learning Python 2000.78                        # -> Кортеж: Learning Python 2000.78
 -----------------------------------------------------------------------------------------------------------------------

 Строка(str) - Не относиться к Последовательностям/Sequences

 cmd = "Hello World"                                  cmd = ["Learning", "Python", 2000.78, 5, 3, 5, 10]  # 7 Элементов

 match cmd:                                           match cmd:
     case (author, title, price, *_):                     case (author, title, price, *_):
         print(f'Кортеж: {author} {title} {price}')           print(f'Список: {author} {title} {price}')
     case _:  # wildcard                                  case _:  # wildcard
         print(f'Непонятный формат данных')                   print(f'Непонятный формат данных')
 # -> Непонятный формат данных                        # -> Список: Learning Python 2000.78

 -----------------------------------------------------------------------------------------------------------------------

 Проверка типов данных внутри переменной и распаковка
 cmd = ("Learning", "Python", 2000.78, 5, 3, 5, 10)  # 7 Элементов Кортеж

 # Проверка прошла!                                                 # Проверка НЕ прошла 3 элемент не list!
 match cmd:                                                         match cmd:
     case [str() as author, str() as title, float() as price, *_]:      case [str(author), str(title), list(price), *_]:
         print(f'Кортеж: {author} {title} {price}')                         print(f'Кортеж: {author} {title} {price}')
     case _:  # wildcard                                                case _:  # wildcard
         print(f'Непонятный формат данных')                                 print(f'Непонятный формат данных')

 # -> Кортеж: Learning Python 2000.78                               # -> Непонятный формат данных

 # Можно Кмобинировать:  case [str() | int() as author, str() | list() as title, float() | dict() as price, *_]:
 -----------------------------------------------------------------------------------------------------------------------

 guard if Проверка типов данных внутри переменной и распаковка

 cmd = ("Learning", "Python", 2000.78, 5, 3, 5, 10)  # 7 Элементов Кортеж
 # Проверка прошла!
 match cmd:
     case [str() as author, str() as title, float() as price, *_] if len(cmd) < 8 and len(author) < 50 and len(title) < 10:
         print(f'Кортеж: {author} {title} {price}')
     case _:  # wildcard
         print(f'Непонятный формат данных')
 # -> Кортеж: Learning Python 2000.78

 -----------------------------------------------------------------------------------------------------------------------

 Несколько форматов
 cmd = ("Learning", "Python", 2000.78)                           # 3 Элемента
 cmd = [1, 10, "Learning", "Python", 2000.78, 5, 3, 5, 10, 'a']  # 10 Элементов

 # Два варианты но во втором убрали дублирование кода:   case [author, title, price] | (_, _, author, title, price, *_)
 # Имена перменных и их количество должны совпадать!!
 match cmd:                                          match cmd:
     case [author, title, price]:                        case (author, title, price) | (_, _, author, title, price, *_):
         print(f'Кортеж 1: {author} {title} {price}')        print(f'Кортеж 1: {author} {title} {price}')
     case [_, _, author, title, price, *_]:              case _:  # wildcard
         print(f'Кортеж 2: {author} {title} {price}')        print(f'Непонятный формат данных')
     case _:  # wildcard
         print(f'Непонятный формат данных')

 # -> Кортеж 2: Learning Python 2000.78              # -> Кортеж 1: Learning Python 2000.78
 -----------------------------------------------------------------------------------------------------------------------
 cmd = (1, 10, "Learning", "Python", 2000.78, 5, 3, 5, 10, 'a')  # 10 Элементов

 # Если Нужно добавить еще элемент
 match cmd:
     case [author, title, price]:
         print(f'Кортеж 1: {author} {title} {price}')
     case [_, _, author, title, price, number, *_]:
         print(f'Кортеж 2: {author} {title} {price}, {number}')  # number
     case _:  # wildcard
         print(f'Непонятный формат данных')
 # -> Кортеж 2: Learning Python 2000.78, 5      # Дополнительно вывели еще 5    <-----
 -----------------------------------------------------------------------------------------------------------------------
 Валидация последовательности в начале

 cmd = [1, 10, "Learning", "Python", 2000.78, 5, 3, 5, 10, 'a']  # 10 Элементов

 # Если Не хотим Список или Кортеж
 match cmd:
     case list() | tuple() as no_valid:  # <-----
         print(f'Список или Кортеж нельзя: {no_valid}')
     case [author, title, price]:
         print(f'Кортеж 1: {author} {title} {price}')
     case [_, _, author, title, price, number, *_]:
         print(f'Кортеж 2: {author} {title} {price}, {number}')
     case _:  # wildcard
         print(f'Непонятный формат данных')

 # -> Список или Кортеж нельзя: [1, 10, 'Learning', 'Python', 2000.78, 5, 3, 5, 10, 'a']

 -----------------------------------------------------------------------------------------------------------------------
 # Решение посмотри:

 book = [1, 'Балакирев С.М.', 'Python', 2100.0, 2023]                                           # YES
 book = [2, 'Зингаро. Д', 'Python без проблем', 1000.0, 2019]                                   # NO
 book = [1, 'Балакирев С.М.', 'Python', 0]                                                      # NO
 book = [4]                                                                                     # NO
 book = [5, 'Яв', 'Python. Лучшие практики и инструменты', 1500.1, 2021]                        # YES
 book = [5, 'Яв', 'Python. Лучшие практики и инструменты']                                      # NO
 book = [5, 'Яворски Михаил', 'Python. Лучшие практики и инструменты']                          # YES

 match book:
     case [_, str(f1), str(f2)] if len(f1) >= 6 and len(f2) >= 10:             # использую  str(f1)
         print('Yes')
     case (_, str(f1), str(f2), float(f3)) if len(f1) >= 6 and f3 > 0:         # использую  str(f1), float(f3)
         print('Yes')
     case (_, str() as f1, str() as f2, int() as f3) if f3 > 2020:             # использую  str() as f1,  int() as f3
         print('Yes')
     case _, str() as f1, str() as f2, float() as f3, int() as f4 if f3 > 0 and f4 > 2020:
         print('Yes')
     case _:
         print('No')

 # Создает переменные можно посмотреть их и использовать  Только которые прошли проверки
 print(f2)  # -> Python. Лучшие практики и инструменты


 # Придумал вместе с регулярками  Тоже самое что и выше!!!                        <-----               <-----

 match book:
     case int(_), str() as author, str() as title if re.search(r'\w{6,}', author) and re.search(r'\w{10,}', title):
         print('Yes')
     case int(_), str(author), str(title), float(price) if re.search(r'\w{6,}', author) and re.match(r'[1-9]', str(price)):
         print('Yes')
     case int(_), str() as author, str() as title, int() as year if re.match(r'202[0-9]+', str(year)):
         print('Yes')
     case int(_), str(author), str(title), float(price), int(year) if re.match(r'[1-9]', str(price)) and re.match(r'202[0-9]+', str(year)):
         print('Yes')
     case _:
         print('No')
 -----------------------------------------------------------------------------------------------------------------------

 -- Работа с Словарями(dict) и Множествами(set)                                                       <-----    <-----
 Sequence Types в match case - list, tuple, range


 -- Словарь(dict)     если прописываем в match case {} - значит мы работает со словарем(dict)
 -----------------------------------------------------------------------------------------------------------------------

 request = {'url': 'https://www.python.org/', 'method': 'GET', 'timeout': 1000}

 # Отрабатывает если на вход поступает словарь
 match request:
     case {'url': str() as url, 'method': str(method)}:  # url если записываем переменную, то значение может быть любое
         print(f'Запрос: url: {url}, method: {method}')
     case _:  # wildcard
         print('Неверный запрос')

 # -> Запрос: url: https://www.python.org/, method: GET
 -----------------------------------------------------------------------------------------------------------------------

 request = {'url': 'https://www.python.org/', 'method': 'GET', 'timeout': 100}

 # Если значение НЕ переменная, то отработает только если указали ТОЧНОЕ ЗНАЧЕНИЕ
 match request:
     case {'url': str() as url, 'method': str(method), 'timeout': 1000}:   # 'timeout' должен быть 100 как и в request
         print(f'Запрос: url: {url}, method: {method}')
     case _:  # wildcard
         print('Неверный запрос')

 # -> Неверный запрос

 Можно использовать ИЛИ  |
 case {'url': str() as url, 'method': str(method), 'timeout': 1000 | 2000 | 3000 | 40}:                         <-----
 Шаблоны можно записывать тоже через ИЛИ  |   Но только с ОДИНАКОВЫМИ  ПЕРЕМЕННЫМИ остальное может быть любое
 case {'url': str() as url, 'method': str(method), 'timeout': 1000} | {'NO': float() as url, 'GOOD': method}:   <-----
 Так же работает    guard(защитник)    Можно использовать все конструкции которые учили ранее
 case {'url': str() as url, 'method': str(method), 'timeout': 1000} if len(request) <= 3:                       <-----
 -----------------------------------------------------------------------------------------------------------------------

 Распакова в словаре **

 request = {'url': 'https://www.python.org/', 'method': 'GET', 'timeout': 1000, 'a': 10, 'b': 20}

 # Можем посмотреть другие ключи: значения   **kwards
 match request:
     case {'url': str() as url, 'method': str(method), **kwards}:
         print(f'Запрос: url: {url}, method: {method}, {kwards}')
     case _:  # wildcard
         print('Неверный запрос')

 # -> Запрос: url: https://www.python.org/, method: GET, {'timeout': 1000, 'a': 10, 'b': 20}

 -----------------------------------------------------------------------------------------------------------------------

 # Дополнительно может быть не более 2-х ключей  используем оператор упаковки **
 match request:
     # case {'url': str() as url, 'method': str(method), **kwards} if len(kwards) <= 2:  # Можно делать разные проверки
     case {'url': str() as url, 'method': str(method), **kwards} if not kwards:      # Можно делать разные проверки
         print(f'Запрос: url: {url}, method: {method}, {kwards}')
     case _:  # wildcard
         print('Неверный запрос')

 # -> Неверный запрос

 -----------------------------------------------------------------------------------------------------------------------
 Валидация данных!

 json_data = {'id': 2, 'type': 'list', 'data': [1, 2, 3], 'access': True, 'date': '14.06.2024'}

 # Проверяет конкретное значение и выводит данные
 match json_data:
     case {'type': 'list', 'data': list() as lst, **kwards}:      # Сработает если 'type'=='list' и 'data'==list
         print(f'JSON-данные: type-list: {lst}')
     case _:  # wildcard
         print('Неверный запрос')

 # -> JSON-данные: type-list: [1, 2, 3]

 -----------------------------------------------------------------------------------------------------------------------
 Более сложная Валидация данных!
 json_data = {'id': 2, 'access': True, 'info': ['14.06.2024', {'login': '123', 'email': 'email@m.ru'}, True, 1000]}

 # Найти в других коллекциях нужные данные
 match json_data:                                                   # Отработает если Список будет содержать 4 элемента
     case {'access': access, 'info': [_, {'email': email}, _, _]}:  # При распаковке нужно указывать все перменные _, _,
         print(f'JSON: access: {access}, email: {email}')           # или используем *_    <-----    <-----
     case _:  # wildcard
         print('Неверный запрос')

 # -> JSON: access: True, email: email@m.ru

 -----------------------------------------------------------------------------------------------------------------------
 # Решение посмотри:
 def parse_json(data):
     match data:
         case {'access': bool() as access, 'data': list([date, *_])}:
             return access, date
     return None

 json_data = {'id': 2, 'access': False, 'data': ['26.05.2023', {'login': '1234', 'email': 'xxx@mail.com'}, 2000, 56.4]}
 print(parse_json(json_data))  # -> (False, '26.05.2023')
 -----------------------------------------------------------------------------------------------------------------------

 # Другое Решение посмотри:
 def parse_json(data):
     match data:
         case {'access': access, 'data': [_, {'login': login, 'email': email}, *_]} if access:
             return login, email

 json_data = {'id': 2, 'access': True, 'data': ['26.05.2023', {'login': '1234', 'email': 'xxx@mail.com'}, 2000, 56.4]}

 print(parse_json(json_data))  # -> ('1234', 'xxx@mail.com')
 -----------------------------------------------------------------------------------------------------------------------


 -- Множество(set)

 primary_keys = {1, 2, 3}

 # Для работы с Множеством(set)  делаем проверку на set и дальше работаем
 match primary_keys:
     case set() as keys if len(keys) == 3:  # Проверили на множество(set) и длина множество(set) == 3
         print(f'Primary Keys: {keys}')
     case _:  # wildcard
         print('Неверный запрос')

 # -> Primary Keys: {1, 2, 3}

 -----------------------------------------------------------------------------------------------------------------------
 Общий пример работы!

 # Шаблоны обрабатывают словари иначе чем кортежи и списки
 def book1_to_tuple(data: dict | tuple | list, min_year=1800, max_year=3000) -> tuple | None:
     price = None
     match data:
         case [book, title, int() as year] if min_year < year < max_year:
             pass
         case (book, title, int() as year, price, *_) if min_year < year < max_year:
             pass
         case {'book': book, 'title': title, 'year': year, 'price': price}:  # Сначала больше проверок в dict (Частный)
             pass
         case {'book': book, 'title': title, 'year': year}:                  # Общий шаблон Должен идти после Частного
             pass
         case _:  # wildcard
             return None
     if not (min_year < year < max_year):
         return None
     return book, title, year, price


 book_1 = ('BOOK', 'Python', 2024)
 book_2 = ['BOOK', 'Python OOP', 3024, 3000]
 book_3 = {'book': 'Pyton', 'title': 'Нейросети', 'year': 2024}
 book_4 = {'book': 'Pyton', 'title': 'Keras + Tensorflow', 'price': 5430, 'year': 2024}

 print(book1_to_tuple(book_1))  # -> ('BOOK', 'Python', 2024, None)
 print(book1_to_tuple(book_2))  # -> None
 print(book1_to_tuple(book_3))  # -> ('Pyton', 'Нейросети', 2024, None)
 print(book1_to_tuple(book_4))  # -> ('Pyton', 'Keras + Tensorflow', 2024, 5430)

 -----------------------------------------------------------------------------------------------------------------------

 --- Битовые операции ---

 Проверка на включенность (1): if flags & mask == mask: # Бит включен (1)
 Выключение бита:              flags & ~mask
 Включение бита:               flags | mask
 Переключение бита:            flags ^ mask
 Инверсия бит:                 ~number == -number - 1
 Смещение бит вправо:          number >> 1 == number // (2 ** 1)
 Смещение бит влево:           number << 1 == number * (2 ** 1)


 Приоритеты             Полная форма   Краткая форма
 1) ИЛИ                  a = a | b     a |= b
 1) ИЛИ(XOR)             a = a & b     a &= b
 2) И                    a = a ^ b     a ^= b
 3) НЕ                   ~a

 >> Смещение бит вправо  a = a >> b    a >>= b  Делит    / Исходное число на выбранное
 << Смещение бит влево   a = a << b    a <<= b  Умножает * Исходное число на выбранное
 >>  <<  Работают быстрее чем обычные операторы / *

 # Битовая операция НЕ ~    1 операнд     ~ Тильда инверсия бит
 a = 121
 print(bin(a))  # -> 0b1111001  Старший Бит Это первый 0   Если он равен 0 число Положительное  -1 число Отрицательное
 print(~a)      # -> -122
 d = 0
 print(~d)      # -> -1
 d = -10
 print(~d)      # -> 9


 # Битовая операция И &     2 операнда    & Амперсанд
 flags = 5                                  flags = 1
 mask = 4                                   mask = 4
 res = flags & mask                         res = flags & mask
 print(res)     # -> 4                      print(res)     # -> 4
 if flags & mask == mask:                   if flags & mask == mask:
     print('Включен 2-й бит числа')             print('Включен 2-й бит числа')
 else:                                      else:
     print('2-й бит Выключен')                  print('2-й бит Выключен')
 # -> Включен 2-й бит числа                 # -> 2-й бит Выключен

 flags = 13
 mask = 5
 flags = flags & ~mask  # Выключение определенных Битов
 print(flags)  # -> 8

 # Битовая операция ИЛИ |     2 операнда    | Вертикальная черта
 flags = 8
 mask = 5
 flags = flags | mask  # Включение отдельных Битов переменной
 flags |= mask         # Тоже самое
 print(flags)  # -> 13

 # Битовая операция XOR Исключающее ИЛИ |     2 операнда    | Вертикальная черта
 # Шифрование так работает в Zip  Пароль mask
 flags = 9
 mask = 1
 flags = flags ^ mask
 print(flags)  # -> 8
 flags ^= mask         # Тоже самое
 print(flags)  # -> 9  # Работает без потерь возвращает Изначальное значение flags

 # Работают быстрее чем обычные операторы / *
 # >> Смещение бит вправо
 # << Смещение бит влево

 # Делит    / Исходное число на выбранное
 # Умножает * Исходное число на выбранное
 x = 160
 print(bin(x))  # -> 0b10100000
 x = x >> 1     # -> Делит / на 2   2*2
 print(x)       # -> 80
 print(bin(x))  # -> 0b1010000  # На 0 меньше
 x = x >> 2     # -> Делит / на 4
 print(x)       # -> 20

 x = 160
 x = x << 2     # -> Умножает * 4
 print(x)       # -> 640

 # Задачи
 a = 100
 print(a | (1 << 3))  # -> 108   Включить третий бит

 -----------------------------------------------------------------------------------------------------------------------



 --- OOP ---

 -----------------------------------------------------------------------------------------------------------------------

 -- Атрибуты класса --

 class Person:
     name = 'Ivan'
     age = 30

 print(Person.__dict__)                #  Словарь всех атрибутов класса
 print(getattr(Person, 'x', 100))      # -> 100    Получить атрибут без ошибки
 print(getattr(Person, 'Ivan', 200))   # -> 200    Получить атрибут без ошибки
 print(Person.name)                    # -> Ivan   Через . точку обращение

 print(hasattr(Person, 'name'))        # -> True   Проверка атрибута

 Person.name = 'Misha'                 #           Присвоение атрибута
 Person.x = 10                         #           Создание атрибута которого не было через точку .
 print(setattr(Person, 'x', 1000))     #           Присвоение атрибута
 print(setattr(Person, 'y', 50))       #           Создание атрибута которого не было

 del Person.x                          #           Удаление атрибута через точку .
 # del Person.x    # AttributeError:.. #           Нельзя Удалить атрибут которого нет
 print(delattr(Person, 'y'))           #           Удаление атрибута

 -----------------------------------------------------------------------------------------------------------------------
 # Создание атрибутов на основе Списка кортежей
 class Empty:
     pass

 my_list = [
     ('apple', 23),
     ('banana', 80),
 ]
                                                                    # Альтернатива
 for i in my_list:                                                  for attr, val in my_list:
     # setattr(Empty, i[0], i[1])                                       setattr(Empty, attr, val)
     setattr(Empty, *i)              # Можно и так распаковать

 # [setattr(Empty, *i) for i in my_list]  # Тоже работает

 # В классе появились атрибуты
 print([i for i in Empty.__dict__.items() if not i[0].endswith('__')])  # -> [('apple', 23), ('banana', 80)]

 -----------------------------------------------------------------------------------------------------------------------


 -- Атрибуты Экземпляра класса  --

 # Работает как поиск LEGB пространство имен

 class Person:
     name = 'Ivan'
     age = 30

 man = Person()                #              # Создаём ЭК и связываем его с переменной man
 print(man.age)                # ->  30       # Получаем текущее значение атрибута age в ЭК man
 man.money = 100               #              # Создаём в ЭК атрибут money со значением 100
 print(man.money)              # ->  100      # Получаем текущее значение атрибута money в ЭК man
 man.money = 250               #              # Изменяем текущее значение атрибута money в ЭК man на 250
 print(man.money)              # ->  250      # Получаем текущее значение атрибута money в ЭК man
 delattr(man, 'money')         #              # Удаляем атрибут money из ЭК
 print(hasattr(man, 'money'))  # ->  False    # Проверяем наличие атрибута money в ЭК man: False

 # атрибуты не создаются в самом ЭК, а получают ссылку на атрибут класса.
 print(man.__dict__)           # -> {}
 print(Person.__dict__)        # -> {'__module__': '__main__', 'name': 'Ivan', 'age': 30, '__dict__': <attribute....

 # Но в случае изменения атрибута из-под ЭК, данный атрибут со своим значением отразится в словаре атрибутов
 print(man.__dict__)           # -> {}
 man.name = 'Alex'
 print(man.__dict__)           # {'name': 'Alex'}

 # Изменения не затронут сам класс, так как изменение значения проводилось из-под ЭК
 print('Атрибуты класса:', Person.__dict__)   # -> Атрибуты класса: {'__module__': '__main__', 'name': 'Ivan',...
 print('Атрибуты ЭК man:', man.__dict__)      # -> Атрибуты ЭК man: {'name': 'Alex'}

 # Атрибуты двух ЭК независимы друг от друга
 dude = Person()
 print('Атрибуты ЭК dude:', dude.__dict__)    # -> Атрибуты ЭК dude: {}
 dude.name = 'Sergey'
 print('Атрибуты ЭК dude:', dude.__dict__)    # -> Атрибуты ЭК dude: {'name': 'Sergey'}
 print('Атрибуты ЭК man:', man.__dict__)      # -> Атрибуты ЭК man: {'name': 'Alex'}

 # При удалении атрибута с одинаковыми именами и разными значениями. ЭК будет выводиться аргумент из самого класса:
 print(Person.name, man.name)                 # -> Ivan Alex
 del man.name
 print(Person.name, man.name)                 # -> Ivan Ivan
 -----------------------------------------------------------------------------------------------------------------------

 # Пример создания атрибутов из функции:
 def _clear() -> None: ...
 def _clear() -> None: pass

 # pass - это просто заглушка
 # ...  - это просто Другая заглушка  ... - объект Ellipsis


 class Config: ...

 def create_instance(n: int) -> Config:
     obj = Config()
     obj.__dict__ = {f'attribute{i}': f'value{i}' for i in range(1, n + 1)}
     return obj

 # Тоже самое
 class Config:
    pass

 def create_instance(num):
     obj = Config()
     for i in range(1,num+1):
         obj.__dict__[f'attribute{str(i)}'] = f'value{str(i)}'
     return obj

 # Ниже расположены проверки для функции create_instance

 config_2 = create_instance(2)
 assert isinstance(config_2, Config)
 assert config_2.__dict__ == {'attribute1': 'value1', 'attribute2': 'value2'}

 -----------------------------------------------------------------------------------------------------------------------

 -- Методы экземпляра. Аргумент self --

 Метод — функция, которая определена внутри класса
 1) Метод связан с ЭК и вызывается от него.
 2) При вызове метода первым параметром будет передан тот ЭК, от которого метод был вызван.  self


  --- Compare with Clipboard   PyCharm  Как сравнить текст или файл ---
 Ctrl + C или Ctrl + Х   и выделяем другой текст  и нажимаем ЛКМ и выбираем Compare with Clipboard
 Можно сравнивать и файлы.  Текст должен быть в тройных кавычках


 # Примеры

 # Установка атрибута экземпляра


# Явное лучше НЕявного
class Robot:                                              class Robot:
    name = None

    def set_name(self, name):                                 def set_name(self, name):
        self.name = name                                          setattr(self, 'name', name)

    def say_hello(self):                                      def say_hello(self):
        if self.name:                                             if hasattr(self, 'name'):
            print(f'Hello, human! My name is {self.name}')            print(f'Hello, human! My name is {self.name}')
        else:                                                     else:
            print('У робота нет имени')                               print(f'У робота нет имени')

 class Robot:
     def set_name(self, name):
         self.name = name

     def say_hello(self):
         try:
             if self.name:
                 print(f'Hello, human! My name is {self.name}')
         except:
             print(f'У робота нет имени')

 c3po = Robot()
 c3po.say_hello()
 c3po.set_name('R2D2')
 c3po.say_hello()

 # Еще один пример Установки значений

 class Constructor:                          class Constructor:
     def add_atribute(self, name, value):        def add_atribute(self, name, value):
         self.__dict__[name] = value                 setattr(self, name, value)

     def display(self):                          def display(self):
         print(self.__dict__)                        print(self.__dict__)

 # Проверка на экземпляр класса
 class Point:                           class Point:                            class Point:

     def set_coordinates(self, x, y):       def set_coordinates(self, x, y):        def set_coordinates(self, x, y):
         self.x = x                             self.x = x                              self.x = x
         self.y = y                             self.y = y                              self.y = y

     def get_distance(self, obj):           def get_distance(self, obj):            def get_distance(self, obj):
         if isinstance(obj, Point):             if hasattr(obj, 'x' and 'y'):           try:
             return self.x, self.y                  return self.x, self.y                   return self.x, self.y
         else:                                  else:                                   except:
             print("Неверно")                       print("Неверно")                        print("Неверно")

 # match case
    def get_distance(self, obj):             def get_distance(self, obj):
        match obj:                               match obj:
            case Point():                            case Point() as my_obj:
                return self.x, self.y                    return self.x, self.y
            case _:                                  case _:
                print("Неверно")                         print("Неверно")

 -----------------------------------------------------------------------------------------------------------------------


 # Примеры  __init__


 class Person:                      class Person:
     def __init__(self, name, age):     def __init__(self, name, age):
         self.name = name                   self.name = name
         self.age = age                     self.age = age
                                            self.greet = lambda: f'Hi, my name is {self.name},I am {self.age} years old'
     def greet(self):
         return f"Hello, my name is {self.name}, and I am {self.age} years old"

 -----------------------------------------------------------------------------------------------------------------------

 # Примеры **kwargs  в __init__   Результат одинаковый   Посмотри третий пример **kwargs и kwargs без **      <-----

class CustomLabel:                       class CustomLabel:                         class CustomLabel:

    def __init__(self, text, **kwargs):      def __init__(self, text:str, **kwargs):    def __init__(self, text, **kwargs):
        self.text = text                         self.text = text                           self.text = text
        for key, value in kwargs.items():        self.config(**kwargs)                      self.__dict__.update(kwargs)
            self.__dict__[key] = value                                                      self.__dict__.update(**kwargs)

    def config(self, **kwargs):             def config(self, **kwargs):                 def config(self, **kwargs):
        for key, value in kwargs.items():       for key, value in kwargs.items():           self.__dict__.update(kwargs)
            self.__dict__[key] = value              setattr(self, key, value)               self.__dict__.update(**kwargs)


 # Присмотрись к решению      Последний класс посмотри     class Employee       <-----             <-----
 class Person:

     def __init__(self, name, age):
         self.name = name
         self.age = age

     def display_person_info(self):
         print(f"Person: {self.name}, {self.age}")

 class Company:

     def __init__(self, company_name, location):
         self.company_name = company_name
         self.location = location

     def display_company_info(self):
         print(f"Company: {self.company_name}, {self.location}")

 class Employee:
     def __init__(self, name, age, company_name, location):
         self.personal_data = Person(name, age)
         self.work = Company(company_name, location)

 emp = Employee('Jessica', 28, 'Google', 'Atlanta')
 print(emp.personal_data.name)                       # -> Jessica
 print(emp.personal_data.age)                        # -> 28
 emp.personal_data.display_person_info()             # -> Person: Jessica, 28
 print(emp.work.company_name)                        # -> Google
 print(emp.work.location)                            # -> Atlanta
 emp.work.display_company_info()                     # -> Company: Google, Atlanta

 -----------------------------------------------------------------------------------------------------------------------




 -----------------------------------------------------------------------------------------------------------------------




 -----------------------------------------------------------------------------------------------------------------------





 -----------------------------------------------------------------------------------------------------------------------

________________________________________________________________________________________________________________________















"""