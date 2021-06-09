turkcekarakter="üÜğĞıİşŞçÇöÖ"

metin=input("Lütfen bir metin yazınız: ")


for harf in metin:          #metnin içindeki her bir harf için
    if harf in turkcekarakter:      #o harf, turkce karakter listesinde var mı
        print("Türkçe Karakter: ",harf)  #varsa ekrana yaz
