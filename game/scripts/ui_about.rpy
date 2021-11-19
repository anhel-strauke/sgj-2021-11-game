define gui.about = _("""{size=+16}Курьерская История{/size}

Эта игра создана во время {a=https://sibgamejam.com/}Siberian Game Jam{/a} в ноябре 2021.
Тема джема: «Закон Мёрфи».

© 2021 Scientific Forest

Над игрой работали:

""")

define gui.game_licenses_info = _("""В игре использован шрифт «Blogger Sans» (создан командой сайта FirstSiteGuide.com, по лицензии Creative Commons Attribution 4.0, {a=https://firstsiteguide.com/new-blogger-sans-font/}подробности здесь{/a}).

Исходный код игры распространяется под лицензией GNU GPL v3 ({a=https://www.gnu.org/licenses/gpl-3.0.html}текст лицензии{/a}).
Тексты, музыка, звуки, графика — под лицензией Creative Commons Attribution-NonCommercial-NoDerivs 3.0 ({a=https://creativecommons.org/licenses/by-nc-nd/3.0/}текст лицензии{/a}).
""")

screen about():
    tag menu
    $ about_text = gui.about + credits_make_about_text()
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
                        text "[about_text!t]"
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
