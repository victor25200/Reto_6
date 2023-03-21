def  CalcularCantidad(gallinas:int,gallos:int,pollos:int) -> int:
    Cantidad = (gallinas*7+gallos*8+pollos)
    return Cantidad
if __name__ == "__main__":
  gallinas= int(input("Ingrese la cantidad de gallinas:"))
  gallos = int(input("Ingrese la cantidad de gallos:"))
  pollos = int(input("Ingrese la cantidad de pollos:"))

  carne = CalcularCantidad(gallinas,gallos,pollos) 

  print("El cantidad de kilos carne es  " + str(carne))