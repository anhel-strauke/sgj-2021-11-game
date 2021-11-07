init python:
    import math

init:
    default murphymeter_visible = True
    default Myo_value = 0
    default money_value = 0
    default Myo_current = 0.0
    default money_current = 0
    define Myo_step = 1.0/30.0

init python:
    def update_murphymeter():
        global Myo_value, Myo_current, Myo_step
        fval = float(Myo_value)
        diff = abs(fval - Myo_current)
        if diff <= Myo_step or renpy.in_rollback():
            Myo_current = Myo_value
            renpy.restart_interaction()
            return
        if renpy.is_skipping():
            Myo_current = Myo_value
        if Myo_current < fval:
            Myo_current += Myo_step
        else:
            Myo_current -= Myo_step
        renpy.restart_interaction()
    
    def update_money():
        global money_value, money_current
        if renpy.is_skipping() or renpy.in_rollback():
            money_current = money_value
        if money_current < money_value:
            money_current += 1
        elif money_current > money_value:
            money_current -= 1
        renpy.restart_interaction()     

screen murphymeter():
    zorder 101
    if murphymeter_visible:
        fixed:
            at trans_murphymeter
            add "ui_images/murphymeter/m_background.png" at:
                pos (587, 0)
            bar value int(100.0 * Myo_current) range 300 style "murph_bar":
                pos (587 + 128, 19)
            if Myo_current >= 3:
                add "ui_images/murphymeter/m_bar_red.png" at trans_murph_red_bar
            add "ui_images/murphymeter/m_foreground.png" at:
                pos (587, 0)
            vbox style "money_vbox":
                pos (927, 85)
                text str(money_current) style "money_text"
            if Myo_value != Myo_current:
                timer (1.0/30.0) action update_murphymeter repeat True
            if money_value != money_current:
                timer (1.0/10.0) action update_money repeat True

style murph_bar:
    xysize (489, 29)
    bar_resizing False
    left_bar "ui_images/murphymeter/m_bar.png"

style money_vbox:
    xysize (39, 32)

style money_text is ui_text:
    size 32
    bold True
    color "#d59f62"
    align (1.0, 0.0)

transform trans_murphymeter:
    on show:
        ypos -175
        linear 0.5 ypos 0
    on hide:
        linear 0.5 ypos -175

transform trans_murph_red_bar:
    pos (587 + 128, 19)
    size (489, 29)
    block:
        alpha 0.0
        0.3
        alpha 1.0
        0.3
        repeat   

init python:
    config.overlay_screens.append("murphymeter")
