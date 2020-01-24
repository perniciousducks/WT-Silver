init python:            
    class DollOutfit(DollMethods): 
        def __init__(self, group, unlocked=False, name="", desc="", price=0):
            self.name = name
            self.group = [x.clone() for x in group]
            self.desc = desc
            self.price = price
            self.char = self.group[0].char
            self.unlocked = unlocked
            self.schedule = {"day": False, "night": False, "cloudy": False, "rainy": False, "snowy": False}
            
            if unlocked:
                self.unlock()
            
            # Append to character outfits list
            self.char.outfits.append(self)
            
            self.rebuild_image()
            
        def build_image(self):
            masks = []
            sprites = []
            
            # Add body parts and skin layers from clothes, then make them grayscale
            sprites.append([self.char.body.get_mannequin(self.group), 0])
            
            for o in self.group:
                sprites.append([o.get_image(), o.zorder])
                if o.back:
                    sprites.extend([x, -100+n+o.zorder] for n, x in enumerate(o.get_back()))
                    if o.back_outline:
                        sprites.append([o.back_outline, -100+o.zorder+o.layers])
                if o.front:
                    sprites.extend([x, 100+n+o.zorder] for n, x in enumerate(o.get_front()))
                    if o.front_outline:
                        sprites.append([o.front_outline, 100+o.zorder+o.layers])
                if o.armfix:
                    sprites.extend([[im.Grayscale("{}armleft/{}_fix.png".format(self.body.imagepath, self.body.get_part("armleft"))), o.zorder+0.5], [im.Grayscale("{}armright/{}_fix.png".format(self.body.imagepath, self.body.get_part("armright"))), o.zorder+0.5]])
                if o.mask:
                    masks.append([o.mask, o.zorder-1])
                        
            sprites.sort(key=lambda x: x[1])

            back_sprites = [x for x in sprites if x[1] < 0]
            sprites = [x for x in sprites if x[1] >= 0]

            # Apply alpha mask
            for m in sorted(masks, key=lambda x: x[1]):
                for i, s in enumerate(sprites):
                    if m[1] <= s[1]:
                        if i > 0:
                            masked = tuple(itertools.chain.from_iterable(((0,0), x[0]) for x in sprites[:i]))
                            c = AlphaMask(Composite(self.size, *masked), m[0])
                            sprites = sprites[i:]
                            sprites.insert(0, (c, m[1]-1))
                        break
            
            sprites = back_sprites + sprites
            sprites = tuple(itertools.chain.from_iterable(((0,0), x[0]) for x in sprites))
            return sprites
            
        def export_data(self, tofile=True, filename="exported"):
            """Exports outfit to .png file or clipboard text."""
            exported = [self.group[0].name]
            exported.extend([x.id, x.color] for x in self.group)
                
            # Encode data
            if tofile:
                path = "{}/game/outfits/{}.png".format(config.basedir, filename)
                renpy.screenshot(path)
                img = pygame.image.load(path)
                img = pygame.transform.smoothscale(img, (1080, 600))
                subsurface = img.subsurface((384, 63, 309, 470))
                pygame.image.save(subsurface, path)
                _image_payload.encode(filename, str(exported))
            else:
                set_clipboard(exported)
            renpy.notify("Export successful!")
            
        def import_data(self, fromfile=True, filename="exported"):
            """Imports outfit from .png file or clipboard text."""
            # Grab data
            if fromfile:
                try:
                    if renpy.loadable("/outfits/{}.png".format(filename)):
                        imported = _image_payload.decode(filename)
                    else:
                        renpy.notify("File doesn't exist!")
                        renpy.block_rollback()
                        return False
                except:
                    if _image_payload._file:
                        _image_payload._file.close()
                    renpy.notify("Corrupted file!")
                    renpy.block_rollback()
                    return False
            else:
                imported = get_clipboard()
            
            # Evaluate data
            if imported:
                try:
                    imported = evaluate(imported)
                except:
                    renpy.notify("Corrupted file!")
                    renpy.block_rollback()
                    return False

                for x in imported:
                    if isinstance(x, list):
                        for o in char_active.wardrobe_list:
                            if x[0] == o.id:
                                if not o.unlocked and not cheats_active:
                                    renpy.notify("You haven't unlocked some of the items yet. Try again later.")
                                    renpy.block_rollback()
                                    return False
                                x[0] = o
                                # TODO: Because of no parent object It would override original object color list, it should be done only on equipping outfits, find a way to provide new color set. Perhaps through DollOutfit constructor?
                                x[0].set_color(x[1])
                                group.append(x[0])
                if len(group) > 0:
                    renpy.notify("Import successful!")     
                    renpy.block_rollback()
                    return DollOutfit(group, True)
            renpy.notify("Import failed!")
            renpy.block_rollback()
            return False
            
        def unlock(self):
            """Unlocks outfit and respective clothing objects from which they were cloned."""
            self.unlocked = True
            for i in self.group:
                i.unlocked, i.parent.unlocked = True, True
                
        def save(self):
            """Overwrites this outfit with clothes currently equipped by the character."""
            self.group = []
            for v in self.char.clothes.itervalues():
                if v[0]:
                    self.group.append(v[0].clone())
            self.rebuild_image()
            return