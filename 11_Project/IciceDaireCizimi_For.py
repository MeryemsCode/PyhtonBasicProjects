import turtle           #turtle modülünü dahil et
turtle.pensize(5)       #kalem kalınlığını 5 yap
turtle.color("white")   #kalem rengi beyaz
turtle.bgcolor("blue")   #arka plan kırmızı
    
for x in range(36):     #36 adet içiçe daire yap
    turtle.home()       #merkeze git
    turtle.left(x*10)   #10,20,30...350 derece sola sön
    turtle.circle(100)  #100 yarı çaplı daire çiz

