meyveler={}   #meyveler isminde bir sözlük
giris=-1      #kullanıcıdan aldıgım secenek

while giris!="0":
    #kullanıcının seçenekleri
    print("Yapacağınız işlemin numarasını seçiniz: ")
    giris=input("1- Kayıt Ekle \n 2- Kayıt Düzelt \n 3- Kayıt Ara\n 4- Tümünü Listele\n 5- KAyıt Sil\n 6-Tümünü Sil\n 0-Çıkış\n")
    

    if giris=="0":   #eğer 0 basarsa, sistmden cıkar
        quit()
    if giris=="1":   #eğer 1 basarsa kayıt ekler
        meyveadi=input("Meyve adı giriniz: ")   #meyve adi gir
        fiyat=input("Fiyat giriniz: ")         #fiyat gir
        meyveler[meyveadi]=fiyat              #meyveler sözlüğüne ekle
        print("Meyve Eklendi")               #kullanıcıya bilgi ver

    if giris=="2":       #kayıt düzelt
        meyveadi=input("Meyve adı giriniz: ")    #meyve adi iste
        if meyveadi in meyveler.keys():        #eğer KEYler arasında varsa
            fiyat=input("Fiyat giriniz: ")       #fiyat iste
            meyveler[meyveadi]=fiyat           #fiyatı güncelle
            print("Meyve Düzeltildi")         #kullanıcıya bilgi ver
        else:         #eğer yoksa
            print("Böyle bir meyve yok")      #meyve olmadığını söyle
    if giris=="3":          #kayıt ara
        meyveadi=input("Meyve adı giriniz: ")    #meyveadi nı iste
        durum=meyveler.get(meyveadi,"Böyle bir meyve yok")   #var
        print(f"{durum}")
    if giris=="4":             #tümünü listele
        for meyveadi in meyveler.keys():       #meyveler sözlüğündeki 
            print(meyveadi,meyveler[meyveadi])    #meyve adi ve fiyatlarını bas
    if giris=="5":           #kaydı sil
        meyveadi=input("Meyve adı giriniz: ")     #meyve adini al
        durum=meyveler.pop(meyveadi,"Böyle bir meyve yok")   #varsa sil, yoksa mesaj
        print(f"{durum}")
    if giris=="6":    #tümünü sil
        meyveler={}   #meyveler sözlüğünü boşalt   meyveler.clear()
        print("Tümü Silindi")
    
        
        
