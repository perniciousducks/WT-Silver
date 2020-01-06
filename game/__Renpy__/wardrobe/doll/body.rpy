init python:
    class DollBody(DollMethods):
        zorder_skin = 5
        
        def __init__(self, obj, body):
            self.char = obj
            self.name = self.char.name
            self.body = body
            self.imagepath = "characters/{}/body/".format(self.name)
            
            self.rebuild_image()
            
        def build_image(self):
            sprites = []
            
            # Add body parts and skin layers from clothes
            sprites.extend(("{}{}/{}.png".format(self.imagepath, k, v[0]), v[1]) for k, v in self.body.iteritems() if v[0])
            sprites.extend((o[0].skin, self.zorder_skin) for o in self.char.clothes.itervalues() if o[0] and o[0].skin)

            sprites.sort(key=lambda x: x[1], reverse=False)
            sprites = itertools.chain.from_iterable(((0,0), x[0]) for x in sprites)
            return sprites
            
        def get_mannequin_parts(self):
            return [(im.MatrixColor("{}{}/{}.png".format(self.imagepath, k, v[0]), im.matrix.desaturate()), v[1]) for k, v in self.body.iteritems() if v[0]]