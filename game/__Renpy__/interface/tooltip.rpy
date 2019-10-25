screen mouse_tooltip():
    zorder 100
    tag tooltip

    $ tooltip = GetTooltip()

    if persistent.tooltip and tooltip:
        add MouseTooltip(
            Window(
                Text(tooltip, color="#FFF", size=14),
                style="frame",
                style_prefix="dropdown_gm"
            ),
            padding=(3,3)
        )

init python:
    class MouseTooltip(renpy.Displayable):
        def __init__(self, child, padding=None, **kwargs):
            super(MouseTooltip, self).__init__(**kwargs)

            self.child = renpy.displayable(child)
            self.padding = padding or (0,0)
            (x,y) = renpy.get_mouse_pos()
            self.x = x
            self.y = y

        def render(self, width, height, st, at):
            # Render child displayable
            child_render = renpy.render(self.child, width, height, st, at)
            self.width, self.height = child_render.get_size()
            render = renpy.Render(self.width, self.height)

            # Adjust position for screen quadrant
            sw = config.screen_width
            sh = config.screen_height
            x = self.x + (-self.width - self.padding[0] if self.x > sw / 2 else self.padding[0])
            y = self.y + (-self.height - self.padding[1] if self.y > sh / 2 else self.padding[1])

            # Place the render near the mouse
            render.blit(child_render, (x,y))
            return render

        def event(self, ev, x, y, st):
            # Check if pointer is in motion
            if ev.type == pygame.MOUSEMOTION:
                # Update mouse position
                self.x = x
                self.y = y
                renpy.redraw(self, 0)
