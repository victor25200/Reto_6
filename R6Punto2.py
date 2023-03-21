import math

def  CalcularAreaFigura(r:float,a:float, b :float ) -> float:
    AreaFigura = 2*(r**2*math.pi)+(a*b)
    return AreaFigura
def  CalcularPerimetroFigura(r:float,a:float, b :float ) -> float:
    PerimetroFigura =2*(r*2*math.pi)+(2*a+2*b)
    return  PerimetroFigura
if __name__ == "__main__":
  r = float(input("Ingrese el radio de los circulos:"))
  a = float(input("Ingrese el alto del rectangulo (a)"))
  b = float(input("Ingrese el ancho del rectangulo (b):"))

  pf =  CalcularPerimetroFigura(r,a,b)
  af=   CalcularAreaFigura(r,a,b) 
  print("El perimetro de la figura es " + str(pf)) 
  print("El area de la figura es " + str(af))