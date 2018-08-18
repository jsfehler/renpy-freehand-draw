init python:
    class FreehandDraw(renpy.Displayable):
        def __init__(self, colour, width, height):
            super(FreehandDraw, self).__init__(self)
            
            self.colour = colour
            
            self.width = width
            self.height = height
            
            self.lines = []
            
            self.drawing = False
            self.active = True

        def render(self, width, height, st, at):
            render = renpy.Render(self.width, self.height)
            
            if self.lines:
                render.canvas().lines(self.colour, False, self.lines)
            
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
   

    class FreehandCanvas(renpy.Displayable):
        def __init__(self, colour, width, height):
            super(FreehandCanvas, self).__init__(self)
            
            self._colour = colour
            self.width = width
            self.height = height
            
            self.children = []
            self.current_child = None
        
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
                new_child = FreehandDraw(self.colour, self.width, self.height)
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
