contador_clientes_totales = 0
contador_clientes = 0
contador_no_clientes = 0
acumulador1 = 0
acumulador2 = 0
acumulador3 = 0
acumulador4 = 0 
entradas= input("¿Entro un cliente? si/no ")
if entradas == "no":
  print("No han llegado ningún cliente a Ollivanders")
while entradas == "si":
  contador_clientes_totales += 1
  compra= input("Compró algo? si/no ")
  if compra == "no":
    contador_no_clientes += 1
  elif compra == "si":
      contador_clientes += 1
      varita = input("Ingrese el tipo de varita que compro: 1.Varita de Saúco, 2.Varita de Espino, 3.Varita de Sauce y 4.Varita de Acebo. ")  
      if varita == 1:
        acumulador1 += 1
      elif varita == 2:
        acumulador2 += 1
      elif varita == 3:
        acumulador3 += 1
      elif varita == 4:
        acumulador4 += 1
  entradas= input("¿Entro un cliente? si/no ")

print ("Han llegado", contador_clientes_totales, " clientes a la tienda")  
print("Han comprado algo", contador_clientes, "clientes")
print("No han comprado algo", contador_no_clientes, "clientes")
print("Hoy se han comprado: ",acumulador1, "Varitas de Saúco, ", acumulador2, "Varitas de Espino, ", acumulador3, "Varitas de Sauce y ", acumulador4, "Varitas de Acebo")
