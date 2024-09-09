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