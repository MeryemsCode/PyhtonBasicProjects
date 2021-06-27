import turtle

def olimpiyat(x,y,renk):
    turtle.pensize(12)
    turtle.pencolor(renk)
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.circle(100)

olimpiyat(-200,50,"blue")
olimpiyat(-50,50,"black")
olimpiyat(100,50,"red")
olimpiyat(-125,-50,"yellow")
olimpiyat(25,-50,"green")