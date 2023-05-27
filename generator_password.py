import random 

#Este codigo genera contraseñas aleatorias y las junta con el nombre del usuario

print("Hola, soy un programa que te dara una contraseña aleatoria")

name = input(print("Dame tu nombre:"))#Nombre del usuario

password1 = int(input(print("introduce la longitud de la contraseña:"))) #Longitud de la contraseña

password2 = ""; #la contraseña que va a generar

generator = "qwertyuiopasdfghjklzxcvbnm123456789ASDFGHJK" #caracteres a elegir con el random.choice

for i in range (password1):
    password2+=random.choice(generator) #Elige los caracteres

print(name + password2)
