"""

 Какой атрибут позволяет указать РЕГУЛЯРНОЕ ВЫРАЖЕНИЕ, которому должно соответствовать значение элемента input?
 Атрибут pattern

 <input type="email" pattern="выражение">
 <input type="tel" pattern="выражение">
 <input type="text" pattern="выражение">
 <input type="search" pattern="выражение">
 <input type="url" pattern="выражение">


 Некоторые типовые регулярные выражения

 \d [0-9]	                           Одна цифра от 0 до 9.
 \D [^0-9]	                           Любой символ кроме цифры.
 \s	                                   Пробел.
 [A-Z]	                               Только заглавная латинская буква.
 [A-Za-z]	                           Только латинская буква в любом регистре.
 [А-Яа-яЁё]	                           Только русская буква в любом регистре.
 [A-Za-zА-Яа-яЁё]	                   Любая буква русского и латинского алфавита.
 [0-9]{3}	                           Три цифры.
 [A-Za-z]{6,}	                       Не менее шести латинских букв.
 [0-9]{,3}	                           Не более трёх цифр.
 [0-9]{5,10}	                       От пяти до десяти цифр.
 ^[a-zA-Z]+$	                       Любое слово на латинице.
 ^[А-Яа-яЁё\s]+$	                   Любое слово на русском включая пробелы.
 ^[ 0-9]+$	                           Любое число.
 [0-9]{6}	                           Почтовый индекс.
 \d+(,\d{2})?	                       Число в формате 1,34 (разделитель запятая).
 \d+(\.\d{2})?	                       Число в формате 2.10 (разделитель точка).
 \d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}	   IP-адрес


 # Простой пример
 <!DOCTYPE html>
 <html>
  <head>
   <meta charset="utf-8">
   <title>Атрибут pattern</title>
  </head>
   <body>
    <form>
     <p>Введите телефон в формате 2-xxx-xxx, где вместо x
     должна быть цифра:</p>
     <p><input type="tel" pattern="2-[0-9]{3}-[0-9]{3}"></p>    #       <---- Тут регулярка
     <p><input type="submit" value="Отправить"></p>
    </form>
   </body>
 </html>





























"""