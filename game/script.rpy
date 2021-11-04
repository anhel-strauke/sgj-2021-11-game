# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define e = Character('Эйлин', color="#c8ffc8")

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:
label start:

    scene bg room

    show eileen happy

    $ ss_set_info("Сохранение")

    pause 0.1

    $ ss_savepoint()

    e "Вы создали новую игру Ren'Py."

    $ ss_save_game(ss_new_save_index())

    e "Добавьте сюжет, изображения и музыку и отправьте её в мир!"

    return
