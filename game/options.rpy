# Ren'Py configuration
define title_version = config.version if len(config.version) < 5 else (config.version[:4] + "." + config.version[4:6])

init -1 python hide: 
    # Internal name and version
    config.name    = "WT Silver" # EXPERIMENTAL VERSION
    config.version = "1.372"

    # Window
    title_version = config.version if len(config.version) < 5 else (config.version[:4] + "." + config.version[4:6])
    config.window_title = "Witch Trainer (Silver) %s" % title_version # EXPERIMENTAL VERSION
    config.window_icon = "interface/icon.png"

    # Window size
    # 16:9 = 1080x600
    # 4:3 = 800x600
    config.screen_width = 1080
    config.screen_height = 600

    config.save_physical_size = True # Save the window size in preferences

    # Garbage collector
    config.manage_gc = True
    config.gc_thresholds = (25000, 10, 10)
    config.idle_gc_count = 2500
    gc_print_unreachable = False
    
    # Graphics
    config.gl_enable = True # Enable openGL acceleration
    config.gl_clear_color = "#000"
    config.hw_video = True
    config.nearest_neighbor = False # Disable pixel art filtering

    # Image cache
    config.cache_surfaces = False # Use image cache
    # config.image_cache_size = 32 # Number of screens worth of images in cache
    config.image_cache_size_mb = 1024 # Image cache size in megabytes
    config.load_before_transition = True # Preload assets (images, sounds etc.) before transition

    # Sound
    config.has_sound = True # Set this to False if the game does not have any sound effects.
    config.has_music = True # Set this to False if the game does not have any music.
    config.has_voice = False # Set this to True if the game has voicing

    config.sound_sample_rate = 48000

    config.main_menu_music = "music/01 Prologue.mp3"
    # config.enter_sound = "click.wav" # Sound that is played when entering the game menu
    # config.exit_sound = "click.wav" # Sound that is played when exiting the game menu
    # config.sample_sound = "click.wav" # Sound that can be played to check the sound volume

    # Default persistent values
    if persistent.delwarning == None:
        persistent.delwarning = True
        persistent.customcursor = False
        persistent.autosave = False
        persistent.tooltip = True

    # Preferences
    config.default_fullscreen = False # Default fullscreen preference
    config.default_text_cps = 40 # Default text speed preference (characters per second, 0 is infinite)
    config.default_afm_time = 40 # Default auto-forward time preference

    # Load custom preference options
    if persistent.customcursor: 
        config.mouse = { 'default' : [ ('interface/cursor.png', 0, 0)] } # Set custom pointer
    else: 
        config.mouse = None

    if persistent.autosave: #True if true, false otherwise, still saves upon exit no matter what
        config.has_autosave = True
        config.autosave_on_choice = True
    else: 
        config.has_autosave = False
        config.autosave_on_choice = False
        config.autosave_on_quit = True

    config.autoreload = False # If False, Ren'Py will reload the game once per press of shift+R

    # Development
    config.developer = "auto" # Will detect if you're using Renpy launcher, if not it will turn off the console
    config.debug = False # Use ONLY for testing, disable before release

    # Help feature
    config.help = None
    # config.help = "README.html"
    # config.help = "LABEL"

    # Transitions
    config.enter_transition         = None # Used when entering the game menu from the game
    config.exit_transition          = None # Used when exiting the game menu to the game
    config.intra_transition         = None # Used between screens of the game menu
    config.main_game_transition     = None # Used when entering the game menu from the main menu
    config.game_main_transition     = None # Used when returning to the main menu from the game
    config.end_splash_transition    = Dissolve(.3) # Used when entering the main menu from the splashscreen
    config.end_game_transition      = Dissolve(.7) # Used when entering the main menu after the game has ended
    config.after_load_transition    = Dissolve(.3) # Used when a game is loaded
    config.window_show_transition   = Dissolve(.3) # Used when the window is shown
    config.window_hide_transition   = Dissolve(.3) # Used when the window is hidden
    config.adv_nvl_transition       = dissolve # Used when showing NVL-mode text directly after ADV-mode text
    config.nvl_adv_transition       = dissolve # Used when showing ADV-mode text directly after NVL-mode text
    config.enter_yesno_transition   = None # Used when yesno is shown
    config.exit_yesno_transition    = None # Used when the yesno is hidden
    config.enter_replay_transition  = None # Used when entering a replay
    config.exit_replay_transition   = None # Used when exiting a replay
    config.say_attribute_transition = None # Used when the image is changed by a say statement with image attributes

    # Gameplay
    config.hard_rollback_limit = 100
    config.narrator_menu = True # If True, then display menu narration using narrator character

    config.quit_action = Quit(True)

# Save directory needs to be set in `python early` block
python early: 
    config.save_directory = "WT SILVER"

# Build configuration
# https://www.renpy.org/doc/html/build.html
init python hide: 
    build.directory_name = "WT_Silver_%s" % title_version # Name directories and archive files
    build.executable_name = "WT Silver" # Name for executables
    build.include_update = False # If True, include update information into packages (allows the updater to run)
    
    build.classify("**.exe", None)
    build.classify("**.psd", None)
    build.classify("**.psd~", None)
    build.classify("**.old", None)
    build.classify('**.bak', None)
    build.classify("**.kra", None)
    build.classify("**.kra~", None)
    build.classify("**.txt", None)
    build.classify("**.xml", None)
    build.classify('**/thumbs.db', None)
    build.classify('saves/**', None)
    build.classify('outfits/**', None)
    