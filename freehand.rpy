init python:
    import pygame


    class FreehandDraw(renpy.Displayable):
        def __init__(self, colour, line_width, width, height):
            super(FreehandDraw, self).__init__(self)

            self.colour = colour
            self.line_width = line_width
            
            self.width = width
            self.height = height

            self.lines = []

            self.drawing = False
            self.active = True

        def render(self, width, height, st, at):
            render = renpy.Render(self.width, self.height)

            if self.lines:
                render.canvas().lines(self.colour, False, self.lines, self.line_width)

            return render

        def event(self, ev, x, y, st):
            if self.active:
                if renpy.map_event(ev, 'mousedown_1'):
                    self.drawing = True

                elif renpy.map_event(ev, 'mouseup_1'):
                    self.drawing = False

                if self.drawing:
                    self.lines.append((x, y))

                    renpy.redraw(self, 0)


    class FreehandLine(FreehandDraw):
        def event(self, ev, x, y, st):
            if self.active:
                if renpy.map_event(ev, 'mousedown_1'):
                    self.lines.append((x, y))

                elif renpy.map_event(ev, 'mouseup_1'):
                    if len(self.lines) >= 2:
                        self.lines = self.lines[:-1]
                    self.lines.append((x, y))

                # If mouse button is held down and then mouse is moved,
                # draw a temporary line.
                pressed = pygame.mouse.get_pressed()
                if pressed[0] and ev.type == pygame.MOUSEMOTION:
                    if len(self.lines) >= 2:
                        self.lines = self.lines[:-1]
                    self.lines.append((x, y))

                renpy.redraw(self, 0)

    class Circle(FreehandDraw):
        def __init__(self, colour, line_width, width, height):
            super(Circle, self).__init__(colour, line_width, width, height)

            self.radius = 0

        def render(self, width, height, st, at):
            render = renpy.Render(self.width, self.height)

            if self.lines:
                x = render.canvas().circle(self.colour, self.lines[0], radius=self.radius, width=self.line_width)

            return render

        def event(self, ev, x, y, st):
            if self.active:
                if renpy.map_event(ev, 'mousedown_1'):
                    self.lines.append((x, y))

                # If mouse button is held down and then mouse is moved,
                # draw a temporary circle.
                pressed = pygame.mouse.get_pressed()
                if pressed[0] and ev.type == pygame.MOUSEMOTION:
                    dx = abs(x - self.lines[0][0])
                    dy = abs(y - self.lines[0][1])                    
                    d = dx + dy

                    self.radius = d

                renpy.redraw(self, 0)

    class CircleFill(Circle):
        def __init__(self, colour, line_width, width, height):
            # Filled circles can only have a line_width of 0.
            line_width = 0
            super(Circle, self).__init__(colour, line_width, width, height)

            self.radius = 0


    class FreehandCanvas(renpy.Displayable):
        # Enums
        PENCIL = 0
        LINE = 1
        CIRCLE = 2
        CIRCLE_FILL = 3

        def __init__(self, colour, width, height):
            super(FreehandCanvas, self).__init__(self)

            self._colour = colour
            self.width = width
            self.height = height

            self.line_width = 1
            
            self.children = []
            self.current_child = None

            self.mode = FreehandCanvas.PENCIL

            self.mode_mapping = {
                0: FreehandDraw,
                1: FreehandLine,
                2: Circle,
                3: CircleFill,
            }

        @property
        def colour(self):
            c = Color(self._colour).rgb
            values = []
            for item in c:
                values.append(int(item) * 255)
            return tuple(values)

        @colour.setter
        def colour(self, colour):
            self._colour = colour

        def render(self, width, height, st, at):
            render = renpy.Render(self.width, self.height)

            for child in self.children:
                render.place(child, 0, 0)

            return render

        def event(self, ev, x, y, st):
            if renpy.map_event(ev, 'mousedown_1'):
                new_child = self.mode_mapping[self.mode](self.colour, self.line_width, self.width, self.height)
                self.children.append(new_child)
                self.current_child = new_child
                renpy.redraw(self, 0)

            if renpy.map_event(ev, 'mouseup_1'):
                self.current_child.active = False

            for child in self.children:
                child.event(ev, x, y, st)


        def clear(self):
            self.children = []
            renpy.redraw(self, 0)

        def visit(self):
            return self.children
