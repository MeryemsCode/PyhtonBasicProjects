sinav=[]                                             #sınav listesi oluşturduk

sayac=1                                              
toplam=0

while sayac <=10:                                    #10 kez not alıyoruz
    notunuz=int(input("Sınav notunuzu yazınız: "))   
    sinav.append(notunuz)                            #listeye ekliyoruz
    toplam=toplam+notunuz                            #toplamı arttırıyoruz
    sayac=sayac+1                                    #sayacı 1 arttırıyoruz

sinav.sort()                                         #notları küçükten büyüğe sıralıyoruz
print("En düşük notunuz: ",sinav[0])                 #en küçük not en başta
print("En yüksek notunuz: ",sinav[-1])               #en yüksek yok en sonda
print("Ortalamanız: ",int(toplam/sayac))             #ortalamayı int yaparak ekrana basıyoruz