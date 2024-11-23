import unittest
from Baseofcars import *
from DB import *
from transports import *
from main import *


class TransportTest (unittest.TestCase):
    def test_adding(self):
        new_car = Transport(5, 'Volvo', 80, 'свободен')
        dataBase = DataBase()
        self.assertIn(new_car.get_all_info(), dataBase.recovery_array())

    def test_deletion(self):
        new_car = Transport(5, 'Volvo', 80, 'свободен')
        dataBase = DataBase()
        characteristic = new_car.get_all_info()
        dataBase.delete_row(new_car.get_number())
        self.assertNotIn(characteristic, dataBase.recovery_array())

    def test_weight_found(self):
        new_car = Transport(5, 'Камаз', 300, 'свободен')
        testData = CarBase()
        self.assertEqual(testData.get_available_cars(250), [new_car.get_all_info()])

    def test_book_car(self):
        new_car = Transport(6, 'Cybertruck', 200, 'свободен')
        testData = CarBase()
        dataBase = DataBase()
        booking = testData.book_current_car(new_car.get_number())
        self.assertIn((6, 'Cybertruck', 200, 'занят'), dataBase.recovery_array())

    def test_print_free_car(self):
        testData = CarBase()
        auto_answer = testData.get_free_cars()
        answer = []
        dataBase = DataBase()
        all_cars = dataBase.recovery_array()
        for car in all_cars:
            if car[3] == 'свободен':
                answer.append(car)
        self.assertEqual(answer, auto_answer)


if __name__ == '__main__':
    unittest.main()
