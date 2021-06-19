#random modülünü dahil ettik
import random
pcpuan=0
benpuan=0

#secenekleri DEMET(TUPLE) olarak yaptık çünkü değişsin istemiyoruz
secenekler=("taş","kağıt","makas")

#benim tahminimi istedik, çıkmak için q
ben=input("taş? kağıt? makas? birini seçiniz (küçük harflerle yazınız) / çıkmak için q: ")

#bu oyun kullanıcı "q" harfine basmadığı sürece devam eder
while ben!="q":
    pc=random.choice(secenekler)       #bigisayar rastgele bir secenek edinsin

    print("ben:",ben,"/ bilgisayar:",pc)   #ekrana bilgi ver

    if (ben=="taş" and pc=="kağıt"):      
        print("PC KAZANDI")
        pcpuan=pcpuan+1
    elif (ben=="taş" and pc=="makas"):
        print("BEN KAZANDIM")
        benpuan=benpuan+1
    elif (ben=="kağıt" and pc=="taş"):
        print("BEN KAZANDIM")
        benpuan=benpuan+1
    elif (ben=="kağıt" and pc=="makas"):
        print("PC KAZANDI")
        pcpuan=pcpuan+1
    elif (ben=="makas" and pc=="taş"):
        print("PC KAZANDI")
        pcpuan=pcpuan+1
    elif (ben=="makas" and pc=="kağıt"):
        print("BEN KAZANDIM")
        benpuan=benpuan+1
    else:                                   #yukarıdakilerden hiç biri değilse
        print("BERABERE")                    #berabere

    ben=input("taş? kağıt? makas? çıkmak için q: ")  #yeniden soru sor
    
#döngü bitti
print("ben:",benpuan,"/ PC:",pcpuan)

