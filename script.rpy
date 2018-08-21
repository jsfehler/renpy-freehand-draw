init python:
    colours = ['#FFFFFF', '#000000', '#FF0000', '#00FF00', '#0000FF', '#FFFF00', '#00FFFF', '#FF00FF']
    default_colour = '#000'
    freehand_canvas = FreehandCanvas(default_colour, 400, 400)

    # Quick and dirty hover icons
    pencil_hover_icon = Fixed(
        Image("pencil_icon.png"),
        Transform(Frame(Solid("#FFF"), 5, 5), alpha=0.5),
        xysize=(32, 32),
    )

    line_hover_icon = Fixed(
        Image("line_icon.png"),
        Transform(Frame(Solid("#FFF"), 5, 5), alpha=0.5),
        xysize=(32, 32),
    )

screen freehand_draw():

    vbox:
        hbox:
            vbox:
                imagebutton idle "pencil_icon.png" hover pencil_hover_icon selected_idle pencil_hover_icon action SetField(freehand_canvas, 'mode', FreehandCanvas.PENCIL)
                imagebutton idle "line_icon.png" hover line_hover_icon selected_idle line_hover_icon action SetField(freehand_canvas, 'mode', FreehandCanvas.LINE)

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
