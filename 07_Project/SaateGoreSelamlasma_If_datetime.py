import datetime 

anlik= datetime.datetime.now()
saat= anlik.hour

print("saat:",saat)

if saat>= 7 and saat <=11:
    print("günaydın")
elif saat> 11 and saat<=14:
    print("tünaydın")
elif saat>18 and saat<=21:
    print("iyi akşamlar")
elif saat>22 and saat<=24:
    print("iyi geceler")
else:
    print("iyi günler")

