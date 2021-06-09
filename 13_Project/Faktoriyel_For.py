sonuc=1

sayi=int(input("Lütfen sayıyı giriniz: "))

for x in range(sayi,0,-1):
    sonuc=sonuc*x

print("Faktoriyel: ",sonuc)