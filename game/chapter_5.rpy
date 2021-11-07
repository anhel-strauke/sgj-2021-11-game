label chapter_5:
    $ location("unknown")

    define h5 = CharacterAt(hero, (940 , 340), "left_tall")
    define h5_idea = CharacterAt(hero, (540, 90), "top_left_th")
    define iso5 = CharacterAt(iso, (0.4, 0.3), "right_tall")

    scene black

    pause 1.0

    show bg door close:
        zoom 0.5

    pause 2.0

    iso5 "Кто, кто это там?"

    show gg_ride:
        anchor (0.7, 0.6) zoom 0.4 xpos 1500-800 ypos 0.99

    menu:
        "Вам посылка":
            h5 "Это курьер. Вам пакет из аптечной лавки"
        "То что вы просили":
            h5 "Вам привезли то, что вы просили"
        "У меня кое что есть для вас":
            h5 "У меня есть нечто ценное для вас от хозяйки аптечной лавки"

    pause 1.0

    h5_idea "Очень нервный и неприятный тип, интересно, что с ним происходит"

    hide gg_ride

    iso5 "Вы очень-очень долго!"
    iso5 " Сколько можно было вас ждать! Да что же такое твориться!"

    hide bg door close

    show bg door open:
        alpha 0
        zoom 0.5
        linear 1 alpha 1

    iso5 "Давайте, давайте скорее, что привезли. Всякое решение плодит новые проблемы"

    menu:
        "i'm the speed":
            show gg_ride:
                anchor (0.7, 0.6) zoom 0.4 xpos 1500-800 ypos 0.99
            h5 "Ваша посылка, летела в клочьях дыма на максимальной скорости."
        "Возьмите пожалуйста":
            show gg_ride:
                anchor (0.7, 0.6) zoom 0.4 xpos 1500-800 ypos 0.99
            h5 "Возьмите пожалуйста, надеюсь успела."
        "Вот то, что вы просили":
            show gg_ride:
                anchor (0.7, 0.6) zoom 0.4 xpos 1500-800 ypos 0.99
            h5 "Вот то, что вы просили от Аптекаря. Все, что может вам помочь тут есть"

    pause 1.0

    hide gg_ride

    iso5 "С-с-спасибо."

    pause 1.0

    iso5 "Когда дела идут хуже некуда, в самом ближайшем будущем они пойдут еще хуже."
    iso5 "Кхе-хе-хе.."

    pause 1.0

    show gg_ride:
        anchor (0.7, 0.6) zoom 0.4 xpos 1500-800 ypos 0.99
    h5 "Мне пора. Я очень-очень спешу"

    h5_idea "Даже если непpиятность не может случиться, она случается."


    pause

    return
    jump chapter_6
