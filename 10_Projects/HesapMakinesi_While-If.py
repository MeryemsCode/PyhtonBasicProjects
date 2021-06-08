while True:                                                          # sonsuz döngü 0 girilene kadar çalışır
    print("-"*30)                                                    # - işaretini 30 kez yanyana yazar
    print("1-Toplama\n 2-Çıkarma\n 3-Çarpma\n 4-Bölme\n 0-Çıkış")    # \n  enter işine yarar
    print("-"*30)

    islem=int(input("İşlemin Sayısını Giriniz"))                     #islemin sayısını kullanıcan alıyoruz

    if islem==0:                                                     #seçilen işlem 0 ise break ile çıkış yapılacak
        print("Çıkış İşlemi Yapılmıştır")
        break

    elif islem==1:                                                   #seçilen işlem 1 ise toplama yapılacak
        sayi1=int(input("1.Sayıyı Giriniz"))
        sayi2=int(input("2.Sayıyı Giriniz"))
        print("Sonuç=",sayi1+sayi2)

    elif islem==2:                                                   #seçilen işlem 2 ise çıkarma yapılacak
        sayi1=int(input("1.Sayıyı Giriniz"))
        sayi2=int(input("2.Sayıyı Giriniz"))
        print("Sonuç=",sayi1-sayi2)

    elif islem==3:                                                   #seçilen işlem 3 ise çarpma yapılacak
        sayi1=int(input("1.Sayıyı Giriniz"))
        sayi2=int(input("2.Sayıyı Giriniz"))
        print("Sonuç=",sayi1*sayi2)

    elif islem==4:                                                   #seçilen işlem 4 ise bölme yapılacak
        sayi1=int(input("1.Sayıyı Giriniz"))
        sayi2=int(input("2.Sayıyı Giriniz"))
        print("Sonuç=",sayi1/sayi2) 

    else:                                                            #yukardakilerden farklı bir işlem numarasında hata yazısı çıkacak
        print("Hatalı İşlem Sayısı Girdiniz")