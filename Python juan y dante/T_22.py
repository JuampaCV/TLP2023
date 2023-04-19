x=0
contador1=0
contador2=0
while x<10:
    nota=int(input("ingrese la nota "))
    x=x+1
    if nota>=7:
    
        contador1=contador1+1
    else:

        contador2=contador2+1
print("la cantidad de notas mayor a 7 son ",contador1)
print("la cantidad de notas menor a 7 son ",contador2)
