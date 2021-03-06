init python:
    class Doll(DollMethods):
        def __init__(self, name, clothes, face, body):
            self.wardrobe = {}
            self.wardrobe_list = []
            self.blacklist = []
            self.outfits = []
            self.name = name
            self.clothes = clothes
            self.face = DollFace(self, face)
            self.body = DollBody(self, body)
            self.cum = DollCum(self)
            self.pose = None

            self.rebuild_image()

        def rebuild(self):
            """Rebuild all character images. Useful for debugging."""
            self.body.rebuild_image()
            self.face.rebuild_image()
            self.cum.rebuild_image()
            for o in self.wardrobe_list:
                o.rebuild_image()
                o.build_icon()
            for o in self.outfits:
                o.rebuild_image()
            self.rebuild_image()

        def build_image(self):
            # Add body, face, cum, clothes, masks
            masks = []
            sprites = [[self.body.get_image(), 0], [self.face.get_image(), 1], [self.cum.get_image(), self.cum.zorder_cum]]

            for o in self.clothes.itervalues():
                if o[0] and o[2]:
                    sprites.append([o[0].get_image(), o[0].zorder])
                    if o[0].back:
                        sprites.extend([x, -100+n+o[0].zorder] for n, x in enumerate(o[0].get_back()))
                        if o[0].back_outline:
                            sprites.append([o[0].back_outline, -100+o[0].zorder+o[0].layers])
                    if o[0].front:
                        sprites.extend([x, 100+n+o[0].zorder] for n, x in enumerate(o[0].get_front()))
                        if o[0].front_outline:
                            sprites.append([o[0].front_outline, 100+o[0].zorder+o[0].layers])
                    if o[0].armfix:
                        armleft = im.MatrixColor("{}armleft/{}_fix.png".format(self.body.imagepath, self.body.get_part("armleft")), im.matrix.hue(self.body.hue))
                        armright = im.MatrixColor("{}armright/{}_fix.png".format(self.body.imagepath, self.body.get_part("armright")), im.matrix.hue(self.body.hue))

                        sprites.extend([[armleft, o[0].zorder+0.5], [armright, o[0].zorder+0.5]])
                    if o[0].mask:
                        masks.append([o[0].mask, o[0].zorder-1])

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

        def get_image(self):
            if not renpy.is_skipping() or self.sprite is None:
                if self.override:
                    sprites = self.build_image()
                    self.sprite = DollDisplayable(Composite(self.size, *sprites))
                elif not self.cached:
                    sprites = self.build_image()
                    self.sprite = DollDisplayable(Composite(self.size, *sprites))
                    self.cached = True
            return self.sprite

        def apply_transition(self):
            scr_name = "{}_main".format(self.name)
            if renpy.get_screen(scr_name):
                renpy.hide_screen(scr_name)
                renpy.show_screen(scr_name)
            else:
                last_doll_images[scr_name] = self.get_image()

        def equip(self, obj):
            """Takes DollCloth or DollOutfit object to equip."""
            if isinstance(obj, DollCloth):
                self.clothes[obj.type][0], self.clothes[obj.type][2] = obj, True
                if self.pose:
                    obj.set_pose(self.pose)
            elif isinstance(obj, DollOutfit):
                self.unequip("all")
                for i in obj.group:
                    self.clothes[i.type][0] = i.parent
                    self.clothes[i.type][0].set_color(i.color)
                    if self.pose:
                        i.parent.set_pose(self.pose)
            self.body.rebuild_image()
            self.rebuild_image()
            self.apply_transition()
            update_chibi(self.name)

        def unequip(self, *args):
            """Takes argument(s) containing string cloth type(s) to unequip."""
            if "all" in args:
                for k, v in self.clothes.iteritems():
                    if not k.startswith(self.blacklist_unequip):
                        if self.pose:
                            v[0].set_pose(None)
                        v[0], v[2] = None, True
            else:
                for arg in args:
                    if self.pose and self.clothes[arg][0]:
                        self.clothes[arg][0].set_pose(None)
                    self.clothes[arg][0] = None

            self.body.rebuild_image()
            self.rebuild_image()
            self.apply_transition()
            update_chibi(self.name)

        def get_equipped(self, type):
            """Takes argument containing string cloth type. Returns equipped object for cloth type."""
            return self.clothes[type][0]

        def strip(self, *args):
            """Takes argument(s) containing string cloth type(s) to temporarily displace (hide)."""
            if "all" in args:
                for k, v in self.clothes.iteritems():
                    if not k.startswith(self.blacklist_toggles):
                        v[2] = False
            else:
                for arg in args:
                    if arg.startswith(self.blacklist_toggles):
                        for k in self.clothes.iterkeys():
                            if k.startswith(arg):
                                self.clothes[k][2] = False
                    else:
                        self.clothes[arg][2] = False
            self.body.rebuild_image()
            self.rebuild_image()
            self.apply_transition()
            update_chibi(self.name)

        def wear(self, *args):
            """Takes argument(s) containing string cloth type(s) to put on (unhide)."""
            if "all" in args:
                for v in self.clothes.itervalues():
                    v[2] = True
            else:
                for arg in args:
                    if arg.startswith(self.blacklist_toggles):
                        for k in self.clothes.iterkeys():
                            if k.startswith(arg):
                                self.clothes[k][2] = True
                    else:
                        self.clothes[arg][2] = True
            self.body.rebuild_image()
            self.rebuild_image()
            self.apply_transition()
            update_chibi(self.name)

        def toggle_wear(self, type):
            """Takes argument containing string cloth type to toggle visibility (hide/unhide). Used in wardrobe."""
            if type.startswith(self.blacklist_toggles):
                for k, v in self.clothes.iteritems():
                    if k.startswith(type):
                        v[2] = not v[2]
            else:
                self.clothes[type][2] = not self.clothes[type][2]
            self.body.rebuild_image()
            self.rebuild_image()
            self.apply_transition()
            update_chibi(self.name)

        def is_equipped(self, arg):
            """Takes argument containing string cloth type. Returns True if slot is occupied, False otherwise."""
            if arg.startswith(self.blacklist_toggles):
                for k, v in self.clothes.iteritems():
                    if k.startswith(arg) and v[0]:
                        return True
                return False
            else:
                return True if self.clothes[arg][0] else False

        def is_worn(self, *args):
            """Takes argument(s) containing string cloth type(s). Returns True if worn, False otherwise."""
            for arg in args:
                if arg.startswith(self.blacklist_toggles):
                    for k, v in self.clothes.iteritems():
                        if k.startswith(arg) and not v[0] or not v[2]:
                            return False
                else:
                    if not self.clothes[arg][0] or not self.clothes[arg][2]:
                        return False
            return True

        def is_any_worn(self, *args):
            """Takes arguments containing string cloth types. Returns True if ANY of them is worn, False otherwise."""
            if "clothes" in args:
                for k, v in self.clothes.iteritems():
                    if not k.startswith(self.blacklist_toggles):
                        if self.is_worn(k):
                            return True
            else:
                for arg in args:
                    if self.is_worn(arg):
                        return True
            return False

        def set_face(self, **kwargs):
            """Takes keyword argument(s) with the string name of expression file(s)."""
            for arg, value in kwargs.iteritems():
                if value not in (self.face.face[str(arg)][0], False):
                    self.face.face[str(arg)][0] = value
            self.face.rebuild_image()
            self.body.rebuild_image()
            self.rebuild_image()

        def get_face(self):
            """Returns a dictionary containing currently set facial expressions. Used in character studio."""
            return dict((k, v[0]) for k, v in self.face.face.iteritems())

        def set_body(self, **kwargs):
            """Takes keyword argument(s) with the string name of body part file(s)."""
            for arg, value in kwargs.iteritems():
                if value != self.body.body[str(arg)][0]:
                    self.body.body[str(arg)][0] = value
            self.body.rebuild_image()
            self.rebuild_image()

        def set_body_hue(self, arg):
            """Takes integer between 0 - 359, rotates the character body colour by given amount."""
            self.body.hue = arg
            self.body.rebuild_image()
            self.rebuild_image()

        def set_cum(self, *args, **kwargs):
            """Takes keyword argument(s) containing string name(s) of cum layers to apply or None."""
            if args:
                for k in self.cum.cum.iterkeys(): # for v in self.cum.cum.itervalues(); Abnormal behaviour when itervalues() used to mutate the value.
                    self.cum.cum[k] = args[0]
            for arg, value in kwargs.iteritems():
                self.cum.cum[str(arg)] = value
            self.cum.rebuild_image()
            self.rebuild_image()
            self.apply_transition()

        def set_pose(self, pose):
            if pose is None or renpy.loadable("characters/{}/poses/{}/loadable.png".format(self.name, pose)):
                self.pose = pose
                self.face.set_pose(pose)
                self.body.set_pose(pose)
                self.cum.set_pose(pose)
                for v in self.clothes.itervalues():
                    if v[0]:
                        v[0].set_pose(pose)
                self.rebuild_image()
                self.apply_transition()
            else:
                raise IOError("'{}' pose doesn't exist for character named '{}'.".format(pose, self.name))

        def reset_blacklist(self, unequip=True):
            """Resets wardrobe blacklist based on worn clothes. Takes optional argument that causes blacklisted clothes to be unequipped."""
            self.blacklist = []
            for v in self.clothes.itervalues():
                if v[0] and v[0].blacklist:
                    self.blacklist.extend(x for x in v[0].blacklist if x not in self.blacklist)
            if unequip and self.blacklist:
                self.unequip(*self.blacklist)

        def is_blacklisted(self, type):
            """Takes string cloth type. Returns True if cloth type is blacklisted."""
            return True if type in self.blacklist else False

        def create_outfit(self):
            """Creates a copy of the current character clothes and stores it."""
            return DollOutfit([x[0] for x in self.clothes.itervalues() if x[0]], True)

        def get_schedule(self):
            """Returns a list of outfits available for current daytime and weather conditions."""
            global daytime, raining, snowing, blizzard, storm, cloudy
            schedule = []

            for o in self.outfits:
                if o.unlocked and o.schedule["day" if daytime else "night"]:
                    if (storm or cloudy) and o.schedule["cloudy"]:
                        schedule.append(o)
                    elif raining and o.schedule["rainy"]:
                        schedule.append(o)
                    elif (snowing or blizzard) and o.schedule["snowy"]:
                        schedule.append(o)
                    elif not (cloudy or storm or raining or snowing or blizzard) and not (o.schedule["cloudy"] or o.schedule["rainy"] or o.schedule["snowy"]):
                        schedule.append(o)
            return schedule

        def equip_random_outfit(self):
            """Equips random outfit based on Outfits Schedule."""
            schedule = self.get_schedule()

            if schedule:
                self.equip(renpy.random.choice(schedule))
