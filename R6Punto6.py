def CalcularContagiadosCovid(actuales:int,dias:int) -> int:
    ContagiadosCovid = actuales*(dias)**2
    return ContagiadosCovid
if __name__ == "__main__":
  actuales= int(input("Ingrese el número de contagiados actuales:"))
  dias  = int(input("Ingrese los  dias transcurridos:"))
  

  ca = CalcularContagiadosCovid(actuales,dias)

  print("El numero de contagiados despues de "+ str(dias)+ " sera "+str(ca))
  