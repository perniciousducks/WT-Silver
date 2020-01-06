init offset = -1
init python:
    class DollMethods(object):
        """Container class for commonly used methods and attributes"""
        size = (1010, 1200)
        sprite = None
        sprites = None
        cached = False
        override = False
        
        layers_extra = ("extra", "outline", "overlay")
        layers_special = ("skin", "mask", "wet_mask")
        layers_additional = ("back", "front")
        
        blacklist_toggles = ("hair", "pubes", "piercing", "makeup", "tattoo", "accessory")
        blacklist_unequip = ("hair")
        
        def rebuild_image(self):
            self.sprites = self.build_image()
            self.cached = False
            
        def get_image(self):
            if self.override:
                self.rebuild_image()
                self.sprite = Composite(self.size, *self.sprites)
            else:
                if not self.cached:
                    self.cached = True
                    self.sprite = Composite(self.size, *self.sprites)
            return Flatten(self.sprite)