init:
    default doll_broken = False
    
label chapter_8:
    $ location("Таксофон на Эббот")

    define h8 = CharacterAt(hero, (600 , 640), "left_very_tall")
    #define h8_long = CharacterAt(hero, (430 , 740), "top_left_big")
    define h8_idea = CharacterAt(hero, (600, 590), "top_left_small_th")
    define ph8 = CharacterAt(pharmacist, (1235, 440), "right_very_tall")
    #define ph8_long = CharacterAt(pharmacist, (1235, 140), "top_right_big")

    scene black
    with dissolve

    if was_in_ritual:
        jump chapter_8_after_ritual

    pause 1.0

    show bg payphone:
        zoom 0.5
    with Dissolve(2)

    $ location("Таксофон на Эббот")

    show gg_ride:
        anchor (0.8, 0.6) zoom 0.5 xpos 0.6 ypos 1.3
    with moveinleft

    pause 1.0

    ph8 "Аптека Амелинды. Таблетки маленькие, проглотит и младенец. Говорите."

    h8 "Амелинда, это Мэллори! Я сейчас была у…"

    ph8 "Секундочку…"
    pause 1.0

    h8_idea "Только о своей аптеке и думает…"

    pause 1.0

    ph8 "Итак, Мэллори, по какой причине ты снова отвлекаешь меня от работы?"

    h8 "Посылка для госпожи Д’Арк доставлена."

    ph8 "Да, я знаю. Госпожа Д’Арк только что звонила мне."

    h8 "Что?.. Она звонила вам?"

    ph8 "Да-да. Ей было очень интересно, почему ты отказалась воспользоваться гостеприимством и сбежала с её деньгами?"

    h8 "Ох… Простите, госпожа Амелинда."

    pause 1.0

    ph8 "Не волнуйся, Мэллори. Я давно знаю эту женщину и уверяю тебя, что ты всё сделала верно."
    ph8 "Добром бы это не кончилось. Хотя твои манеры оставляют желать лучшего."

    h8 "Я взяла деньги за свою работу. Там было немного…"

    ph8 "Вот и оставь их себе. Но впредь пообещай мне, что будешь более обходительна с клиентами."

    h8 "Да, конечно, госпожа."

    pause 1.0

    jump chapter_8_end

label chapter_8_after_ritual:

    scene black
    with dissolve

    pause 1.0

    show bg payphone:
        zoom 0.5
    with Dissolve(2)

    show gg_ride:
        anchor (0.8, 0.6) zoom 0.5 xpos 0.6 ypos 1.3
    with moveinleft

    pause 1.0

    ph8 "Аптека Амелинды. Таблетки маленькие, проглотит и младенец. Говорите."

    h8 "Амелинда, это Мэллори! Я сейчас была у…"

    ph8 "Секундочку."
    pause 1.0

    h8_idea "Только о своей аптеке и думает…"

    pause 1.0

    ph8 "Итак, Мэллори, по какой причине ты снова отвлекаешь меня от работы?"

    h8 "Вы хоть знаете, где я сейчас была?"

    ph8 "Если только это не бал у самого императора, то мне не интересно."

    h8 "Госпожа, вы поручили мне отвезти посылку госпоже Д’Арк, и она попросила меня спуститься с ней в подвал, а потом…"

    ph8 "Послушай меня, девочка. Твоя задача — донести мои товары до адресатов. Таков был наш уговор, помнишь?"
    ph8 "Что происходит с тобой после, меня не интересует. То, что должно произойти, произойдёт, так или иначе."

    menu:
        "Но это неправильно… Я не хотела, чтобы со мной так поступали.":
            ph8 "Ривенбург — опасное место. И чем раньше ты это поймёшь, тем лучше."
        "Почему вы не предупредили меня об опасности?":
            ph8 "А какой смысл?"
            ph8 "Я могу предупредить тебя о шести опасностях, но наверняка найдётся седьмая."
        "Я всего лишь курьер, и не готовилась к такому.":
            ph8 "{size=-2}Можешь считать, что твоя подготовка уже началась.{/size}"

    h8 "Но…"
    ph8 "Не трать время."

label chapter_8_end:
    ph8 "Ты должна успеть отвезти лекарства на фабрику в районе Пахифеи."
    ph8 "И поторопись, уже темнеет."
    ph8 "В этом районе может произойти всё, что угодно. Особенно вечером."

    h8 "Поняла, госпожа."

    ph8 "Подожди."
    #ph8_long "Перед этим доставь посылку с куклой малютке Нэлли на набережной Бьеншан. Я дала слово её матери, что куклу они получат сегодня."
    ph8 "Перед этим доставь посылку с куклой малютке Нэлли на набережной Бьеншан."
    ph8 "Я дала слово её матери, что куклу они получат сегодня."

    h8 "Я отправляюсь."

    ph8 "И Мэллори…"

    h8 "Да?"

    ph8 "Я надеюсь, с куклой всё в будет в порядке?"
    ph8 "Внутри у неё целебная трава, вымоченная в лечебных микстурах. Береги её."

    h8 "Все будет хорошо, уверяю вас. Что может случиться?"

    ph8 "И всё же… Будь осторожна."

    pause 1.0

    if Myo_value < 3:
        $ map_info = ("8-9", "chapter_9")
    else:
        $ map_info = ("8-9-acc", "chapter_9")
    jump map
