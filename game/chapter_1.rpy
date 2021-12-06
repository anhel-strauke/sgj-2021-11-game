label start:
    $ location(_("Дом Меллори"))

    define h1 = CharacterAt(hero, (20, 307), "left_big")
    define c1 = CharacterAt(cat, (1253, 815), "cat", name="")

    scene black
    with fade

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

    $ location(_("Дом Меллори"))

    show cat happy:
        anchor (0.5, 1.0) zoom 0.2 xpos 1920-400 ypos 0.95
    with moveinright

    c1 "Мяу!"

    h1 "Сейчас, сейчас!"

    c1 "Мауууу-мау!"

    h1 "Подожди, будет тебе еда!"

    pause 1.0

    h1 "Ох, кажется, ничего не осталось."
    h1 "Может, на полке или в ящике…"

    pause 1.0

    h1 "Чёрт, там тоже нет!"

    c1 "Мяу?"

    #h1 "Сейчас сбегаю в лавку, принесу тебе ."

    pause 1.0

    h1 "В кармане пара медяков, на еду ни тебе, ни мне не хватит."

    show cat trouble
    with dissolve

    c1 "Мяу…"

    $ Myo_value = 0

    h1 "Корм для Томми стоит 30 монет."
    h1 "Котик, я обязательно принесу поесть вечером, только заработаю…"

    $ map_info = ("1-2", "chapter_2")
    jump map
