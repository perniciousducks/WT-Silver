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
            sprites.extend((x, self.zorder_skin) for x in self.char.face.get_skin())

            sprites.sort(key=lambda x: x[1], reverse=False)
            sprites = tuple(itertools.chain.from_iterable(((0,0), x[0]) for x in sprites))
            return sprites
            
        def build_mannequin(self, group=None):
            sprites = []
            
            # Add body parts and skin layers from clothes
            sprites.extend(("{}{}/{}.png".format(self.imagepath, k, v[0]), v[1]) for k, v in self.body.iteritems() if v[0])
            if group:
                sprites.extend((o.skin, self.zorder_skin) for o in group if o and o.skin)

            sprites.sort(key=lambda x: x[1], reverse=False)
            sprites = tuple(itertools.chain.from_iterable(((0,0), im.MatrixColor(x[0], im.matrix.desaturate())) for x in sprites))
            return sprites
            
        def get_mannequin(self, group=None):
            mannequin = self.build_mannequin(group)
            return Composite(self.size, *mannequin)
            
        def get_part(self, arg):
            return self.body[arg][0]