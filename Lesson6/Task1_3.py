# Создайте класс с базовым исключением и дочерние классы-исключения:
# ошибка уровня,
# ошибка доступа.

class Base(Exception):
    pass

class LevelError(Base):
    pass

class AccessError(Base):
    pass

def authorisation(name, level):
    db = {'Вася':1, 'Света':3,'Лёша':5}
    try:
        if name not in db.keys():
            raise AccessError
        if db[name] != level:
            raise LevelError
    except AccessError:
        print('Access Error')
    except LevelError:
        print('Wrong access level')
    else:
        print('Доступ получен')

authorisation('Вася', 1)
authorisation('Света', 5)