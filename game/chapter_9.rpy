label chapter_9:
    $ location("doll")
    
    define h9 = CharacterAt(hero, (1140 , 640), "left_tall")
    define h9_idea = CharacterAt(hero, (740, 140), "top_left_th")
    define v9 = CharacterAt(vivi, (1235, 440), "right_tall")
    define ne9 = CharacterAt(nelly, (1235, 440), "right_tall")

    if Myo_value < 3:
        jump chapter_9s1

    scene black

    show bg doll:
        alpha 0
        zoom 0.5
        linear 2 alpha 1

    show gg_ride:
        anchor (0.8, 0.6) zoom 0.5 xpos 0.6 ypos 1.3
    with moveinleft

    show vv:
        zoom 0.2
        xpos 1200 ypos 0.3


    h9 "Добрый день! У меня посылка для маленькой Нелли."

    v9 "Мы вас давно ждем!"

    h9 "Летела на максимальном пару"

    n9 "Моя кукла! Где моя кукла!"

    v9 "Нэлли, прояви терпение! Что за несносный ребенок.."
    v9 "И все же мы рады, что вы до нас добрались. А теперь, пожалуйста, вручите нам нашу посылку"

    pause

label chapter_9s1:




    return
    jump chapter_10
