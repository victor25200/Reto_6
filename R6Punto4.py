def  CalcularCantidad(panes:int,leche:int,huevos:int,dinero:int) -> float:
    Cantidad = (panes*300+leche*3300+huevos*350-dinero)
    return Cantidad
if __name__ == "__main__":
  panes= int(input("Ingrese la cantidad de panes:"))
  leche = int(input("Ingrese la cantidad de leche:"))
  huevos = int(input("Ingrese la cantidad de huevos:"))
  dinero = int(input("Ingrese el valor del billete:"))

  vueltas = CalcularCantidad(panes,leche,huevos,dinero) 
  if vueltas < 0:
     vueltas = -vueltas
     print("las vueltas son  " + str(vueltas))
  else:
     print("queda deviendo  " + str(vueltas))
  