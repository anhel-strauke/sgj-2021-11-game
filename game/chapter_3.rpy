init:
     transform trans_ch3_claude:
          anchor (0.5, 0.45) zoom 0.6 xpos 1100 ypos 0.99
     
     transform trans_ch3_mellory:
          anchor (0.5, 0.6) zoom 0.4 xpos 1500-800 ypos 0.99
     
     default claude_died = False

label chapter_3:
     $ location("Эббот Роуд, 15")

     define h3 = CharacterAt(hero, (560, 740), "top_left_big")
     define h3_idea = CharacterAt(hero, (140, 640), "top_left_th")
     define h3_last_idea = CharacterAt(hero, (540, 180), "top_left_th")
     define su3 = CharacterAt(suicide, (664, 324), "right_very_tall")

     scene black
     with dissolve

     show bg street:
          zoom 0.5
     with dissolve
     
     $ location("Эббот Роуд, 15")

     show gg_ride:
          anchor (0.5, 0.6) zoom 0.4 xpos 1500-800 ypos 0.99
     with moveinleft

     pause 0.5

     h3 "Эббот Роуд, 15… Кажется, это здесь."

     hide gg_ride
     show bg door2 close:
          zoom 1.0
     with dissolve

     pause 1.0

     h3_idea "Постучу в дверь."

     pause 1.0

     h3_idea "Почему никто не открывает? Не могла же я напутать с адресом…"

     #Звук стука в дверь

     h3_idea "Ну вот, теперь придётся возвращаться в аптеку с пустыми руками."

     show bg door2 open
     with dissolve

     pause 1.0


     show suicide at trans_ch3_claude
     with dissolve

     su3 "Кто вы?" 

     call ch3_show_mellory from _call_ch3_show_mellory
     h3 "Добрый день. У меня посылка к господину Фолкстону. Это вы?"

     call ch3_show_claude from _call_ch3_show_claude
     su3 "Всё верно."

     pause 1.0

     #Дверь открывается шире, парень протягивает руку за посылкой.
     #Мэллори достает из своей сумки сверток с маленьким флаконом. Она отдает его парню.

     #Клауд загибается от кашля, видимо тут нужен звук.

     su3 "“Гарпирий”, как я и просил…"

     h3_idea "Что он сказал? Мне послышалось?"

     su3 "Я очень ждал этого момента."
     su3 "Спасибо вам, юная леди. И передайте мою благодарность хозяйке аптечной лавки."

     su3 "Кхе-кхе…"
     

     su3 "Возьмите. Это за средство и за доставку. Даже больше.\nПрощайте…"

     call ch3_show_mellory from _call_ch3_show_mellory_1

     h3 "Постойте! В этом флаконе…"
     h3 "Вы сказали, что это “Гарпирий”? Это же сильнейший яд!"
     h3 "Его же вводят преступникам во время казни! Зачем он вам?"

     call ch3_show_claude from _call_ch3_show_claude_1

     su3 "Надо же… Я вижу, вы не просто курьер, а прилежная ученица аптекаря."
     su3 "Кхе-кхе-кхе…"
     su3 "Видите ли… Моя болезнь неизлечима. И причиняет мне сильнейшую боль. Вам не понять."
     su3 "Возьмите деньги и оставьте меня в покое…"

     h3_idea "Отдать яд в руки человека, который пытается покончить с собой… Я всегда мечтала помогать людям, что же я делаю?"

     menu:
          "Выхватить флакон и убежать":
               call ch3_show_mellory from _call_ch3_show_mellory_2
               h3 "Простите меня, но я не смогу с этим жить!"
               show gg_ride:
                    anchor (0.5, 0.6) zoom 0.4 xpos 700 ypos 0.99
                    ease 0.2 xpos 300
               pause 0.2
               show gg_ride:
                    anchor (0.5, 0.6) zoom 0.4 xpos 300 ypos 0.99
               h3_last_idea "Госпоже это точно не понравится… Но как она могла поручить мне такое?"
               hide gg_ride
               with moveoutleft
               pause 2.0

          "Попытаться отговорить":
               call ch3_show_mellory from _call_ch3_show_mellory_3
               h3 "Вы ошибаетесь! "
               h3 "Я всего лишь ученица аптекаря, но знаю что существует великое множество лекарств."
               h3 "Что-то из них может вам помочь!"
               
               call ch3_show_claude from _call_ch3_show_claude_2
               pause 1.0
               su3 "Так наивно… Учитель ещё многого не рассказал вам."
               su3 "{size=-2}Плохие вещи случаются, как бы мы ни старались это предотвратить.{/size}"
               hide suicide
               with dissolve
               show bg door2 close
               with hpunch
               $ Myo_value += 1
               $ money_value += 5
               $ claude_died = True
               pause 2.0

          "Забрать деньги и уйти":
               su3 "Спасибо за вашу работу. Еще раз, моя искренняя благодарность госпоже…"
               hide suicide
               with dissolve
               $ money_value +=10
               $ Myo_value += 2
               $ claude_died = True
               show bg door2 close
               with dissolve
               pause 1.0

     $ map_info = ("3-4", "chapter_4")
     jump map

label ch3_show_claude:
     hide gg_ride
     show bg door2 open:
          zoom 1.0
     show suicide at trans_ch3_claude
     with None
     return

label ch3_show_mellory:
     hide suicide
     show bg street:
          zoom 0.5
     show gg_ride at trans_ch3_mellory