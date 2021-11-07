screen save_slots_list(for_save=False):
    zorder 810
    python:
        save_slots = ss_list_save_slots()
        new_slot_index = ss_new_save_index(save_slots)
    window style "save_slot_list_fixed":
        vbox:
            if for_save: # "New save file" button
                button action SaveSlotAction(for_save, new_slot_index) style "slot_button":
                    default_focus for_save
                    hbox:
                        style "slot_button_hbox"
                        frame style "slot_thumb_frame":
                            add "ui_images/new_save_slot.png" align (0.5, 0.5)
                        vbox:
                            style "slot_button_vbox"
                            text _("Новое сохранение") style "slot_name_text"
                            text " " style "slot_date_text"
            $ focus_value = not for_save
            for (slot_index, slot_description, slot_thumbnail, slot_utime) in save_slots:
                button action Confirm(_("Вы хотите переписать это сохранение?"), yes=SaveSlotAction(for_save, slot_index)) style "slot_button":
                    default_focus focus_value
                    $ focus_value = False
                    hbox:
                        style "slot_button_hbox"
                        frame style "slot_thumb_frame":
                            add slot_thumbnail xsize config.thumbnail_width ysize config.thumbnail_height align (0.5, 0.5)
                        vbox:
                            style "slot_button_vbox"
                            text slot_description style "slot_name_text"
                            text ss_format_save_time(slot_utime) style "slot_date_text"
                        if not for_save:
                            key "save_delete" action Confirm(
                                        _("Удалить это сохранение? Его нельзя будет восстановить."),
                                        yes=DeleteSaveSlot(slot_index)
                                    )

style save_slot_list_fixed:
    padding (33, 28)

style slot_thumb_frame:
    xysize (292, 169)
    background Frame("ui_images/save_slot_thumb_bg.png", 6, 6, 5, 6)
    padding (6, 6, 5, 6)

style slot_button:
    hover_background "ui_images/button/save_slot_hover_bg.png"
    padding (16, 20, 9, 12)
    xfill True
    xysize (1012, 207)

style slot_button_vbox:
    spacing 4
    xsize 634
    yoffset 28

style slot_button_hbox:
    spacing 16

style slot_name_text is ui_text:
    hover_color "#bfa292"
    color "#85766e"
    xalign 0.0
    size 48
    bold True

style slot_date_text is ui_text:
    hover_color "#bfa292"
    color "#85766e"
    size 30

style delete_slot_buton:
    xysize (40, 40)
    background None
    hover_background "white"
    foreground "ui_images/button/delete_save_button.png"
    hover_foreground "ui_images/button/delete_save_button_hover.png"


screen load():
    zorder 810
    tag menu
    fixed:
        add "ui_images/bg_window.png"
        add "ui_images/saves_name.png" at:
            pos (673, 43)
        fixed:
            style_prefix "slots_vp"
            add "ui_images/textbox_bg.png" size (1098, 599)
            vpgrid:
                cols 1
                yinitial 0.0
                scrollbars "vertical"
                vscrollbar_unscrollable "hide"
                mousewheel True
                pagekeys True
                draggable True
                use save_slots_list()

        button action Return() style "back_button"


screen save():
    zorder 810
    fixed:
        add "ui_images/bg_window.png"
        add "ui_images/save_game_name.png" at:
            pos (673, 43)
        fixed:
            style_prefix "slots_vp"
            add "ui_images/textbox_bg.png" size (1098, 599)
            vpgrid:
                cols 1
                yinitial 0.0
                scrollbars "vertical"
                vscrollbar_unscrollable "hide"
                mousewheel True
                pagekeys True
                draggable True
                use save_slots_list(True)
        button action ShowMenu("game_menu") style "back_button"

style slots_vp_fixed:
    ypos 274
    xalign 0.5
    xysize (1098, 599)

style slots_vp_vpgrid:
    xfill True
