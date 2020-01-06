init python:
    class DollFace(DollMethods):
        def __init__(self, obj, face):
            self.char = obj
            self.name = self.char.name
            self.face = face
            self.imagepath = "characters/{}/face/".format(self.name)
            
            self.rebuild_image()
            
        def build_image(self):
            sprites = []
            
            # Add facial expressions
            sprites.extend(("{}{}/{}.png".format(self.imagepath, k, v[0]), v[1]) for k, v in self.face.iteritems() if v[0])

            sprites.sort(key=lambda x: x[1], reverse=False)
            sprites = itertools.chain.from_iterable(((0,0), x[0]) for x in sprites)
            return sprites