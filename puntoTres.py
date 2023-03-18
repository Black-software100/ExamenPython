mul2 = 0
mul3 = 0
mul23 = 0
for f in range(3):
    val=int(input("Ingres el valor: "))
    if val % 2 == 0:
        mul2 = mul2 + 1
    if val % 3 == 0:
        mul3 = mul3 + 1
    if val % 3 == 0 or val %2 == 0:
        mul23 =  mul23 + 1
print("Cantidad de valores ingresados múltiplos de 2: ")
print(mul2)
print("Cantidad de valores ingresados múltiplos de 3: ")
print(mul3)
print("Cantidad de valores que son múltiplos de 3 y de 2 son: ")
print(mul23)