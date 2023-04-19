sueldo=int(input("ingrese el sueldo"))
antigu=int(input("ingrese la antiguedad"))
if sueldo<500 and 10<antigu:
    total=sueldo+0.20*sueldo
    print("su sueldo aumento un 20% y es ", total)
if sueldo<500 and 10>antigu:
    total=sueldo+0.05*sueldo
    print("su sueldo aumento un 5% y es ", total)
if sueldo>=500:
    print("su sueldo no aumento y es ", sueldo)

