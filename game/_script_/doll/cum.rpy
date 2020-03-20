init python:
    class DollCum(DollMethods):
        zorder_cum = 100

        def __init__(self, obj):
            self.char = obj
            self.name = self.char.name
            self.imagepath = "characters/{}/cum/".format(self.name)

            self.cum = dict((k, None) for k in ("hair", "face", "breasts", "body", "crotch", "pussy", "legs"))

            self.rebuild_image()

        def build_image(self):
            sprites = tuple(itertools.chain.from_iterable(((0,0), "{}{}/{}.png".format(self.imagepath, k, v)) for k, v in self.cum.iteritems() if v != None))
            return sprites

        def set_pose(self, pose):
            if pose is None:
                self.imagepath = "characters/{}/cum/".format(self.name)
            else:
                self.imagepath = "characters/{}/poses/{}/cum/".format(self.name, pose)
            self.rebuild_image()
            return
