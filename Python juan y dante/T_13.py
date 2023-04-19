num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))
num3 = int(input("Ingresa el tercer número: "))
if num1 >= num2 and num1 >= num3:
    num_mayor= num1
else:
    if num2 >= num3:
        num_mayor= num2
    else:
        num_mayor= num3
if num1 <= num2 and num1 <= num3:
            min_num= num1
else:
    if num2 <= num3:
                min_num= num2
    else:
                min_num= num3




print("El número máximo es:", num_mayor)
print("El número mínimo es:", min_num)
