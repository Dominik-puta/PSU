ocjena = input("Unesite broj izmedu 0.0 i 1.0: ")


try:
    ocjena = float(ocjena)
    if(ocjena >= 0.0 and ocjena <=1.0):    
        if(ocjena >= .9):
            print("A")
        elif(ocjena < .9 and ocjena >= .8):
            print("B")
        elif(ocjena < .8 and ocjena >= .7):
            print("C")
        elif(ocjena < .7 and ocjena >= .6):
            print("D")
        elif(ocjena < .6):
            print("F")
    else:
        print("Broj je izvan intervala")
except:
    print("Niste unijeli broj")
