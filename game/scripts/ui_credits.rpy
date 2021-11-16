init:
    define game_credits = [
        {
            "name": "Дина Грико",
            "role": ["Концепция", "Управление проектом"]
        },
        {
            "name": "Тимирлан Кенджибаев",
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


    scene black with dissolve
    
    $ renpy.pause(5.0, hard=True)
    pause 40
    scene black with dissolve

    python:
        quick_menu = old_quick_menu
        murphymeter_visible = old_murphymeter_visible
        config.rollback_enabled = old_rollback_enabled
        config.allow_skipping = old_skip_allowed
    return
