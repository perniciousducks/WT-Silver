init python:
    class DollLipstick(DollCloth):

        def set_imagepath(self):
            self.imagepath = "{}/characters/{}/clothes/makeup/lipstick/".format(self.modpath, self.name)

        def set_layers(self):
            for x in self.layers_special:
                self.__dict__[x] =  None

            for x in self.layers_additional:
                self.__dict__[x] = []
                for i in xrange(self.layers):
                    path = "{}{}_{}.webp".format(self.imagepath, i, x)
                    if renpy.loadable(path):
                        self.__dict__[x].append(path)
                self.__dict__[x+"_outline"] = None

            return

        def build_image(self):
            mouth = self.char.face.face["mouth"][0]
            image = self.apply_color("{}{}.webp".format(self.imagepath, mouth), 0)
            sprites = ((0,0), image)
            return sprites

        def build_icon(self):
            mouth = self.char.face.face["mouth"][0]
            bounds = "{}{}.webp".format(self.imagepath, mouth)
            self.ico = CroppedImage(self.build_image(), bounds)

        def set_pose(self, pose):
            if pose is None:
                path = "{}/characters/{}/clothes/makeup/lipstick/".format(self.modpath, self.name)
                self.imagepath = path
            else:
                path = "{}/characters/{}/poses/{}/clothes/makeup/lipstick/".format(self.modpath, self.name, pose)
                if renpy.loadable(path + "base.webp"):
                    self.imagepath = path

            self.rebuild_image()
            return
