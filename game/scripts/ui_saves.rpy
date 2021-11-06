screen save_slots_list(for_save=False):
    python:
        save_slots = ss_list_save_slots()
        new_slot_index = ss_new_save_index(save_slots)
    if for_save: # "New save file" button
        button action SaveSlotAction(for_save, new_slot_index) style "slot_button":
            default_focus for_save
            hbox:
                style "slot_button_hbox"
                add "ui_images/new_save_slot.png"
                vbox:
                    style "slot_button_vbox"
                    text _("Новое сохранение") style "slot_name_text"
                    text " " style "slot_date_text"
    $ focus_value = not for_save
    for (slot_index, slot_description, slot_thumbnail, slot_utime) in save_slots:
        button action SaveSlotAction(for_save, slot_index) style "slot_button":
            default_focus focus_value
            $ focus_value = False
            hbox:
                style "slot_button_hbox"
                add slot_thumbnail xsize config.thumbnail_width ysize config.thumbnail_height
                vbox:
                    style "slot_button_vbox"
                    text slot_description style "slot_name_text"
                    text ss_format_save_time(slot_utime) style "slot_date_text"
                if not for_save:
                    button:
                        style "delete_slot_buton"
                        action ConfirmWithButtons(
                            _("Удалить это сохранение? Его нельзя будет восстановить."),
                            yes=DeleteSaveSlot(slot_index),
                            yes_label=_("Удалить"), no_label=_("Отмена")
                        )
                if not for_save:
                    key "save_delete" action ConfirmWithButtons(
                                _("Удалить это сохранение? Его нельзя будет восстановить."),
                                yes=DeleteSaveSlot(slot_index),
                                yes_label=_("Удалить"), no_label=_("Отмена")
                            )

style slot_button:
    hover_background "ui_images/button/save_slot_hover_bg.png"
    padding (20, 8, 16, 20)
    xfill True
    ysize 94

style slot_button_vbox:
    spacing 4
    xsize 700

style slot_button_hbox:
    spacing 16

style slot_name_text is ui_text:
    color "#ffffff"
    xalign 0.0
    size 40

style slot_date_text is slot_name_text:
    size 20

style delete_slot_buton:
    xysize (40, 40)
    background None
    hover_background "white"
    foreground "ui_images/button/delete_save_button.png"
    hover_foreground "ui_images/button/delete_save_button_hover.png"


screen load():
    tag menu
    fixed:
        add "ui_images/main_menu_background.png"
        text _("Продолжить с сохранения") style "secondary_screen_title"
        fixed:
            style_prefix "slots_vp"
            vpgrid:
                cols 1
                yinitial 0.0
                scrollbars "vertical"
                vscrollbar_unscrollable "hide"
                mousewheel True
                pagekeys True
                draggable True
                use save_slots_list()

        textbutton _("Вернуться") action Return() style "back_button"

style slots_vp_fixed:
    xalign 0.5
    yanchor 0.0
    ypos 0.25
    xsize (1920/2+10)
    ysize (1080/2+102)

style slots_vp_vpgrid:
    xfill True
