#https://replit.com/join/wdovguljrq-danielgonzal232

lt = int(input("¿Cuántas lecturas de temperatura tienes? "))
c = 0
t = 0
eq = 0

while c < lt:
      c += 1
      t = float(input("Escribe la temperatura: "))
      if t >= 10 and t <= 40:
          pass
      else:
          eq += 1

print("Número de lecturas fuera del rango:", eq)
po = (eq * 100) / lt
print("Porcentaje de lecturas fuera del rango:", po)
