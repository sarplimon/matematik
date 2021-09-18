DONE = False

while not DONE:
    HAS_ERROR = False; PRIME_NUMBER = True
    USER_INPUT = input("// enter a number that is +1 [e/E: Exit] => ")
    if USER_INPUT == "e" or USER_INPUT == "E": raise SystemExit

    try:
        x = int(USER_INPUT)
        if x < 2:
            print("// Error: number is not bigger than 1 //")
            print("---------------------------------------------------")
            HAS_ERROR = True
    except ValueError:        
        print("// Error: entery is not a number //")
        print("---------------------------------------------------")
        HAS_ERROR = True

    if not HAS_ERROR:
        for i in range(2, x):
            if x % i == 0: PRIME_NUMBER = False; break

        if PRIME_NUMBER:
            print("// "+USER_INPUT+" is a prime number! //")
        else:
            print("// "+USER_INPUT+" is NOT a prime number! //")
        print("---------------------------------------------------")

