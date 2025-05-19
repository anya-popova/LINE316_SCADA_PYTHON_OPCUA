from opcua import Server
import time

server = Server()
url = "opc.tcp://localhost:4840"
server.set_endpoint(url)

# Указываем пространство имён
name = "MasterSCADA_Emulator"
addspace = server.register_namespace(name)

# Создаём объект ("папку" для тегов)
objects = server.get_objects_node()
my_obj = objects.add_object(addspace, "PLC_Emulator")

# Создаём теги
processing_input_6_hole_detected = my_obj.add_variable(addspace, "processing_input_6_hole_detected", False)
sorting_input_3_box_on_conveyor = my_obj.add_variable(addspace, "sorting_input_3_box_on_conveyor", False)
sorting_input_4_box_is_down = my_obj.add_variable(addspace, "sorting_input_4_box_is_down", False)
processing_output_0_drill = my_obj.add_variable(addspace, "processing_output_0_drill", False)
processing_output_1_rotate_carousel = my_obj.add_variable(addspace, "processing_output_1_rotate_carousel", False)
processing_output_4_fix_workpiece = my_obj.add_variable(addspace, "processing_output_4_fix_workpiece", False)
processing_output_5_detect_hole = my_obj.add_variable(addspace, "processing_output_5_detect_hole", False)
handling_input_1_gripper_at_packing_station = my_obj.add_variable(addspace, "handling_input_1_gripper_at_packing_station", False)
handling_input_2_gripper_at_start = my_obj.add_variable(addspace, "handling_input_2_gripper_at_start", False)
handling_input_3_gripper_at_right = my_obj.add_variable(addspace, "handling_input_3_gripper_at_right", False)
handling_input_4_gripper_down_pack_lvl = my_obj.add_variable(addspace, "handling_input_4_gripper_down_pack_lvl", False)
handling_output_3_gripper_to_right = my_obj.add_variable(addspace, "handling_output_3_gripper_to_right", False)
handling_output_4_gripper_to_left = my_obj.add_variable(addspace, "handling_output_4_gripper_to_left", False)
handling_output_6_gripper_to_open = my_obj.add_variable(addspace, "handling_output_6_gripper_to_open", False)
packing_output_4_push_box = my_obj.add_variable(addspace, "packing_output_4_push_box", False)
packing_output_5_fix_box_upper_side = my_obj.add_variable(addspace, "packing_output_5_fix_box_upper_side", False)
packing_output_6_fix_box_tongue = my_obj.add_variable(addspace, "packing_output_6_fix_box_tongue", False)
packing_output_7_pack_box= my_obj.add_variable(addspace, "packing_output_7_pack_box", False)
Red = my_obj.add_variable(addspace, "Red", False)
Black = my_obj.add_variable(addspace, "Black", False)
Silvery = my_obj.add_variable(addspace, "Silvery", False)
work = my_obj.add_variable(addspace, "work", False)

# Делаем теги доступными для записи
processing_input_6_hole_detected.set_writable()
sorting_input_3_box_on_conveyor.set_writable()
sorting_input_4_box_is_down.set_writable()
processing_output_0_drill.set_writable()
processing_output_1_rotate_carousel.set_writable()
processing_output_4_fix_workpiece.set_writable()
processing_output_5_detect_hole.set_writable()
handling_input_1_gripper_at_packing_station.set_writable()
handling_input_2_gripper_at_start.set_writable()
handling_input_3_gripper_at_right.set_writable()
handling_input_4_gripper_down_pack_lvl.set_writable()
handling_output_3_gripper_to_right.set_writable()
handling_output_4_gripper_to_left.set_writable()
handling_output_6_gripper_to_open.set_writable()
packing_output_4_push_box.set_writable()
packing_output_5_fix_box_upper_side.set_writable()
packing_output_6_fix_box_tongue.set_writable()
packing_output_7_pack_box.set_writable()
Red.set_writable()
Black.set_writable()
Silvery.set_writable()
work.set_writable()

server.start()
print(f"OPC UA сервер запущен на {url}")

# Выбор положения фишки: дном вверх/дном вниз
dnom_vverh = False

# Текущий процесс на установке (вся работа разбита на 15 частей)
process = 1

try:
    while True:
        while work.get_value():
            # Эмуляция работы установки
            # 1. Работа гриппера
            if process == 1:
                handling_input_1_gripper_at_packing_station.set_value(True)
                handling_input_4_gripper_down_pack_lvl.set_value(False)
                handling_output_6_gripper_to_open.set_value(False)
                print("Гриппер вверху, закрыт")
                time.sleep(0.5)
                handling_output_6_gripper_to_open.set_value(True)
                print("Гриппер вверху, открыт")
                time.sleep(1)
                handling_input_4_gripper_down_pack_lvl.set_value(True)
                print("Гриппер внизу, открыт")
                time.sleep(0.5)
                handling_output_6_gripper_to_open.set_value(False)
                print("Гриппер внизу, закрыт")
                time.sleep(1)
                handling_input_4_gripper_down_pack_lvl.set_value(False)
                print("Гриппер вверху, закрыт")
                process = 2
                if not work.get_value():
                    print("===Пауза===")
                    break

            # 2.
            if process == 2:
                time.sleep(2)
                handling_output_4_gripper_to_left.set_value(True)
                time.sleep(0.5)
                handling_output_4_gripper_to_left.set_value(False)
                print("Гриппер вверху, закрыт")
                time.sleep(1)
                handling_input_4_gripper_down_pack_lvl.set_value(True)
                print("Гриппер внизу, закрыт")
                time.sleep(0.5)
                handling_output_6_gripper_to_open.set_value(True)
                print("Гриппер внизу, открыт")
                time.sleep(1)
                handling_input_4_gripper_down_pack_lvl.set_value(False)
                print("Гриппер вверху, открыт")
                time.sleep(1.5)
                handling_input_1_gripper_at_packing_station.set_value(False)
                process = 3
                if not work.get_value():
                    print("===Пауза===")
                    break

            #####################################################
            # 3. работа Обработки
            if process == 3:
                processing_output_1_rotate_carousel.set_value(True)
                print("Крутилка крутится")
                time.sleep(3)
                processing_output_1_rotate_carousel.set_value(False)
                print("Крутилка не крутится")
                time.sleep(0.5)
                process = 4
                if not work.get_value():
                    print("===Пауза===")
                    break

            # 4. дном вниз
            if process == 4  and not(dnom_vverh):
                Black.set_value(True)
                processing_output_5_detect_hole.set_value(True)
                processing_input_6_hole_detected.set_value(True)
                print("Определены цвет и положение(дном вниз)")
                time.sleep(1)
                processing_output_5_detect_hole.set_value(False)
                process = 5
                if not work.get_value():
                    print("===Пауза===")
                    break

            # 4. дном вверх
            if process == 4 and dnom_vverh:
                Black.set_value(True)
                processing_output_5_detect_hole.set_value(True)
                processing_input_6_hole_detected.set_value(False)
                print("Определены цвет и положение(дном вниз)")
                time.sleep(1)
                processing_output_5_detect_hole.set_value(False)
                process = 5
                if not work.get_value():
                    print("===Пауза===")
                    break

            # 5.
            if process == 5:
                time.sleep(1)
                processing_output_1_rotate_carousel.set_value(True)
                print("Крутилка крутится")
                time.sleep(2.5)
                processing_output_1_rotate_carousel.set_value(False)
                print("Крутилка не крутится")
                process = 6
                if not work.get_value():
                    print("===Пауза===")
                    break

            # 6. Дном вниз
            if process == 6 and not(dnom_vverh):
                time.sleep(0.5)
                processing_output_4_fix_workpiece.set_value(True)
                print("Заготовка зафиксирована")
                time.sleep(0.5)
                processing_output_0_drill.set_value(True)
                print("Заготовку сверлят")
                time.sleep(2.5)
                processing_output_0_drill.set_value(False)
                print("Заготовку досверлили")
                time.sleep(1)
                processing_output_4_fix_workpiece.set_value(False)
                print("Заготовка не зафиксирована")
                time.sleep(0.5)
                process = 7
                if not work.get_value():
                    print("===Пауза===")
                    break

            # 6. Дном вверх
            if process == 6 and dnom_vverh:
                time.sleep(1)
                process = 7
                if not work.get_value():
                    print("===Пауза===")
                    break

            # 7.
            if process == 7:
                time.sleep(1)
                processing_output_1_rotate_carousel.set_value(True)
                print("Крутилка крутится")
                time.sleep(2.5)
                processing_output_1_rotate_carousel.set_value(False)
                print("Крутилка не крутится")
                process = 8
                if not work.get_value():
                    print("===Пауза===")
                    break

            #####################################################
            # 8. Гриппер
            if process == 8:
                handling_input_2_gripper_at_start.set_value(True)
                handling_input_4_gripper_down_pack_lvl.set_value(False)
                handling_output_6_gripper_to_open.set_value(False)
                print("Гриппер вверху, закрыт")
                time.sleep(0.5)
                handling_output_6_gripper_to_open.set_value(True)
                print("Гриппер вверху, открыт")
                time.sleep(1)
                handling_input_4_gripper_down_pack_lvl.set_value(True)
                print("Гриппер внизу, открыт")
                time.sleep(0.5)
                handling_output_6_gripper_to_open.set_value(False)
                print("Гриппер внизу, закрыт")
                time.sleep(1)
                handling_input_4_gripper_down_pack_lvl.set_value(False)
                print("Гриппер вверху, закрыт")
                time.sleep(1.5)
                handling_input_2_gripper_at_start.set_value(False)
                process = 9
                if not work.get_value():
                    print("===Пауза===")
                    break

            #####################################################
            # 9. Упаковка
            if process == 9:
                packing_output_4_push_box.set_value(True)
                print("коробку толкнули")
                time.sleep(2)
                packing_output_4_push_box.set_value(False)
                process = 10
                if not work.get_value():
                    print("===Пауза===")
                    break

            # 10.
            if process == 10:
                packing_output_5_fix_box_upper_side.set_value(True)
                print("крышка зафиксирована")
                time.sleep(1)
                packing_output_5_fix_box_upper_side.set_value(False)
                process = 11
                if not work.get_value():
                    print("===Пауза===")
                    break

            # 11.
            if process == 11:
                packing_output_6_fix_box_tongue.set_value(True)
                print("боковые язычки зафиксированы")
                time.sleep(1)
                packing_output_6_fix_box_tongue.set_value(False)
                process = 12
                if not work.get_value():
                    print("===Пауза===")
                    break

            # 12.
            if process == 12:
                packing_output_7_pack_box.set_value(True)
                print("шайба закрыта в коробке")
                time.sleep(2)
                packing_output_7_pack_box.set_value(False)
                process = 13
                if not work.get_value():
                    print("===Пауза===")
                    break

            #####################################################
            # 13. Гриппер
            if process == 13:
                handling_input_3_gripper_at_right.set_value(True)
                handling_input_4_gripper_down_pack_lvl.set_value(False)
                handling_output_6_gripper_to_open.set_value(False)
                print("Гриппер вверху, закрыт")
                time.sleep(0.5)
                handling_output_6_gripper_to_open.set_value(True)
                print("Гриппер вверху, открыт")
                time.sleep(1)
                handling_input_4_gripper_down_pack_lvl.set_value(True)
                print("Гриппер внизу, открыт")
                time.sleep(0.5)
                handling_output_6_gripper_to_open.set_value(False)
                print("Гриппер внизу, закрыт")
                time.sleep(1)
                handling_input_4_gripper_down_pack_lvl.set_value(False)
                print("Гриппер вверху, закрыт")
                time.sleep(1.5)
                handling_input_3_gripper_at_right.set_value(False)
                process = 14
                if not work.get_value():
                    print("===Пауза===")
                    break

            #####################################################
            # 14. Сортировка
            if process == 14:
                sorting_input_3_box_on_conveyor.set_value(True)
                time.sleep(0.5)
                sorting_input_3_box_on_conveyor.set_value(False)
                process = 15
                if not work.get_value():
                    print("===Пауза===")
                    break

            # 15.
            if process == 15:
                sorting_input_4_box_is_down.set_value(True)
                print("найдено количество отсортированных заготовок")
                time.sleep(7)
                sorting_input_4_box_is_down.set_value(False)
                Black.set_value(False)
                processing_output_5_detect_hole.set_value(False)
                processing_input_6_hole_detected.set_value(False)
                process = 1
                if not work.get_value():
                    print("===Пауза===")
                    break

finally:
    server.stop()