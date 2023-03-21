def  CalcularValorPrestamo(prestamo:int,interes:int,meses:int) -> int:
    ValorPrestamo = prestamo*(1+(interes/100))**meses
    return ValorPrestamo
if __name__ == "__main__":
  prestamo= int(input("Ingrese el valor del prestamo:"))
  interes  = int(input("Ingrese el porcentaje de inters:"))
  meses  = int(input("Ingrese la cantidad de meses :"))

  vp = CalcularValorPrestamo(prestamo, interes ,meses)

  print("El valor del pretamo es " + str(vp))
  