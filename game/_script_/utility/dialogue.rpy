
# Handling of doll transitions in dialogue

default last_doll_images = dict()
default last_say_who = None

transform doll_transition(old_img, new_img, trans=d3):
    old_img
    new_img with trans

init python:
    config.all_character_callbacks.append(set_last_say)
    config.mode_callbacks.append(reset_last_say)

init -1 python:
    def apply_doll_transition(doll, scr_name, img_name, use_head):
        """Apply a transition between old and new images of a doll that's on screen"""
        doll_new = doll.get_image()
        doll_old = last_doll_images.get(scr_name, None)

        if doll_new != doll_old:
            if not doll_old or (use_head and last_say_who != get_say_who()):
                doll_old = doll_new

            scope = renpy.get_screen(scr_name).scope
            scope[img_name] = doll_transition(doll_old, doll_new)

            last_doll_images[scr_name] = doll_new

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
