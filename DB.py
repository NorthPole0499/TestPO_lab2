import sqlite3


class DataBase:
    def add_to_db(self, car_id, name, weight, free):
        with sqlite3.connect(r"C:\Users\aleks\OneDrive\Рабочий стол\итмо\2 сем\прога\идз\Transports.db") as self._connection:
            self._cursor = self._connection.cursor()
            self._cursor.execute("""INSERT or REPLACE INTO tCars VALUES (?, ?, ?, ?)""", (car_id, name, weight, free))
            self._cursor.close()
            self._connection.commit()

    def delete_row(self, num):
        with sqlite3.connect(r"C:\Users\aleks\OneDrive\Рабочий стол\итмо\2 сем\прога\идз\Transports.db") as self._connection:
            self._cursor = self._connection.cursor()
            self._cursor.execute("""DELETE from tCars WHERE id = ?""", (num, ))
            self._cursor.close()
            self._connection.commit()

    def update_free(self, num):
        with sqlite3.connect(r"C:\Users\aleks\OneDrive\Рабочий стол\итмо\2 сем\прога\идз\Transports.db") as self._connection:
            self._cursor = self._connection.cursor()
            self._cursor.execute("""UPDATE tCars SET free = ? WHERE id = ?""", ("занят", int(num)))
            self._cursor.close()
            self._connection.commit()

    def recovery_array(self):
        with sqlite3.connect(r"C:\Users\aleks\OneDrive\Рабочий стол\итмо\2 сем\прога\идз\Transports.db") as self._connection:
            self._cursor = self._connection.cursor()
            self._cursor.execute('SELECT * FROM tCars')
            record = self._cursor.fetchall()
            self._cursor.close()
            self._connection.commit()
        return list(record)
