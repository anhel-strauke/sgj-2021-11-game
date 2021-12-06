init python:
    _game_menu_screen = "game_menu"
    pause_screenshot = None

screen _game_menu():
    zorder 800
    fixed:
        #add background at trans_blur_background
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
    blur 1.0
    linear 0.3 blur 5.0

label game_menu:
    python:
        renpy.hide_screen("hint")
        try:
            if not pause_screenshot:
                pause_screenshot = im.Data(renpy.screenshot_to_bytes((1920/10, 1080/10)), "screenshot.png")
        except NameError:
            pause_screenshot = im.Data(renpy.screenshot_to_bytes((1920/10, 1080/10)), "screenshot.png")
        #ss_save_pause()
    show expression pause_screenshot as pause_screenshot at trans_blur_background
    with None
    pause 0.3
    call screen _game_menu
    hide pause_screenshot
    with None
    python:
        del pause_screenshot
        pause_screenshot = None
        #ss_load_pause()