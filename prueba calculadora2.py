num1 = float(input("digite un número -> "))
signo = input("ponga un signo -> ")
num2 = float(input("digite un número -> "))
i = 0
while i<=0:
    if signo == '+':
        suma = float(num1 + num2 )
        p = input("si desea agregar ponga s y siquiere el resultado ponga r ->")
        if  p == 's':
            print(suma)
            num3 = float(input("digite un numero ->"))
            suma = float(suma + num3 )
            print("resultado :",suma)   
        elif p== 'r':
            print("resultado ->",suma)
            i+=1

        else:
            print("Error")
    elif signo == '-':
        resta = float(num1-num2)
        print("el resultado es ",resta)
    elif signo == '*':
        multiplicacion=float(num1*num2)
        print(multiplicacion)
        p = input("si desea aagregar ponga s y si quiere el resultado ponga r")
        if p =='s':
            print(multiplicacion)
            num3 = float(input("digite un numero ->"))
            multiplicacion= float(multiplicacion+ num3)
            print("resultado :", multiplicacion)
        elif p=='r':
            print("resultado ->",multiplicacion)
            i+=1
        else:
            print("Error")
    elif signo =='/':
        divicion = float(num1/num2)
        p = input("si desea agregar ponga s y siquiere el resultado ponga r ->")
        if p== 's':
            print(divicion)
            num3 = float(input("digite un numero ->"))
            divicion = float(divicion/num3)
            print("resultado:",divicion)
        elif p=='r':
            print("resultado:",divicion)
            i+=1
    else:
        print("Error")
