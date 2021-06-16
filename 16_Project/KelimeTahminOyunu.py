aranan="MERYEM"

gorunen="?"*len(aranan)

while aranan!=gorunen:
    harf=input(gorunen + " => icin büyük harf giriniz: ")

    for i in range(0,len(aranan)):

        if harf==aranan[i]:
            gorunen=gorunen[:i]+harf+gorunen[i+1:]


print ("Bravo! "+ gorunen + " kelimesini buldunuz")
