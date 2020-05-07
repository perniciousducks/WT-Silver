
# Demo only, code is NOT final.

transform CGCamera(zoom, endzoom, pos, endpos, rotate, endrotate, t):
    offset pos
    zoom zoom
    rotate rotate
    parallel:
        ease_cubic t zoom endzoom
    parallel:
        ease_quad t xoffset endpos[0] yoffset endpos[1]
    parallel:
        linear t rotate endrotate

image cho_hj base = Movie(play="images/CG/cho_bj/hj/loop_base.webm", image="images/CG/cho_bj/hj/mid_base_half.png", start_image="images/CG/cho_bj/hj/mid_base_half.png")
image cho_hj annoyed = Movie(play="images/CG/cho_bj/hj/loop_annoyed.webm", image="images/CG/cho_bj/hj/mid_annoyed_half.png", start_image="images/CG/cho_bj/hj/mid_annoyed_half.png")
image cho_hj up = Movie(play="images/CG/cho_bj/hj/loop_up.webm", image="images/CG/cho_bj/hj/up_base_half.png", start_image="images/CG/cho_bj/hj/up_base_half.png")
image cho_hj blush = Movie(play="images/CG/cho_bj/hj/loop_blush.webm", image="images/CG/cho_bj/hj/mid_blush_half.png", start_image="images/CG/cho_bj/hj/mid_blush_half.png")

image cho_hj blush fast = Movie(play="images/CG/cho_bj/hj/loop_blush_fast.webm", image="images/CG/cho_bj/hj/mid_blush_half.png", start_image="images/CG/cho_bj/hj/mid_blush_half.png")

init python:

    class CGController(object):
        default_timer = 1.0

        def __init__(self, imagepath, image, min_zoom=0.39, max_zoom=1.0, type="png"):
            self.imagepath = "images/CG/{}".format(imagepath)
            self.type = type

            self.scale = 1.0

            self.last_image = image
            self.image = image

            self.max_zoom = max_zoom
            self.min_zoom = min_zoom

            self.last_zoom = min_zoom
            self.zoom = min_zoom

            self.last_pos = (0, 0)
            self.pos = (0, 0)

            self.last_rotate = 0
            self.rotate = 0

            self.child = None

        def set_imagepath(self, path):
            self.imagepath = "images/CG/{}/".format(path)

        def set_image(self, img):
            p = max(0, self.get_pause() - 0.3)

            self.last_image = self.image
            self.image = img

            # Reset last variables to new variables to not redraw the transform.
            self.last_zoom = self.zoom
            self.last_pos = self.pos
            self.last_rotate = self.rotate

            renpy.pause(p)
            self.redraw(self.default_timer)
            renpy.with_statement(d3)

        def set_zoom(self, n):
            self.last_zoom = self.zoom
            self.zoom = float(clamp(n, self.min_zoom, self.max_zoom))

        def set_rotation(self, n):
            self.last_rotate = self.rotate
            self.rotate = n

        def set_pos(self, pos):
            self.last_pos = tuple(self.pos)
            self.pos = pos

        def set(self, zoom=None, rotate=None, pos=None, t=None, initialize=False, pause=False):
            if not zoom:
                zoom=self.last_zoom
            if not rotate:
                rotate=self.last_rotate
            if not pos:
                pos=self.last_pos
            if not t:
                t = self.default_timer

            self.set_zoom(zoom)
            self.set_rotation(rotate)
            self.set_pos(pos)

            if initialize:
                self.last_zoom = zoom
                self.last_rotate = rotate
                self.last_pos = pos

            self.redraw(t)

            if pause:
                renpy.pause(t)

        def redraw(self, t):
            d = renpy.get_registered_image(self.image)

            if d is None:
                d = Image("{}{}.{}".format(self.imagepath, self.image, self.type))

            if isinstance(d, Movie):
                self.scale = 2.0
            else:
                self.scale = 1.0

            last_zoom = self.last_zoom * self.scale
            zoom = self.zoom * self.scale

            self.child = At(d, CGCamera(last_zoom, zoom, self.last_pos, self.pos, self.last_rotate, self.rotate, t))

        def get_image(self):
            return self.child

        def get_pause(self):
            d = renpy.get_registered_image(self.image)
            if isinstance(d, Movie) and renpy.music.is_playing(d.channel):
                p = renpy.music.get_pos(d.channel)
                t = renpy.music.get_duration(d.channel)
                return t - p
            else:
                return 0

default camera = CGController(imagepath="cho_bj/kneel/", image="0")

screen animatedCG():
    tag cg
    zorder 16

    add camera.get_image() align (0.5, 0.5)
