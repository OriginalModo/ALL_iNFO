"""

 -- Что такое FastAPI? --

 FastAPI - высокопроизводительным веб-фреймворком, разработанным для упрощения создания API с помощью Python.
 FastAPI построен на базе Starlette и Pydantic, которые обеспечивают его замечательную скорость и простоту использования.

 FastAPI - основан на Python 3.6+ type hints**

 Что позволяет FastAPI обеспечивать автоматическую проверку данных, сериализацию и документирование с использованием
 моделей Pydantic. Одним из наиболее привлекательных аспектов FastAPI является его впечатляющая производительность:
 он способен обрабатывать тысячи запросов в секунду с минимальными накладными расходами, что делает его отличным выбором
 для приложений с высоким трафиком.



 -- Ключевые особенности FastAPI --

 a. Поддержка асинхронности: FastAPI полностью поддерживает асинхронное программирование, позволяя вам писать асинхронные
  обработчики маршрутов и использовать преимущества синтаксиса async /await в Python для неблокирующих операций ввода-вывода.

 b. Автоматическое документирование: FastAPI автоматически генерирует интерактивную и удобную для пользователя
  документацию по API. Он использует стандарты OpenAPI и JSON Schema для предоставления исчерпывающей документации
  для вашего API, включая проверку входных данных, ожидаемые ответы и многое другое.

 c. Подсказки типов и проверка данных: Благодаря интеграции FastAPI с Pydantic вы можете определять модели данных
  с помощью подсказок типов (type hints) Python, обеспечивая автоматическую проверку данных и сериализацию.
  Эта функция помогает выявлять ошибки на ранних стадиях процесса разработки и повышает читаемость кода.

 d. Внедрение зависимостей: FastAPI поддерживает внедрение зависимостей, позволяя вам эффективно управлять
  зависимостями и организовывать их. Эта функция особенно полезна при работе с подключениями к базе данных,
  аутентификацией и другими общими ресурсами.

 e. Простой и интуитивно понятный синтаксис: синтаксис FastAPI понятен, легок для чтения и очень похож на стандартное
  определение функций Python, что делает его доступным как для начинающих, так и для опытных разработчиков.



 -- Почему именно FastAPI? --

 1. Flask - это легкий и широко используемый веб-фреймворк в экосистеме Python. Он прост в использовании и с ним легко
  начать работу, но ему не хватает встроенной поддержки асинхронности и автоматической проверки на основе подсказок типов.

 2. Django - это полнофункциональный веб-фреймворк, который следует философии "батарейки включены"
  (швейцарский нож - все в комплекте). Он предоставляет множество готовых функциональных возможностей, включая ORM,
  интерфейс администратора и многое другое, но для небольших и простых API это может оказаться излишним. В дополнение
  можно поругать джангу, тем что в нем зашит паттерн MVC (model-view-controller, или model-view-template по-джанговски),
  а также это по сути модульный монолит и он не такой гибкий, как FastAPI.



 --  Основные плюсы FastAPI --

 1) скорость (питон всегда считался медленным, но API на FastAPI сопоставим с языком Go
 (язык гугла, в котором изначально зашита асинхронность и скорость работы) или
 Node.js (довольно быстрым и популярным сейчас в российском бэкенде). По итогу fastapi является на данный момент
 самым быстрым веб-фреймворком питона (он где-то в 4-5 раз быстрее джанги и фласка - его основных конкурентов).

 2) встроенная поддержка проверки типов (питон это динамический язык со строгой типизацией, что означает возможность
 преобразовать один тип данных в другой, но строгость означает, что питон не делает это преобразование неявно;
 проблема у разработчика-питониста была в том, что иногда можно было поймать неожидаемый тип данных, из-за чего
 программа могла лечь). FastAPI эту проблему снимает (при помощи Pydantic'а, о котором расскажем дальше в курсе).

 3) ну и асинхронность "из коробки", то есть на нем можно писать реально высоконагруженные API-шки.


 -- Вопросы --
 Какова цель аутентификации в веб-приложениях? - ПРОВЕРКА ЛИЧНОСТИ ПОЛЬЗОВАТЕЛЯ

 Что означает JWT в контексте аутентификации? -  ВЕБ-ТОКЕН JSON
 JWT - это объект JSON с цифровой подписью, который содержит утверждения о пользователе.
 JWT обычно отправляются в заголовке `Authorization`.

 В чем преимущество использования аутентификации на основе JWT в распределенной системе?
 ЭТО ПОЗВОЛЯЕТ ОСУЩЕСТВЛЯТЬ АУТЕНТИФИКАЦИЮ БЕЗ УЧЕТА СОСТОЯНИЯ.



 -- Using Dataclasses --
 FastAPI построен на основе Pydantic , и я показал вам, как использовать модели Pydantic для объявления запросов и ответов.

 Но FastAPI также поддерживает использованиеdataclasses

 from dataclasses import dataclass
 from typing import Union

 from fastapi import FastAPI


 @dataclass
 class Item:
     name: str
     price: float
     description: Union[str, None] = None
     tax: Union[float, None] = None


 app = FastAPI()


 @app.post("/items/")
 async def create_item(item: Item):
     return item


 -- Тестирование в FastAPI --
 Какой фреймворк тестирования рекомендуется для тестирования приложений FastAPI из-за его дополнительных возможностей
 тестирования?  -- pytest


 from fastapi.testclient import TestClient
 from my_app import app

 client = TestClient(app)

 def test_calculate_sum():
     response = client.get("/sum/?a=5&b=10")
     assert response.status_code == 200
     assert response.json() == {"result": 15}


 -- Понимание WebSockets веб-сокетов в веб-приложениях --

 WebSockets предоставляют двунаправленный канал связи между клиентом и сервером по единственному долговременному
 соединению. В отличие от традиционных HTTP-запросов, когда клиент отправляет запрос и ожидает ответа, WebSockets
 обеспечивают асинхронную связь в режиме реального времени. Это делает их идеальными для приложений, требующих
 постоянного обновления данных, приложений для чата, игр в реальном времени и инструментов совместной работы.

 Поддержка WebSocket в FastAPI:
 FastAPI имеет встроенную поддержку для обработки подключений WebSocket, что упрощает интеграцию функций реального
 времени в ваши приложения. С помощью класса `WebSocket`, предоставляемого FastAPI, вы можете создавать маршруты WebSocket
 и обрабатывать события WebSocket, такие как подключение, отключение и получение сообщений.




 from fastapi import FastAPI, WebSocket, WebSocketDisconnect

 app = FastAPI()

 # список для хранения подключённых WebSocket клиентов
 connected_clients = []


 # WebSocket-роут для обработки WebSocket подключений
 @app.websocket("/ws/")
 async def websocket_endpoint(websocket: WebSocket):
     await websocket.accept()
     connected_clients.append(websocket)

     try:
         while True:
             data = await websocket.receive_text()
             await websocket.send_text(f"Message text was: {data}")
     except WebSocketDisconnect:
         connected_clients.remove(websocket)


 # роут для массовой рассылки сообщений всем подключённым клиентам
 @app.get("/broadcast/")
 async def broadcast_message(message: str):
     for client in connected_clients:
         await client.send_text(f"Broadcast message: {message}")





























"""

