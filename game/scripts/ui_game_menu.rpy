init python:
    _game_menu_screen = "game_menu"

screen _game_menu(background):
    zorder 800
    fixed:
        add background at trans_blur_background
        add "ui_images/overlay/confirm.png"
        window:
            style_prefix "game_menu"
            vbox:
                button action Return():
                    background "ui_images/button/[prefix_]gm_continue.png"
                button action ShowMenu("save"):
                    background "ui_images/button/[prefix_]gm_save.png"
                button action ShowMenu("settings"):
                    background "ui_images/button/[prefix_]gm_settings.png"
                button action MainMenu():
                    background "ui_images/button/[prefix_]gm_exit.png"

style game_menu_window:
    anchor (0, 0)
    pos (576, 106)
    background "ui_images/pause_bg.png"
    xysize (690, 848)

style game_menu_vbox:
    anchor (0, 0)
    pos (123, 303)
    xsize 472
    spacing 8

style game_menu_button:
    xysize (472, 88)

transform trans_blur_background:
    pos (0, 0)
    size (1920, 1080)
    blur 19.0

label game_menu:
    default pause_screenshot = None
    python:
        renpy.hide_screen("hint")
        if not pause_screenshot:
            pause_screenshot = im.Data(renpy.screenshot_to_bytes((1920/2, 1080/2)), "screenshot.png")
        ss_save_pause()
        renpy.take_screenshot()
        renpy.call_screen("_game_menu", pause_screenshot)
        del pause_screenshot
        pause_screenshot = None
        ss_load_pause()