from turtle import*
setposition(-60,0)                       #move turtle to x=-60,y=0,starting drawing slightly left of center

speed(0)                                 #Fastest drawing speed
bgcolor("black")                          #background color
colors=["red","green"]
pensize(2)
for i in range(50):
    color(colors[i%2])
    rt(i)                                  #Turns turle right by i degrees
    circle(90,i)
    up()                                   #Turtle moves without drawing
    fd(i+50)
    down()                                 #Drawing resumes
    rt(90)                                 #turns Turtle right by 90
    fd(i-65)
    hideturtle()
done()