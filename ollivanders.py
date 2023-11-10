#https://replit.com/join/tykmytiqkg-danielgonzal232

cl= str(input("Entra un cliente? (si/no):"))
ac = 0
contador = 0
ttc = 0
noc = 0
quec = 0
acv1 = 0
acv2 = 0
acv3 = 0
acv4 = 0
while cl == "si": 
  c = str(input("Compra algo?  (si/no): "))
  if c == "si":
     ac += 1
     quec = str(input("Que compro?  Varita de sauco [1] varita de espino [2]  varita [3]  varita de acebo [4]" ))
 
     if quec == "1":
       acv1 += 1
     elif quec == "2":
       acv2 += 1
     elif quec == "3":
       acv3 += 1
     elif quec == "4":
       acv4 += 1
     cl = str(input("Entro un cliente? (si/no): "))
     ttc += 1
     noc = ttc - ac
     print(f"Los clientes que compraron son {ac}")
     print(f"Los clientes que no compraron {noc}")
     print(f"El total de clientes es {ttc}")
     print(f"Las varitas de sauco son {acv1}, las varitas de espino son {acv2}, las varitas de sauce son {acv3}, las varitas de acebo son {acv4}")
