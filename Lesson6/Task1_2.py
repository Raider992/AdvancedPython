# Создайте функцию аналог get для словаря.
# Помимо самого словаря функция принимает ключ и
# значение по умолчанию.
# При обращении к несуществующему ключу функция должна
# возвращать дефолтное значение.
# Реализуйте работу через обработку исключений.

def custom_get(dct, key, default_key=0):
    try:
        return dct[key]
    except:
        print('Nonexistent key. Default key value returned')
        return dct[default_key]

print(custom_get({0: '123', 1:'123', 2:'123'}, 15))