#https://replit.com/join/nvegpeihmh-danielgonzal232

gryffindor_score = 0
slytherin_score = 0

while True:
      quidditch_events = input("¿Qué pasó (goal/snitch/foul)? ").lower()

      if quidditch_events == "goal":
          equipo = input("¿Quién lo anotó (gryffindor o slytherin)? ").lower()
          if equipo == "gryffindor":
              gryffindor_score += 10
              print("Gryffindor gana 10 puntos!")
          elif equipo == "slytherin":
              slytherin_score += 10
              print("Slytherin gana 10 puntos!")

      elif quidditch_events == "snitch":
          equipo = input("¿Quién lo anotó (gryffindor o slytherin)? ").lower()
          if equipo == "gryffindor":
              gryffindor_score += 150
              print("Gryffindor gana 150 puntos!")
          elif equipo == "slytherin":
              slytherin_score += 150
              print("Slytherin gana 150 puntos!")

      elif quidditch_events == "foul":
          equipo = input("¿Quién lo anotó (gryffindor o slytherin)? ").lower()
          if equipo == "gryffindor":
              gryffindor_score -= 30
              print("Gryffindor pierde 30 puntos!")
          elif equipo == "slytherin":
              slytherin_score -= 30
              print("Slytherin pierde 30 puntos!")

      print(f"Gryffindor: {gryffindor_score}")
      print(f"Slytherin: {slytherin_score}")

      continuar = input("¿Fin del juego (si o no)? ").lower()
      if continuar != 'no':
          break

if gryffindor_score > slytherin_score:
      print("Gryffindor gana!")
elif slytherin_score > gryffindor_score:
      print("Slytherin gana!")
else:
      print("Empate!")
