label chapter_11:
    
    define m11 = CharacterAt(hero, (450, 307), "left_big")
    define c11 = CharacterAt(cat, (1253, 795), "cat", name="")

    scene black
    with dissolve
    scene bg home:
        xalign 0.5 yalign 0.5 alpha 1.0 zoom 0.5
    with dissolve

    if money_value < 30:
        jump bad_ending
    jump good_ending

label good_ending:

    show gg_def:
        zoom 0.16 anchor (0.5, 1.0) pos (0.2, 0.9)
    with moveinleft
    show cat_trouble:
        anchor (0.5, 1.0) zoom 0.2 xpos 1920-400 ypos 0.95
    with moveinright

    m11 "Я дома. Все ужасы и кошмары этого дня позади. Усталая и разбитая, но дома с котейкой."
    c11 "Мяу."
    m11 "Котик, мой любимый пушистик. Ты же моё когтистое сокровище."
    m11 "Сейчас пересчитаю деньги, их должно хватить. Хоть 30 монет-то я заработала?"
    c11 "Мяууу-Мяууу!"
    m11 "Их хватает. Хватает тебе на еду! Сегодня все было не зря, ты поешь вкусненькое."

    hide cat_trouble
    show cat:
        anchor (0.5, 1.0) zoom 0.2 xpos 1920-400 ypos 0.95
    with dissolve

    c11 "Мяу!"

    m11 "Хорошее завершение этого странного и удивительного дня."

    pause 1.0

    scene black
    with dissolve

    pause 1.0

    return

label bad_ending:
    
    show gg_def:
        zoom 0.16 anchor (0.5, 1.0) pos (0.2, 0.9)
    with moveinleft
    show cat_trouble:
        anchor (0.5, 1.0) zoom 0.2 xpos 1920-400 ypos 0.95
    with moveinright

    m11 "Воспоминания о сегодняшнем дне будут снится мне в кошмарах."
    m11 "Хотя, мне часто снятся кошмары."

    c11 "Мяу."

    m11 "День сложных выборов и тяжёлых событий. Возможно, все было не зря. Мой кот поест."

    c11 "Мяууу-Мяууу!"

    m11 "Надо пересчитать заработанное, мешок корма для Тимми стоит 30 монет."

    c11 "Мяу?"

    m11 "Тут их нет. Мой кот целый день голоден, и даже сейчас я не могу его покормить."
    m11 "Денег за весь день не набирается даже на пакет корма для него."

    c11 "Мяу? Мяу!!!"

    m11 "Мне очень жаль."

    hide cat_trouble
    show cat_sad:
        anchor (0.5, 1.0) zoom 0.2 xpos 1920-400 ypos 0.95
    with dissolve

    c11 "Мяу..."

    show cat_sad:
        anchor (0.5, 1.0) xzoom 0.2 yzoom 0.2 xpos 1920-400 ypos 0.95
        linear 0.1 xzoom -0.2
    pause 0.1
    hide cat_sad
    with moveoutright

    m11 "Да, Тимми, тебе надо покушать."
    m11 "Может новые хозяева тебя покормят. Они будут лучше меня."

    pause 1.0

    scene black
    with dissolve

    pause 1.0

    return