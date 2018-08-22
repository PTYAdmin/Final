"""
Creado el 15 de agosto de 2018
authores:
Carlos rivera
didiel Saenz
jo han Castillero
Jose Barragan
Jahiro coba
"""

cocacola=10
sprite=10
fanta=5
"""
Ingreso de datos
y presentacion de productos
"""
producto=input("Bienvenido, por favor elija el refresco que desea comprar, tenemos cocacola, sprite y fanta: ")
print("Solo se aceptan Billetes de 1, 5, 10 o 20")
pago=int(input("Introduzca la cantidad con la que desea pagar,: "))
#verificacion de valores de moneda
if pago==1 or pago==5 or pago==10 or pago==20:
  #ciclo de verificacion de de prodcuto y proceso de venta
  if producto=="cocacola":
    while True:
      if pago>=10:
        print("Gracias por su compra")
        cambio=(pago-10)
        print("Su cambio es: "+str(cambio))
        tcococolas=(cocacola-1)
        #impresion de invnetario remanente
        print("La máquina cuenta con "+str(cocacola)+" cocacola")
        break
        #verificacion de producto y proceso deventa
      else:
          faltante=(10-pago)
          print("Dinero insuficiente para la compra $"+str(faltante))
          opcion=input("¿Desea continuar con la compra? ")
          if opcion=="si":
            total=int(input("Introduce el dinero que falta: "))
            pago=(pago+total)
          else:
            print("Dinero devuelto $"+str(pago))
            break
  elif producto=="sprite":
    while True:
      if pago>=12:
        print("Gracias por su compra")
        tsprite=(sprite-1)
        cambio=(pago-12)
        print("Su cambio es: "+str(cambio))
        print("La máquina cuenta con "+str(tsprite)+" sprite")
        break
        #Veriifca de faltar dinero,  indica si desa continuar o cancelar la compra
      else:
        faltante=(12-pago)
        print("Dinero insuficiente para la compra $"+str(faltante))
        opcion=input("¿Desea continuar con la compra? ")
        if opcion=="si":
          total=int(input("Introduce el dinero que falta: "))
          pago=(pago+total)
        else:
          print("dinero Devuelto $"+str(pago))
          break
  elif producto=="fanta":
    while True:
      if pago>=14:
        print("Gracias por su compra")
        #resta de inventario
        tfanta=(fanta-1)
        cambio=(pago-14)
        print("Su cambio es: "+str(cambio))
        print("La máquina cuenta con "+str(fanta)+" fanta")
        break
      else:
        #Verificacion de dinero para confirmar venta comprando variables de pago con valor fijado
        faltante=(14-pago)
        print("La cantidad no es suficiente, te faltan $"+str(faltante))
        opcion=input("¿Desea continuar con la compra? ")
        if opcion=="si":
          total=int(input("Introduce el dinero que falta: "))
          pago=(pago+total)
        else:
          print("Dinero Devuelto $"+str(pago))
          break
else:
  print("Moneda no válida")