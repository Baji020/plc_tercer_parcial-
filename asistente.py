#https://replit.com/join/evrexnglrd-danielgonzal232

x = input("Escribe el nombre: ")
p = x.split()
va = p.count("Alexa")

if va == 1:
    print("Dime cómo puedo ayudarte?")
elif va > 1:
    print("¡Tranquilo, solo di mi nombre una vez!")

