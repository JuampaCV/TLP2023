cantp= int(input("ingrese la cantidad de piezas "))
x=0
y=0
while x<cantp:
    long=float(input("ingrese la longitud de las piezas "))
    x=x+1
    if long<1.30 and long>1.20:
        y=y+1
print("las piezas aptas son ",y)
