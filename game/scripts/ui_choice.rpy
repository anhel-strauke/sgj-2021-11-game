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
    xsize 991

style choice_button:
    xysize (991, 110)
    background "ui_images/button/[prefix_]choice.png"
    padding (116, 12, 991-116-844, 110-77-12)

style choice_window is choice_button

style choice_button_text is bubble_text:
    xalign 0.5
    yalign 0.5
    size 42

style choice_text is choice_button_text