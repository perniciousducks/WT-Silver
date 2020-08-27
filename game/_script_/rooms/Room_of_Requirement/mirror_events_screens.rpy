image dark_overlay:
    "images/rooms/room_of_requirement/dark_overlay_1.webp" with d3
    pause 0.4
    "images/rooms/room_of_requirement/dark_overlay_2.webp" with d3
    pause 0.4
    "images/rooms/room_of_requirement/dark_overlay_3.webp" with d3
    pause 0.4
    repeat

screen whose_points_screen():
    add "images/rooms/room_of_requirement/whose_points.webp"

screen quistion_pop_up(content=""):
    zorder 33

    add "interface/room_of_req/quistion_mark.webp" xpos 10 ypos 10 zoom 0.5
    text content xpos 40 ypos 15

screen day_to_night():
    use blkfade
    add "images/rooms/room_of_requirement/day_to_night.webp" xalign 0.5 yalign 0.5
    zorder 5

screen add_overlay():
    add "dark_overlay"  xpos 0 ypos 0
    zorder 6

