'''
num1 = float(input("digite un número -> "))
signo = input("ponga un signo -> ")
num2 = float(input("digite un número -> "))
i = 1
while i<10:
    if signo == '+':
        suma = float(num1 + num2 )
        p = input("si desea agregar ponga s y siquiere el resultado ponga r ->")
        if  p == 's':
            print(suma)
            num3 = float(input("digite un numero ->"))
            suma = float(suma + num3 )
            print("resultado :",suma)
            i+1
        elif p== 'r':
            print("resultado ->",suma)
            i+=9

        else:
            print("Error")
    else:
        print("Error")
num3 = float(num3)
suma = float(suma)
'''

num1 = float(input("digite un número -> "))
signo = input("ponga un signo -> ")
num2 = float(input("digite un número -> "))
i = 1

while i<10:

    if signo == '+':
        
        suma = float(num1 + num2)
        p = input("si desea agregar ponga s y si quiere el resultado ponga r -> ")
        
        if p == 'r':
            print("resultado ->", suma)
            i+=9
        
        elif p == 's':
            print(suma)
            num3 = float(input("digite un numero -> "))
            suma = float(suma + num3)
            print("resultado ->", suma)
        
        else:
            print("Error")
            i+=9
    
    else: 
        print("Error")
        i+=9