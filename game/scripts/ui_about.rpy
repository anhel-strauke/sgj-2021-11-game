define gui.about = _("""Эта игра создана во время {a=https://sibgamejam.com/}Siberian Game Jam{/a} в ноябре 2021.
Тема джема: «Закон Мёрфи».

© 2021 Scientific Forest

Над игрой работали:

Дина Грико — концепция, управление проектом
Тимирлан Кенджибаев — сценарий, тексты
Наталья «NielNoel» Субботина-Чукальская — сценарий, тексты
Яна Юрцевич — графика
Ольга «Ринделин» Сердюк — графика
Анна «Крапива» Тимофеева — UI
Анатолий «Анхель» Грико — программирование, анимации
Ekko — программирование, анимации
Ziczin — музыка
""")

define gui.game_licenses_info = _("""Исходный код игры распространяется под лицензией GNU GPL v3
Музыка, звуки, графика — CC BY-NC-ND 4.0
""")

screen about():
    tag menu
    fixed:
        add "ui_images/bg_window.png"
        add "ui_images/about_name.png" at:
            pos (675, 43)
        fixed:
            add "ui_images/textbox_bg.png"
            style_prefix "about_vp"
            viewport:
                yinitial 0.0
                scrollbars "vertical"
                mousewheel True
                pagekeys True
                draggable True
                window:
                    style_prefix "about"
                    vbox:
                        text "[gui.about!t]"
                        null height 20
                        text _("Сделано в {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n{size=20}[renpy.license!t]{/size}\n\n{size=20}[gui.game_licenses_info!t]{/size}")

        button action Return() style "back_button"

style about_vp_fixed:
    pos (366, 274)
    xysize (1154, 599)

style about_window:
    padding (40, 20)

style about_text is ui_text:
    size 32
    
style hyperlink_text is ui_text:
    color "#fed6a2"
    hover_color "#ffffff"
    underline True