# Encapsulation
class Person:

    def __init__(self, f_name, email):
        self.f_name = f_name  # public variable
        self._email = email  # private variable _string is used to make private

    def update_email(self, email):
        self._email = email

    def get_email(self):
        return self._email


person_1 = Person("Jimmy", "jimmy@sample.com")
print(person_1.get_email())
person_1.update_email("jimmy@gmail.com")
print(person_1.get_email())


class Person_2:
    def __init__(self, f_name, age):
        self.name = f_name
        self._age = age

    def show_age(self):  # here the function becomes visible
        return self._get_age()

    def _get_age(self):  # here the function is private
        return self._age


person_2 = Person_2("Sam", 35)
print(person_2.show_age())

