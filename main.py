#Translates text to Kotoron Glyphs

import drawsvg as draw
fill_colour = '#0fd414'
fill_opacity = '0.278605'
stroke_width = '2.624'
stroke_colour = '#edea00'
misc_shape_data = [fill_colour, fill_opacity, stroke_width, stroke_colour]

def draw_circle(d,x,y,r,misc_shape_data):
    d.append(draw.Circle(x, y, r,
        fill=misc_shape_data[0], fill_opacity=misc_shape_data[1], stroke_width=misc_shape_data[2], stroke=misc_shape_data[3]))
    return d

def calc_end_of_line(x,y,angle,size):
    end_x = 0
    end_y = 0
    end_coords = [end_x,end_y]
    return end_coords

def draw_triangle(d,x_start,y_start,height,misc_shape_data): #TODO
    upper_point = [0,0]
    left_point = [0,0]
    right_point = [0,0]
    triangle = draw.Lines(48, 16, 16, 96, 96, 48, 0, 48, 88, 96,
        stroke=misc_shape_data[3], fill=misc_shape_data[0], close='true')
    d.append(triangle)
    return d

def calc_coords_on_circle(parent_x,parent_y,parent_r):
    child_x = parent_x
    child_y = parent_y - parent_r
    child_r = 10

    child_data = [child_x,child_y,child_r]
    return child_data

syllable = input("What do you want to translate?")

shape_sides = len(syllable)
print("There are " + str(shape_sides) + " letters in this syllable")



d = draw.Drawing(200, 100, origin='center')
r = draw.Rectangle(-80, -50, 40, 50, fill=fill_colour)
d.append(r)

d = draw_circle(d,-40,10,30,misc_shape_data)
child_data = calc_coords_on_circle(-40,10,30)
d = draw_circle(d,child_data[0], child_data[1], child_data[2],misc_shape_data)
draw.tri

#Save and end
d.save_svg("Kotoron_"+str(syllable)+".svg")
