label chapter_4:
    $ location("payphone")

    define h4 = CharacterAt(hero, (1140 , 640), "left_tall")
    define h4_idea = CharacterAt(hero, (140, 240), "top_left_th")
    define ph4 = CharacterAt(pharmacist, (1235, 440), "right_tall")

    scene black

    pause 1.0

    show bg payphone:
        alpha 0
        zoom 0.5
        linear 2 alpha 1
    pause 2

    show gg_ride:
        anchor (0.8, 0.6) zoom 0.5 xpos 0.6 ypos 1.3
    with moveinleft

    pause

    ph4 "Да-да?"

    h4 "Здравствуйте... Это Mallory"
    h4 "Это был очень тяжёлый заказ, не уверена, что поступила правильно."

    ph4 "В жизни бывает сложный выбор Mallory. Порой, мы все должны его принять."
    ph4 "Не усматривайте злого умысла в том, что вполне объяснимо глупостью."
    ph4 "Твой следующий клиент, по адресу Клихинбецке 334/2, успей к нему побыстрее"
    ph4 "Дальше, не задерживайся и отправляйся на Бульвар Надежды к Господину Росцхлеру."
    ph4 "Все остальные адреса у тебя есть."

    h4 "Да, бегу, до связи."
    h4_idea "Все, что хорошо начинается, кончается плохо."
    h4_idea "Все, что начинается плохо, кончается еще хуже"

    pause
    return

    jump chapter_5
