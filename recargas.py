monto= int(input("ingrese la cantidad de dinero: "))
if monto >= 25:
    queda = monto // 25
    print("existen" + str(queda) + "recargas de 25")
    monto = monto % 25
    
if monto >= 10:
    queda = monto // 10
    print("existen" + str(queda) + "recargas de 10")
    monto = monto % 10
    
if monto >= 5:
    queda = monto // 5
    print("existen" + str(queda) + "recargas de 5")
    monto = monto % 5

