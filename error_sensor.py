contador = 0
acumulador1 =0
acumulador2 = 0
lecturas = int(input("¿Cuántas lecturas de temperatura tienes?  "))
while contador < lecturas:
  pregunta= int(input("Insertar la temperatura: "))
  contador += 1
  if pregunta >= 10 and pregunta <=40:
    acumulador1 += 1
  else:
    acumulador2 += 1
errores = acumulador2*100/ lecturas
print(f"El sensor se equivoco {acumulador2}")
print(f"El porcentaje de error fue del {errores}")
