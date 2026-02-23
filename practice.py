from turtle import*
speed(0)
bgcolor("black")
colors=["orange","white"]
hideturtle()
for i in range(122):
    goto(0,0)             #move turtle to center of design
    color(colors[i%2])    #change color alternativley between orange and white
    #i    i%2     color
    # 0     0        orange
    # 1     1        white
    # 2     0         orange
    # 3     1         white


    forward(130)          #draw a length of 130 and move ahead
    left(3)                 #Turns turtle 3 degrees left
    circle(40)              #Draw a circle of radius 40
    forward(130)             #extend the shape further
    rt(180)               #Turns turtle around
done()


#turtle-->is agraphics library in python used to draw shapes 
# using commands like forward(),left(),right(),circle()
# speed=0--->set maximum drawing speed(0=fastest)
# bgcolor-->set background colour

