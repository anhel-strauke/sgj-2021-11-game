init python:
    class NonRollbackValue(NoRollback):
        def __init__(self, val=None):
            self.value=val

    class SkipIfEnable(Action, DictEquality):
        def __init__(self, var):
            self._var = var
        
        def __call__(self):
            if self._var.value:
                Skip()()

init:
    define q_enable_skip = NonRollbackValue(False)

screen quick_hint_rollback():
    tag hint
    zorder 500
    window:
        ypos 831
        style_prefix "hint"
        text _("Отменить")

screen quick_hint_skip():
    tag hint
    zorder 500
    window:
        ypos 909
        style_prefix "hint"
        text _("Перемотка")

screen quick_hint_menu():
    tag hint
    zorder 500
    window:
        ypos 987
        style_prefix "hint"
        text _("Пауза")


style hint_window:
    xpos 1798
    yoffset 10
    anchor (1.0, 0.0)
    background "ui_images/button/q_hint_background.png"
    xysize (174, 50)

style hint_text is ui_text:
    size 30
    bold True
    align (0.5, 0.5)
    color "#000000"
    

screen quick_menu():
    zorder 500
    fixed:
        at trans_quick_menu
        style_prefix "quick_menu"
        if quick_menu:
            fixed:
                add "ui_images/button/q_background.png" at:
                    anchor (0, 0)
                    pos (1832, 846)
                vbox:
                    button action [Hide("hint"), Rollback()] hovered Show("quick_hint_rollback") unhovered Hide("hint"):
                        background "ui_images/button/[prefix_]q_rollback.png"
                    button action Function(renpy.choice_for_skipping):
                        hovered [Show("quick_hint_skip"), SetField(q_enable_skip, "value", True)]
                        unhovered [Hide("hint"), SetField(q_enable_skip, "value", False)]
                        key "mousedown_1" action [Hide("hint"), SkipIfEnable(q_enable_skip)]
                        background "ui_images/button/[prefix_]q_skip.png"
                    button action [Hide("hint"), ShowMenu(_game_menu_screen)] hovered Show("quick_hint_menu") unhovered Hide("hint"):
                        background "ui_images/button/[prefix_]q_menu.png"

style quick_menu_vbox:
    align (1.0, 1.0)
    offset (-26, -21)
    spacing 3

style quick_menu_button:
    xysize (84, 74)
    xalign 1.0 yalign 1.0

transform trans_quick_menu:
    on show:
        xpos 115
        linear 0.5 xpos 0
    on hide:
        xpos 0
        linear 0.5 xpos 115

screen skip_indicator():
    zorder 499
    fixed:
        add "ui_images/overlay/skip_overlay.png"
        text "ПЕРЕМОТКА >>>":
            color "#ffffff"
            bold True
            font "BloggerSans.ttf"
            pos (80, 80)
            size 60

init python:
    config.overlay_screens.append("quick_menu")