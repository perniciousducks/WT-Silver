
default screenshot_image = None

init -1 python:
    class ScreenshotImage(im.ImageBase):
        def __init__(self, root, **properties):
            super(ScreenshotImage, self).__init__(root, **properties)
            self.root = root
            # self.cache = False
            # Sometimes causes segfault, maybe only if cache = True?

        def load(self):
            sw, sh = config.screen_width, config.screen_height
            render = renpy.display.render.render_screen(self.root, sw, sh)
            shot = renpy.display.draw.screenshot(render, preferences.fullscreen)
            shot = renpy.display.scale.real_transform_scale(shot, (config.screen_width, config.screen_height))
            return shot

        @staticmethod
        def capture(retain=True):
            if renpy.display.interface.surftree:
                if retain:
                    # Prevent the image from being recaptured after load
                    renpy.retain_after_load()
                # Grab the most recently rendered displayables
                try:
                    root = renpy.display.interface.surftree.render_of[0].children[-1].layers["screens"]
                except:
                    root = renpy.display.interface.surftree.render_of[0]
                return ScreenshotImage(root)
            elif config.developer:
                raise Exception("Root surface tree is not available.")
            else:
                return None

# Usage example

screen screenshot_image():
    zorder 100
    if screenshot_image:
        add im.Blur(screenshot_image, 2)