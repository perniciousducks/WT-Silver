screen _performance():
    zorder 1000
    layer "interface"

    on "show" action Function(_clear_performance)

    python:
        frame_times = renpy.display.interface.frame_times

        if len(frame_times) < 11:
            fps = 0.0
            cur_time = 0
            max_time = 0
        else:
            ift = [ (j - i) for i, j in zip(frame_times, frame_times[1:]) ]

            fps = 1.0 / (sum(ift[-10:]) / 10.0)

            cur_time = ift[-1] * 1000
            max_time = max(ift) * 1000

    drag:
        draggable True
        focus_mask None
        xpos 0
        ypos 0

        frame:
            style_prefix "_performance"
            style "empty"
            background "#0004"
            xpadding 5
            ypadding 5
            xminimum 150

            vbox:
                text "[fps:.1f] fps\n[cur_time:.3f] ms\n[max_time:.3f] ms max":
                    style "_default"
                    color "#fff"
                    size gui._scale(14)

                if _preferences.gl_powersave:
                    $ mode = "powersave"
                else:
                    $ mode = "performance"

                textbutton "[mode]":
                    style "_default"
                    action Preference("gl powersave", "toggle")
                    text_color "#ddd"
                    text_hover_color "#fff"
                    text_size gui._scale(14)

screen _image_load_log():
    zorder 1500
    layer "interface"

    default show_help = True

    style_prefix ""

    python:
        load_log = list(renpy.get_image_load_log(5))
        tex_size, tex_count = renpy.get_texture_size()
        tex_size_mb = tex_size / 1024.0 / 1024.0

        cache_size = renpy.display.im.cache.get_current_size(2)
        cache_size_mb = cache_size * 4.0 / 1024 / 1024
        cache_pct = 100.0 * cache_size / renpy.display.im.cache.cache_limit

    drag:
        draggable True
        focus_mask None
        xpos 0
        ypos 0

        frame:
            style "empty"
            background "#0004"
            xpadding 5
            ypadding 5
            xminimum 200

            has vbox

            text _("Textures: [tex_count] ([tex_size_mb:.1f] MB)"):
                size 14
                color "#fff"

            text _("Image cache: [cache_pct:.1f]% ([cache_size_mb:.1f] MB)"):
                size 14
                color "#fff"

            if load_log:
                text "\n" size 14

            for when, filename, preload in load_log:
                if preload:
                    $ color="#ccffcc"
                    $ prefix=__("✔ ")
                else:
                    $ color="#ffcccc"
                    $ prefix=__("✘ ")

                text "[prefix][filename!q]" color color size 14

            if show_help:
                text _("\n{color=#cfc}✔ predicted image (good){/color}\n{color=#fcc}✘ unpredicted image (bad){/color}\n{color=#fff}Drag to move.{/color}"):
                    size 14

    timer 10.0 action SetScreenVariable("show_help", False)
