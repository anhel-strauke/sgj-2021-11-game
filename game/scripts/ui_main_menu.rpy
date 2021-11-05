screen main_menu():
    tag menu
    add "ui_images/main_menu_background.png"
    add "ui_images/game_logo.png" at:
        pos (1124, 54)
    vbox:
        style_prefix "main_menu"
        if ss_has_continue():
            button action ContinueGame() style "main_menu_cta_button" foreground "ui_images/button/[prefix_]mm_continue.png"
            if ss_has_saves():
                button foreground "ui_images/button/[prefix_]mm_saves.png" action ShowMenu("load", _transition=CropMove(0.3, "slideleft"))
            button foreground "ui_images/button/[prefix_]mm_start_again.png" action Confirm(
                _("Вы хотите начать игру заново? Весь несохранённый прогресс будет потерян."), 
                yes=Start()
            )
        else:
            button action Start() style "main_menu_cta_button" foreground "ui_images/button/[prefix_]mm_start.png"
            if ss_has_saves():
                button foreground "ui_images/button/[prefix_]mm_saves.png" action ShowMenu("load", _transition=CropMove(0.3, "slideleft"))
        button foreground "ui_images/button/[prefix_]mm_settings.png" action ShowMenu("settings", _transition=CropMove(0.3, "slideleft"))
        button foreground "ui_images/button/[prefix_]mm_about.png" action ShowMenu("about", _transition=CropMove(0.3, "slideleft"))
        if renpy.variant("pc"):
            button foreground "ui_images/button/[prefix_]mm_exit.png" action Quit(confirm=False)

style main_menu_vbox:
    spacing 12
    first_spacing 19
    xpos 1237 ypos 348
    xsize 496

style main_menu_button:
    xalign 1.0
    xysize (472, 88)

style main_menu_cta_button:
    xysize (496, 168)
    xalign 1.0
