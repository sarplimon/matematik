anapara=int(input("Anaparayı giriniz: "))
oran=int(input("Oran giriniz: "))
yıl=int(input("Yıl giriniz: "))
basit_faiz=(anapara*oran*yıl)/100
print("Faiz miktarı: ",basit_faiz)
print("{} yıl sonraki toplam para miktarı: {}₺".format(yıl,anapara+basit_faiz))
