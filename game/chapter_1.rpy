label start:

    define h1 = CharacterAt(hero, (20, 307), "left_big")
    define c1 = CharacterAt(cat, (1213, 795), "cat", name="")

    scene black

    pause 1.0

    show bg home:
        xalign 0.5 yalign 0.5 alpha 0.0 zoom 1.0
        parallel:
            easein 1.0 alpha 1.0
        parallel:
            easeout 1.5 zoom 0.5
    pause 2.0
    show bg home:
        xalign 0.5 yalign 0.5 alpha 1.0 zoom 0.5

    show cat temporary:
        anchor (0.5, 1.0) zoom 0.6 xpos 1920-400 ypos 0.95
    with moveinright

    pause 1.0

    c1 "Мяу!"

    h1 "Сейчас, сейчас!"

    c1 "Мауууу-мау!"

    h1 "Подожди, сейчас проверю пачку."

    pause 1.0

    h1 "Кажется, ничего не осталось."
    h1 "Может, на полке или в ящике…"

    pause 1.0

    h1 "Чёрт, там тоже нет!"

    c1 "Мяу?"

    h1 "Подожди, сейчас сбегаю в лавку, оставалась же мелочь."

    pause 1.0

    h1 "В кармане пара монет, на еду ни тебе, ни мне не хватит."

    c1 "Мяу…"

    h1 "Котик, я обязательно принесу поесть вечером, только заработаю…"



    jump chapter_2
