from DB import DataBase
from transports import Transport


class CarBase:
    def __init__(self, *args):
        self._cars_list = list(args)
        self._base_car = DataBase()
        data = self._base_car.recovery_array()
        for i in range(len(data)):
            num, name, weight, free = i + 1, data[i][1], data[i][2], data[i][3]
            self._cars_list.append(Transport(num, name, weight, free))

    def get_all_cars(self):
        new_list = []
        for i in range(len(self._cars_list)):
            new_list.append(
                (self._cars_list[i].get_number(), self._cars_list[i].get_name(), self._cars_list[i].get_carrying(),
                 self._cars_list[i].is_free()))
        return new_list

    def add_cars(self, *args):
        for i in range(len(args)):
            self._cars_list.append(args[i])

    def get_free_cars(self):
        new_list = []
        for i in range(len(self._cars_list)):
            if self._cars_list[i].is_free() == 'свободен':
                new_list.append(
                    (self._cars_list[i].get_number(), self._cars_list[i].get_name(),
                     self._cars_list[i].get_carrying(), self._cars_list[i].is_free()))
        return new_list

    def get_busy_cars(self):
        new_list = []
        for i in range(len(self._cars_list)):
            if self._cars_list[i].is_free() == 'занят':
                new_list.append(
                    (self._cars_list[i].get_number(), self._cars_list[i].get_name(),
                     self._cars_list[i].get_carrying(), self._cars_list[i].is_free()))
        return new_list

    def get_range_cars(self):
        new_list = self.get_all_cars()
        new_list.sort(key=lambda x: x[2])
        return new_list

    def get_available_cars(self, weight):
        new_list = []
        for i in range(len(self._cars_list)):
            if self._cars_list[i].is_free() == 'свободен' and self._cars_list[i].get_carrying() >= weight:
                new_list.append(
                    (self._cars_list[i].get_number(), self._cars_list[i].get_name(),
                     self._cars_list[i].get_carrying(), self._cars_list[i].is_free()))
        return new_list

    def del_cars(self, num):
        flag = 0
        for i in range(len(self._cars_list)):
            if self._cars_list[i].get_number() == num:
                del self._cars_list[i]
                flag = 1
        if flag:
            self._base_car.delete_row(num)
        else:
            raise Exception

    def book_current_car(self, num):
        flag = 0
        for i in self._cars_list:
            if i.get_number() == num:
                i.book_car()
                flag = 1
                break
        if flag:
            return True
        else:
            return False

