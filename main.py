from KompasClass import *

kompas = Kompas()  # Запуск или подключение к Компас
kompas.info_general()  # Вывод информации о программе

#kompas.newfile_drawing()  # Создание нового чертежа
kompas.newfile_fragment()  # Создание нового фрагмента

#view1 = kompas.new_view(25, 50, "Тестовый вид", 1 / 15, state=0, color=0x00FF00)  # Создание нового вида

# Построение геометрии
rectangle = kompas.draw_rectangle(0, 0, 100, 200, 5, 0)
circle = kompas.draw_circle(200, 100, 40, 3)
line = kompas.draw_line(0, 0, 200, 100, 4)
point = kompas.draw_point(500, 500, 2)

True
