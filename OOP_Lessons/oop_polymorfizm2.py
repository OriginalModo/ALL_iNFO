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


class MongoDatabase:
    def connect(self):
        print('Conencting to database SQLiteDatabase')

    def get_users(self):
        print('get users with NoSQL')


class Server:
    def get_users(self, db):
        # db = SQLiteDatabase()
        db.connect()
        users = db.get_users()
        return users


def get_db_from_config():
    print('read config')
    return SQLiteDatabase()
    # return MongoDatabase()


if __name__ == '__main__':
    server = Server()
    # server.get_users(MongoDatabase())
    server.get_users(get_db_from_config())
