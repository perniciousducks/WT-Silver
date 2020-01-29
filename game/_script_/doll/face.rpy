init python:
    class DollFace(DollMethods):
    
        blacklist_blink = ("closed", "happyCl")
        
        def __init__(self, obj, face):
            self.char = obj
            self.name = self.char.name
            self.face = face
            self.imagepath = "characters/{}/face/".format(self.name)
            self.blink = "spr_{} blink".format(self.name) if renpy.has_image("spr_{} blink".format(self.name)) else None
            
            self.rebuild_image()
            
        def build_image(self):
            sprites = []
            
            # Add facial expressions
            sprites.extend(("{}{}/{}.png".format(self.imagepath, k, v[0]), v[1]) for k, v in self.face.iteritems() if not k == "pupils" and v[0])
            
            if self.blink and self.face["eyes"][0] not in self.blacklist_blink:
                sprites.append((self.blink, 10))
                
            path = "{}eyes/{}_mask.png".format(self.imagepath, self.face["eyes"][0])
            if renpy.loadable(path):
                sprites.append((AlphaMask("{}pupils/{}.png".format(self.imagepath, self.face["pupils"][0]), "{}eyes/{}_mask.png".format(self.imagepath, self.face["eyes"][0])), self.face["pupils"][1]))

            sprites.sort(key=lambda x: x[1], reverse=False)
            sprites = tuple(itertools.chain.from_iterable(((0,0), x[0]) for x in sprites))
            return sprites
            
        def get_skin(self):
            return ["{}{}/{}_skin.png".format(self.imagepath, k, v[0]) for k, v in self.face.iteritems() if renpy.loadable("{}{}/{}_skin.png".format(self.imagepath, k, v[0]))]
            
        def set_pose(self, pose):
            if pose is None:
                self.imagepath = "characters/{}/face/".format(self.name)
                self.blink = "spr_{} blink".format(self.name) if renpy.has_image("spr_{} blink".format(self.name)) else None
            else:
                self.imagepath = "characters/{}/poses/{}/face/".format(self.name, pose)
                self.blink = "spr_{} blink {}".format(self.name, pose) if renpy.has_image("spr_{} blink {}".format(self.name, pose)) else None
            self.rebuild_image()
            return