init python:
    def catch_character_call(label, called):
        if called:
            if label.startswith(("her_main", "cho_main", "ast_main", "ton_main")):
                editor.catch(label)
                
    class ExpressionEditor(object):
        transitions = ("d1", "d2", "d3", "d4", "d5", "d6", "d7", "d8", "d9", "flash", "flashbulb", "flashbb", "flashblood", "kissiris", "black_magic", "blackfade", "morph", "teleport", "vpunch_repeat", "hpunch", "vpunch", "pushleft", "dissolve", "slideawayright", "wipedown", "slidedown", "pixellate", "blinds", "squares", "slideup", "pushup", "slideleft", "pushright", "wiperight", "irisin", "wipeleft", "slideawayleft", "pushdown", "irisout", "slideawayup", "wipeup", "slideawaydown", "slideright")
        
        transforms = ("move_fade", "sprite_fly_idle")
        
        char = {"her_main": "hermione",
                "ton_main": "tonks",
                "ast_main": "astoria",
                "cho_main": "cho"}
                
        def __init__(self):
            self.label = None
            self.line = None
            self.line_contents = None
            self.args = None
            
            self._file = None
            self._file_contents = None
            self._statement = None
            
            self.define_expressions()
            self.changes = {}
            
        def overwrite_statement(self):
            # Backup file contents
            with open(self._file, "r") as f:
                self._file_contents = f.readlines()

            try:
                new = self.get_new_statement()

                # Overwrite the file contents
                with open(self._file, "w") as f:
                    for n, l in enumerate(self._file_contents, 1):
                        if n == self.line:
                            f.writelines(l.replace(self.line_contents, new))
                            if n not in self.changes.get(self._file, []):
                                self.changes.setdefault(self._file, []).append(n)
                        else:
                            f.writelines(l)
            except:
                # Restore backup
                with open(self._file, "w") as f:
                    for l in self._file_contents:
                        f.writelines(l)
                renpy.notify("An error occured, no changes were made.")
                return
            self.line_contents = new
            renpy.notify("Saved.")
                        
        def get_new_statement(self):
            text = "\"\", " if not self.args["text"] else "\"{}\", ".format(self.args["text"].replace("\"", "\\\""))
            
            mouth = "" if self.args["mouth"] == False else "\"{}\", ".format(self.args["mouth"])
            eyes = "" if self.args["eyes"] == False else "\"{}\", ".format(self.args["eyes"])
            eyebrows = "" if self.args["eyebrows"] == False else "\"{}\", ".format(self.args["eyebrows"])
            pupils = "" if self.args["pupils"] == False else "\"{}\", ".format(self.args["pupils"])
            hair = "" if self.label != "ton_main" or not self.args["hair"] else "hair=\"{}\", ".format(self.args["hair"])
            
            cheeks = "" if self.args["cheeks"] in (None, "(No change)") else "cheeks=\"{}\", ".format(self.args["cheeks"])
            tears = "" if self.args["tears"] in (None, "(No change)") else "tears=\"{}\", ".format(self.args["tears"])
            extra = "" if self.args["extra"] == None else "extra=\"{}\", ".format(self.args["extra"])
            emote = "" if self.args["emote"] == None else "emote=\"{}\", ".format(self.args["emote"])
            face = "" if self.args["face"] == None else "face=\"{}\", ".format(self.args["face"])
            
            xpos = "" if self.args["xpos"] == None else "xpos=\"{}\", ".format(self.args["xpos"])
            ypos = "" if self.args["ypos"] == None else "ypos=\"{}\", ".format(self.args["ypos"])
            flip = "" if self.args["flip"] == None else "flip=\"{}\", ".format(self.args["flip"])

            trans = "" if self.args["trans"] == None else "trans={}, ".format(self.args["trans"])            
            animation = "" if self.args["animation"] == False else "animation={}".format(self.args["animation"])
            
            new = "call {}({}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{})".format(self.label, text, mouth, eyes, eyebrows, pupils, hair, cheeks, tears, extra, emote, face, xpos, ypos, flip, trans, animation)
            
            new = new.replace(", )", ")")
            return new
            
        def catch(self, label):
            self.label = label
            
            # Get file and line number
            stack = renpy.get_return_stack()[-1]
            node = renpy.game.script.namemap.get(stack, None)
        
            self._file = config.basedir+"/"+node.filename
            self.line = node.linenumber
            
            # Get arguments
            node = renpy.game.script.lookup_or_none(self.label)
            
            self.args = dict([(k, getattr(store, k)) for k in node.parameters.apply(None, None).iterkeys()])
            
            if self.args["cheeks"] == None:
                self.args["cheeks"] = "(No change)"
            if self.args["tears"] == None:
                self.args["tears"] = "(No change)"
            
            # Lookup transition name
            if self.args["trans"] != None:
                _transitions = dict([(obj.callable, name) for (name, obj) in store.__dict__.iteritems() if name in self.transitions])
                self.args["trans"] = _transitions[self.args["trans"].callable]
                
            # Lookup transform name
            if not self.args["animation"] in (False, None):
                _transforms = dict([(obj, name) for (name, obj) in store.__dict__.iteritems() if name in self.transforms])
                self.args["animation"] = _transforms[self.args["animation"]]
            
            # Read file and find the line in question
            with open(self._file) as f:
                for n, l in enumerate(f, 1):
                    if n == self.line:
                        self._statement = l
                        l = l.partition("#")[0].strip() # Ignore comments and strip spaces
                        if l.startswith("call {}".format(self.label)):
                            self.line_contents = l
                            break
            return
            
        def set_data(self, arg, val):
            self.args[arg] = val
            self.set_expressions()
            
        def set_expressions(self):
            c = getattr(renpy.store, self.char[self.label])
            
            cheeks = None if self.args["cheeks"] in (None, "(No change)") else self.args["cheeks"]
            tears = None if self.args["tears"] in (None, "(No change)") else self.args["tears"]
            
            c.set_face(mouth=self.args["mouth"], eyes=self.args["eyes"], eyebrows=self.args["eyebrows"], pupils=self.args["pupils"], cheeks=cheeks, tears=tears)
            c.apply_transition()
            
        def get_expressions(self, type):
            return sorted(self.expressions[self.char[self.label]][type])
        
        def define_expressions(self):
            def scan_files(char):
                mouths = tuple(x[:-4] for x in system.listdir(config.basedir+"/game/characters/"+char+"/face/mouth/") if x.endswith(".png") and not "_mask" in x and not "_skin" in x)
                eyes = tuple(x[:-4] for x in system.listdir(config.basedir+"/game/characters/"+char+"/face/eyes/") if x.endswith(".png") and not "_mask" in x and not "_skin" in x)
                eyebrows = tuple(x[:-4] for x in system.listdir(config.basedir+"/game/characters/"+char+"/face/eyebrows/") if x.endswith(".png") and not "_mask" in x and not "_skin" in x)
                pupils = tuple(x[:-4] for x in system.listdir(config.basedir+"/game/characters/"+char+"/face/pupils/") if x.endswith(".png") and not "_mask" in x and not "_skin" in x)
                
                cheeks = ["(No change)"]
                tears = ["(No change)"]
                cheeks.extend([x[:-4] for x in system.listdir(config.basedir+"/game/characters/"+char+"/face/cheeks/") if x.endswith(".png") and not "_mask" in x and not "_skin" in x])
                tears.extend([x[:-4] for x in system.listdir(config.basedir+"/game/characters/"+char+"/face/tears/") if x.endswith(".png") and not "_mask" in x and not "_skin" in x])
                
                return dict([("mouths", mouths), ("eyes", eyes), ("eyebrows", eyebrows), ("pupils", pupils), ("cheeks", cheeks), ("tears", tears)])
            
            self.expressions = dict([(x, scan_files(x)) for x in self.char.itervalues()])
            
    def editor_reset():
        editor.changes = {}
        
    if config.developer:
        config.label_callback = catch_character_call
        config.after_load_callbacks.append(editor_reset)
        
default editor = ExpressionEditor()

screen editor():
    tag editor
    zorder 999
    
    drag:
        drag_name "editor"
        draggable True
        drag_offscreen False
        drag_handle (0, 0, 1.0, 0.2)
        pos (50, 50)
        frame:
            xysize (250, 450)
            button action NullAction() style "empty" xysize (250, 450) ypos 18
            
            text "Editor" size 15 color "#FFF" outlines [(1, "#00000080", 1, 0)]
            
            frame:
                style "empty"
                xysize (236, 2) 
                pos (0, 18)
                background "#FFFFFF80"
            
            if editor.label:
                $ f = editor._file.split("/")[-1]
                $ l = editor.line
                
                text "File: [f]\nLine: [l]" size 10 color "#FFF" xpos 60 yoffset -3 outlines [(1, "#00000080", 1, 0)]
                
                if editor.changes.get(editor._file, None):
                    $ n = 0
                    $ nn = 0
                    for k, v in editor.changes.iteritems():
                        $ n += 1
                        $ nn += len(v)
                    text "Reload to apply [nn] changes in [n] files" size 10 color "#FFF" align (0.5, 0.9) outlines [(1, "#00000080", 1, 0)]
                
                textbutton "Save" action Function(editor.overwrite_statement) align (0.0, 1.0)
                textbutton "Reload" action Function(_reload_game) xanchor 1.0 align (1.0, 1.0)
    
                if not False in (editor.args["pupils"], editor.args["eyebrows"], editor.args["eyes"], editor.args["mouth"]):
                    use dropdown_menu(name="Tears: "+str(editor.args["tears"]), pos=(0, 140), items_offset=(0, 0), background="#FFFFFF80"):
                        for i in editor.get_expressions("tears"):
                            textbutton "[i]" text_size 10 action [SelectedIf(i==str(editor.args["tears"])), Function(editor.set_data, "tears", i)]
                    use dropdown_menu(name="Cheeks: "+str(editor.args["cheeks"]), pos=(0, 120), items_offset=(0, 0), background="#FFFFFF80"):
                        for i in editor.get_expressions("cheeks"):
                            textbutton "[i]" text_size 10 action [SelectedIf(i==str(editor.args["cheeks"])), Function(editor.set_data, "cheeks", i)]
                    if editor.label == "ton_main":
                        use dropdown_menu(name="Hair: "+str(editor.args["hair"]), pos=(0, 100), items_offset=(0, 0), background="#FFFFFF80"):
                            for i in xrange(0, 10):
                                textbutton "hello world"
                    use dropdown_menu(name="Pupils: "+str(editor.args["pupils"]), pos=(0, 80), items_offset=(0, 0), background="#FFFFFF80"):
                        for i in editor.get_expressions("pupils"):
                            textbutton "[i]" text_size 10 action [SelectedIf(i==str(editor.args["pupils"])), Function(editor.set_data, "pupils", i)]
                    use dropdown_menu(name="Eyebrows: "+str(editor.args["eyebrows"]), pos=(0, 60), items_offset=(0, 0), background="#FFFFFF80"):
                        for i in editor.get_expressions("eyebrows"):
                            textbutton "[i]" text_size 10 action [SelectedIf(i==str(editor.args["eyebrows"])), Function(editor.set_data, "eyebrows", i)]
                    use dropdown_menu(name="Eyes: "+str(editor.args["eyes"]), pos=(0, 40), items_offset=(0, 0), background="#FFFFFF80"):
                        for i in editor.get_expressions("eyes"):
                            textbutton "[i]" text_size 10 action [SelectedIf(i==str(editor.args["eyes"])), Function(editor.set_data, "eyes", i)]
                    use dropdown_menu(name="Mouth: "+str(editor.args["mouth"]), pos=(0, 20), items_offset=(0, 0), background="#FFFFFF80"):
                        for i in editor.get_expressions("mouths"):
                            textbutton "[i]" text_size 10 action [SelectedIf(i==str(editor.args["mouth"])), Function(editor.set_data, "mouth", i)]
                else:
                    text "This character line uses unrecognized expression and requires to be changed manually." size 10 color "#FFF" align (0.5, 0.5) outlines [(1, "#00000080", 1, 0)]
            else:
                text "Not applicable." size 15 color "#FFF" align (0.5, 0.5) outlines [(1, "#00000080", 1, 0)]