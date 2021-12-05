n = input("ingrese un numero del 1 al 10: ")
m = input("ingrese un numero del 1 al 10: ")

file_name = "./tabla-{}.text".format(n)

try:
    f = open(file_name,'r')
except FileNotFoundError:
    print("No existe el fichero con la tabla del",n)
else:
    x = f.readlines()
    print(x[m-1])
