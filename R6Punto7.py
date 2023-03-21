def  CalcularPromedio(a:float, b :float,c: float, d:float,e:float ) -> float:
    promedio = (a+b+c+d+e)/(5)
    return promedio
def CalcularProMult(a:float, b :float,c: float, d:float,e:float ) -> float:
    promult= (a*b*c*d*e)**(1/5)
    return promult
def ordenarDosNums(b,c):
  if b <= c:
    m2, m3 = b, c
  else:
    m2, m3 = c, b
  return m2, m3
def ordenarTresNums(a,b,c):
  m1 , m2, m3 = a, b, c
  if a <= b and a <= c:
    m1 = a
    m2, m3 = ordenarDosNums(b,c)
  elif b <= a and b <= c:
    m1 = b
    m2, m3 = ordenarDosNums(a,c)
  elif c <= b and c <= a:
    m1 = c
    m2, m3 = ordenarDosNums(b,a)
  return m1, m2, m3
def ordenarCuatroNums(a,b,c,d):
  m1, m2, m3, m4 = a, b, c, d
  if a <= b and a <= c and a<=d:
    m1 = a
    m2, m3, m4= ordenarTresNums(b,c,d)
  elif b <= a and b <= c and b <= d:
    m1 = b
    m2, m3, m4 = ordenarTresNums(a,c,d)
  elif c <= b and c <= a and c <= d:
    m1 = c
    m2, m3, m4 = ordenarTresNums(b,a,d)
  elif d <= a and d <= b and d <= c:
    m1 = d
    m2, m3, m4 = ordenarTresNums(a,b,c)
  return m1, m2, m3, m4
def ordenarCincoNums(a,b,c,d,e):
  m1, m2, m3, m4, m5 = a, b, c, d , e
  if a <= b and a <= c and a<=d and a<=e:
    m1 = a
    m2, m3, m4, m5= ordenarCuatroNums(b,c,d,e)
  elif b <= a and b <= c and b<=d and b<=e:
    m1 = b
    m2, m3, m4, m5= ordenarCuatroNums(a,c,d,e)
  elif c <= a and c <= b and c<=d and c<=e:
    m1 = c
    m2, m3, m4, m5= ordenarCuatroNums(a,b,d,e)
  elif d <= a and d <= b and d<=c and d<=e:
    m1 = d
    m2, m3, m4, m5= ordenarCuatroNums(a,b,c,e)
  elif e <= a and e <= b and e<=c and e<=d:
    m1 = e
    m2, m3, m4, m5= ordenarCuatroNums(a,b,c,d)
  return m1, m2, m3, m4, m5
def CalcularPotencia(m1:float,m5:float):
  LaPotencia = m5**m1
  return LaPotencia
def CalcularRaism(m1:float):
  Raism = (m1)**(1/2)
  return Raism
if __name__ == "__main__":


 a = float(input("Ingrese el primer número real: "))
 b = float(input("Ingrese el segundo número real: "))
 c = float(input("Ingrese el tercer número real: "))
 d = float(input("Ingrese el cuarto número real: "))
 e = float(input("Ingrese el quinto número real: "))
 m1, m2, m3, m4, m5 = ordenarCincoNums(a,b,c,d,e)
 prome = CalcularPromedio(a,b,c,d,e)
 Prom = CalcularProMult(a,b,c,d,e)
 pot = CalcularPotencia(m1,m5)
 rai = CalcularRaism(m1)
 print ("los números ingresados son ("+ str(a)+ ", "+ str(b)+", "+ str(c)+ ", "+str(d)+ ", "+str(e) +")" )
 print("El promedio es "+ str(prome))
 print("la mediana es "+ str(m3))
 print("El promedio multilpicativo es "+ str(Prom))
 print("los numeros en orden descendente son ("+ str(m5)+ ", "+ str(m4)+", "+ str(m3)+ ", "+str(m2)+ ", "+str(m1) +")") 
 print("los numeros en orden ascendente son ("+ str(m1)+ ", "+ str(m2)+", "+ str(m3)+ ", "+str(m4)+ ", "+str(m5) +")") 
 print("la potencia del mayor numero elvado el menor numero  es "+ str(pot))
 print("la raiz del menor número es " + str (rai))