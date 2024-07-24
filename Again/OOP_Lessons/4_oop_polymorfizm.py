# Полиморфизм(Много форм) -  это механизм, позволяющий выполнять один и тот же код по-разному
# Ducktyping (утиная типизация) - наличие поведения для использования в полиморфизме

# В ЯП со статической типизацией для полиморфизма важно кто ты (какой тип)
# Для питона важно что ты умеешь (поведение)

# В питоне везде полиморфизм (требуются методы)

class SQLiteDatabase:
    def connect(self):
        print('Conencting to database SQLiteDatabase')

    def get_users(self):
        print('get users with SQL')


class MongoDataBase:
    def connect(self):
        print('Conencting to database MongoDataBase')

    def get_users(self):
        print('get users with NoSQL')


class Server:
    def get_users(self, db):
        db.connect()
        users = db.get_users()
        return users


def get_db_from_config():
    print('real config')
    return MongoDataBase()


class FakeDb:
    def connect(self):
        pass

    def get_users(self):
        return [1]


if __name__ == '__main__':
    server = Server()
    assert [1] == server.get_users(FakeDb())
