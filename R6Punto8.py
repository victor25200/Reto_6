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