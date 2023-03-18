from time import sleep
cuentas = [1]
a = 0
for i in range(10):
    a += 1
    cuenta = int(input(f"Ingrese el valor de la cuenta N°{a}: "))
    cuentas.append(cuenta)



cuentas[0] = 2

print(cuentas)

def metodoBurbuja ():
    k = 1
    for i in range(10):
        
        if(cuentas[i]>cuentas[k]):

            c = cuentas[i]
            d = cuentas[k]

            print(f"{c} y {d}")
            print("-----------------")
            print(cuentas)
            print("-----------------")
            cuentas[i] = d
            cuentas[k] = c
            

        k = k + 1
        
        if(k == len(cuentas)):
            break
for i in range(10):
    metodoBurbuja()

print (cuentas)

