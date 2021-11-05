init offset = -1

init:
    image white = "#ffffff"


style ui_text:
    font gui.interface_text_font
    size 40
    color "#ffffff"

style secondary_screen_title is ui_text:
    size 60
    xalign 0.5
    yalign 0.2

style back_button:
    background None
    hover_background "white"
    xsize 1920/3
    xalign 0.5
    yalign 1.0
    yoffset -32

style back_button_text is ui_text:
    hover_color "#000000"
    xalign 0.5
    yalign 0.5

define gui.vscrollbar_borders = Borders(6, 6, 6, 6)

style vscrollbar:
    xsize 10
    base_bar Frame("ui_images/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=False)
    thumb Frame("ui_images/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=False)
