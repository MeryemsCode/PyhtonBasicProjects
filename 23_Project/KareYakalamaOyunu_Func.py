#modülleri dahil et
import turtle
import random

#oyun alanım 400,400 olsun
turtle.setup(400,400)

#ok isminde 1 adet Turtle üret
ok=turtle.Turtle()
ok.penup()

#hedef isminde 1 adet Turtle üret, sekli kare olsun
hedef=turtle.Turtle()
hedef.shape("square")

#hedefin rastgele yerlere gitmesini sağlayan FONK
def rastgelekonum():
    hedef.penup()
    hedef.setpos(random.randint(-300,300),random.randint(-300,300))
    hedef.showturtle()

#oku yukarı döndürür
def yukari():
    ok.right(15)
#oku asagı dondurur
def asagi():
    ok.left(15)

#yukari ve asagi fonksiyonlarını YUKARI ve AŞAĞI yön tuşlarına ata
turtle.onkeypress(yukari,"Up")
turtle.onkeypress(asagi,"Down")
#hangi tuşlara basıldığını takip etmem
turtle.listen()

#hedefi rastgele bir konuma at
rastgelekonum()
while True: #sürekli olarak
    ok.fd(1)    #ok 1 adum gitsin.

    #uzaklık hesaplamak için yazdığım PİSAGOR kodu
    x=(ok.xcor()-hedef.xcor())
    y=(ok.ycor()-hedef.ycor())
    uzaklik=((x*x)+(y*y))**0.5

    #eğer uzaklık 15ten az ise,
    if uzaklik<15:
        hedef.hideturtle()    #önce hedefi gizle
        rastgelekonum()         #rastgele konuma gönder
















    
