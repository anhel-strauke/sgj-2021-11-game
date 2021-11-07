label chapter_3:

     $ location("Эббот Роуд, 15")

     define h3 = CharacterAt(hero)
     define h3_idea = CharacterAt(hero, (140, 640), "top_left_th")
     define su3 = CharacterAt(suicide, (0.3, 0.3), "right_tall", name ='Клод')

     scene black
     with dissolve

     show bg street:
          zoom 0.5
          alpha 0
          linear 2 alpha 1
     pause 2.0
     show bg street:
          zoom 0.5 alpha 1
     
     $ location("Эббот Роуд, 15")

     show gg_ride:
          anchor (0.5, 0.6) zoom 0.4 xpos 1500-800 ypos 0.99
     with moveinleft

     pause 1.0

     hide gg_ride

     show bg door2 close:
          zoom 1.0
     with dissolve

     pause 1.0

     h3_idea "Постучу в дверь."

     pause 1.0

     h3_idea "Почему никто не открывает? Не могла же я напутать с адресом.."

     #Звук стука в дверь

     h3_idea "Ну вот, теперь придется возвращаться в лавку с пустыми руками"

     show bg door2 open
     with dissolve

     pause 1.0


     show suicide:
          anchor (0.5, 0.6) zoom 0.4 xpos 1000 ypos 0.99
     with dissolve

     su3 "Кто вы?"

     # show suicide:
     #      xpos 1000
     #      linear 0.5 xpos 1400
     # pause 0.5
     # show suicide:
     #      xpos 1400

     # show gg_def:
     #      anchor (0.8, 0.6) zoom 0.4 xpos 1800-800 ypos 0.99
     # with moveinleft

     h3 "Добрый день. У меня посылка к господину Фолкстону. Это вы?"

     su3 "Всё верно."

     pause 1.0

     #Дверь открывается шире, парень протягивает руку за посылкой.
     #Мэллори достает из своей сумки сверток с маленьким флаконом. Она отдает его парню.

     #Клауд загибается от кашля, видимо тут нужен звук.

     su3 "“Гарпирий”, как я просил…"

     h3_idea "Что он сказал? Мне послышалось?"

     su3 "Я очень ждал этого момента."
     su3 "Спасибо вам, юная леди. И передайте мою благодарность хозяйке аптечной лавки."

     su3 "Кхе-кхе…"

     su3 "Возьмите. Это за средство и за доставку. Даже больше. Прощайте…"

     # hide suicide

     # show gg_def:
     #      anchor (0.8, 0.6) zoom 0.4 xpos 1800-800 ypos 0.99

     h3 "Постойте! В этом флаконе…"
     h3 "Вы сказали, что это “Гарпирий”? Это же сильнейший яд!"
     h3 "Его же вводят преступникам во время казни! Зачем он вам?"

     # hide gg_def

     #show suicide:
     #     anchor (0.5, 0.6) zoom 0.4 xpos 1800-800 ypos 0.99

     su3 "Хах… Я вижу, вы не просто курьер, а прилежная ученица аптекаря."
     su3 "Кхе-кхе-кхе…"
     su3 "Вам не понять."
     su3 "Возьмите деньги и оставьте меня в покое.."

     h3_idea "Отдать яд в руки человека, который пытается покончить с собой… Я всегда мечтала помогать людям, что же я делаю?"

     menu:
          "Выхватить флакон и убежать":
               # hide suicide
               # show gg_def:
               #      anchor (0.8, 0.6) zoom 0.4 xpos 1800-800 ypos 0.99
               h3 "Простите меня, но я не смогу с этим жить!"
               pause 1.0
               #hide gg_def
               h3_idea "Госпоже это точно не понравится… Но как она могла поручить мне такое?"
               pause 1.0
               $ Myo_value += 2
               pause 1.0

          "Попытаться отговорить":
               # hide suicide
               # show gg_def:
               #      anchor (0.8, 0.6) zoom 0.4 xpos 1800-800 ypos 0.99
               h3 "Вы ошибаетесь! "
               h3 "Я всего лишь ученица аптекаря, но знаю что существует великое множество лекарств."
               h3 " Что-то из них может вам помочь!"
               pause 1.0
               # hide gg_def
               # show suicide:
               #      anchor (0.5, 0.6) zoom 0.4 xpos 1800-800 ypos 0.99

               su3 "Так наивно… Учитель еще многого не рассказал вам."
               pause 1.0
               $ Myo_value += 1
               $ money_value += 5
               pause 1.0

          "Забрать деньги и уйти":
               su3 "Спасибо за вашу работу. Еще раз, моя искренняя благодарность госпоже…"
               $ money_value +=10
               hide bg door_open
               show bg door close:
                    zoom 0.5
               pause 1.0

     $ map_info = ("3-4", "chapter_4")
     jump map
