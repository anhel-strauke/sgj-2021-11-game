init offset = -1

init:
    image white = "#ffffff"


style bubble_text:
    font gui.text_font
    size 48
    color "#000000"
    italic True

style bubble_name_text is bubble_text:
    font gui.name_text_font
    size 54
    bold True
    italic False

style ui_text:
    font gui.interface_text_font
    size 40
    color "#ffffff"

style secondary_screen_title is ui_text:
    size 60
    xalign 0.5
    yalign 0.2

style back_button:
    xysize (472, 88)
    background "ui_images/button/[prefix_]back.png"
    xalign 0.5
    yalign 1.0
    yoffset -73

style back_button_text is ui_text:
    hover_color "#000000"
    xalign 0.5
    yalign 0.5

style vscrollbar:
    xsize 20
    base_bar Frame("ui_images/scrollbar/vertical_idle_bar2.png", tile=False)
    thumb Frame("ui_images/scrollbar/vertical_idle_bar1.png", 4, 8, 4, 6, tile=False)
