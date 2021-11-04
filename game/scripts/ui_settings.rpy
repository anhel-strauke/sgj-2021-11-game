screen settings():
    tag menu
    add "ui_images/main_menu_background.png"
    text _("Настройки") style "secondary_screen_title"
    vbox:
        style "settings_vbox"
        $ grid_rows = (2 if renpy.variant("pc") else 0) + (1 if config.has_sound or config.has_music else 0) + (1 if config.has_sound else 0) + (1 if config.has_music else 0)
        grid 2 grid_rows:
            style_prefix "settings"
            if renpy.variant("pc"):
                text _("Играть")
                textbutton _("На полном экране") action Preference("display", "fullscreen") style "radio_button"
                null
                textbutton _("В окне") action Preference("display", "window") style "radio_button"

            if config.has_sound or config.has_music:
                null
                null

            if config.has_music:
                text _("Музыка")
                bar value Preference("music volume")
            if config.has_sound:
                text _("Звук")
                bar value Preference("sound volume")
    if main_menu:
        textbutton _("Вернуться") action Return() style "back_button"
    else:
        textbutton _("Вернуться") action ShowMenu("game_menu") style "back_button"

style settings_vbox:
    xalign 0.5
    yalign 0.5
    xsize 1920/2
    ymaximum 900

style settings_grid:
    spacing 10
    xfill True
    ymaximum 900

style settings_grid_text is ui_text

style radio_button:
    xfill True
    hover_background "white"

style radio_button_text is ui_text:
    xalign 0.0
    hover_color "#000000"
    selected_color "#40a0ff"

define gui.slider_borders = Borders(6, 6, 6, 6)

style slider:
    ysize 53
    xsize 415
    base_bar Frame("ui_images/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=False)
    thumb "ui_images/slider/horizontal_[prefix_]thumb.png"