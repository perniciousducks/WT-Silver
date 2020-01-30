
init -1 python:
    class DollMethods(object):
        """Container class for commonly used methods and attributes"""
        size = (1010, 1200)
        sprite = None
        cached = False
        override = False
        
        layers_extra = ("extra", "outline", "overlay")
        layers_special = ("skin", "mask", "wet_mask")
        layers_additional = ("back", "front")
        
        blacklist_toggles = ("hair", "pubes", "piercing", "makeup", "tattoo", "accessory")
        blacklist_unequip = ("hair")
        
        def rebuild_image(self):
            # Defers rebuild until next time get_image is called
            self.cached = False
            
        def get_image(self):
            if not renpy.is_skipping() or self.sprite is None:
                IgnoresEvents = renpy.display.layout.IgnoresEvents
                if self.override:
                    sprites = self.build_image()
                    self.sprite = IgnoresEvents(Composite(self.size, *sprites))
                elif not self.cached:
                    sprites = self.build_image()
                    self.sprite = IgnoresEvents(Composite(self.size, *sprites))
                    self.cached = True
            return self.sprite
            
# Notes and todo's:
#   Avoid passing generators to the cache through first or third party functions, Ren'py will have problems pickling the manipulated images causing no image being displayed at all after the game reloads, alternatively the game may refuse to load at all. Use a tuple instead. This applies to renpy.start_predict(x) as well.
#   AlphaMask and Flatten are costly operations which cause noticeable slowdowns, an alternative would be nice.
#   
#