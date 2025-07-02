import datetime

# Задание 1.
# Напишите класс для хранения информации о человеке:
# ФИО, возраст и т.п. на ваш выбор.
# У класса должны быть методы birthday для увеличения
# возраста на год, full_name для вывода полного ФИО и т.п. на
# ваш выбор.
# Убедитесь, что свойство возраст недоступно для прямого
# изменения, но есть возможность получить текущий возраст.

class User:

    def __init__(self, first_name, middle_name, last_name, birthday):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.birthday = datetime.datetime.strptime(birthday, "%Y-%m-%d").date()

        self._set_age()

    def _set_age(self):
        day = self.birthday.day
        month = self.birthday.month
        year = self.birthday.year
        today = datetime.date.today()

        self._age = today.year - year - ((today.month, today.day) < (month, day))

    @property
    def get_age(self):
        return self._age


me = User('Василий', 'Иванович', 'Иванов', '1992-08-18')

print(me.get_age)
