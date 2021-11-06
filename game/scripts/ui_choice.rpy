screen choice(items):
    vbox:
        style_prefix "choice"
        for item in items:
            if item.action:
                textbutton item.caption action item.action
            else:
                window:
                    text item.caption

style choice_vbox:
    xalign 0.5
    yalign 1.0
    yoffset -28
    spacing 5
    xsize 1331

style choice_button:
    xysize (1331, 107)
    background "ui_images/button/[prefix_]choice.png"
    padding (19, 18, 1331-1292-19, 107-71-18)

style choice_window:
    xysize (1331, 107)
    background "ui_images/button/idle_choice.png"
    padding (19, 18, 1331-1292-19, 107-71-18)

style choice_button_text is bubble_text:
    xalign 0.5
    yalign 0.5
    size 42

style choice_text is choice_button_text