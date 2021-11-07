label chapter_6:
    $ location("Городская Площадь")

    define h6 = CharacterAt(hero, (940 , 540), "left_tall")
    define h6_idea = CharacterAt(hero, (540, 90), "top_left_th")
    define art6 = CharacterAt(artist, (0.7, 0.4), "right_tall", name = "Роцхлер")
    define art6_long = CharacterAt(artist, (0.7, 0.12), "top_right_big", name = "Роцхлер")

    scene black
    with dissolve

    show bg street:
        zoom 0.5
    show artist:
        zoom 0.2
        xpos 1400 ypos 0.3
    with Dissolve(2.0)


    
    
    pause 1.0


    show gg_ride:
        anchor (0.5, 0.8) zoom 0.2 xpos 1200-800 ypos 0.95
    with moveinleft

    h6 "Прошу прощения."
    h6 "Это вы господин Роцхлер? По описанию подходите."

    art6 "Да-да. Да, молодая леди. Всё так, именно я."
    art6 "Я уже много лет рисую город и людей, здания и пейзажи."
    art6 "Красота этого мира завораживает меня."

    h6 "У меня для вас посылка, она весьма увесистая. Что там?"

    art6 "О, это мои краски. Новые тюбики, ещё больше цветов!"
    art6 "Я смогу рисовать и рисовать этот прекрасный город, чудесных и немного сумасшедших горожан."
    art6 "Вы ведь знаете, вы сами из таких жителей."
    art6 "Я готов не есть и не спать, лишь бы творить прекрасное."
    pause 0.5
    art6 "У меня совсем нет денег, я отдаю за доставку последнее и остаюсь без ужина."
    art6 "Такова цена искусства, мы, художники, все её платим."
    pause 0.5
    art6 "Я подарю вам житейскую мудрость."
    art6_long "Ели могут случиться несколько непpиятностей, они пpоисходят в самой неблагопpиятной последовательности."
    art6 "У меня так было не раз и не два."
    art6 "Молодая леди, может, договоримся на ваш портрет в обмен на оплату доставки?"

    menu:
        "Вы великий мастер! Конечно я согласна!":
            art6 "Отлично!"
            art6 "Давайте приступим к работе! Вы изумительно красивы!"
            scene black
            with dissolve
            pause 1.0
            show bg street:
                zoom 0.5
            show gg_ride:
                anchor (0.5, 0.8) zoom 0.2 xpos 1200-800 ypos 0.95
            show artist:
                zoom 0.2
                xpos 1400 ypos 0.3
            with dissolve

            art6 "Вот ваш портрет, юная леди! Вы получились, как живая."

            pause 1.0

        "Мне сейчас тоже нужны деньги, и очень хочется свой портрет. Может договоримся на половину стоимости?":
            art6 "Да, конечно, я всё понимаю и сам в подобном положении."
            scene black
            with dissolve
            pause 1.0
            show bg street:
                zoom 0.5
            show gg_ride:
                anchor (0.5, 0.8) zoom 0.2 xpos 1200-800 ypos 0.95
            show artist:
                zoom 0.2
                xpos 1400 ypos 0.3
            with dissolve


            art6 "Вот ваш портрет!"
            art6 "Вы очень хорошо получились, юная леди."
            $ money_value += 5
            $ Myo_value += 1

            pause 1.0

        "Вы прекрасно рисуете, но сейчас я не в том положении.":
            h6 "Мне очень нужны деньги за доставку."
            art6 "Я понимаю, я всё понимаю. Нарисую вас, когда вы решитесь."
            art6 "Теперь вы знаете, как меня найти и, надеюсь, найдёте в ближайшее время."

            $ money_value += 10
            $ Myo_value += 2

            pause 1.0
    if Myo_value < 3:
        $ map_info = ("6-7", "chapter_7")
    else:
        $ map_info = ("6-7-acc", "chapter_7")
    jump map
