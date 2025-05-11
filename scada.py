from opcua import Server
import time

# Создаём OPC UA сервер
server = Server()
url = "opc.tcp://localhost:4840"
server.set_endpoint(url)

# Пространство имён
name = "MasterSCADA_Emulator"
addspace = server.register_namespace(name)

# Создаём объект и переменные (теги)
objects = server.get_objects_node()
my_obj = objects.add_object(addspace, "PLC_Emulator")

# Добавляем теги (аналог переменных SCADA)
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

# Запускаем сервер
server.start()
print(f"OPC UA сервер запущен на {url}")

try:
    while True:
        # print(work.get_value())
        while work.get_value():
            # Меняем значения тегов (эмуляция работы установки)
            # Работа гриппера
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
            if not work.get_value():  # Проверяем здесь
                print("===Пауза===")
                break

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
            if not work.get_value():  # Проверяем здесь
                print("===Пауза===")
                break

            #####################################################
            # работа Обработки
            processing_output_1_rotate_carousel.set_value(True)
            print("Крутилка крутится")
            time.sleep(4)
            processing_output_1_rotate_carousel.set_value(False)
            print("Крутилка не крутится")
            time.sleep(2)
            if not work.get_value():  # Проверяем здесь
                print("===Пауза===")
                break

            Black.set_value(True)
            processing_output_5_detect_hole.set_value(True)
            print("Определены цвет и положение(дном вниз)")
            time.sleep(1)
            processing_output_5_detect_hole.set_value(False)
            if not work.get_value():  # Проверяем здесь
                print("===Пауза===")
                break

            time.sleep(1)
            processing_output_1_rotate_carousel.set_value(True)
            print("Крутилка крутится")
            time.sleep(2.5)
            processing_output_1_rotate_carousel.set_value(False)
            print("Крутилка не крутится")
            if not work.get_value():  # Проверяем здесь
                print("===Пауза===")
                break

            time.sleep(1)
            processing_output_4_fix_workpiece.set_value(True)
            print("Заготовка зафиксирована")
            time.sleep(0.5)
            processing_output_0_drill.set_value(True)
            print("Заготовку сверлят")
            time.sleep(3)
            processing_output_0_drill.set_value(False)
            print("Заготовку досверлили")
            time.sleep(1)
            processing_output_4_fix_workpiece.set_value(True)
            print("Заготовка не зафиксирована")
            if not work.get_value():  # Проверяем здесь
                print("===Пауза===")
                break

            #####################################################
            # Гриппер
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
            if not work.get_value():  # Проверяем здесь
                print("===Пауза===")
                break

            #####################################################
            # Упаковка
            packing_output_4_push_box.set_value(True)
            print("коробку толкнули")
            time.sleep(2)
            packing_output_4_push_box.set_value(False)
            if not work.get_value():  # Проверяем здесь
                print("===Пауза===")
                break

            packing_output_5_fix_box_upper_side.set_value(True)
            print("крышка зафиксирована")
            time.sleep(1)
            packing_output_5_fix_box_upper_side.set_value(False)
            if not work.get_value():  # Проверяем здесь
                print("===Пауза===")
                break

            packing_output_6_fix_box_tongue.set_value(True)
            print("боковые язычки зафиксированы")
            time.sleep(1)
            packing_output_6_fix_box_tongue.set_value(False)
            if not work.get_value():  # Проверяем здесь
                print("===Пауза===")
                break

            packing_output_7_pack_box.set_value(True)
            print("шайба закрыта в коробке")
            time.sleep(2)
            packing_output_7_pack_box.set_value(False)
            if not work.get_value():  # Проверяем здесь
                print("===Пауза===")
                break

            #####################################################
            # Гриппер
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
            if not work.get_value():  # Проверяем здесь
                print("===Пауза===")
                break

            #####################################################
            # Сортировка
            sorting_input_3_box_on_conveyor.set_value(True)
            time.sleep(0.5)
            sorting_input_3_box_on_conveyor.set_value(False)
            if not work.get_value():  # Проверяем здесь
                print("===Пауза===")
                break

            sorting_input_4_box_is_down.set_value(True)
            print("найдено количество отсортированных заготовок")
            time.sleep(7)
            sorting_input_4_box_is_down.set_value(False)
            if not work.get_value():  # Проверяем здесь
                print("===Пауза===")
                break

finally:
    server.stop()