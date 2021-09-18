DONE = False

while not DONE:
    HAS_ERROR = False; VALS = ""; TOTAL_VALS = 0
    USER_INPUT = input("// Pozitif bir sayı girin [e/E: Çıkış] => ")
    if USER_INPUT == "e" or USER_INPUT == "E": raise SystemExit

    try:
        x = int(USER_INPUT)
        if x < 0:
            print("// Hata: Sayı pozitif değil! //")
            print("---------------------------------------------------")
            HAS_ERROR = True
    except ValueError:        
        print("// Hata: Girilen değer bir sayı değil! //")
        print("---------------------------------------------------")
        HAS_ERROR = True

    if not HAS_ERROR:
        for i in range(1, x+1):
            if x % i == 0:
                VALS += str(i); TOTAL_VALS += 1
                if not i == x: VALS += ", "

        print("// "+USER_INPUT+" sayısının toplam "+str(TOTAL_VALS)+" böleni vardır. Bunlar...")
        print("// "+VALS)
        print("---------------------------------------------------")
90
