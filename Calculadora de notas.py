cant_de_notas = int(input("Introduzca la cantidad de notas que va a ingresar a continuación: "))
contador = cant_de_notas
limitación = "no"
if cant_de_notas > 1 and cant_de_notas <= 10:
    while contador <= cant_de_notas:
        if limitación == "yes":
            break
        if contador >= 1:
            a = float(input("introduzca la primera nota: "))
            if not a > 1 and not a < 20:
                print("nota inválida")
                break
            else:
                if contador >= 2:
                    b = float(input("introduzca la segunda nota: "))
                    if not b > 1 and not b < 20:
                        print("nota inválida")
                        break
                    else:
                        if contador >= 3:
                            c = float(input("introduzca la tercera nota: "))
                            if not c > 1 and not c < 20:
                                print("nota inválida")
                                break
                            else:
                                if contador >= 4:
                                    d = float(input("introduzca la cuarta nota: "))
                                    if not d > 1 and not d < 20:
                                        print("nota inválida")
                                        break
                                    else:
                                        if contador >= 5:
                                            e = float(input("introduzca la quinta nota: "))
                                            if not e > 1 and not e < 20:
                                                print("nota inválida")
                                                break
                                            else:
                                                if contador >= 6:
                                                    f = float(input("introduzca la sexta nota: "))
                                                    if not f > 1 and not f < 20:
                                                        print("nota inválida")
                                                        break
                                                    else:
                                                        if contador >= 7:
                                                            g = float(input("introduzca la séptima nota: "))
                                                            if not g > 1 and not g < 20:
                                                                print("nota inválida")
                                                                break
                                                            else:
                                                                if contador >= 8:
                                                                    h = float(input("introduzca la octava nota: "))
                                                                    if not h > 1 and not h < 20:
                                                                        print("nota inválida")
                                                                        break
                                                                    else:
                                                                        if contador >= 9:
                                                                            i = float(input("introduzca la novena nota: "))
                                                                            if not i > 1 and not i < 20:
                                                                                print("nota inválida")
                                                                                break
                                                                            else:
                                                                                if contador >= 10:
                                                                                    j = float(input("introduzca la décima nota: "))
                                                                                    limitación = "yes"
                                                                                    if j > 1 and j < 20:
                                                                                        continue
                                                                                    elif not j > 1 and not j < 20:
                                                                                        print("nota inválida")
                                                                                        limitación = "yes"
                                                                                        continue
                                                                                else:
                                                                                    break
                                                                        else:
                                                                            limitación = "yes"
                                                                            continue
                                                                else:
                                                                    limitación = "yes"
                                                                    continue
                                                        else:
                                                            limitación = "yes"
                                                            continue
                                                else:
                                                    limitación = "yes"
                                                    continue
                                        else:
                                            limitación = "yes"
                                            continue
                                else:
                                    limitación = "yes"
                                    continue
                        else:
                            limitación = "yes"
                            continue
                else:
                    limitación = "yes"
                    continue
        else:
            limitación = "yes"
            continue
        
else:
    print("cantidad de notas inválida")
# bloque 1
if contador == 1:
    suma = a
    nota_menor = a
    nota_mayor = a
# bloque 2
elif contador == 2:
    suma = a+b
    notas = [a, b]
    nota_mayor = max(notas)
    nota_menor = min(notas)
# bloque 3
elif contador == 3:
    suma = a+b+c
    notas = [a, b, c]
    nota_mayor = max(notas)
    nota_menor = min(notas)
# bloque 4
elif contador == 4:
    suma = a+b+c+d
    notas = [a, b, c, d]
    nota_mayor = max(notas)
    nota_menor = min(notas)
# bloque 5
elif contador == 5:
    suma = a+b+c+d+e
    notas = [a, b, c, d, e]
    nota_mayor = max(notas)
    nota_menor = min(notas)
# bloque 6
elif contador == 6:
    suma = a+b+c+d+e+f
    notas = [a, b, c, d, e, f]
    nota_mayor = max(notas)
    nota_menor = min(notas)
# bloque 7 
elif contador == 7:
    suma = a+b+c+d+e+f+g
    notas = [a, b, c, d, e, f, g]
    nota_mayor = max(notas)
    nota_menor = min(notas)
# bloque 8 
elif contador == 8:
    suma = a+b+c+d+e+f+g+h
    notas = [a, b, c, d, e, f, g, h]
    nota_mayor = max(notas)
    nota_menor = min(notas)
# bloque 9 
elif contador == 9:
    suma = a+b+c+d+e+f+g+h+i
    notas = [a, b, c, d, e, f, g, h, i]
    nota_mayor = max(notas)
    nota_menor = min(notas)
# bloque 10 
elif contador == 10:
    suma = a+b+c+d+e+f+g+h+i+j
    notas = [a, b, c, d, e, f, g, h, i, j]
    nota_mayor = max(notas)
    nota_menor = min(notas)
print(f"Esta es tu mejor nota {nota_mayor}, Esta es tu peor nota {nota_menor}, Este es tu promedio {float(suma)/cant_de_notas}")
