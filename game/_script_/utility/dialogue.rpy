
# Handling of doll transitions in dialogue

define sprite_pos = {
    "x": {
        "base": 640,
        "default": 640,
        "far_right": 640,
        "mid": 300,
        "left": 200,
        "far_left": -80,
        "right": 400,
        "wardrobe": 540,
        "close": 540
    },

    "y": {
        "base": 0,
        "default": 0,
        "head": 200,
        "low": 170
    }
}

default last_doll_images = dict()
default last_say_who = None

transform doll_transition(old_img, new_img, trans=d3):
    old_img
    new_img with trans

init python:
    config.all_character_callbacks.append(set_last_say)
    config.mode_callbacks.append(reset_last_say)
    config.interact_callbacks.append(track_skipping_interact)

    after_skip_callbacks.append(update_doll_transitions)

init -1 python:
    def apply_doll_transition(doll_new, scr_name, use_head):
        """Apply a transition between old and new images of a doll."""
        doll_old = last_doll_images.get(scr_name, None)

        if doll_new != doll_old and not renpy.in_rollback():
            if not doll_old or (use_head and last_say_who != get_say_who()):
                doll_old = doll_new

            last_doll_images[scr_name] = doll_new

            return doll_transition(doll_old, doll_new)

        return doll_new

    def update_doll_transitions():
        """Used after skip to update doll images on all visible character screens."""
        for doll in [astoria, cho, hermione, tonks]:
            doll.apply_transition()

    def get_say_who():
        say_screen = renpy.get_screen("say")
        if say_screen:
            return say_screen.scope["who"]
        else:
            return None

    def reset_last_say(mode, modes):
        """Unset last speaking character on mode change (esp. when a sequence of say statements begins or ends)"""
        global last_say_who
        last_say_who = None

    def set_last_say(event, interact=True, **kwargs):
        """Keep track of the character that has most recently spoken"""
        global last_say_who
        if event == "show_done":
            last_say_who = get_say_who()

    was_skipping = False
    after_skip_callbacks = []
    def track_skipping_interact():
        """Determines if the game started or stopped skipping and invokes callbacks after skip."""
        global was_skipping
        if not was_skipping and renpy.is_skipping():
            # Skipping started
            was_skipping = True
        elif was_skipping and not renpy.is_skipping():
            # Skipping stopped
            was_skipping = False
            for c in after_skip_callbacks:
                c()
