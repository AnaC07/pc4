
n = int(input("ingrese un numero del 1 al 10: "))

file_name = "./tabla-{}.text".format(n)

with open(file_name, mode="w") as f:
    for i in range(1,13):
        cadena = "{} x {} ={}\n".format(n,i,i*n)
        f.write(cadena)
