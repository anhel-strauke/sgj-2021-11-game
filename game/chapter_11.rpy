init:
    image bridge_layer_1 = Composite((1964 * 2, 1080), (0, 0), "bridge_l1", (1964, 0), "bridge_l1")
    image bridge_layer_2 = Composite((3840 * 2, 614), (0, 0), "bridge_l2", (3840, 0), "bridge_l2")
    image bridge_layer_3 = Composite((2240 * 2, 680), (0, 0), "bridge_l3", (2240, 0), "bridge_l3")
    image bridge_layer_4= Composite((2070 * 2, 399), (0, 0), "bridge_l4", (2070, 0), "bridge_l4")
    image bridge_layer_5 = Composite((1920 * 2, 698), (0, 0), "bridge_l5", (1920, 0), "bridge_l5")

    transform trans_bridge_moving_layer(target_x, base_y, t):
        anchor (0, 0)
        ypos base_y
        block:
            xpos target_x
            linear t xpos 0
            repeat
    
    transform trans_bridge_zep:
        anchor (0, 0)
        ypos 29
        xpos 558
        linear 175 xpos -387
        block:
            5.0
            xpos 1920
            linear 420.0 xpos -387
            repeat

label chapter_11:
    scene black
    with dissolve

    $ renpy.maximum_framerate(3600 * 24 * 365) # Максимальный FPS на год

    show bridge_layer_1 at trans_bridge_moving_layer(-1964, 0, 120.0)
    show bridge_layer_2 at trans_bridge_moving_layer(-3840, 0, 108.0)
    show bridge_zep at trans_bridge_zep
    show bridge_layer_3 at trans_bridge_moving_layer(-2240, 0, 36.0)
    show bridge_layer_4 at trans_bridge_moving_layer(-2070, 393, 16.0)
    show bridge_layer_5 at trans_bridge_moving_layer(-1920, 382, 0.8)
    with dissolve

    pause 1.0

    show gg_ride:
        xzoom -0.3
        yzoom 0.3
        anchor (0.5, 1.0)
        ypos 1320
        xpos 2579
        easein_quad 1.0 xpos 1360
    pause 1.0
    show gg_ride:
        xpos 1360
    
    pause

    $ renpy.maximum_framerate(None)

    $ map_info = ("11-12", "chapter_12")
    jump map