init:
    define game_credits = [
        {
            "name": "Дина Грико",
            "role": ["Концепция", "Управление проектом"]
        },
        {
            "name": "Тимирлан Кенжибаев",
            "role": ["Сценарий", "Тексты"]
        },
        {
            "name": "Наталья «NielNoel» Субботина-Чукальская",
            "role": ["Сценарий", "Тексты"]
        },
        {
            "name": "Яна Юрцевич",
            "role": ["Концепт-арт", "Персонажи"]
        },
        {
            "name": "Ольга «Rindelin» Сердюк",
            "role": ["Фоны"]
        },
        {
            "name": "Анна «Крапива» Тимофеева",
            "role": ["Интерфейс"]
        },
        {
            "name": "Анатолий «Анхель» Грико",
            "role": ["Программирование", "Анимации", "Укрощение движка"]
        },
        {
            "name": "Ekko",
            "role": ["Программирование", "Анимации"]
        },
        {
            "name": "Ziczin",
            "role": ["Музыка"]
        },
    ]

    define credits_full_time = 33
    define credits_darkness_time = 0.5
    define credits_before_movement_time = 2.5
    define credits_unskipable_time = 8
    define credits_moving_time = 25

    define credits_name_text_size = 60
    define credits_role_text_size = 50
    define credits_team_title_text_size = 80
    define credits_block_margin = 240
    define credits_name_margin = 20

    style credits_name_text:
        font "BloggerSans.ttf"
        size credits_name_text_size
        color "#e0e0e0"
        xalign 0.5
        text_align 0.5
    
    style credits_role_text:
        font "BloggerSans.ttf"
        size credits_role_text_size
        color "#e0e0e0"
        italic True
        xalign 0.5
        text_align 0.5
    
    style credits_team_title_text is credits_name_text:
        color "#ffffff"
        size credits_team_title_text_size
    
    style credits_final_phrase is credits_name_text:
        size 50
        italic True
    style credits_final_copyright_text is credits_name_text:
        text_align 0.0
        size 40
    
    transform trans_credits_cat:
        size (300, 272)
        align (1.0, 1.0)
        offset (-20, -20)
        alpha 0.0
        credits_moving_time+credits_before_movement_time+0.5
        linear 0.5 alpha 1.0
    
    image credits_black = "#000000"
    image game_logo = "ui_images/game_logo.png"
    image scientific_forest_text = Text(_("Команда Scientific Forest"), slow=False, style="credits_team_title_text")
    image credits_cat = "ui_images/window_icon.png"
    image credits_final_text = Fixed(
        Text(_("Играйте в хорошие игры\nи берегите себя."), slow=False, align=(0.5, 0.5), style="credits_final_phrase"),
        Text(_("© 2021 Scientific Forest"), align=(0.0, 1.0), offset=(20, -40), style="credits_final_copyright_text"),
        At("credits_cat", trans_credits_cat),
        xsize=1920, ysize=1080, anchor=(0.0, 0.0)
    )

init python:
    def credits_make_scene():
        global game_credits
        height = 0
        items = []
        for item in game_credits:
            item_displayables = [Text(item["name"], slow=False, style="credits_name_text"), Null(height=credits_name_margin)]
            height += credits_name_text_size + credits_name_margin
            for role in item["role"]:
                item_displayables.append(Text(role, slow=False, style="credits_role_text"))
                height += credits_role_text_size
            items.append(VBox(*item_displayables, xalign=0.5, spacing=0, xsize=1920))
            items.append(Null(height=credits_block_margin))
            height += credits_block_margin
        return (height, VBox(*items, spacing=0, xalign=0.5, xsize=1920))
    
    def credits_make_about_text():
        global game_credits
        result = []
        for item in game_credits:
            roles_str = ", ".join([s.lower() for s in item["role"]])
            result.append(item["name"] + " — " + roles_str)
        return "{vspace=24}".join(result)

label credits:
    python:
        old_quick_menu = quick_menu
        quick_menu = False
        old_murphymeter_visible = murphymeter_visible
        murphymeter_visible = False
        old_rollback_enabled = config.rollback_enabled
        config.rollback_enabled = False
        old_skip_allowed = config.allow_skipping
        config.allow_skipping = False
        ss_game_end()

    $ (cr_height, cr_vbox) = credits_make_scene()
    $ cr_height += credits_team_title_text_size + credits_block_margin

    scene black
    with dissolve

    show credits_black:
        size (1920, 1080 * 2 + cr_height)
        anchor (0.0, 0.0)
        pos (0, 0)

    show game_logo:
        align (0.5, 0.5)
        alpha 0.0
        credits_darkness_time
        linear 0.5 alpha 1.0

    show scientific_forest_text:
        anchor (0.5, 0.0)
        pos (960, 1080)

    show expression cr_vbox:
        anchor (0.5, 0.0)
        pos (960, 1080 + credits_team_title_text_size + credits_block_margin)
    
    show credits_final_text:
        anchor (0, 0)
        pos (0, 1080 + cr_height)

    camera:
        xpos 0
        ypos 0
        credits_before_movement_time
        easeout 1 ypos -100 
        linear (credits_moving_time - 1) ypos -(1080 + cr_height)

    $ renpy.pause(credits_unskipable_time, hard=True)
    pause (credits_full_time - credits_unskipable_time)
    
    show credits_black as credits_overlay:
        size (1920, 1080 * 2 + cr_height)
        align (0.0, 0.0)
        pos (0, 0)
    with dissolve

    python:
        quick_menu = old_quick_menu
        murphymeter_visible = old_murphymeter_visible
        config.rollback_enabled = old_rollback_enabled
        config.allow_skipping = old_skip_allowed
    return
