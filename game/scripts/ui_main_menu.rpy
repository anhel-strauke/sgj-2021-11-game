screen main_menu():
    tag menu
    add "ui_images/main_menu_background.png"
    text "Courier Story" style "main_menu_title" at:
        xalign 0.5 yanchor 0.5 ypos 0.3
    vbox:
        style_prefix "main_menu"
        if ss_has_continue():
            textbutton _("Продолжить") action ContinueGame() style "main_menu_cta_button"
            if ss_has_saves():
                textbutton _("Сохранения") action ShowMenu("load", _transition=CropMove(0.3, "slideleft"))
            textbutton _("Начать заново") action ConfirmWithButtons(
                _("Вы хотите начать игру заново? Весь несохранённый прогресс будет потерян."), 
                yes=Start(),
                yes_label=_("Начать игру"),
                no_label=_("Отмена")
            )
        else:
            textbutton _("Начать") action Start() style "main_menu_cta_button"
            if ss_has_saves():
                textbutton _("Сохранения") action ShowMenu("load", _transition=CropMove(0.3, "slideleft"))
        textbutton _("Настройки") action ShowMenu("settings", _transition=CropMove(0.3, "slideleft"))
        textbutton _("Создатели") action ShowMenu("about", _transition=CropMove(0.3, "slideleft"))
        if renpy.variant("pc"):
            textbutton _("Выход") action Quit(confirm=False)

style main_menu_title:
    size 80

style main_menu_vbox:
    spacing 13
    first_spacing 26
    xalign 0.5
    yanchor 0.0
    ypos 0.5
    xsize 500

style main_menu_button:
    xalign 0.5
    background None
    xfill True
    hover_background "white"

style main_menu_button_text is ui_text:
    size 32
    xalign 0.5
    hover_color "#000000"

style main_menu_cta_button is main_menu_button

style main_menu_cta_button_text is main_menu_button_text:
    size 60