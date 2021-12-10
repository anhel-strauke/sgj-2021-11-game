init:
    image bridge_layer_1 = Composite((1964 * 2, 1080), (0, 0), "bridge_l1", (1964, 0), "bridge_l1")
    image bridge_layer_2 = Composite((3840 * 2, 614), (0, 0), "bridge_l2", (3840, 0), "bridge_l2")
    image bridge_layer_3 = Composite((2240 * 2, 680), (0, 0), "bridge_l3", (2240, 0), "bridge_l3")
    image bridge_layer_4= Composite((2070 * 2, 399), (0, 0), "bridge_l4", (2070, 0), "bridge_l4")
    image bridge_layer_5 = Composite((1920 * 2, 698), (0, 0), "bridge_l5", (1920, 0), "bridge_l5")

    image bridge_blur = Composite((1920 * 2, 1080), (0, 0), "bridge_blur_mid", (1920, 0), "bridge_blur_mid")

    # Трансформа для бесконечного движения слоя
    # Параметры трансформы: начальное положение по x, положение по y, время изменения x до 0
    # (когда задаём время, надо учитывать разную ширину слоёв)
    transform trans_bridge_moving_layer(target_x, base_y, t):
        anchor (0, 0)
        ypos base_y
        block:
            xpos target_x
            linear t xpos 0
            repeat

    # Эта простая трансформа для показа слоя моста, чтоб писать меньше
    transform trans_bridge_static_layer(x, y):
        anchor (0, 0)
        xpos x
        ypos y
    
    # Бесконечный полёт дирижабля справа налево
    transform trans_bridge_zep:
        anchor (0, 0)
        ypos 29
        xpos 558
        linear 175.0 xpos -387 # 175 секунд от центра экрана за левый край. Да, он оооочень медленно и величественно летит
        block:
            5.0 # Пять секунд паузы между исчезновением дирижабля и появлением снова из-за правого края
            xpos 1920
            # Пролёт через весь экран — 420 секунд.
            linear 420.0 xpos -387  # 387 — это ширина самого дирижабля, надо, чтобы он полностью за край ушёл
            repeat

label chapter_11:
    scene black
    with dissolve

    $ renpy.maximum_framerate(3600 * 24 * 365) # Максимальный FPS на год

    # Мост с эффектом параллакса. Каждый слой движется со своей скоростью бесконечно.
    # Слои движутся из-за левого края экрана, поэтому позиции по x отрицательные
    show bridge_layer_1 at trans_bridge_moving_layer(-1964, 0, 120.0) 
    show bridge_layer_2 at trans_bridge_moving_layer(-3840, 0, 108.0) #  x и y — левый верхний угол слоя
    show bridge_zep at trans_bridge_zep # Между слоями 2 и 3 — дирижабль
    show bridge_layer_3 at trans_bridge_moving_layer(-2240, 0, 36.0)
    show bridge_layer_4 at trans_bridge_moving_layer(-2070, 393, 16.0)
    show bridge_layer_5 at trans_bridge_moving_layer(-1920, 382, 0.8)
    with dissolve # Показываем всю красоты выше из затемнения

    pause 1.0

    $ location("Мост")

    # Приезжает Мэллори из-за правого края экрана
    show gg_ride:
        xzoom -0.3
        yzoom 0.3
        anchor (0.5, 1.0)
        ypos 1320
        xpos 2579
        easein_quad 1.0 xpos 1360
    pause 1.0 # Ждём, пока она приедет
    # Теперь бесконечно немного покачиваем её вперёд-назад (типа у неё немного скорость меняется)
    show gg_ride:
        xpos 1360
        ease 3.0 xpos 1310
        block:
            ease 12.0 xpos 1420
            ease 12.0 xpos 1310
            repeat

    
    pause

    # Быстро летим камерой налево, чтобы показать статичную сцену на мосту, типа это то, что Мэл видит впереди
    # Сначала правый край заблюренного моста, он с полупрозрачным градиентом
    show bridge_blur_right zorder 1:
        anchor (0, 0)
        ypos 0
        xpos -460
        linear 0.1 xpos 0 # Быстро летит, за 0.1 сек
    # Теперь непосредственно блюренный мост, его дважды проносим перед глазами, для эффекта
    # Внимание, он по координате x далеко за левым краем, мы будем двигать саму камеру влево, это проще, чем смещать многослойный мост вправо
    show bridge_blur zorder 1:
        anchor (0, 0)
        ypos 0
        xpos -3840
        0.2 # Пауза перед началом движения: 0.1 сек, чтобы успеть показать правый край, и ещё 0.1 сек, чтобы камера сдвинулась
        block:
            # Дважды проматываем блюренный мост слева направо, очень быстро
            xpos -3840
            linear 0.1 xpos -1920
            repeat 2
        block: # В конце перекрываем блюрным мостом статичную сцену, она соберётся за ним
            xpos -3840
    #... А это движение камеры налево. Почему-то у камеры ось x смотрит в другую сторону, поэтому у неё координаты без минуса
    camera:
        0.1
        xpos 0
        linear 0.1 xpos 1920

    pause 0.4 # Ждём завершения анимаций — 0.1 + 0.1 + два раза по 0.1 = 0.4

    # Фиксируем позицию камеры, если игрок прокликал паузу
    camera:
        xpos 1920
    
    # Собираем нашу статичную сцену моста из тех же слоёв, она совсем далеко слева, так как у нас опять поедет камера
    show bridge_layer_1 at trans_bridge_static_layer(-1964 - 3840, 0) 
    show bridge_layer_2 at trans_bridge_static_layer(-3840 - 3840, 0)
    show bridge_layer_3 at trans_bridge_static_layer(-2240 - 3840, 0)
    show bridge_layer_4 at trans_bridge_static_layer(-2070 - 3840, 393)
    show bridge_layer_5 at trans_bridge_static_layer(-1920 - 3840, 382)
    
    # ... И двигаем камеру ещё раз, чтобы показать статичную сцену
    camera:
        xpos 1920
        linear 0.1 xpos 3840
    pause 0.1 # Ждём завершения предыдущей анимации 0.2 сек

    # Фиксируем камеру после паузы в новом положении. Теперь экран у нас по x от -3840 до -1920, далее про это не забываем
    camera:
        xpos 3840
    
    # Скрываем блюрный мост, он тоже больше не нужен. Хз, сообразит ли Ren'Py освободить память от него
    hide bridge_blur_right
    hide bridge_blur
    with None

    $ renpy.maximum_framerate(None) # Всё, быстрые анимации больше не нужны, снижаем нагрузку на проц и видеокарту


    pause
    

    show black zorder 1:
        align (0, 0)
        xpos -3840
        ypos 0
    with dissolve

    # Вертаем камеру взад
    camera:
        xpos 0
    

    $ map_info = ("11-12", "chapter_12")
    jump map