contador = 0
while contador < 10:
    print ("El contador va en, ", contador)

    if contador == 5:
        print("Cortando el ciclo...")
        break #corta la ejecucion del ciclo
    contador += 1

peticionSOAP= None
reintentos= 0

while reintentos < 3:
    try:
        #Peticion al SOAP, si puedo recuperar la info, necesito cortar
        #el ciclo del while
        #peticionSOAP = {"RUT: ": 25326652, "dv": '-K', "nombre": "Joneiker"}
        if reintentos == 2:
            peticionSOAP = {"RUT: ": 25326652, "dv": '-K', "nombre": "Joneiker"}
        if peticionSOAP is not None:
            break
        raise Exception('Peticion SOAP invalida')

    except Exception:
        reintentos += 1

print(reintentos,peticionSOAP)


