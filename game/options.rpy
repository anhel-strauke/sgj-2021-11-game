## Game itself
define config.name = _("delivery_story")
define config.version = "0.1"
define build.name = "DeliveryStory"

define config.has_sound = False
define config.has_music = True
define config.has_voice = False
# define config.sample_sound = "sample-sound.ogg"
# define config.sample_voice = "sample-voice.ogg"

# define config.main_menu_music = "main-menu-theme.ogg"

## Default transitions

define config.enter_transition = dissolve
define config.exit_transition = dissolve


## Main menu transitions

define config.intra_transition = CropMove(0.3, "slideawayright")
define config.after_load_transition = None
define config.end_game_transition = None

## Dialog window behavior

define config.window = "auto"
define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)


## Dialog text settings

default preferences.text_cps = 80
default preferences.afm_time = 15

## Save system settings

define config.has_autosave = False
define config.autosave_slots = 0

define config.thumbnail_width = 133
define config.thumbnail_height = 75

## Директория сохранений #######################################################
##
## Контролирует зависимое от платформы место, куда Ren'Py будет складывать файлы
## сохранения этой игры. Файлы сохранений будут храниться в:
##
## Windows: %APPDATA\RenPy\<config.save_directory>
##
## Macintosh: $HOME/Library/RenPy/<config.save_directory>
##
## Linux: $HOME/.renpy/<config.save_directory>
##
## Этот параметр обычно не должен изменяться, а если и изменился, должен быть
## текстовой строчкой, а не выражением.

define config.save_directory = "delivery_story-1633105503"


## Иконка ######################################################################
##
## Иконка, показываемая на панели задач или на dock.

define config.window_icon = "ui_images/window_icon.png"


## Настройка Дистрибутива ######################################################
##
## Эта секция контролирует, как Ren'Py строит дистрибутивные файлы из вашего
## проекта.

init python:

    ## Следующие функции берут образцы файлов. Образцы файлов не учитывают
    ## регистр и соответствующе зависят от директории проекта (base), с или без
    ## учёта /, задающей директорию. Если обнаруживается множество одноимённых
    ## файлов, то используется только первый.
    ##
    ## Инструкция:
    ##
    ## / — разделитель директорий.
    ##
    ## * включает в себя все символы, исключая разделитель директорий.
    ##
    ## ** включает в себя все символы, включая разделитель директорий.
    ##
    ## Например, "*.txt" берёт все файлы формата txt из директории base, "game/
    ## **.ogg" берёт все файлы ogg из директории game и всех поддиректорий, а
    ## "**.psd" берёт все файлы psd из любого места проекта.

    ## Классифицируйте файлы как None, чтобы исключить их из дистрибутивов.

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)

    build.classify('**/*.rpy', None) # Clean up game sources, leave bytecode only
    build.classify('game/**.rpyc', 'archive')

    ## Чтобы архивировать файлы, классифицируйте их, например, как 'archive'.

    # build.classify('game/**.png', 'archive')
    # build.classify('game/**.jpg', 'archive')

    ## Файлы, соответствующие образцам документации, дублируются в приложениях
    ## Mac, чтобы они появлялись и в приложении, и в zip архиве.

    build.documentation('*.html')
    # build.documentation('*.txt')


## Лицензионный ключ Google Play требуется для загрузки файлов расширений и
## поддержки внутриигровых покупок. Он может быть найден на странице "Services &
## APIs" консоли разработчика Google Play.

# define build.google_play_key = "..."


## Имя пользователя и название проекта, ассоциированные с проектом на itch.io,
## разделённые дробью.

# define build.itch_project = "renpytom/test-project"
