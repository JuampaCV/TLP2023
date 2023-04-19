print("Ingese los sueldos del gurpo de la mañana ")
x=1
suma=0
suma2=0
while x<=15:
    num1=int(input("Sueldo: "))
    suma=suma+num1
    x=x+1
while x<=15:
    num2=int(input("Sueldo2: "))
    suma2=suma2+num2
    x=x+1
if num1 <num2:
    print("El mayor es ",num2)
else:
    if num2 <num1:
        print("El mayor es ",num1)
