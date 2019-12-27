init python:
    ui_rewindFrame = 0
    
    def animationHandler(trans, st, at):
        global ui_rewindFrame
        if ui_rewindFrame < 80:
            ui_rewindFrame += 1
        else:
            ui_rewindFrame = 0
        
image ui_rewind:
    function animationHandler
    DynamicImage("interface/rewind/[ui_rewindFrame].png")
    pause 0.05
    repeat