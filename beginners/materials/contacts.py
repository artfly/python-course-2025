# Сделать записную книжку с контактами
# создавать, удалять, редактировать, искать

# - хотим понимать, добавили ли контакт в итоге
# - картинка для списка контактов и отдельно для каждого (книжка с ними?)
# - дописываем класс контактов: как-то будем там хранить наш контакт (одна запись)
# - __repr__
# - делаем список контактов, добавляем второй, проверяем
# - добавляем дубликат
# - __eq__ vs. == всех полей
# - пишем удаление по индексу?

class Contact:
    def __init__(self, name, phone_number, email):
        self.name = name
        self.phone_number = phone_number
        self.email = email

    def __eq__(self, other_contact):
        return self.name == other_contact.name and self.phone_number == other_contact.phone_number

    def __repr__(self):
        return f'*** {self.name}, {self.phone_number}, {self.email} ***'

class Contacts:
    def __init__(self):
        self.contacts = []

    def create_contact(self, new_contact):
        found_duplicate = False
        for contact in self.contacts:
            b = contact.__eq__(new_contact)
            if b:
                found_duplicate = True
        if not found_duplicate:
            self.contacts.append(new_contact)

c1 = Contact('Artemiy', '89139267132', 'a.sartakov@g.nsu.ru')
c2 = Contact('Женя', '89735672837', 'zh.novosad@g.nsu.ru')
c1.__eq__(c2)
c3 = Contact('Женя', '89735672837', 'zh.novosad@g.nsu.ru')
cs = Contacts()
cs.create_contact(c1)
cs.create_contact(c2)
cs.create_contact(c3)

print(cs.contacts)


