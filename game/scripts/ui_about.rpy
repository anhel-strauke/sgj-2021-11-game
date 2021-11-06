define gui.about = _("""Эта игра создана во время {a=https://sibgamejam.com/}Siberian Game Jam{/a} в ноябре 2021.
Тема джема: «Закон Мёрфи».

© 2021 Scientific Forest

Над игрой работали:

Дина Грико — идея, сценарий
Тимирлан Кенджибаев — идея, сценарий, тексты
Наталья Субботина-Чукальская — сценарий, тексты
Яна Юрцевич — графика
Ольга Ринделин — графика
Анна Тимофеева — UI
Анатолий Грико — программирование, анимации, звук
Ekko — программирование
Ziczin — музыка
""")

define gui.game_licenses_info = _("""Исходный код игры распространяется под лицензией GNU GPL v3
Музыка, звуки, графика — CC BY-NC-ND 4.0
""")

screen about():
    tag menu
    fixed:
        add "ui_images/main_menu_background.png"
        text _("Создатели") style "secondary_screen_title"
        fixed:
            style_prefix "about_vp"
            viewport:
                yinitial 0.0
                scrollbars "vertical"
                mousewheel True
                pagekeys True
                draggable True
                vbox:
                    style_prefix "about"
                    text "[gui.about!t]"
                    null height 20
                    text _("Сделано в {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n{size=20}[renpy.license!t]{/size}\n\n[gui.game_licenses_info!t]")

        textbutton _("Вернуться") action Return() style "back_button"

style about_vp_fixed:
    xalign 0.5
    yanchor 0.0
    ypos 0.30
    xsize (1920/3*2)
    ysize (1080/2 + 50)
