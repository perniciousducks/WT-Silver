screen mouse_tooltip():
    layer "interface"
    tag tooltip
    zorder 5

    $ tooltip = GetTooltip()

    if preferences.tooltip and tooltip:
        add MouseTooltip(Window(Text(tooltip, style="tooltip_text"), style="frame", background="#00000080"), padding=(10,5))

init python:
    class MouseTooltip(renpy.Displayable):
        def __init__(self, child, padding=None, **kwargs):
            super(MouseTooltip, self).__init__(**kwargs)

            self.child = renpy.displayable(child)
            self.padding = padding or (0,0)
            self.x, self.y = renpy.get_mouse_pos()

        def render(self, width, height, st, at):
            # Render child displayable
            child_render = renpy.render(self.child, width, height, st, at)
            self.width, self.height = child_render.get_size()
            render = renpy.Render(self.width, self.height)

            # Position bottom-right of cursor, unless it's off screen
            x = self.x + self.padding[0]
            y = self.y + self.padding[1]
            if x + self.width > config.screen_width:
                x = self.x- self.width - self.padding[0]
            if y + self.height > config.screen_height:
                y = self.y - self.height - self.padding[1]

            render.blit(child_render, (x,y))
            return render

        def event(self, ev, x, y, st):
            # Update mouse position
            if ev.type == pygame.MOUSEMOTION:
                self.x, self.y = x, y
                renpy.redraw(self, 0)
