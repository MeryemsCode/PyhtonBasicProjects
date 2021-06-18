#şifre en az 8 karakter, en az 1 büyük harf, en az 1 küçük harf, en az 1 sayıdan olusmalı

sifre=input("Lütfen şifre giriniz: ")
buyuk="ABCDEFGHIJKLMNOPRSTUVYZWXQ"   #buyuk harf listesi olusturduk
kucuk="abcdefghijklmnoprstuvyzwxq"   #küçük harf listesi olusturduk
digit="0123456789"                  #sayı listesi olusturduk

bhsayi=0                            #kaç adet büyük harf var
khsayi=0                            #kaç adet küçük harf var
dsayi=0                             #kaç adet sayı var

for harf in sifre:                  #şifredeki her bir harf için
    if harf in buyuk:               #eğer büyük harf ise, sayilari bir arttır
        bhsayi=bhsayi+1

    elif harf in kucuk:
        khsayi=khsayi+1

    elif harf in digit:
        dsayi=dsayi+1

#döngü bitti
 
#eğer büyük harf yoksa ya da küçük harf yoksa ya da sayı yoksa ya da şifre 8 karakterden az ise;

if (bhsayi==0) or (khsayi==0) or (dsayi==0) or (len(sifre)<8): 
    print("GÜVENSİZ ŞİFRE! TEKRAR DENEYİNİZ")
else:
    print("GÜVENLİ ŞİFRE")
