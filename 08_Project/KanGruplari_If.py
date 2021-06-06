grup=input("Kan grubunu giriniz (A/AB/B/0): ")
faktor=input("Rh faktörünü giriniz (+/-): ")

if grup=="0" and faktor=="+":
    print("0+ ve 0- den alır")
elif grup=="0" and faktor=="-":
    print("sadece 0- den alır :(")
elif grup=="AB" and faktor=="+":
    print("Tüm gruplardan alır")
elif grup=="AB" and faktor=="-":
    print("tüm - lerden alır")
elif grup=="A" and faktor=="+":
    print("0-, 0+, A+, A- den alır")
elif grup=="A" and faktor=="-":
    print("0-, A- den alır")
elif grup=="B" and faktor=="+":
    print("0-,0+,B-,B+ dan alır")
elif grup=="B" and faktor=="-":
    print("0-,B- den alır")