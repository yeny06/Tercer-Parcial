texto= input("Ingrese su texto: ")
x = texto.split()
y = texto.count("Alexa")

if y == 2:
  print("Tranquilo, solo dime mi nombre una vez")
elif y == 1:
  print("¿Cómo puedo ayudarte?")
