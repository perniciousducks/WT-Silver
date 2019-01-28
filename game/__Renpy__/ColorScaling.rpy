screen color_map(color, cursor, alpha=True, title=""):
    zorder 9
    
    button:
        xsize 1080
        ysize 600
        action NullAction()
        style "empty"
        
    frame:
        xsize 600
        ysize 350
        xpos 150
        ypos 100
        #style "empty"
        background "#19458ce0"

        imagebutton:
            ypos 25
            xpos 25
            idle UI_color_scale
            clicked Return("main_color")
            
        imagebutton:
            ypos 25
            xpos 290
            idle im.Scale( UI_color_bar, 30,255, False)
            clicked Return("color_bar")
        
        if alpha:
            imagebutton:
                ypos 290
                xpos 25
                idle im.Scale(UI_alpha_bar, 255, 30, False)
                clicked Return("alpha_bar")
            text "Alpha: " + str(int(color[3])) xpos 360 ypos 130
            
        text "Red  : " + str(int(color[0])) xpos 360 ypos 25
        text "Green: " + str(int(color[1])) xpos 360 ypos 60
        text "Blue : " + str(int(color[2])) xpos 360 ypos 95

        text title xalign 0.5 text_align 0.5
        
        textbutton "Apply" xalign 0.9 yalign 0.9 clicked Return("finish")
        
        
        add Solid(get_hex_string(color[0]/255.0,color[1]/255.0,color[2]/255.0,color[3]/255.0)) xpos 360 ypos 165 zoom 0.1
    
    use close_button
    
    #Cursor
    add "interface/check_01_grey.png" xpos int(cursor[0]-11) ypos int(cursor[1]-12)
    
init python:
    import pygame
    import _renpy
    
    def color_picker(color = [255.0, 255.0, 0.0, 255.0], alpha = True, title=""):
        global color_scale
        global UI_color_bar
        original_color = [color[0],color[1],color[2],color[3]]
        choicen_scale = [125.0,125.0]
        cursor_position = [175, 125]
        while True:
            renpy.show_screen("color_map", color, cursor_position, alpha, title)

            _return = ui.interact()

            renpy.hide_screen("color_map")

            #Needed for screen scaling
            screen_height = renpy.get_physical_size()[1]
            screen_width = renpy.get_physical_size()[0]
            x, y = renpy.get_mouse_pos() #pygame.mouse.get_pos()
            #if screen_width*5 > screen_height*9:
            #    x -= (screen_width-float((screen_height*9.0)/5.0))/2
            #    scaling_modifier = (float(screen_height)/float(config.screen_height))
            #else:
            #    y -= (screen_height-float((screen_width*5.0)/9.0))/2
            #scaling_modifier = (float((screen_width*5.0)/9.0)/float(config.screen_height))
            #scaling_modifier = 1
            
            
            
            if _return == "Close":
                return original_color
            elif _return == "main_color":
                cursor_position = [x, y]
                x = x-175.0
                y = y-125.0
                color = UI_color_scale.get_main_color( x ,y)
            elif _return == "color_bar":
                y -= 125.0
                ypos_to_color = float(y)
                
                renpy.free_memory()
                new_color = UI_color_bar.get_color(ypos_to_color)
                UI_color_scale.set_color(new_color)
                color = UI_color_scale.get_main_color(choicen_scale[0], choicen_scale[1])

                renpy.restart_interaction()
            elif _return == "alpha_bar":
                x -= 175.0
                alpha = 255 - x
                color[3] = 0 if alpha < 0 else alpha
                
            elif _return == "finish":
                return color
                
    
    class o_color_bar(im.ImageBase):
        def __init__(self, **properties):
            im = Image("interface/color_palete/color_bar.png")
            super(o_color_bar, self).__init__(im, 30, 255, **properties)

            self.image = im

        def get_hash(self):
            return self.image.get_hash()

        def load(self):
            surf = im.Cache().get(self.image)

            try:
                renpy.display.render.blit_lock.acquire()
                rv = color_bar(surf)
            finally:
                renpy.display.render.blit_lock.release()

            return rv

        def predict_files(self):
            return self.image.predict_files()
         
        def get_color(self, y):
            new_color = [0.0,0.0,0.0,255.0]

            if y < 255/6:
                new_color[0] = 255
                new_color[1] = 255*(float(y)/(255.0/6.0))
            elif y < (255/6)*2:
                new_color[0] = 255-((y-(255/6))*6)
                new_color[1] = 255
            elif y < (255/6)*3:
                new_color[1] = 255
                new_color[2] = 255*(float(y-(255/6)*2)/(255.0/6.0))
            elif y < (255/6)*4:
                new_color[1] = 255-((y-((255/6)*3))*6)
                new_color[2] = 255
            elif y < (255/6)*5:
                new_color[0] = 255*(float(y-(255/6)*4)/(255.0/6.0))
                new_color[2] = 255
            else:
                new_color[0] = 255
                new_color[2] = 255-((y-((255/6)*5))*5)
            
            new_color[0] = 255.0 if new_color[0] > 255 else new_color[0]
            new_color[1] = 255.0 if new_color[1] > 255 else new_color[1]
            new_color[2] = 255.0 if new_color[2] > 255 else new_color[2]
            
            return new_color
            
    class o_alpha_bar(im.ImageBase):
        def __init__(self, **properties):
            im = Image("interface/color_palete/color_bar.png")
            super(o_alpha_bar, self).__init__(im, 255, 1, **properties)

            self.image = im

        def get_hash(self):
            return self.image.get_hash()

        def load(self):
            surf = im.Cache().get(self.image)

            try:
                renpy.display.render.blit_lock.acquire()
                rv = alpha_bar(surf)
            finally:
                renpy.display.render.blit_lock.release()

            return rv

        def predict_files(self):
            return self.image.predict_files()

    class o_color_scale(im.ImageBase):
        def __init__(self, color=[255.0,255.0,0.0,255.0], imagepath="interface/color_palete/color_palete.png", **properties):
            im = Image(imagepath)
            super(o_color_scale, self).__init__(im, 255, 255, **properties)
            self.image = im
            self.color = color

        def get_hash(self):
            return self.image.get_hash()

        def load(self):
            surf = im.Cache().get(self.image)

            try:
                renpy.display.render.blit_lock.acquire()
                rv = color_palette(surf, self.color)
            finally:
                renpy.display.render.blit_lock.release()

            return rv

        def predict_files(self):
            return self.image.predict_files()
        
        
        
        def set_color(self, color):
            self.color = color
            
        def get_main_color(self, x, y):
            new_color = [self.color[0],self.color[1],self.color[2], self.color[3]]
            
            for apply_x in xrange(3):
                new_color[apply_x] += (255-new_color[apply_x])*(float(x)/255.0)
            for apply_y in xrange(3):
                new_color[apply_y] -= new_color[apply_y]*(float(y)/255.0)
                new_color[apply_y] = clamp(new_color[apply_y], 0, 255)

                
            return new_color
            
    class MyScale(im.ImageBase):
        def __init__(self, im, width, height=None, **properties):

            if height is None:
                height = width

            im = Image(im)
            super(MyScale, self).__init__(im, width, height, **properties)

            self.image = im
            self.width = width
            self.height = height

        def get_hash(self):
            return self.image.get_hash()

        def load(self):

            surf = im.Cache().get(self.image)
            width, height = surf.get_size()

            width = int(width * self.width)
            height = int(height * self.height)


            try:
                renpy.display.render.blit_lock.acquire()
                rv = bilear_scale(surf, (width, height))
            finally:
                renpy.display.render.blit_lock.release()
            return rv

        def predict_files(self):
            return self.image.predict_files()
      
    def color_bar(src, dest=None):
        width = 1
        height = 255
        new_surface = renpy.display.pgrender.surface_unscaled((width, height), src)    
        
        height_six = 255.0/6.0
        
        for y in xrange(height):
            new_color = [0.0,0.0,0.0,255.0]

            if y < 255/6:
                new_color[0] = 255
                new_color[1] = 255*(float(y)/height_six)
            elif y < (255/6)*2:
                new_color[0] = 255-((y-height_six)*6)
                new_color[1] = 255
            elif y < (255/6)*3:
                new_color[1] = 255
                new_color[2] = 255*(float(y-height_six*2)/height_six)
            elif y < (255/6)*4:
                new_color[1] = 255-((y-(height_six*3))*6)
                new_color[2] = 255
            elif y < (255/6)*5:
                new_color[0] = 255*(float(y-height_six*4)/height_six)
                new_color[2] = 255
            else:
                new_color[0] = 255
                new_color[2] = 255-((y-(height_six*5))*5)
            
            new_color[0] = 255 if new_color[0] > 255 else new_color[0]
            new_color[1] = 255 if new_color[1] > 255 else new_color[1]
            new_color[2] = 255 if new_color[2] > 255 else new_color[2]
            new_color[0] = 0 if new_color[0] < 0 else new_color[0] 
            new_color[1] = 0 if new_color[1] < 0 else new_color[1] 
            new_color[2] = 0 if new_color[2] < 0 else new_color[2]
            
            new_surface.set_at((0,y), new_color)
                
        src = new_surface

        return src 
        
    def alpha_bar(src, dest=None):
        width = 255
        height = 1
        new_surface = renpy.display.pgrender.surface_unscaled((width, height), src)    
            
        for x in xrange(width):
            new_color = [255.0,255.0,255.0, 255.0-x]

            new_surface.set_at((x,0), new_color)
                
        src = new_surface

        return src 
      
    def color_palette(src, color, dest=None):
        width = 255
        height = 255
        new_surface = renpy.display.pgrender.surface_unscaled((width, height), src)     

        for y in xrange(height):
            for x in xrange(width):
                new_color = [0.0,0.0,0.0,255.0]

                new_color[0] = color[0]
                new_color[1] = color[1]
                new_color[2] = color[2]
                
                x_scaling = (float(x)/float(width))
                y_scaling = (float(y)/float(height)) 
                
                for j in xrange(3):
                    new_color[j] += (255-new_color[j]) * x_scaling
                    new_color[j] -= new_color[j] * y_scaling
                    new_color[j] = 0 if new_color[j] < 0 else new_color[j]
                    
                new_surface.set_at((x,y), new_color)
                
        src = new_surface

        return src 
        
    def bilear_scale(src, size, dest=None):
        """
        This scales src up or down to size. This uses both the pixellate
        and the transform operations to handle the scaling.
        """
        width, height = size
        srcwidth, srcheight = src.get_size()
        iwidth, iheight = srcwidth, srcheight

        if dest is None:
            dest = renpy.display.pgrender.surface_unscaled(size, src)

        if width == 0 or height == 0:
            return dest

        xshrink = 1
        yshrink = 1

        while iwidth >= width * 2:
            xshrink *= 2
            iwidth /= 2

        while iheight >= height * 2:
            yshrink *= 2
            iheight /= 2

        if iwidth != srcwidth or iheight != srcheight:
            new_surface = renpy.display.pgrender.surface_unscaled((iwidth, iheight), src)
            nx = iwidth / (srcwidth - 1.0)
            ny = iheight / (srcheight - 1.0)
            
            
            for y in xrange(iheight):
                for x in xrange(iwidth):
                    i = int(x / nx)
                    j = int(y / ny)
                    
                    #Need to be float so it not floor since it is a int else.
                    point1 = (float(x - i * nx),float( y - j * ny))
                    point2 = (float(nx - point1[0]), float(ny - point1[1]))

                    #Need to be float since much of the time it going to be a decimal number when apply weight.
                    cornor1 = src.get_at((i,j))
                    cornor2 = src.get_at((i,j+1))
                    cornor3 = src.get_at((i+1,j))
                    cornor4 = src.get_at((i+1,j+1))
                    new_color = cornor1
                    
                    for p in xrange(4):
                        summing = float(cornor1[p]) * point2[0] * point2[1]
                        summing += float(cornor2[p]) * point1[0] * point2[1]
                        summing += float(cornor3[p]) * point2[0] * point1[1]
                        summing += float(cornor4[p]) * point1[0] * point1[1]
                        
                        summing /= float(nx * ny)           
                        summing = int(abs(summing))
                        
                        new_color[p] = summing
                        
                    new_surface.set_at((x,y), new_color)
            src = new_surface

        _renpy.transform(src, dest,
                             0, 0,
                             1.0 * iwidth / width , 0,
                             0, 1.0 * iheight / height,
                             precise=1,
                             )

        return dest    
        
    UI_color_scale =  o_color_scale()
    UI_color_bar = o_color_bar()
    UI_alpha_bar = o_alpha_bar()