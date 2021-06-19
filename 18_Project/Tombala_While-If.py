import random                
tombala=[]                                    #tombala adında boş bir liste üret

while len(tombala)<15:                        #tombala 15 elamandan az olduğu sürece
    rastgele=random.randint(1,99)             #random bir sayı üret(1,99 arasında)
    if rastgele not in tombala:               #eğer sayı o listede yoksa
        tombala.append(rastgele)              #listeye ekle

tombala.sort                                  #listeyi sırala

while len(tombala)>0:
    print(tombala)
    okunan=int(input("Torbadan çıkan sayıyı giriniz (çıkış için 0): "))

    if okunan==0:
        quit()
    else:
        if okunan in tombala:
            print(f"{okunan} kartınızda var")
            tombala.remove(okunan)
        else:
            print(f"{okunan} kartınızda yok")

print("Oyun bitti!")
