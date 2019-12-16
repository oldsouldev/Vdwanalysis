import random
tap1 = 0
tap2 = 0
tap3 = 0
tap4 = 0
tap5 = 0
tap6 = 0
tap7 = 0
tap8 = 0
tap9 = 0
tap10 = 0
tap11 = 0
tap12 = 0
tap13 = 0
tap14 = 0
tap15 = 0
tap16 = 0
balance = 0
w = 0
while w != 10:
 X = 9
 w = w + 1
 ap1 = 0
 ap2 = 0
 ap3 = 0
 ap4 = 0
 ap5 = 0
 ap6 = 0
 ap7 = 0
 ap8 = 0
 ap9 = 0
 ap10 = 0
 ap11 = 0
 ap12 = 0
 ap13 = 0
 ap14 = 0
 ap15 = 0
 ap16 = 0
 i = 0
 tlist = [X, X, X, X, X, X, X, X, X]
 while i != 9:
  print("                    ")
  print("_____________________________________ ", i + 1)
  print("                    ")
  x = random.choice([0,1])
  tlist[i] = x
  i = i + 1
  print(tlist)
  if i == 3:
     if tlist[0] == tlist[1] == tlist[2]:
         ap1 = ap1 + 1
         print("                    ")
         print("You win", ap1)
  if  i == 4:
     if tlist[1] == tlist[2] == tlist[3] and ap1 == 0:
         ap2 = ap2 + 1
         print("                    ")
         print("You win", ap2)
  if  i == 5:
     if tlist[0] == tlist[2] == tlist[4] and ap1 == 0 and ap2 == 0:
         ap3 = ap3 + 1
         print("                    ")
         print("You win", ap3)
     if tlist[2] == tlist[3] == tlist[4] and ap1 == 0 and ap2 == 0:
         ap4 = ap4 + 1
         print("                    ")
         print("You win", ap4)
  if  i == 6:
     if tlist[1] == tlist[3] == tlist[5] and ap1 == 0 and ap2 == 0 and ap3 == 0 and ap4 == 0:
         ap5 = ap5 + 1
         print("                    ")
         print("You win", ap5)
     if tlist[3] == tlist[4] == tlist[5] and ap1 == 0 and ap2 == ap3 == ap4 == 0:
         ap6 = ap6 + 1
         print("                    ")
         print("You win", ap6)
  if  i == 7:
     if tlist[0] == tlist[3] == tlist[6] and ap1 == 0 and ap2 == ap3 == ap4 == ap5 == ap6 == 0:
         ap7 = ap7 + 1
         print("                    ")
         print("You win", ap7)
     if tlist[2] == tlist[4] == tlist[6] and ap1 == 0 and ap2 == ap3 == ap4 == ap5 == ap6 == 0:
         ap8 = ap8 + 1
         print("                    ")
         print("You win", ap8)
     if tlist[4] == tlist[5] == tlist[6] and ap1 == 0 and ap2 == ap3 == ap4 == ap5 == ap6 == 0:
         ap9 = ap9 + 1
         print("                    ")
         print("You win", ap9)
  if  i == 8:
     if tlist[1] == tlist[4] == tlist[7] and ap1 == 0 and ap2 == ap3 == ap4 == ap5 == ap6 == ap7 == ap8 == ap9 == 0:
         ap10 = ap10 + 1
         print("                    ")
         print("You win", ap10)
     if tlist[3] == tlist[5] == tlist[7] and ap1 == 0 and ap2 == ap3 == ap4 == ap5 == ap6 == ap7 == ap8 == ap9 == 0:
         ap11 = ap11 + 1
         print("                    ")
         print("You win", ap11)
     if tlist[5] == tlist[6] == tlist[7] and ap1 == 0 and ap2 == ap3 == ap4 == ap5 == ap6 == ap7 == ap8 == ap9 == 0:
         ap12 = ap12 + 1
         print("                    ")
         print("You win", ap12)
  if  i == 9:
     if tlist[0] == tlist[4] == tlist[8] and ap1 == ap2 == ap3  == ap4 == ap5 == ap6 == ap7 == ap8 == ap9 == ap10 == ap11 == ap12 == 0:
         ap13 = ap13 + 1
         print("                    ")
         print("You win", ap13)
     if tlist[2] == tlist[5] == tlist[8] and ap1 == ap2 == ap3  == ap4 == ap5 == ap6 == ap7 == ap8 == ap9 == ap10 == ap11 == ap12 == 0:
         ap14 = ap14 + 1
         print("                    ")
         print("You win", ap14)
     if tlist[4] == tlist[6] == tlist[8] and ap1 == ap2 == ap3  == ap4 == ap5 == ap6 == ap7 == ap8 == ap9 == ap10 == ap11 == ap12 == 0:
         ap15 = ap15 + 1
         print("                    ")
         print("You win", ap15)

     if tlist[6] == tlist[7] == tlist[8] and ap1 == ap2 == ap3  == ap4 == ap5 == ap6 == ap7 == ap8 == ap9 == ap10 == ap11 == ap12 == 0:
         ap16 = ap16 + 1
         print("                    ")
         print("You win", ap16)
 print("                    ")
 print("                    ")
 print("                    ")

 print("Ap List : ", ap1, ap2, ap3, ap4, ap5, ap6, ap7, ap8, ap9, ap10, ap11, ap12, ap13, ap14, ap15, ap16)

 tap1 = tap1 + ap1
 tap2 = tap2 + ap2
 tap3 = tap3 + ap3
 tap4 = tap4 + ap4
 tap5 = tap5 + ap5
 tap6 = tap6 + ap6
 tap7 = tap7 + ap7
 tap8 = tap8 + ap8
 tap9 = tap9 + ap9
 tap10 = tap10 + ap10
 tap11 = tap11 + ap11
 tap12 = tap12 + ap12
 tap13 = tap13 + ap13
 tap14 = tap14 + ap14
 tap15 = tap15 + ap15
 tap16 = tap16 + ap16

print("Ap 1 :", tap1)
print("Ap 2 :", tap2)
print("Ap 3 :", tap3)
print("Ap 4 :", tap4)
print("Ap 5 :", tap5)
print("Ap 6 :", tap6)
print("Ap 7 :", tap7)
print("Ap 8 :", tap8)
print("Ap 9 :", tap9)
print("Ap 10:", tap10)
print("Ap 11:", tap11)
print("Ap 12:", tap12)
print("Ap 13:", tap13)
print("Ap 14:", tap14)
print("Ap 15:", tap15)
print("Ap 16:", tap16)
