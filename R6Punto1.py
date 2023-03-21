import math
def CalcularVolumenFigura(re:float,rc:float,h:float)-> float:
    VolumenFigura = (re*3*4*math.pi)/3+(rc**2*h*math.pi)/3
    return VolumenFigura 
def  CalcularAreaFigura(re:float,rc:float,h:float) -> float:
    AreaFigura = (re*2*4*math.pi)+(rc*math.pi)*(rc+(rc**2+h**2)**(1/2))
    return AreaFigura
if __name__ == "__main__":
  re = float(input("Ingrese el radio de la esfera:"))
  rc = float(input("Ingrese el radio del cono:"))
  h = float(input("Ingrese la h del cono:"))

  vf =  CalcularVolumenFigura(re,rc,h)
  af=   CalcularAreaFigura(re,rc,h) 
  print("El volumen de la figura es " + str(vf)) 
  print("El area de la figura es " + str(af))