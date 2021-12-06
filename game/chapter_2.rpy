label chapter_2:
    

    define h2 = CharacterAt(hero, (440 , 740), "top_left_big")
    define ph2 = CharacterAt(pharmacist, (1235, 740), "top_right_big_real")

    scene black
    with dissolve

    $ location("Аптека Амелинды")

    show bg_pharmacy:
        anchor (0.5, 0.5)
        pos (0, 1080)
        alpha 0.0
        zoom 1.0
        block:
            parallel:
                linear 0.5 alpha 1.0
            parallel:
                ease 3.0 xpos 1920 ypos 0
        ease 1.0 zoom 0.5 xpos 960 ypos 540
    pause 4.0
    show bg_pharmacy:
        anchor (0.5, 0.5)
        pos (960, 540)
        zoom 0.5
        alpha 1.0
    with None

    $ location("Аптека Амелинды")

    show gg_def:
        anchor (0.5, 0.65) zoom 0.4 xpos 0.25 ypos 1.0
    with moveinleft

    show pharm:
        anchor (0.5, 0.65) zoom 0.4 xpos 0.75 ypos 1.0
    with moveinright

    h2 "Доброе утро, госпожа Амелинда!"

    ph2 "Мэл! Ты как всегда вовремя! У нас сегодня много заказов."

    menu:
        "Это отличные новости!":
            h2 "Надеюсь, получится хорошо заработать!"
        "Похоже день сегодня будет сложный!":
            h2 "Надеюсь, я справлюсь."
        "Ох, тяжело будет!":
            h2 "Но что поделать, деньги сами себя не заработают."

    pause 1.0

    ph2 "Держи, это для первого заказа, будь внимательна."
    ph2 "Обычно я не берусь за такое, но заказчик был весьма убедителен и предложил неплохую цену."
    ph2 "Осторожнее с этой ампулой!"
    ph2 "Остальные заказы я уже упаковала, забери под прилавком."

    h2 "Ух! И правда много! А вот на этом большом пакете нет адреса."

    ph2 "Позвони мне после первой доставки, я уточню, куда его отвезти."

    ph2 "Не забывай, на окраинах опасно!"
    ph2 "Сейчас многие не могут заработать себе на жизнь и лекарства честным трудом."
    ph2 "Береги свою жизнь, особенно к вечеру."

    h2 "Спасибо за заботу, госпожа! Я мигом все развезу!"

    hide gg_def
    with moveoutleft

    $ map_info = ("2-3", "chapter_3")
    jump map
