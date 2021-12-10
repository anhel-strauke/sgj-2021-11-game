init:
    define industrial_bg_t = 0.7

init python:
    def moving_bg_pause_time():
        bounds = renpy.get_image_bounds("moving_industrial_bg")
        if not bounds:
            return 0
        curr_x = bounds[0]
        return ((-1920 - curr_x) / -1920) * industrial_bg_t
        

label chapter_10:
    image moving_industrial_bg = Composite((1920 * 2, 1080), 
        (0, 0), "bg_industrial_move",
        (1920, 0), "bg_industrial_move"
    )
    image still_industrial_bg = "images/bg industrial2.png"

    image rogue_1 = "rogue"
    image rogue_2 = "rogue"
    image rogue_3 = "rogue"

    define h10 = CharacterAt(hero, (475 , 540), "left_very_tall")
    define h10_idea = CharacterAt(hero, (580, 180), "top_left_th")
    define h10_idea_sm = CharacterAt(hero, (510, 540), "top_left_small_th")

    define r10 = CharacterAt(rogue, (1140 , 520), "right_very_tall")
    define s10 = CharacterAt(rogue, (1640 , 400), "top_right")
    define a10 = CharacterAt(rogue, (1340 , 720), "right_very_tall")

    define p10_unknown = CharacterAt(poor, (1260 , 520), "right_very_tall", name="???")
    define p10 = CharacterAt(poor, (1260 , 520), "right_very_tall")
    define p10_long = CharacterAt(poor, (1335, 90), "top_right_big")
    define k10 = CharacterAt(speaker, (0.45, 0.5), "top_left")
    define k10_2 = CharacterAt(speaker, (0.45, 0.5), "top_left", name="")

    transform trans_move_industrial:
        anchor (0, 0)
        xpos 0
        ypos 0
        block:
            linear industrial_bg_t xpos -1920
            xpos 0
            repeat
    
    transform trans_stop_industrial_bg:
        #linear industrial_bg_t xpos -1920
        easein 1.0 xpos -1920
    
    transform trans_show_still_bg:
        anchor (0, 0)
        ypos 0
        xpos 1920
        #industrial_bg_t
        easein 1.0 xpos 0
    transform trans_fix_still_bg:
        xpos 0

    scene black

    $ renpy.maximum_framerate(3600 * 24 * 365) # Максимальный FPS на год

    show moving_industrial_bg at trans_move_industrial
    show gg_ride:
        anchor (0.5, 1.0)
        zoom 0.3
        xpos 400 ypos 1500
    with dissolve

    pause 0.1
    $ location("Район Пахифеи")

    if Myo_value >= 3:
        h10_idea "Ох, ну и запах. Столько отходов от одного предприятия…"
    else:
        h10_idea "Ох, ну и запах. Это все из-за отходов фабрики…"
    pause 1.0
    h10_idea "Район Пахифеи… Здешняя производственная фабрика Пахлстона разрослась и захватила часть городских доков Феилтон."
    h10_idea "Так этот район и получил своё название."
    pause 2.0
    h10_idea "По крайней мере, фабрика даёт людям работу."
    pause 2.0
    h10_idea "Ой, я должна проверить, на месте ли лекарства."

    pause moving_bg_pause_time() # Чтобы синхронизировать анимации

    show moving_industrial_bg at trans_stop_industrial_bg
    show still_industrial_bg behind gg_ride at trans_show_still_bg
    pause 1.0
    show still_industrial_bg behind gg_ride at trans_fix_still_bg

    $ renpy.maximum_framerate(None)

    if Myo_value >= 3:
        jump chapter_10_robbery

    pause 1.0

    show poor:
        xpos 1200 ypos 0.35
        zoom 0.3
    with dissolve

    p10_unknown "Приветствую вас в Пахифеи, самом свободном районе Ривенбурга."

    h10 "{size=-2}А! Вы меня напугали… Кто вы?{/size}"

    p10_unknown "Я прощу прощения. Зовите меня Яноро."
    p10 "Позвольте спросить, что вы делаете в таком месте, как Пахифеи в столь поздний час? К тому же с полной сумкой вакцины."

    h10 "Что? Откуда вы знаете, что у меня в сумке?"

    p10 "{size=-2}Вы сами показали содержимое всей улице, когда открыли сумку. Вы даже не подозреваете, какие люди здесь живут.{/size}"

    h10 "Эти лекарства… Это имущество директора фабрики. Я…"

    p10 "{size=-2}…Всего лишь курьер, который их доставляет. Я так и думал.{/size}"
    p10 "{size=-2}Послушайте меня, вы сейчас находитесь в районе, где живут работники этой фабрики со своими семьями, как и я сам.{/size}"
    p10 "Все мы страдаем от отравленного химикатами воздуха."
    p10 "{size=-5}Единственное, что может нам помочь — это дорогое лекарство, которое вы несёте в сумке.{/size}"

    h10 "Как это меня касается? Я всего лишь курьер!"

    p10 "Вы больше, чем курьер."
    p10 "Вы — мессия для жителей этого района."
    p10 "Мы бедны и больны. Нам нечего вам дать взамен, но только вы можете спасти нас."

    h10 "Как я могу это сделать?"
    h10 "У меня есть чёткие инструкции — доставить посылку на фабрику."

    p10 "{size=-2}Посылку с вакциной вы несёте директору фабрики и его семье.{/size}"
    p10 "У них достаточно средств, чтобы купить себе ещё."
    p10 "{size=-1}Всё просто. Вы отдаёте лекарство тем, кто действительно в них нуждается.{/size}"
    p10 "Ну же, отдайте мне посылку."

    menu:
        "Хорошо. Возьмите посылку и передайте тем, кто болеет.":
            p10 "Говорю спасибо вам от всех жителей района Пахифеи."
            p10 "Вы только что спасли многих из нас."
            pause 0.5
            hide poor
            with dissolve
            pause 1.0
            h10_idea "Правильно ли я поступила?"
            h10_idea "Наверное, не стоит говорить об этом событии госпоже Амелинде."
            h10_idea "А если спросит — технически, меня просто ограбили."
            pause 1.0
            hide gg_ride
            with moveoutright
        "Не мешайте мне делать мою работу!":
            p10 "Вы пытаетесь отсрочить неизбежное! За каждый свой поступок вы несёте ответственность…"
            hide poor
            with dissolve
            pause 1.0
            h10_idea "Теперь я могу спокойно отнести посылку. Оу, вот и фабрика."

            hide still_industrial_bg
            hide moving_industrial_bg
            hide gg_ride
            with dissolve
            show bg industrial:
                align (0.5, 0.5)
                zoom 0.5
            with dissolve
            pause 1.0
            show gg_ride:
                anchor (0.5, 1.0)
                zoom 0.2
                xpos 400 ypos 1100
            with moveinleft
            pause 1.0
            k10 "Представьтесь!"
            h10 "Я курьер Мэллори из аптеки Амелинды."
            k10 "Мы ждали вас."
            k10 "Положите посылку в окно у стены и заберите оттуда деньги за доставку."
            h10_idea "Интересно, у них всё здесь автоматизировано?"
            pause 1.0
            h10_idea "Даже чаевые положили! Неплохой конец дня."
            pause 1.0
            hide gg_ride
            with moveoutright
            $ money_value += 10

    $ map_info = ("10-11", "chapter_11")
    jump map

label chapter_10_robbery:



    show rogue_1:
        xpos 1020 ypos 0.3
        zoom 0.3
    show rogue_2:
        xpos 1220 ypos 0.26
        zoom 0.3
    show rogue_3:
        xpos 1420 ypos 0.3
        zoom 0.3
    with dissolve


    r10 "Кто это у нас тут?"
    r10 "{size=-2}Эй, парни, смотрите, кого я тут нашёл.{/size}"
    s10 "Да это же девчонка."#2
    a10 "Смотрите, у неё что-то в сумке!"#3
    s10 "Что-то блестит. Деньги, что-ли?"#2
    r10 "А девочка-то при парокате…"
    r10 "Давно я такой себе хотел. Бугай, забери у неё сумку."

    h10 "Не трогайте меня!"

    show rogue_2:
        linear 0.3 xpos 350
        0.5
        linear 0.3 xpos 1220
    pause 1.7

    a10 "Чёрт! Это не бабло, это склянки."#3
    s10 "Не выбрасывай."#2
    r10 "Почему нет? На кой чёрт нам эти склянки?"
    a10 "Может, у неё в карманах что-нибудь есть? Или же под юбкой?.."#3

    h10_idea_sm "Кажется, мне конец."

    s10 "Ух-ты… Это не просто склянки. Это же…"#2
    r10 "Что там, Умник?"
    a10 "Говори, не томи! Ты единственный из нас умеешь читать."#3
    s10 "Вакцина, братаны. У неё восемь ампул с вакциной!"#2
    r10 "Да ладно!"
    a10 "Отлично! Хватит нам, и ещё останется!"#3
    a10 "Босс, что будем с ней делать?" #3
    r10 "{size=-2}Так, девка, мы забираем твою сумку с лекарствами. О нас никому не слова, понятно?{/size}"

    menu:
        "Забирайте сумку, только не трогайте меня!":
            r10 "Правильный выбор."
            r10 "Ведь некоторые события имеют тенденцию развиваться от плохого к худшему."
            hide rogue_1
            with Dissolve(0.5)
            hide rogue_2
            with Dissolve(0.5)
            hide rogue_3
            with Dissolve(0.5)
            h10_idea "О, боже… Я провалила это задание."
        "Верните лекарства, уроды!":
            r10 "Сама напросилась. Бугай, посмотри, что у нее в карманах."
            show rogue_2:
                linear 0.3 xpos 350
                0.5
                linear 0.3 xpos 1220
            pause 0.5
            $ money_value = 0
            pause 1.2
            a10 "Забрал всё, что было, Босс."
            hide rogue_1
            with Dissolve(0.5)
            hide rogue_2
            with Dissolve(0.5)
            hide rogue_3
            with Dissolve(0.5)
            h10_idea_sm "О, боже… Я провалила это задание."

    $ Myo_value = 0

    pause 2.0

    $ map_info = ("10-11", "chapter_11")
    jump map
