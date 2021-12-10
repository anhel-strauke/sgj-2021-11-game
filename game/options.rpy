## Game itself
define config.name = _("Курьерская История")
define config.version = "0.3"
define build.name = "CourierStory"

define config.has_sound = True
define config.has_music = True
define config.has_voice = False
# define config.sample_sound = "sample-sound.ogg"
# define config.sample_voice = "sample-voice.ogg"

# define config.main_menu_music = "main-menu-theme.ogg"

## Default transitions

define config.enter_transition = dissolve
define config.exit_transition = dissolve


## Main menu transitions

define config.intra_transition = Dissolve(0.3)
define config.after_load_transition = fade
define config.end_game_transition = fade
define config.end_splash_transition = Dissolve(1.0)
define config.game_main_transition = fade

## Dialog window behavior

define config.window = "hide"
define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)

define config.enter_yesno_transition = Dissolve(0.1)
define config.exit_yesno_transition = Dissolve(0.1)

## Dialog text settings

default preferences.text_cps = 80
default preferences.afm_time = 15

# Display settings

default preferences.fullscreen = True
default preferences.gl_powersave = False
define config.cache_surfaces = True


## Save system settings

define config.has_autosave = False
define config.autosave_slots = 0

define config.thumbnail_width = 279
define config.thumbnail_height = 157

define config.rollback_enabled = True
default quick_menu = True

## Save directory #############################################################
##
## Windows: %APPDATA\RenPy\<config.save_directory>
##
## Macintosh: $HOME/Library/RenPy/<config.save_directory>
##
## Linux: $HOME/.renpy/<config.save_directory>
##

define config.save_directory = "delivery_story-1633105503"

define config.window_icon = "ui_images/window_icon.png"

## Distribution build setup ####################################################

init python:
    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)

    build.classify('**/*.rpy', None) # Clean up game sources, leave bytecode only
    build.classify('**/*.rpym', None)
    build.classify('**/LICENSE', None)
    build.classify('game/cache/*.*', None)

    build.classify('game/**.rpyc', 'archive')
    build.classify('game/**.rpymc', 'archive')

    build.classify('game/**.png', 'archive')
    build.classify('game/**.jpg', 'archive')
    build.classify('game/**.ttf', 'archive')

    build.documentation('*.html')
    # build.documentation('*.txt')
