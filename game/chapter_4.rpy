label chapter_4:
    $ location("Таксофон на Эббот")

    define h4 = CharacterAt(hero, (1140 , 640), "left_tall")
    define h4_idea = CharacterAt(hero, (740, 180), "top_left_th")
    define ph4 = CharacterAt(pharmacist, (1235, 440), "right_tall")

    scene black
    with dissolve

    show bg payphone:
        alpha 0
        zoom 0.5
        linear 2 alpha 1
    pause 2
    show bg payphone:
        alpha 1
        zoom 0.5
    $ location("Таксофон на Эббот")

    show gg_ride:
        anchor (0.8, 0.6) zoom 0.5 xpos 0.6 ypos 1.3
    with moveinleft

    ph4 "Да-да?"

    h4 "Здравствуйте… Это Мэллори."
    h4 "Это был очень тяжёлый заказ, не уверена, что поступила правильно."

    ph4 "В жизни бывает сложный выбор, дитя моё. Порой мы все должны его принять."
    ph4 "Не усматривай злого умысла в том, что вполне объяснимо глупостью."
    ph4 "Твой следующий клиент по адресу Броад Стрит 54, поторопись."
    ph4 "Дальше не задерживайся и отправляйся на городскую площадь к Господину Росцхлеру."
    ph4 "Все остальные адреса у тебя есть."

    h4 "Да, бегу, до связи."
    h4_idea "Все, что хорошо начинается, кончается плохо."
    h4_idea "Все, что начинается плохо, кончается еще хуже."

    pause 1.0

    $ map_info = ("4-5", "chapter_5")

    jump map
