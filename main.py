from transports import Transport
from Baseofcars import CarBase
from tkinter import *
from DB import DataBase
from tkinter import messagebox


def adding_car():
    data = []
    for i in base.get_all_cars():
        data.append(int(i[0]))
    num, name, weight = max(data) + 1, name_enter.get(), weight_enter.get()
    if not str(weight).isdigit():
        messagebox.showerror('Удаление', 'Неверные данные!')
    elif len(name) > 30:
        messagebox.showerror('Удаление', 'Слишком длинное имя!')
    elif int(weight) > 1000000 or int(weight) <= 0:
        messagebox.showerror('Удаление', 'Некорректная грузоподъёмность!')
    else:
        car1 = Transport(num, name, int(weight))
        base.add_cars(car1)
        messagebox.showinfo('Добавление', 'Транспорт добавлен!')


def delete_car():
    try:
        base.del_cars(int(num_enter.get()))
        messagebox.showinfo('Удаление', 'Транспорт удалён!')
    except Exception:
        messagebox.showerror('Удаление', 'Неверный номер!')


def show_all():
    data = base.get_all_cars()
    string = 'номер, имя, грузоподъёмность, статус \n'
    for i in data:
        for j in i:
            string += str(j) + ', '
        string += '\n'
    messagebox.showinfo('Транспорт', string)


def show_range():
    data = base.get_range_cars()
    string = 'номер, имя, грузоподъёмность, статус \n'
    for i in data:
        for j in i:
            string += str(j) + ', '
        string += '\n'
    messagebox.showinfo('Транспорт', string)


def show_free():
    data = base.get_free_cars()
    if len(data) == 0:
        string = 'Таких машин на данный момент нет!'
    else:
        string = 'номер, имя, грузоподъёмность, статус \n'
        for i in data:
            for j in i:
                string += str(j) + ', '
            string += '\n'
    messagebox.showinfo('Транспорт', string)


def show_busy():
    data = base.get_busy_cars()
    if len(data) == 0:
        string = 'Таких машин на данный момент нет!'
    else:
        string = 'номер, имя, грузоподъёмность, статус \n'
        for i in data:
            for j in i:
                string += str(j) + ', '
            string += '\n'
    messagebox.showinfo('Транспорт', string)


def show_available():
    try:
        if int(weight_sel_enter.get()) > 1000000 or int(weight_sel_enter.get()) < 0:
            raise Exception
        data = base.get_available_cars(int(weight_sel_enter.get()))
        string = 'номер, имя, грузоподъёмность, статус \n'
        for i in data:
            for j in i:
                string += str(j) + ', '
            string += '\n'
        messagebox.showinfo('Транспорт', string)
    except Exception:
        messagebox.showerror('Транспорт', 'Неверная грузоподъёмность!')


def booking():
    try:
        flg = base.book_current_car((int(num_book_enter.get())))
        if flg:
            messagebox.showinfo('Удаление', 'Транспорт забронирован!')
        else:
            messagebox.showerror('Удаление', 'Неверный номер!')
    except Exception as error:
        messagebox.showerror('Удаление', 'Неверный номер!')


def exit_app():
    window.quit()


base = CarBase()
window = Tk()
window.title("Учёт грузового транспорта")  # создаём окно
window.geometry('700x400')
window.resizable(False, False)


start_lbl = Label(window,
                  text="Добро пожаловать в приложение для учёта грузового транспорта",
                  font=("Arial Bold", 10))
start_lbl.grid(column=80, row=0, columnspan=400)

adding_lbl = Label(window, text="Добавление транспорта",
                   font=("Arial Bold", 10))  # создаём блок с добавлением транспорта
adding_lbl.grid(column=0, row=20, columnspan=100)

name_lbl = Label(window, text="Название машины:",
                 font=("Arial Bold", 10))
name_lbl.grid(column=0, row=50, columnspan=80)
name_enter = Entry(window, width=10)
name_enter.grid(column=90, row=50)

weight_lbl = Label(window, text="Грузоподъёмность:",
                   font=("Arial Bold", 10))
weight_lbl.grid(column=0, row=80, columnspan=80)
weight_enter = Entry(window, width=10)
weight_enter.grid(column=90, row=80)

adding_btn = Button(window, text="Добавить", command=adding_car)
adding_btn.grid(column=90, row=120)


del_lbl = Label(window, text="Удаление транспорта",
                font=("Arial Bold", 10))  # создаём блок с удалением транспорта
del_lbl.grid(column=200, row=20, columnspan=350)

num_lbl = Label(window, text="Номер машины:",
                font=("Arial Bold", 10))
num_lbl.grid(column=200, row=50, columnspan=250)

num_enter = Entry(window, width=10)
num_enter.grid(column=450, row=50)

delete_btn = Button(window, text="Удалить", command=delete_car)
delete_btn.grid(column=430, row=80)


all_cars_lbl = Label(window, text="Показать все машины:",
                font=("Arial Bold", 10))             # создаём вывод всех машин
all_cars_lbl.grid(column=0, row=150, columnspan=100)

all_cars_btn = Button(window, text="Вывести", command=show_all)
all_cars_btn.grid(column=75, row=180)


range_cars_lbl = Label(window, text="Показать машины по грузоподъёмности:",
                font=("Arial Bold", 10))             # создаём вывод машин по грузоподъёмености
range_cars_lbl.grid(column=200, row=150, columnspan=450)

range_cars_btn = Button(window, text="Вывести", command=show_range)
range_cars_btn.grid(column=430, row=180)


free_cars_lbl = Label(window, text="Показать свободные машины:",
                font=("Arial Bold", 10))             # создаём вывод свободных машин
free_cars_lbl.grid(column=0, row=210, columnspan=150)

free_cars_btn = Button(window, text="Вывести", command=show_free)
free_cars_btn.grid(column=75, row=240)


busy_cars_lbl = Label(window, text="Показать занятые машины:",
                font=("Arial Bold", 10))             # создаём вывод занятых машин
busy_cars_lbl.grid(column=260, row=210, columnspan=200)

busy_cars_btn = Button(window, text="Вывести", command=show_busy)
busy_cars_btn.grid(column=430, row=240)


select_lbl = Label(window, text="Подбор транспорта:",
                font=("Arial Bold", 10))  # создаём блок с подбором транспорта
select_lbl.grid(column=0, row=300, columnspan=100)

weight_sel_lbl = Label(window, text="Грузоподъёмность:",
                font=("Arial Bold", 10))
weight_sel_lbl.grid(column=0, row=330, columnspan=80)

weight_sel_enter = Entry(window, width=10)
weight_sel_enter.grid(column=90, row=330)

select_btn = Button(window, text="Подобрать", command=show_available)
select_btn.grid(column=90, row=370)


book_lbl = Label(window, text="Бронирование транспорта:",
                font=("Arial Bold", 10))  # создаём блок с бронированием транспорта
book_lbl.grid(column=270, row=300, columnspan=200)

num_book_lbl = Label(window, text="Номер:",
                font=("Arial Bold", 10))
num_book_lbl.grid(column=250, row=330, columnspan=150)

num_book_enter = Entry(window, width=10)
num_book_enter.grid(column=400, row=330)

book_btn = Button(window, text="Забронировать", command=booking)
book_btn.grid(column=400, row=370)


exit_btn = Button(window, text="Выход", command=exit_app)
exit_btn.grid(column=700, row=450)



window.mainloop()
# c_id, name, weight = len(base.get_all_cars()) + 1, 'Opel', 60
# car1 = Transport(c_id, name, weight)
# base.add_cars(car1)
# car2 = Transport(len(base.get_all_cars()) + 1, 'Kia', 30, )
# base.add_cars(car2)
# car2.book_car()
# print(base.get_available_cars(80))
