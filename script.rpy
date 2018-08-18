init python:
    colours = ['#FFFFFF', '#000000', '#FF0000', '#00FF00', '#0000FF', '#FFFF00', '#00FFFF', '#FF00FF']
    default_colour = '#000'
    freehand_canvas = FreehandCanvas(default_colour, 400, 400)


screen freehand_draw():

    frame:
        background "#FFF"
        xsize 400
        ysize 400

        add freehand_canvas
        
    hbox:
        for colour in colours:
            button:
                xsize 20
                ysize 20
                background colour
                action SetField(freehand_canvas, 'colour', colour)
        

        textbutton "Clear Canvas" action Function(freehand_canvas.clear)
        
label start:

    call screen freehand_draw
    return
