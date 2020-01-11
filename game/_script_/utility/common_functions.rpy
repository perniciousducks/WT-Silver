init -1 python:
    # Import commonly used python modules
    #import os as system # Already imported in devtools.rpy
    import time
    import math
    import random
    import pygame
    import colorsys
    import itertools
    
    def num_to_word(n, readable=True):
        """Transcript numbers (integers) into readable words."""
        n = int(n)
        units = ("","one","two","three","four","five","six","seven","eight","nine")
        teens = ("","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen")
        tens = ("","ten","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety")
        thousands = ("","thousand","million","billion","trillion","quadrillion","quintillion","sextillion","septillion","octillion","nonillion","decillion","undecillion","duodecillion","tredecillion","quattuordecillion","sexdecillion","septendecillion","octodecillion","novemdecillion","vigintillion")
        
        output = []
        if n == 0: 
            output.append("zero")
        else:
            s = str(n)
            groups = (len(s)+2)/3
            s = s.zfill(groups*3)
            for i in xrange(0, groups*3, 3):
                h,t,u = int(s[i]),int(s[i+1]),int(s[i+2])
                g = groups-(i/3+1)
                if h >= 1:
                    output.append(units[h])
                    output.append("hundred")
                if t > 1:
                    output.append(tens[t])
                    if u >= 1: output.append(units[u])
                elif t == 1:
                    output.append(teens[u]) if u >=1 else output.append(tens[t])
                else:
                    if u >= 1: output.append(units[u])
                if (g>=1) and ((h+t+u)>0): output.append(thousands[g]+",")
        if readable:
            return " ".join(output)
        return output
        
    def clamp(n, smallest, largest):
        return max(smallest, min(n, largest))
        
    def whiteTint(image):
        return im.MatrixColor( image, im.matrix.tint(1.1, 1.1, 1.1))

    def grayTint(image):
        return im.MatrixColor( image, im.matrix.desaturate() * im.matrix.tint(1.0, 1.0, 1.0))

    def yellowTint(image):
        return im.MatrixColor( image,  im.matrix.tint(1.2, 1.1, 0.7))
        
    def get_head_icon(name):
        return "interface/icons/head/head_"+str(name)+"_1.png"

    def get_zoom(image, xsize, ysize):
        if isinstance(image, basestring):
            image = im.Image(image)
        
        r = renpy.render(image, 800, 800, 0, 0)
        x, y = r.get_size()

        if xsize / x < ysize / y:
            return min(1.0, xsize / x)
        return min(1.0, ysize / y)
        
    def get_boundries(image):
        if isinstance(image, basestring):
            image = im.Image(image)

        myRender = renpy.render(image, 800, 800, 0, 0)
        sizes = myRender.get_size()
        return (0, 0, sizes[0], sizes[1])
        
    def image_hover(image):
        """Returns slightly brighter image used during hover events"""
        return im.MatrixColor(image, im.matrix.brightness(0.12))

    def image_alpha(image, alpha=0.5):
        """Returns an image with changed alpha 0 - fully transparent 1 - fully visible"""
        return im.MatrixColor(image, im.matrix.opacity(alpha))
        
    def set_clipboard(txt):
        txt = str(txt)
        pygame.scrap.put(pygame.scrap.SCRAP_TEXT, txt.encode("utf-8"))
        
    def get_clipboard():
        clipboard = pygame.scrap.get(pygame.scrap.SCRAP_TEXT)
        if clipboard:
            return clipboard
        return None
        
    def evaluate(txt):
        return __import__('ast').literal_eval(txt)
        
    def set_text_color(day=True):
        # This function must be invoked in a new context by preferences screen
        renpy.show_screen("preferences")
        # Temporarily change interface color
        tmp_color = renpy.store.interface_color
        renpy.call_in_new_context("update_interface_color", "gray")
        if day:
            preferences.text_color_day = color_picker(get_rgb_list(preferences.text_color_day), False, "Day Text Colour")
            preferences.text_color_day = get_hex_string(preferences.text_color_day[0]/255.0, preferences.text_color_day[1]/255.0, preferences.text_color_day[2]/255.0)
        else:
            preferences.text_color_night = color_picker(get_rgb_list(preferences.text_color_night), False, "Night Text Colour")
            preferences.text_color_night = get_hex_string(preferences.text_color_night[0]/255.0, preferences.text_color_night[1]/255.0, preferences.text_color_night[2]/255.0)
        # Reset interface color
        renpy.call_in_new_context("update_interface_color", tmp_color)