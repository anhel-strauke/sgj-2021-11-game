label chapter_5:
    $ location("Броад Стрит 54")

    define h5 = CharacterAt(hero)
    define h5_idea = CharacterAt(hero, (140, 640), "top_left_th")
    define iso5 = CharacterAt(iso, (0.4, 0.3), "right_tall", name = "Неизвестный")

    scene black
    with dissolve

    show bg door close:
        zoom 0.5
    with dissolve
    
    $ location("Броад Стрит 54")

    pause 2.0

    iso5 "Кто, кто это там?"

    # show gg_ride:
    #     anchor (0.7, 0.6) zoom 0.4 xpos 1500-800 ypos 0.99
    # with dissolve

    menu:
        "Вам посылка!":
            h5 "Это курьер. Вам пакет из аптечной лавки."
        "То, что вы просили.":
            h5 "Вам привезли то, что вы просили."
        "У меня кое что есть для вас.":
            h5 "У меня есть нечто ценное для вас от хозяйки аптечной лавки."

    pause 1.0

    h5_idea "Очень нервный и неприятный тип. Интересно, что с ним происходит?"

    #hide gg_ride

    iso5 "Вы очень-очень долго!"
    iso5 "Сколько можно было вас ждать?! Да что же такое творится?!"

    show bg door open
    with dissolve

    iso5 "Давайте, давайте скорее, что привезли. Всякое решение плодит новые проблемы."

    menu:
        "Да я быстрее света!":
            # show gg_ride:
            #     anchor (0.7, 0.6) zoom 0.4 xpos 1500-800 ypos 0.99
            h5 "Ваша посылка буквально летела в клочьях дыма на максимальной скорости!"
        "Возьмите, пожалуйста.":
            # show gg_ride:
            #     anchor (0.7, 0.6) zoom 0.4 xpos 1500-800 ypos 0.99
            h5 "Возьмите пожалуйста. Надеюсь, успела."
        "Вот то, что вы просили.":
            # show gg_ride:
            #     anchor (0.7, 0.6) zoom 0.4 xpos 1500-800 ypos 0.99
            h5 "Вот то, что вы просили от Аптекаря. Всё, что может вам помочь, тут есть."

    pause 1.0

    iso5 "С-с-спасибо."

    $ money_value += 10

    pause 1.0

    iso5 "Когда дела идут хуже некуда, в самом ближайшем будущем они пойдут ещё хуже."
    iso5 "Кхе-хе-хе.."

    pause 1.0

    h5 "Мне пора. Я очень-очень спешу."

    show bg door close
    with dissolve

    h5_idea "Даже если непpиятность не может случиться, она случается."

    pause 1.0

    $ map_info = ("5-6", "chapter_6")

    jump map
