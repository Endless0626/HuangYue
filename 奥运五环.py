import turtle
coordA=(-110,0,110,-55,55)     #五个图起点坐标的x值
coordB=(-25,-25,-25,-75,-75)   #五个圆起点坐标的y值
color=('red','blue','green','yellow','black')
turtle.pensize(10)
for i in range(5):
    turtle.penup()
    turtle.goto(coordA[i],coordB[i]) #移动到第i个圆的起点坐标处
    turtle.pendown()
    turtle.pencolor(color[i])
    turtle.circle(45,None)
    i=i+1
turtle.hideturtle()
turtle.done()
