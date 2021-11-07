label chapter_3:

    $ location("Street")

    define h3 = CharacterAt(hero, (1040, 340), "left_tall")
    define h3_idea = CharacterAt(hero, (140, 240), "top_left_th")
    define su3 = CharacterAt(suicide, (0.4, 0.3), "right_tall", name ='Клод')

    scene black

    pause 1.0

    show bg street:
        zoom 0.5
        alpha 0
        linear 2 alpha 1

    pause 1.0

    show gg_ride:
        anchor (0.5, 0.6) zoom 0.4 xpos 1500-800 ypos 0.99
    with moveinleft

    pause 1.0

    hide gg_ride

    show bg door2 close
    #Звук стука в дверь

    pause

    h3_idea "Почему никто не открывает? Не могла же я напутать с адресом.."

    #Звук стука в дверь

    h3_idea "Ну вот, теперь придется возвращаться в лавку с пустыми руками"

    hide bg door2 close

    show bg door2 open:
        alpha 0
        zoom 0.5
        linear 1 alpha 1

    show suicide:
        anchor (0.5, 0.6) zoom 0.4 xpos 1800-800 ypos 0.99

    su3 "Кто вы?"

    hide suicide

    show gg_def:
        anchor (0.8, 0.6) zoom 0.4 xpos 1800-800 ypos 0.99

    h3 "Добрый день. У меня посылка к.."
    h3 "господину Фолкстону. Это вы?"

    hide gg_def

    show suicide:
        anchor (0.5, 0.6) zoom 0.4 xpos 1800-800 ypos 0.99

    su3 "Всё верно."

    pause 1.0

    #Дверь открывается шире, парень протягивает руку за посылкой.
    #Мэлори достает из своей сумки сверток с маленьким флаконом. Она отдает его парню.

    #Клауд загибается от кашля, видимо тут нужен звук.

    su3 "'Гарпирий', как я просил.."

    h3_idea "Что он сказал? Мне послышалось?"

    su3 "Я очень ждал этого момента."
    su3 "Спасибо вам, юная леди. И передайте мою благодарность хозяйке аптечной лавки"

    #кашель

    su3 "Возьмите. Это за средство и за доставку. Даже больше. Прощайте.."

    hide suicide

    show gg_def:
        anchor (0.8, 0.6) zoom 0.4 xpos 1800-800 ypos 0.99

    h3 "Постойте! В этом флаконе…"
    h3 " Вы сказали, что это “Гарпирий”? Это же сильнейший яд!"
    h3 " Его же вводят преступникам во время казни! Зачем он вам?"

    hide gg_def

    show suicide:
        anchor (0.5, 0.6) zoom 0.4 xpos 1800-800 ypos 0.99

    su3 "Хах.. Я вижу, вы не просто курьер, а прилежная ученица аптекаря."
    #кашель
    su3 "Вам не понять"
    su3 "Возьмите деньги и оставьте меня в покое.."

    h3_idea "Отдать яд в руки человека, который пытается покончить с собой… Я всегда мечтала помогать людям, что же я делаю?"

    menu:
        "Выхватить флакон и убежать":
            hide suicide
            show gg_def:
                anchor (0.8, 0.6) zoom 0.4 xpos 1800-800 ypos 0.99
            h3 "Простите меня, но я не смогу с этим жить!"
            pause 1.0
            hide gg_def
            h3_idea "Госпоже это точно не понравится… Но как она могла поручить мне такое?"
            pause 1.0
            $ Myo_value += 2
            pause 1.0
            jump chapter_4
        "Попытаться отговорить":
            hide suicide
            show gg_def:
                anchor (0.8, 0.6) zoom 0.4 xpos 1800-800 ypos 0.99
            h3 "Вы ошибаетесь! "
            h3 "Я всего лишь ученица аптекаря, но знаю что существует великое множество лекарств"
            h3 " Что-то из них может вам помочь!"
            pause 1.0
            hide gg_def
            show suicide:
                anchor (0.5, 0.6) zoom 0.4 xpos 1800-800 ypos 0.99

            su3 "Так наивно.. Учитель еще многого не рассказал вам"
            pause 1.0
            $ Myo_value += 1
            $ money_value += 5
            pause 1.0
            jump chapter_4
        "Забрать деньги и уйти":
            su3 "Спасибо за вашу работу. Еще раз, моя искренняя благодарность госпоже.."
            $ money_value +=10
            hide bg door_open
            show bg door close:
                zoom 0.5
            pause 1.0
            jump chapter_4
    pause
