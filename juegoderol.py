print("Bienvenido a la isla del tesoro")
print("Tu mision es no caer en la trampa y salirte con la tuya")

pregunta_1 =input ("Tienes un camino delante, uno a un castillo y otro a una iglesia abandonada, que eliges? iglesia o castillo ").lower()
if pregunta_1 == "castillo":
  pregunta_2 = input("Te encuentras con un ciego y con un caballero, con quien hablas? ciego o caballero").lower()
  if pregunta_2 == "ciego":
    pregunta_3 = input(" el ciego tiene una bolsa llena de oro, o puedes decirdir ayudarle, que es lo que haces? ayuda o robo ?")
  elif pregunta_2 == "caballero":
    pregunta_3 = input ("el caballero te dice que o le ayudas a matar al ciego o te retará a ti a un duelo a muerte duelo o help")
    if pregunta_3 == "duelo":
      print("mueres")
    if pregunta_3 == "help":
      print("mueres")
    if pregunta_3 == "robo":
      print("mueres")
    if pregunta_3 == "ayuda":
      print("te da todo su dinero y te haces rico")
if pregunta_1 == "iglesia":
  pregunta_2 = input("Te encuentras en una iglesia que esta abierta pero tambien ves algo resplandecer en el cementerio eliges cementerio o entrar ?")
  if pregunta_2 == "entrar":
      pregunta_3 = input("entras en la iglesia y esta llena de tesoros, decides cogerlos o dejarlos ?")
      if pregunta_3 == cogerlos:
        print(" te haces rico y vives como un rey toda tu vida")
      if pregunta_3 == dejarlos:
        print( "Te mueres de hambre y te mata una comadreja")
  if pregunta_2 == "cementerio":
    pregunta_3 = input("Ves que lo que brilla esta debajo de la tierra y hay que cavar, decides cavar o pasar ?")
    if pregunta_3 == "cavar":
      print("encontraste los tesoros del cementerio!")
    if pregunta_3 == "pasar":
      print("un zombi salta y te muerde el cuello")

elif pregunta_1 == "iglesia":
  print("eres un pipa")
