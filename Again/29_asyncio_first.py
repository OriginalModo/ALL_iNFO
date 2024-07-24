import asyncio
import aiohttp
import requests
import time

# asyncio - асинхронное выполнение, подходит для IO-bound задач, работает ровно 1 поток
# Плюсы:
# + скорость и экономия времени, вместо x + y + z -> max(x, y, z)
# + управляемость
# + меньше потребление ресурсов (в сравнении с потоками)
# Минусы:
# - "умирает" из-за одного блокирующего вызова (!)
# - event loop не безразмерный, нужно понимать, что корутины не бесплатные
# -

# 1) корутина работает как генератор
# 2) async - явный флаг, что данная функция является асинхронной (корутиной)
# 3) await - явный флаг, что в этом месте функция встает на паузу и дает работать другим, пока ждёт свои данные
# 4) event loop - цикл событий, механизм, который отвечает за планирование и запуск корутин. Можно представить как
# список/очередь, из которого в вечном цикле достаются и запускаются корутины

# Частые ошибки:
# - не использование await внутри корутины
# - создание корутины, но использование ее, как функции
# - использование внутри корутин синхронного(блокирующего) кода, в том числе IO

def gen():
    x = 10
    print(x)
    yield x

async def example():
    print(100)
    # print(100)
    # print(100)
    # print(100)

async def blocking():
    resp = requests.get('http://ya.ru')
    print(resp.status_code)

async def async_http():
    async with aiohttp.ClientSession() as session:
        async with session.get('http://ya.ru') as resp:
            print(resp.status)


async def one():
    print('Start one')
    await asyncio.sleep(1)
    print('Stop one')

async def two():
    print('Start two')
    await asyncio.sleep(2)
    # time.sleep(5)
    print('Stop two')

async def three():
    print('Start three')
    await asyncio.sleep(3)
    print('Stop three')

async def main():
    # await asyncio.gather(*(async_http() for _ in range(5)))
    # await asyncio.gather(*(blocking() for _ in range(5)))
    # await asyncio.gather(one(), two(), three())
    asyncio.create_task(one())
    asyncio.create_task(two())
    await asyncio.create_task(three())


if __name__ == '__main__':
    start = time.time()
    asyncio.run(main())
    print(time.time() - start)


