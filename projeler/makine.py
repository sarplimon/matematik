print("+----------+")
print("| NekiBuki |")
print("+----------+")

DONE = False

while not DONE:
    HAS_ERROR = False; VALS = ""; TOTAL_VALS = 0; print("")
    USER_INPUT = input("> Pozitif bir sayı girin [ENTER: Çıkış] > ")
    if USER_INPUT == "": raise SystemExit

    try:
        x = int(USER_INPUT)
        if x < 1:
            print("[!] Hata: Girilen sayı pozitif değil.")
            HAS_ERROR = True
    except ValueError:        
        print("[!] Hata: Girilen değer bir sayı değil.")
        HAS_ERROR = True

    if not HAS_ERROR:
        for i in range(1, x+1):
            if x % i == 0:
                VALS += str(i); TOTAL_VALS += 1
                if not i == x: VALS += ", "


        print(""); print(USER_INPUT+" sayısı için...")
        print("[1] Bölenleri şöyledir: "+VALS+".")
        print("[2] "+str(TOTAL_VALS)+" tane pozitif böleni vardır.")
        print("[3] "+str(TOTAL_VALS)+" tane negatif böleni vardır.")
        print("[4] "+str(TOTAL_VALS*2)+" tane tamsayı böleni vardır.")        

        if TOTAL_VALS == 2:
            TXT = "[5] Bu bir ASAL sayıdır."
        else:
            TXT = "[5] Bu bir asal sayı değildir."
        print(TXT)

        if TOTAL_VALS % 2 == 1:
            KK = str(int(x**0.5))
            TXT = "[6] Bu bir TAM KARE sayıdır ("+KK+" x "+KK+" = "+USER_INPUT+")."
        else:
            TXT = "[6] Bu bir tam kare sayı değildir."
        print(TXT)

972