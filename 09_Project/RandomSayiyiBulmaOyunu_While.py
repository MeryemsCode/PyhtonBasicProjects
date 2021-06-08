import random                                     #random modülünü kullan
randomsayi= random.randint(1,100)                 #1 ile 100 arasında random sayı üret

sayac=0                                           #kac kere tahmin ettiğimi tut
tahmin=0                                        

while tahmin!=randomsayi:                         #tahmin random sayıya eşit olmadığı sürece devam et
    tahmin=int(input("Tahmini giriniz [1,100]"))
    sayac=sayac+1                                 #her döngüde sayacı 1 arttır
    
    if tahmin>randomsayi:
        print("Aşağı")
    if tahmin<randomsayi:
        print("Yukarı")

#döngü bitince aşağıdakini yaz
print("Bravo",sayac,"kerede bildiniz.")