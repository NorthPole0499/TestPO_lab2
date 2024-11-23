from DB import DataBase


class Transport:
    def __init__(self, num, name, weight, freedom='свободен'):
        self._name = name
        self._carry_ability = weight
        self._free = freedom
        self._number = num
        self._bd = DataBase()
        self._bd.add_to_db(num, name, weight, freedom)

    def get_all_info(self):
        return self._number, self._name, self._carry_ability, self._free

    def get_carrying(self):
        return self._carry_ability

    def get_name(self):
        return self._name

    def get_number(self):
        return self._number

    def can_carry(self, weight):
        if weight <= self._carry_ability:
            return True
        else:
            return False

    def is_free(self):
        return self._free

    def book_car(self):
        self._free = 'занят'
        self._bd.update_free(self._number)
