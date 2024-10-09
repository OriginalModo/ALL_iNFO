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


--- Модуль pandas, анализ данных в Python ---


 -- Hadoop   Spark --
 Выполняют операции MapReduce
 MapReduce Техника
 В модели программирования MapReduce большой набор данных сначала разбивается на меньшие части.
 После того как все задачи для всех поднаборов решены, мы может объединить результаты.

 MapReduce — это модель обработки больших данных, состоящая из двух этапов:

 1. **Map**: Разделение данных на пары ключ-значение и их предварительная обработка.
 2. **Reduce**: Агрегация промежуточных результатов по ключам для получения финальных результатов.

 Применяется для параллельной обработки и анализа данных


 ЭКСТРАПОЛЯЦИЯ и ИНТЕРПОЛЯЦИЯ — это методы прогнозирования и оценки значений функций или данных.

 1. **Интерполяция** - это процесс оценки значений функции на основе известных данных в пределах заданного диапазона.
 Например, если у вас есть набор точек, интерполяция позволяет определить значения между этими точками.

 2. **Экстраполяция** - это метод предсказания значений функции за пределами известных данных. Это более рискованная
 операция, так как предполагает, что тенденции, наблюдаемые в имеющихся данных, будут продолжаться и за их пределами.

 В итоге, ИНТЕРПОЛЯЦИЯ работает внутри диапазона данных, а ЭКСТРАПОЛЯЦИЯ — за его пределами.


 Kaggle - это международная платформа, на которой проводятся соревнования по анализу данных.

 Разработка модели машинного обучения строится из стандартных этапов, я их кратко опишу ниже.

 0. Сбор данных и оценка их качества в свете требований к модели.

 1. Предобработка данных: удаление дубликатов и пропусков; преобразование категориальных переменных в числовые (One-Hot
 Encoding, Label Encoding); нормализация числовых переменных; в Вашем случае – добавление/интерполяция данных для дат,
 когда данные отсутствуют.

 2. Разделение данных на обучающую, валидационную и тестовую выборки (например, 70%/15%/15%).

 3. Исследование тенденций в данных (в Вашем случае, например, есть ли сезонность продаж и др.). Это влияет на то,
  что в разработку модели добавляются дополнительные признаки (features): дни недели, месяцы, годы,
  лаги — это некоторые предыдущие значения временного ряда.

 4. Выбор модели, в Вашем случае для задачи регрессии (например, линейная регрессия, случайный лес, градиентный бустинг).

 5. Обучение модели на обучающей выборке, используя выбранные алгоритмы и параметры.

 6. Валидация модели на валидационной выборке, используя метрики, такие как MSE (среднеквадратичная ошибка) или MAE (средняя
 абсолютная ошибка).

 7. Тюнинг модели – настройка гипер-параметров модели для улучшения качества предсказания.

 8. Тестирование модели на тестовой выборке для финальной оценки качества модели.

 9. Деплой модели в продакшн-среде для использования в реальных условиях



 DataSet обычно представляет собой файл с таблицей в формате JSON или CSV.
 Dataset – это обработанная и структурированная информация в табличном виде.

 SciPy — это библиотека для языка Python, построена поверх NumPy, но для более глубоких и сложных научных вычислений
 Matplotlib – это библиотека для визуализации данных на Python.  - для создания графиков и диаграмм
 Seaborn - это библиотека для визуализации данных на Python. Построена поверх Matplotlib - для создания статистических графиков

 Библиотека Pandas построена на базе NumPy.
 Numeric Python (NumPy) - Она ускоряет работу с многомерными массивами и матрицами, а также позволяет вычислять
 много высокоуровневых математических функций при работе с массивами данных.

 matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]            # -> Матрица через списки(list) в Python

 import numpy as np
 matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])  # -> Матрица через numpy

  Две основные структуры данных, pandas.Series (1-мерная) и pandas.DataFrame (2-мерная)

 pandas.DataFrame - двумерный массив.  представляет собой двумерную помеченную структуру данных со столбцами
 потенциально разных типов.
 pandas.Series - одномерный массив.    это одномерный помеченный массив, способный хранить данные любого типа
 Каждый pandas.DataFrame и pandas.Series имеют индекс pandas.Index, который представляет собой метки строк данных.

 Series представляет один столбец DataFrame

 import pandas as pd

 df_filtered = df[df['column'] == 'condition']

 # только на больших ДФ .query() работает медленнее.
 df_filtered = df.query('column == "condition"')

# Предположим, что game_events — это ваш DataFrame
 game_events = pd.read_csv('путь_к_вашему_файлу.csv')  # Загрузите данные, если это необходимо

 Разные функции pandas              # Так тоже можно
 game_events['revenue'].count()     game_events.revenue.count()
 game_events['revenue'].sum()       game_events.revenue.sum()
 game_events['revenue'].mean()      game_events.revenue.mean()
 game_events['revenue'].max()       game_events.revenue.max()
 game_events['revenue'].min()       game_events.revenue.min()
 game_events['revenue'].median()    game_events.revenue.median()

 # Получить столбец
 df['type']
 game_events['type']

 # Только уникальные
 game_events['user_id'].unique()   #  ['7f0344f8' '00aa49ac' 'f5ef9841' '13d17d67']  сами уникальные элементы
 game_events['user_id'].nunique()  #  4                                              количество уникальных элементов

 # Фильтрация
 count_events = game_events[game_events['user_id'] == 'f5ef9841']['event_name'].count()

 # Тоже самое но SQL
 SELECT COUNT(event_name) AS count_events
 FROM game_events
 WHERE user_id = 'f5ef9841'


 # Фильтрация с датой
 count_events = game_events[game_events['event_date'] == '2021-01-15']['event_name'].count()

 # Выберите только те строки, где внутриигровые покупки пользователей больше или равны числу 7.49.
 game_events[game_events['revenue'] >= 7.49]

  # Получение/извлечение значений Series/DataFrame

 DataFrame.loc[]    - доступ к срезу данных DataFrame по индексным меткам;
 Series.loc[]       - доступ к срезу данных Series по индексным меткам;
 DataFrame.iloc[]   - доступ к срезу данных DataFrame по позиции;          # целочисленная индексация
 Series.iloc[]      - доступ к срезу данных Series по позиции;             # целочисленная индексация

 df = pd.DataFrame([[1, 2], [4, 5], [7, 8]],
 index=['cobra', 'viper', 'sidewinder'],
 columns=['max_speed', 'shield'])

 print(df) # Вывод ниже

 #             max_speed  shield
 # cobra               1       2
 # viper               4       5
 # sidewinder          7       8

 # Одно значение loc[]                      # Несколько значений loc[[]]
 print(df.loc['cobra']) # Вывод ниже        print(df.loc[['cobra', 'viper']])

 # max_speed    1                           #        max_speed  shield
 # shield       2                           # cobra          1       2
 # Name: cobra, dtype: int64                # viper          4       5

 # Интересные примеры loc
 df.loc[df['shield'] > 6]
 df.loc[df['shield'] > 6, ['max_speed']]
 df.loc[lambda df: df['shield'] == 8]
 df.loc['cobra':'viper', 'max_speed']
 df.loc[['viper', 'sidewinder'], ['shield']] = 50
 df.loc[(df['max_speed'] > 1) & (df['shield'] < 8)]
 df.loc[(df['max_speed'] > 4) | (df['shield'] < 5)]
 df.loc['cobra'] = 10

 # iloc
 df = pd.DataFrame([[1, 2], [4, 5], [7, 8]],
 columns=['max_speed', 'shield'])


 # Одно значение iloc[]                     # Несколько значений iloc[[]]
 print(df.iloc[1])                          print(df.iloc[[1, 2]])

 # max_speed    4                           #    max_speed  shield
 # shield       5                           # 1          4       5
 # Name: 1, dtype: int64                    # 2          7       8

 # Интересные примеры iloc
 df.iloc[[True, False, True]]
 df.iloc[lambda x: x.index % 2 == 0]
 df.iloc[:3]                            # что в отличие от обычных срезов python, включены как начало, так и конец.


 # Применить функцию с столбцу                                                              <-----
 df = pd.DataFrame({'hehe': ['Y', 'N']})

 print(df)  # Вывод ниже

 #   hehe
 # 0    Y
 # 1    N


 def split_it(year):
     return re.findall('Y', year)
                                                  # Тоже самое с lambda
 df['hehe'] = df['hehe'].apply(split_it)          df['hehe'] = df['hehe'].apply(lambda x: x.re.findall('Y', year))

 print(df) # Вывод ниже

 #   hehe
 # 0  [Y]
 # 1   []


 # Чтобы применить функцию только к одному столбцу:                                    <-----  Важно

 df = pd.DataFrame({'hehe': ['Y Yes', 'N No']})

 def get_first_word(s):
     return s.split(maxsplit=1)[0]

 df['first'] = df['hehe'].apply(get_first_word)

 print(df) # Вывод ниже

 #     hehe first
 # 0  Y Yes     Y
 # 1   N No     N


 # Еще вариант   Также можно воспользоваться готовыми векторизированными Pandas методами:
 df['hehe'].str.split(n=1).str[0]               # Тоже самое
 df['hehe'].str.extract(r'(Y)', expand=False)   # Тоже самое


 # Иногда при работе со строковыми данными list comprehension оказывается быстрее встроенных векторизированных функций.

 df['first'] = [n.split(maxsplit=1)[0] for n in df['hehe']]


 # Интересный пример

 def find_products(products: pd.DataFrame) -> pd.DataFrame:
     df = products
     pattern = r'Y'
     filtered_df = df[(df['low_fats'].str.contains(pattern)) & \
     (df['recyclable'].str.contains(pattern))
     ]
     return filtered_df[['product_id']]


 -- Регулярки в Pandas     Использование регулярных выражений в Pandas --

 Метод Series.str.count()     - подсчитывает вхождения шаблона в строке;
 Метод Series.str.replace()   - заменит каждое вхождение шаблона регулярного выражения;
 Метод Series.str.contains()  - проверяет, содержится ли регулярное выражение в каждой строке;
 Метод Series.str.extract()   - извлекает группы захвата из шаблона регулярного выражения;
 Метод Series.str.findall()   - найдет все вхождения регулярного выражения;
 Метод Series.str.match()     - определяет, начинается ли каждая строка с совпадения с регулярным выражением;
 Метод Series.str.split()     - разбивает строки по заданному разделителю;
 Метод Series.str.rsplit()    - разбивает строки по заданному разделителю начиная справа.


 # ! Абстрактный код
 # новая переменная
 sorted_df = df.sort_values("col1")
 # перезапись исходного `DataFrame`
 df = df.sort_values("col1")

 -- Операция SQL SELECT --

 tips = pd.read_csv(url)

 SELECT total_bill, tip, smoker, time FROM tips;       tips[["total_bill", "tip", "smoker", "time"]]

 # Вызов DataFrame без списка имен столбцов отобразит все столбцы (аналогично * в SQL).
 SELECT * FROM tips;                                   df

 # В SQL можно добавить вычисляемый столбец:
 SELECT *, tip/total_bill as tip_rate FROM tips;       tips.assign(tip_rate=tips["tip"] / tips["total_bill"])


 -- Операция SQL WHERE --

 SELECT * FROM tips WHERE time = 'Dinner';                  tips['time' == 'Dinner']
 SELECT * FROM tips WHERE time = 'Dinner' AND tip > 5.00;   tips[(tips['time'] == 'Dinner') & (tips['tip'] > 5.00)]
 SELECT * FROM tips WHERE size >= 5 OR total_bill > 45;     tips[(tips['size'] >= 5) | (tips['total_bill'] > 45)]

 SELECT * FROM tips WHERE 'day'  IN ('Sun', 'Sat') and sex='Female'
 # Pandas
 tips[(tips['day'].isin(['Sun', 'Sat'])) & (tips['sex'] == 'Female')]


 frame = pd.DataFrame(
    {"col1": ["A", "B", np.nan, "C", "D"], "col2": ["F", np.nan, "G", "H", "I"]}
 )

 # Проверка NULL выполняется с помощью методов .notna() и .isna().
 SELECT * FROM frame WHERE col2 IS NULL;                    frame[frame['col2'].isna()]
 SELECT * FROM frame WHERE col1 IS NOT NULL;                frame[frame['col2'].notna()]


 -- Операция SQL GROUP BY --

 SELECT sex, count(*) FROM tips GROUP BY sex;               tips.groupby("sex").size()
                                                            tips.groupby("sex")["total_bill"].count() # Альтернатива

 Обратите внимание, что в коде с pandas используется .size(), а не .count(). Это связано с тем, что метод .count()
 применяет функцию к КАЖДОМУ столбцу, возвращая количество записей NOT NULL в КАЖДОМ столбце.

 tips.groupby("sex").count()

 SELECT day, AVG(tip), COUNT(*) FROM tips GROUP BY day;     tips.groupby('day').agg({'tip': 'mean', 'day': 'size'})


 SELECT smoker, day, COUNT(*), AVG(tip) FROM tips GROUP BY smoker, day;

 # Pandas
 tips.groupby(["smoker", "day"]).agg({"tip": ["size", "mean"]})


 # Пример JOIN в pandas   pandas.DataFrame.join
 DataFrame.join(other, on=None, how='left', lsuffix='', rsuffix='', sort=False, validate=None)

 df.join(other, lsuffix='_caller', rsuffix='_other')
 df.set_index('key').join(other.set_index('key'))
 df.join(other.set_index('key'), on='key')
 df.join(other.set_index('key'), on='key', validate='m:1')


 # Пример JOINs в pandas   pandas.DataFrame.merge

 DataFrame.merge(right, how='inner', on=None, left_on=None, right_on=None, left_index=False, right_index=False,
                 sort=False, suffixes=('_x', '_y'), copy=None, indicator=False, validate=None)

 # Примеры!!!
 df1 = pd.DataFrame({'lkey': ['foo', 'bar', 'baz', 'foo'],
                    'value': [1, 2, 3, 5]})
 df2 = pd.DataFrame({'rkey': ['foo', 'bar', 'baz', 'foo'],
                    'value': [5, 6, 7, 8]})

 # Объединить df1 и df2 в столбцах lkey и rkey. Столбцы значений имеют суффиксы по умолчанию, _x и _y, добавленные.

 df1.merge(df2, left_on='lkey', right_on='rkey')

 # Объединить фреймы данных df1 и df2 с указанными левыми и правыми суффиксами, добавленными ко всем перекрывающимся столбцам.

 df1.merge(df2, left_on='lkey', right_on='rkey', suffixes=('_left', '_right'))

 # Объединить DataFrames df1 и df2, но вызвать исключение, если DataFrames имеют перекрывающиеся столбцы.

 df1.merge(df2, left_on='lkey', right_on='rkey', suffixes=(False, False))



 df1 = pd.DataFrame({'a': ['foo', 'bar'], 'b': [1, 2]})
 df2 = pd.DataFrame({'a': ['foo', 'baz'], 'c': [3, 4]})

 df1.merge(df2, how='inner', on='a')
 df1.merge(df2, how='left', on='a')
 df1.merge(df2, how='cross')



   --- Pandas vs SQL ---

 # Таблицы
 df1 = pd.DataFrame({"key": ["A", "B", "C", "D"], "value": np.random.randn(4)})
 df2 = pd.DataFrame({"key": ["B", "D", "D", "E"], "value": np.random.randn(4)})

 -- INNER JOIN --

 SELECT *                     # Pandas
 FROM df1                     pd.merge(df1, df2, on="key")
 INNER JOIN df2
   ON df1.key = df2.key;


 merge() также предлагает параметры для случаев, когда вы хотите объединить столбец одного DataFrame с индексом другого DataFrame.
 indexed_df2 = df2.set_index("key")
 pd.merge(df1, indexed_df2, left_on="key", right_index=True)


 -- LEFT OUTER JOIN --

 SELECT *                      # Pandas
 FROM df1                      pd.merge(df1, df2, on="key", how="left")
 LEFT OUTER JOIN df2
   ON df1.key = df2.key;


 -- RIGHT JOIN --

 SELECT *                      # Pandas
 FROM df1                      pd.merge(df1, df2, on="key", how="right")
 RIGHT OUTER JOIN df2
   ON df1.key = df2.key;


 -- FULL JOIN --

 SELECT *                       # Pandas
 FROM df1                       pd.merge(df1, df2, on="key", how="outer")
 FULL OUTER JOIN df2
   ON df1.key = df2.key;


 -- UNION --

 df1 = pd.DataFrame({"city": ["Chicago", "San Francisco", "New York City"], "rank": range(1, 4)})
 df2 = pd.DataFrame({"city": ["Chicago", "Boston", "Los Angeles"], "rank": [1, 4, 5]})

 SELECT city, rank              # Pandas
 FROM df1                       pd.concat([df1, df2])
 UNION ALL
 SELECT city, rank
 FROM df2;


 -- LIMIT --

 SELECT * FROM tips             # Pandas
 LIMIT 10;                      tips.head(10)


 Jupyter-ноутбук — это среда разработки, где сразу можно видеть результат выполнения кода и его отдельных фрагментов.
 расширение файлов  .ipynb
 IPython – это интерактивная оболочка с широким набором возможностей и ядро для Jupyter
 Jupyter notebook является графической веб-оболочкой для IPython
 jupyter magics — метаязык, команды которого обычно начинаются с % или %%
_______________________________________________________________________________________________________________________

_______________________________________________________________________________________________________________________

_______________________________________________________________________________________________________________________

_______________________________________________________________________________________________________________________

_______________________________________________________________________________________________________________________

_______________________________________________________________________________________________________________________


"""