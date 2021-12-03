#Uzrakstīt programmu, kas pieprasa no lietotāja ievadīt trīs leņķus (kas varētu piederēt vienam trīssturim) un ar programma parbauda vai leņķi ir 180° (ja jā, tad var taisīt trijstūri)
def lenkuParbaude(len1,len2,len3):
  rezultats=False
  if len1+len2+len3==180:
    rezultats=True
  return rezultats
len1 = int(input("Ievadiet 1.leņķi"))
len2 = int(input("Ievadiet 2.leņķi"))
len3 = int(input("Ievadiet 3.leņķi"))
rez=lenkuParbaude(len1,len2,len3)
if rez:
  print("Trīsstūris eksistē!")
else:
  print("Trīsstūris neeksistē!")