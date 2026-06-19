from collections import UserDict
import datetime as dt

def input_error(function):
    def inner(*args):
        try: return function(*args)
        except ValueError:
            print("Give me valid arguments")
        except IndexError:
            print("Enter the argument for the command")
        except KeyError:
            print("Enter correct name")
    return inner

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
		pass

class Phone(Field):
    def __init__(self, value):
        if not(value.isdigit() and len(value) == 10): 
            raise ValueError("Phone must contain 10 digits")
        super().__init__(value)

class Birthday(Field):
    def __init__(self, value):
        try:
            self.value = dt.datetime.strptime(value, "%d.%m.%Y").date()
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")
    
class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None
    
    @input_error
    def add_phone(self, phone):
        self.phones.append(Phone(phone))
        print("Phone added") 
    
    # @input_error
    # def remove_phone(self, phone):
    #     phone_obj = self.find_phone(phone)
    #     if phone_obj: self.phones.remove(phone_obj)

    @input_error
    def edit_phone(self, old_phone, new_phone):
        phone_obj = self.find_phone(old_phone)
        if phone_obj is None:
            raise ValueError("Phone not found")
        phone_obj.value = Phone(new_phone).value
        print("Phone changed")

    # @input_error
    # def find_phone(self, phone):
    #     for p in self.phones:
    #         if p.value == phone:
    #             return p
    #     return None
    
    @input_error
    def find_phone_owner(self):
        for phone in self.phones:
            print(phone)

    @input_error
    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)
        print("Birthday added")

    @input_error
    def show_birthday(self):
        print(self.birthday)

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}, birthday: {self.birthday}"

class AddressBook(UserDict):
    @input_error
    def add_record(self, record):
        self.data[record.name.value] = record
        print("Record added")
    
    # @input_error
    # def find(self, name):
    #     return self.data.get(name)

    # @input_error
    # def delete(self, record):
    #     if record in self.data:
    #         del self.data[record]

    @input_error
    def get_upcoming_birthdays(self):
        week = []
        today = dt.date.today()
        i = 0
        while i < 7:
            week.append(dt.date.today() + dt.timedelta(i))
            i+=1

        for record in self.data.values():
            if record.birthday == None:
                continue 
            if record.birthday.value in week:
                print(f"{record.name}: {record.birthday}")
    
    @input_error
    def all_contacts(self):
        for record in self.data.values():
            print(record)

    def __str__(self):
        return "\n".join(str(record) for record in self.data.values())