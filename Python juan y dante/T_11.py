num1= int (input ("Ingrese coordenada X"))
num2= int (input ("Ingresar coordenada Y"))

if num1>0 and num2>0:
    print ("Sus coordenadas estan en el primer cuadrante")

else:
        if num1<0 and num2>0:
            print ("Sus coordenadas estan en el segundo cuadrante")

        else:
            if num1<0 and num2<0:
                print ("Sus coordenadas estan en el tercer cuadrante")

            else:
                if num1>0 and num2<0:
                        print ("Sus coordenadas estan en el cuarto cuadrante")

                        

    
