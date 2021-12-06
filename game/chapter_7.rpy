label chapter_7:
    image black_overlay = "#000000"
    $ location("Серенити 22")

    default was_in_ritual = False

    define h7 = CharacterAt(hero, (0.28, 0.5), "left_very_tall")
    define h7_idea = CharacterAt(hero, (0.28, 0.48), "top_left_small_th")
    define h7_2 = CharacterAt(hero, (0.6, 0.75), "top_left")
    define h7_idea_2 = CharacterAt(hero, (0.62, 0.78), "top_left_small_th")
    define d7 = CharacterAt(darklady, (0.63, 0.4), "right_very_tall")
    define d7_2 = CharacterAt(darklady, (0.43, 0.4), "left_very_tall")
    define d7_dark = CharacterAt(darklady)

    scene black
    with dissolve

    show bg door lady:
        zoom 0.5
    show darklady:
        zoom 0.2
        xpos 1200 ypos 0.3
    with Dissolve(1)
    pause 1.0
    $ location("Серенити 22")

    show gg_ride:
        anchor (0.5, 0.8) zoom 0.2 xpos 440 ypos 0.95
    with moveinleft

    pause 1.0

    d7 "Ты вовремя… Я ждала тебя."

    h7 "Здравствуйте, мисс…"

    d7 "Называй меня Д’Арк."

    pause 1.0

    h7 "Вот Ваша посылка, возьмите, пожалуйста."

    d7 "Как тебя зовут, маленькая леди?"

    h7 "Эмм…"
    h7 "Мэллори, мисс Д’Арк. Меня зовут Мэллори."

    d7 "Мэллори…"
    d7 "Красивое имя."
    pause 1.0
    d7 "Мэллори, милое дитя, мне очень нужна твоя помощь. Без тебя я совершенно точно не справлюсь."
    d7 "Пойдём, пойдём скорее, Мэллори, время не ждёт."

    menu:
        "Извините, но нет. Мне нужно быстро доставить остальные заказы.":
            d7 "Ты меня очень разочаровала, но так уж и быть, вот деньги за заказ."
            $ Myo_value += 1
            $ money_value += 5
            pause 1.0
            hide darklady
            with dissolve
            pause 1.0
            $ map_info = ("7-8", "chapter_8")
            jump map
        "Если это недолго, то я готова помочь.":
            h7 "Что от меня требуется?"
            d7 "Пойдем со мной в дом. Там в подвале надо кое-что передвинуть."
            h7 "Звучит странно, но я вам помогу."
            pause 1.0
            jump chapter_7s1


label chapter_7s1:

    $ was_in_ritual = True

    scene black
    with dissolve

    show bg basement:
        zoom 0.5
    show gg_def:
        zoom 0.2
        xpos 20 ypos 400
    show darklady:
        zoom 0.2
        xpos 1200 ypos 0.3
    with Dissolve(2)

    h7_idea "Тут мрачная и давящая атмосфера... "
    h7 "Для чего здесь свечи, кубки и ножи? Красное — это чья-то кровь?!"
    d7 "Ничего не бойся, милая."
    d7 "Иди вот сюда, в центр пентаграммы, и ложись."
    d7 "Руки будут связаны, но ты не переживай. Свечи уже горят, не хватает только тебя."
    d7 "Ну же, быстрее! Что ты медлишь? Время начинать!"
    menu:
        "Нет-нет, я к такому точно не готова!":
            h7 "Это очень ж-ж-жутко выглядит."
            h7 "Простите, мне пора идти."
            h7_idea "Скорее бежать! Там в прихожей несколько монет, прихвачу их за доствку."
            $ Myo_value += 1
            $ money_value += 5
            pause 1.0
            scene black
            with dissolve
            $ map_info = ("7-8", "chapter_8")
            jump map
            
        "Выглядит жутковато, но я согласна.":
            pause 1.0
            hide gg_def
            hide darklady
            show darklady:
                xzoom -0.2
                yzoom 0.2
                xpos 360 ypos 0.3
            show gg_penta_1:
                pos (1023, 742)
            with dissolve
            d7_2 "Прекрасно!"
            hide darklady
            show darklady_tape:
                xzoom -0.2
                yzoom 0.2
                xpos 360 ypos 0.3
            with dissolve
            pause 0.5
            h7_2 "А зачем синяя изолента?…"
            d7_2 "Давай сюда руки, узнаешь."
            hide gg_penta_1
            show gg_penta_2:
                pos (1023, 742)
            hide darklady_tape
            show darklady_hand:
                xzoom -0.2
                yzoom 0.2
                xpos 360 ypos 0.3
            with dissolve
            pause 1.0
            h7_2 "Мне немного туго, я не могу пошевелиться."
            h7_2 "Что будет дальше? Мне страшно!"
            d7_2 "Кляп. Дальше будет кляп."
            pause 0.5
            hide gg_penta_2
            show gg_penta_3:
                pos (1023, 742)
            with dissolve
            pause 1.0
            
            h7_2 "Ммжлмл... (нечленораздельная речь)"

            h7_idea_2 "Я думала, что этот день не может быть еще хуже. Но, кажется, ошиблась."
            h7_idea_2 "Скорее всего, это будет стоить мне жизни."

            pause 1.0

            # Тэг {sc} — это дрожащий текст из библиотеки Kinetic-Text-Tags (https://github.com/SoDaRa/Kinetic-Text-Tags)
            # Переводы строки \n расставлены вручную, потому что текст, обёрнутый в {sc}{/sc}, не переносится на новую строку
            # автоматически (особенность библиотеки).
            # Кроме того, стиль текста нужно применять так же вручную, из-за особенностей реализации Kinetic-Text-Tags,
            # это делается тегом {=название_стиля}.
            d7_2 "{sc=4}{=bubble_right_tall_what}Уииииии! Тёмные\nСилы, Бессмертные\nДухи, явитесь на\nмой зов!!!{/sc}"
            d7_2 "{sc=2}{=bubble_right_tall_what}Пусть свершится\nпредначертанное,\nумрёт больной и\nневинный, души\nголода с окраин\nполучат свои\nжертвы, да омоется\nэто в слезах ребёнка!{/sc}"
            d7_2 "{sc=2}{=bubble_right_tall_what}Да придёт в город\nДух Мёрфи, да\nбудут его законы!{/sc}"

            show black_overlay
            with dissolve
            pause 1.0
            d7_dark "{cps=6}Оуууууу!{/cps}"
            pause 3.0 #sound
            d7_dark "Вот всё и кончилось. Сейчас я развяжу тебя и сниму кляп."

            hide black_overlay
            hide gg_penta_3
            hide darklady_hand
            show gg_def:
                zoom 0.2
                xpos 20 ypos 400
            show darklady_hand:
                zoom 0.2
                xpos 1200 ypos 0.3
            with dissolve
            
            pause 1.0
            h7 "Фух…"
            h7 "Эм… Можно, я пойду?"
            d7 "Да, вот тебе деньги."
            $ Myo_value += 2
            $ money_value +=10
            h7 "Это было лучше, чем я думала."
            d7 "И ещё, Мэллори, на будущее."
            d7 "Не ходи с незнакомыми людьми в подвал."
            d7 "Ну это я так, к слову."

            $ map_info = ("7-8", "chapter_8")
            jump map
