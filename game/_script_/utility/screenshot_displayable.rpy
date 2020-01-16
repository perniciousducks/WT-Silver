
init -1 python:

    class ScreenshotImage(im.ImageBase):
        def __init__(self, **properties):
            super(ScreenshotImage, self).__init__(**properties)
            root_widget = renpy.display.interface.surftree
            if not root_widget:
                raise Exception("Root widget not available.")
            self.shotsurf = shot = renpy.display.draw.screenshot(root_widget, preferences.fullscreen)
        
        def load(self):
            return self.shotsurf

define screenshot_image = None

screen screenshot_image():
    zorder 100
    add im.Blur(screenshot_image, 2)

label test_screenshot_blur:
    $ screenshot_image = ScreenshotImage()
    show screen screenshot_image
    pause
    hide screen screenshot_image
