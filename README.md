# Reto_6
## Punto 1
Dado la figura de la imagen, desarrollando:
[![image.png](https://i.postimg.cc/Z5Ftm6MM/image.png)](https://postimg.cc/tsTmtny3)
- Una funcion matematica para calcular el volumen y el area superficial.
- Cree dos funciones en python para calcular los valores antes establecidos, al ingresar por teclado r1, r2y h.
- Revise como utilizar el valor de pi usando import math y math.pi

    ```python
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
```
## Punto 2
Dado la figura de la imagen, desarrollando:
[![image.png](https://i.postimg.cc/tJCt1Gq6/image.png)](https://postimg.cc/Pp98cc8f)
- Una función matemática para calcular el área y el perímetro.
- Cree dos funciones en python para calcular los valores antes establecidos, al ingresar por teclado r, ay b.
- Revise como utilizar el valor de pi usando import math y math.pi
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
	  
## Punto 3
Diseñe una función que calcule la cantidad de carne de aves en kilos si se tienen N gallinas, M gallos y K pollitos cada uno pesando 6 kilos, 7 kilos y 1 kilo respectivamente.


    def  CalcularCantidad(gallinas:int,gallos:int,pollos:int) -> int:
        Cantidad = (gallinas*7+gallos*8+pollos)
        return Cantidad
    if __name__ == "__main__":
      gallinas= int(input("Ingrese la cantidad de gallinas:"))
      gallos = int(input("Ingrese la cantidad de gallos:"))
      pollos = int(input("Ingrese la cantidad de pollos:"))
    
      carne = CalcularCantidad(gallinas,gallos,pollos) 
    
      print("El cantidad de kilos carne es  " + str(carne))

## Punto 4
Mi mamá me manda a comprar p panes a 300 cada uno, m bolsas de leche a 3300 cada una y h huevos a 350 cada uno. hacer un programa que me diga las vueltas (o lo que quedo debiendo) cuando me da un billete de b pesos.


```python
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
```
##  Punto 5 
Haga un programa que utilice una función para calcular el valor de un préstamo C usando interés compuesto de i por n meses.

```python
 def  CalcularValorPrestamo(prestamo:int,interes:int,meses:int) -> int:
        ValorPrestamo = prestamo*(1+(interes/100))**meses
        return ValorPrestamo
    if __name__ == "__main__":
      prestamo= int(input("Ingrese el valor del prestamo:"))
      interes  = int(input("Ingrese el porcentaje de inters:"))
      meses  = int(input("Ingrese la cantidad de meses :"))

      vp = CalcularValorPrestamo(prestamo, interes ,meses)

      print("El valor del pretamo es " + str(vp))
```

## Punto 6
El número de contagiados de Covid-19 en el país de NuncaLandia se duplica cada día. Hacer un programa que diga el número total de personas que se han contagiado cuando pasen D días a partir de hoy, si el número de contagiados actuales es C.
```python
def CalcularContagiadosCovid(actuales:int,dias:int) -> int:
    ContagiadosCovid = actuales*(dias)**2
    return ContagiadosCovid
if __name__ == "__main__":
  actuales= int(input("Ingrese el número de contagiados actuales:"))
  dias  = int(input("Ingrese los  dias transcurridos:"))
  

  ca = CalcularContagiadosCovid(actuales,dias)

  print("El numero de contagiados despues de "+ str(dias)+ " sera "+str(ca))
```

## Punto 7
Escriba un programa que pida 5 números reales y calcule las siguientes usando una función para cada una:

- El promedio
- La mediana
- El promedio multiplicativo (multiplica todos y luego calcula la raíz de la cantidad de operadores)
- Ordenar los números de forma ascendente
- Ordenar los numeros de forma descendente
- La potencia del mayor número elevado al menor número
- La raíz cúbica del menor número

```python
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
```
## Punto 8
Para el punto anterior incluir las funciones en un archivo independiente e importarlas para su uso.
```python
from R6Punto7 import CalcularPotencia,CalcularRaism,ordenarCincoNums,CalcularPromedio,CalcularProMult
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
```

## Punto 10 
Hacer un listado de módulos populares para python que se pueden instalar com pip y consultar cómo instalarlos.

- Matplotlib
- TensorFlow
- PyTorch
- Keras
- Scikit-learn
- Pandas
- Seaborn
- Bokeh
- NumPy
