style draw_ui:
    spacing 2

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

    circle_hover_icon = Fixed(
        Image("circle_icon.png"),
        Transform(Frame(Solid("#FFF"), 5, 5), alpha=0.5),
        xysize=(32, 32),
    )
  
    circle_fill_hover_icon = Fixed(
        Image("circle_icon.png"),
        Transform(Frame(Solid("#FFF"), 5, 5), alpha=0.5),
        xysize=(32, 32),
    )
  
    thickness_hover_icon = Fixed(
        Image("thickness.png"),
        Transform(Frame(Solid("#FFF"), 5, 5), alpha=0.5),
        xysize=(32, 32),
    )
    
    thickness_2_hover_icon = Fixed(
        Image("thickness_2.png"),
        Transform(Frame(Solid("#FFF"), 5, 5), alpha=0.5),
        xysize=(32, 32),
    )
  
    thickness_3_hover_icon = Fixed(
        Image("thickness_4.png"),
        Transform(Frame(Solid("#FFF"), 5, 5), alpha=0.5),
        xysize=(32, 32),
    )
  
    thickness_4_hover_icon = Fixed(
        Image("thickness_4.png"),
        Transform(Frame(Solid("#FFF"), 5, 5), alpha=0.5),
        xysize=(32, 32),
    )
  
screen freehand_draw():

    vbox:
        hbox:
            vbox:
                style "draw_ui"
                imagebutton idle "pencil_icon.png" hover pencil_hover_icon selected_idle pencil_hover_icon action SetField(freehand_canvas, 'mode', FreehandCanvas.PENCIL)
                imagebutton idle "line_icon.png" hover line_hover_icon selected_idle line_hover_icon action SetField(freehand_canvas, 'mode', FreehandCanvas.LINE)
                imagebutton idle "circle_icon.png" hover circle_hover_icon selected_idle circle_hover_icon action SetField(freehand_canvas, 'mode', FreehandCanvas.CIRCLE)
                imagebutton idle "circle_icon_fill.png" hover circle_fill_hover_icon selected_idle circle_fill_hover_icon action SetField(freehand_canvas, 'mode', FreehandCanvas.CIRCLE_FILL)
            
            frame:
                background "#FFF"
                xsize 400
                ysize 400

                add freehand_canvas
         
        hbox:
            style "draw_ui"
            for colour in colours:
                button:
                    xsize 20
                    ysize 20
                    background colour
                    action SetField(freehand_canvas, 'colour', colour)

            textbutton "Clear Canvas" action Function(freehand_canvas.clear)
     
        hbox:
            style "draw_ui"
            imagebutton idle "thickness.png" hover thickness_hover_icon selected_idle thickness_hover_icon action SetField(freehand_canvas, 'line_width', 1)
            imagebutton idle "thickness_2.png" hover thickness_2_hover_icon selected_idle thickness_2_hover_icon action SetField(freehand_canvas, 'line_width', 2)
            imagebutton idle "thickness_3.png" hover thickness_3_hover_icon selected_idle thickness_3_hover_icon action SetField(freehand_canvas, 'line_width', 4)
            imagebutton idle "thickness_4.png" hover thickness_4_hover_icon selected_idle thickness_4_hover_icon action SetField(freehand_canvas, 'line_width', 8)
    
label start:

    call screen freehand_draw
    return
