import turtle
import random

turtle.bgcolor("black")
turtle.pencolor("white")

#ekrana tıklanınca gelecek X,Y parametreli olan yildizcizme fonk tanımlıyorum
def yildizcizme(x,y):
    boyut=random.randint(5,30) #yıldız boyutunu belirle 2 ile 10 arası
    turtle.penup()             #kalemi kaldır
    turtle.goto(x,y)           #X,Y noktasına git
    turtle.pendown()           #kalemi bastır
    turtle.fillcolor("gray")   #dolgu rengini belirle 
    turtle.begin_fill()        #dolguya başla
    for x in range(5):         #yıldız çiz
        turtle.fd(boyut)
        turtle.right(120)
        turtle.fd(boyut)
        turtle.left(48)
    turtle.end_fill()          #döngü bitince, içini doldurmayı bırak

    #turtle ekranı tıklandığında YILDIZCIZME fonksiyonu cagirilacak
turtle.onscreenclick(yildizcizme)
