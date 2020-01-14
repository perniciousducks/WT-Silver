
# The game starts here
label start:
    call wardrobe_init

    $ save_internal_version = config.version
    $ achievement_fix()

    $ restart_achievements_thread()

    $ start_image_crop()
    #scene black
    jump start_wt

init python:
    renpy.music.register_channel("bg_sounds", "sfx", True)
    renpy.music.register_channel("weather", "sfx", True)
