label splashscreen:
    image jam_splash = "ui_images/splash/jam_splash.png"
    image sf_splash = "ui_images/splash/splash_sf.png"

    scene black with None
    pause 0.5
    
    show jam_splash:
        zoom 0.5 xalign 0.5 yalign 0.5
    with dissolve
    pause 2.0
    hide jam_splash with dissolve

    pause 0.5

    show sf_splash:
        xalign 0.5 yalign 0.5
    with dissolve
    pause 2.0
    hide sf_splash with dissolve

    pause 0.5


