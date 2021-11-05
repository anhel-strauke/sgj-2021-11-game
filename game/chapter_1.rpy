label start:
    scene black

    pause 1.0

    show bg home:
        xalign 0.5 yalign 0.5 alpha 0.0 zoom 1.0
        parallel:
            easein 1.0 alpha 1.0
        parallel:
            easeout 1.5 zoom 0.5
    pause 2.0
    show bg home:
        xalign 0.5 yalign 0.5 alpha 1.0 zoom 0.5

    show cat temporary:
        anchor (0.5, 1.0) zoom 0.6 xpos 1920-400 ypos 0.95
    with moveinright

    pause



    return

    jump chapter_2
