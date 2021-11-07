screen settings():
    default sel_section = -1
    zorder 810
    tag menu
    add "ui_images/bg_window.png"
    add "ui_images/settings_name.png" at:
        pos (670, 43)
    vbox:
        style_prefix "settings"

        fixed:
            if sel_section == 1:
                add "ui_images/section_hover.png"
            else:
                add "ui_images/section.png"
            hbox:
                label _("Играть")
                textbutton _("В окне"):
                    action Preference("display", "any window")
                    hovered [SetScreenVariable("sel_section", 1), Function(renpy.restart_interaction)]
                    unhovered [SetScreenVariable("sel_section", -1), Function(renpy.restart_interaction)]
                    style "settings_checkbox"
                textbutton _("На полном экране"):
                    action Preference("display", "fullscreen")
                    hovered [SetScreenVariable("sel_section", 1), Function(renpy.restart_interaction)]
                    unhovered [SetScreenVariable("sel_section", -1), Function(renpy.restart_interaction)]
                    style "settings_checkbox"

        if config.has_music:
            fixed:
                if sel_section == 2:
                    add "ui_images/section_hover.png"
                else:
                    add "ui_images/section.png"
                hbox:
                    label _("Музыка")
                    bar:
                        yoffset 8
                        value Preference("music volume")
                        hovered [SetScreenVariable("sel_section", 2), Function(renpy.restart_interaction)]
                        unhovered [SetScreenVariable("sel_section", -1), Function(renpy.restart_interaction)]
        
        if config.has_sound:
            fixed:
                if sel_section == 3:
                    add "ui_images/section_hover.png"
                else:
                    add "ui_images/section.png"
                hbox:
                    label _("Звуки")
                    bar:
                        yoffset 8
                        value Preference("sound volume")
                        hovered [SetScreenVariable("sel_section", 3), Function(renpy.restart_interaction)]
                        unhovered [SetScreenVariable("sel_section", -1), Function(renpy.restart_interaction)]

    if main_menu:
        button action Return() style "back_button"
    else:
        button action ShowMenu("game_menu") style "back_button"

style settings_vbox:
    xsize 1164 
    align (0, 0)
    pos (360, 310)
    spacing 69

style settings_fixed:
    ysize 113

style settings_hbox:
    align (0, 0)
    xoffset 119
    spacing 60

style settings_label:
    align (0, 0)
    yoffset 24
    xysize (247, 68)

style settings_label_text is ui_text:
    color "#fed6a2"
    size 52

style settings_checkbox:
    background Frame("ui_images/button/[prefix_]check.png", 0, 0, 74, 0)
    padding (0, 0, 80, 0)
    ysize 62
    yoffset 24

style settings_checkbox_text is ui_text:
    color "#796c65"
    hover_color "#bfa292"
    size 42
    yalign 0.5

define gui.slider_borders = Borders(6, 6, 6, 6)

style slider:
    ysize 89
    xsize 650
    left_bar "ui_images/slider/hslider_left.png"
    right_bar "ui_images/slider/hslider_right.png"
    thumb "ui_images/slider/[prefix_]hthumb.png"
    left_gutter 13
    right_gutter 12