# coding : utf-8

import csv

fichier1 = "pl0910.csv"
fichier2 = "pl1011.csv"
fichier3 = "pl1112.csv"
fichier4 = "pl1213.csv"
fichier5 = "pl1314.csv"
fichier6 = "pl1415.csv"
fichier7 = "pl1516.csv"
fichier8 = "pl1617.csv"
fichier9 = "pl1718.csv"
fichier10 = "pl1819.csv"

fichier11 = "liga0910.csv"
fichier12 = "liga1011.csv"
fichier13 = "liga1112.csv"
fichier14 = "liga1213.csv"
fichier15 = "liga1314.csv"
fichier16 = "liga1415.csv"
fichier17 = "liga1516.csv"
fichier18 = "liga1617.csv"
fichier19 = "liga1718.csv"
fichier20 = "liga1819.csv"

fichier21 = "bundes0910.csv"
fichier22 = "bundes1011.csv"
fichier23 = "bundes1112.csv"
fichier24 = "bundes1213.csv"
fichier25 = "bundes1314.csv"
fichier26 = "bundes1415.csv"
fichier27 = "bundes1516.csv"
fichier28 = "bundes1617.csv"
fichier29 = "bundes1718.csv"
fichier30 = "bundes1819.csv"

fichier31 = "calcio0910.csv"
fichier32 = "calcio1011.csv"
fichier33 = "calcio1112.csv"
fichier34 = "calcio1213.csv"
fichier35 = "calcio1314.csv"
fichier36 = "calcio1415.csv"
fichier37 = "calcio1516.csv"
fichier38 = "calcio1617.csv"
fichier39 = "calcio1718.csv"
fichier40 = "calcio1819.csv"

fichier41 = "france0910.csv"
fichier42 = "france1011.csv"
fichier43 = "france1112.csv"
fichier44 = "france1213.csv"
fichier45 = "france1314.csv"
fichier46 = "france1415.csv"
fichier47 = "france1516.csv"
fichier48 = "france1617.csv"
fichier49 = "france1718.csv"
fichier50 = "france1819.csv"

f1 = open(fichier1)
pl0910 = csv.reader(f1)
f2 = open(fichier2)
pl1011 = csv.reader(f2)
f3 = open(fichier3)
pl1112 = csv.reader(f3)
f4 = open(fichier4)
pl1213 = csv.reader(f4)
f5 = open(fichier5)
pl1314 = csv.reader(f5)
f6 = open(fichier6)
pl1415 = csv.reader(f6)
f7 = open(fichier7)
pl1516 = csv.reader(f7)
f8 = open(fichier8)
pl1617 = csv.reader(f8)
f9 = open(fichier9)
pl1718 = csv.reader(f9)
f10 = open(fichier10)
pl1819 = csv.reader(f10)

f11 = open(fichier11)
liga0910 = csv.reader(f11)
f12 = open(fichier12)
liga1011 = csv.reader(f12)
f13 = open(fichier13)
liga1112 = csv.reader(f13)
f14 = open(fichier14)
liga1213 = csv.reader(f14)
f15 = open(fichier15)
liga1314 = csv.reader(f15)
f16 = open(fichier16)
liga1415 = csv.reader(f16)
f17 = open(fichier17)
liga1516 = csv.reader(f17)
f18 = open(fichier18)
liga1617 = csv.reader(f18)
f19 = open(fichier19)
liga1718 = csv.reader(f19)
f20 = open(fichier20)
liga1819 = csv.reader(f20)

f21 = open(fichier21)
bundes0910 = csv.reader(f21)
f22 = open(fichier22)
bundes1011 = csv.reader(f22)
f23 = open(fichier23)
bundes1112 = csv.reader(f23)
f24 = open(fichier24)
bundes1213 = csv.reader(f24)
f25 = open(fichier25)
bundes1314 = csv.reader(f25)
f26 = open(fichier26)
bundes1415 = csv.reader(f26)
f27 = open(fichier27)
bundes1516 = csv.reader(f27)
f28 = open(fichier28)
bundes1617 = csv.reader(f28)
f29 = open(fichier29)
bundes1718 = csv.reader(f29)
f30 = open(fichier30)
bundes1819 = csv.reader(f30)

f31 = open(fichier31)
calcio0910 = csv.reader(f31)
f32 = open(fichier32)
calcio1011 = csv.reader(f32)
f33 = open(fichier33)
calcio1112 = csv.reader(f33)
f34 = open(fichier34)
calcio1213 = csv.reader(f34)
f35 = open(fichier35)
calcio1314 = csv.reader(f35)
f36 = open(fichier36)
calcio1415 = csv.reader(f36)
f37 = open(fichier37)
calcio1516 = csv.reader(f37)
f38 = open(fichier38)
calcio1617 = csv.reader(f38)
f39 = open(fichier39)
calcio1718 = csv.reader(f39)
f40 = open(fichier40)
calcio1819 = csv.reader(f40)

f41 = open(fichier41)
france0910 = csv.reader(f41)
f42 = open(fichier42)
france1011 = csv.reader(f42)
f43 = open(fichier43)
france1112 = csv.reader(f43)
f44 = open(fichier44)
france1213 = csv.reader(f44)
f45 = open(fichier45)
france1314 = csv.reader(f45)
f46 = open(fichier46)
france1415 = csv.reader(f46)
f47 = open(fichier47)
france1516 = csv.reader(f47)
f48 = open(fichier48)
france1617 = csv.reader(f48)
f49 = open(fichier49)
france1718 = csv.reader(f49)
f50 = open(fichier50)
france1819 = csv.reader(f50)
#######################################################

domicile = 0
exterieur = 0
nul = 0
domicile2 = 0
exterieur2 = 0
nul2 = 0
domicile3 = 0
exterieur3 = 0
nul3 = 0
domicile4 = 0
exterieur4 = 0
nul4 = 0
domicile5 = 0
exterieur5 = 0
nul5 = 0
p = 0
l = 0
b = 0
s = 0
f = 0

for colonne in pl0910:
    p += 1
    #print(colonne[4])
    if colonne[6] == "H":
        domicile += 1
    elif colonne[6] == "A":
        exterieur += 1
    elif colonne[6] == "D":
        nul += 1

for colonne in pl1011:
    p += 1
    #print(colonne[4])
    if colonne[6] == "H":
        domicile += 1
    elif colonne[6] == "A":
        exterieur += 1
    elif colonne[6] == "D":
        nul += 1

for colonne in pl1112:
    p += 1
    #print(colonne[4])
    if colonne[6] == "H":
        domicile += 1
    elif colonne[6] == "A":
        exterieur += 1
    elif colonne[6] == "D":
        nul += 1

for colonne in pl1213:
    p += 1
    #print(colonne[4])
    if colonne[6] == "H":
        domicile += 1
    elif colonne[6] == "A":
        exterieur += 1
    elif colonne[6] == "D":
        nul += 1

for colonne in pl1314:
    p += 1
    #print(colonne[4])
    if colonne[6] == "H":
        domicile += 1
    elif colonne[6] == "A":
        exterieur += 1
    elif colonne[6] == "D":
        nul += 1

for colonne in pl1415:
    p += 1
    #print(colonne[4])
    if colonne[6] == "H":
        domicile += 1
    elif colonne[6] == "A":
        exterieur += 1
    elif colonne[6] == "D":
        nul += 1

for colonne in pl1516:
    p += 1
    #print(colonne[4])
    if colonne[6] == "H":
        domicile += 1
    elif colonne[6] == "A":
        exterieur += 1
    elif colonne[6] == "D":
        nul += 1

for colonne in pl1617:
    p += 1
    #print(colonne[4])
    if colonne[6] == "H":
        domicile += 1
    elif colonne[6] == "A":
        exterieur += 1
    elif colonne[6] == "D":
        nul += 1

for colonne in pl1718:
    p += 1
    #print(colonne[4])
    if colonne[6] == "H":
        domicile += 1
    elif colonne[6] == "A":
        exterieur += 1
    elif colonne[6] == "D":
        nul += 1

for colonne in pl1819:
    p += 1
    #print(colonne[4])
    if colonne[6] == "H":
        domicile += 1
    elif colonne[6] == "A":
        exterieur += 1
    elif colonne[6] == "D":
        nul += 1

for colonnes in liga0910:
    l += 1
    #print(colonne[4])
    if colonnes[6] == "H":
        domicile2 += 1
    elif colonnes[6] == "A":
        exterieur2 += 1
    elif colonnes[6] == "D":
        nul2 += 1

for colonnes in liga1011:
    l += 1
    #print(colonne[4])
    if colonnes[6] == "H":
        domicile2 += 1
    elif colonnes[6] == "A":
        exterieur2 += 1
    elif colonnes[6] == "D":
        nul2 += 1

for colonnes in liga1112:
    l += 1
    #print(colonne[4])
    if colonnes[6] == "H":
        domicile2 += 1
    elif colonnes[6] == "A":
        exterieur2 += 1
    elif colonnes[6] == "D":
        nul2 += 1

for colonnes in liga1213:
    l += 1
    #print(colonne[4])
    if colonnes[6] == "H":
        domicile2 += 1
    elif colonnes[6] == "A":
        exterieur2 += 1
    elif colonnes[6] == "D":
        nul2 += 1

for colonnes in liga1314:
    l += 1
    #print(colonne[4])
    if colonnes[6] == "H":
        domicile2 += 1
    elif colonnes[6] == "A":
        exterieur2 += 1
    elif colonnes[6] == "D":
        nul2 += 1

for colonnes in liga1415:
    l += 1
    #print(colonne[4])
    if colonnes[6] == "H":
        domicile2 += 1
    elif colonnes[6] == "A":
        exterieur2 += 1
    elif colonnes[6] == "D":
        nul2 += 1

for colonnes in liga1516:
    l += 1
    #print(colonne[4])
    if colonnes[6] == "H":
        domicile2 += 1
    elif colonnes[6] == "A":
        exterieur2 += 1
    elif colonnes[6] == "D":
        nul2 += 1

for colonnes in liga1617:
    l += 1
    #print(colonne[4])
    if colonnes[6] == "H":
        domicile2 += 1
    elif colonnes[6] == "A":
        exterieur2 += 1
    elif colonnes[6] == "D":
        nul2 += 1

for colonnes in liga1718:
    l += 1
    #print(colonne[4])
    if colonnes[6] == "H":
        domicile2 += 1
    elif colonnes[6] == "A":
        exterieur2 += 1
    elif colonnes[6] == "D":
        nul2 += 1

for colonnes in liga1819:
    l += 1
    #print(colonne[4])
    if colonnes[6] == "H":
        domicile2 += 1
    elif colonnes[6] == "A":
        exterieur2 += 1
    elif colonnes[6] == "D":
        nul2 += 1

for colonne in bundes0910:
    b += 1
    #print(colonne[4])
    if colonne[6] == "H":
        domicile3 += 1
    elif colonne[6] == "A":
        exterieur3 += 1
    elif colonne[6] == "D":
        nul3 += 1

for colonne in bundes1011:
    b += 1
    #print(colonne[4])
    if colonne[6] == "H":
        domicile3 += 1
    elif colonne[6] == "A":
        exterieur3 += 1
    elif colonne[6] == "D":
        nul3 += 1

for colonne in bundes1112:
    b += 1
    #print(colonne[4])
    if colonne[6] == "H":
        domicile3 += 1
    elif colonne[6] == "A":
        exterieur3 += 1
    elif colonne[6] == "D":
        nul3 += 1

for colonne in bundes1213:
    b += 1
    #print(colonne[4])
    if colonne[6] == "H":
        domicile3 += 1
    elif colonne[6] == "A":
        exterieur3 += 1
    elif colonne[6] == "D":
        nul3 += 1

for colonne in bundes1314:
    b += 1
    #print(colonne[4])
    if colonne[6] == "H":
        domicile3 += 1
    elif colonne[6] == "A":
        exterieur3 += 1
    elif colonne[6] == "D":
        nul3 += 1

for colonne in bundes1415:
    b += 1
    #print(colonne[4])
    if colonne[6] == "H":
        domicile3 += 1
    elif colonne[6] == "A":
        exterieur3 += 1
    elif colonne[6] == "D":
        nul3 += 1

for colonne in bundes1516:
    b += 1
    #print(colonne[4])
    if colonne[6] == "H":
        domicile3 += 1
    elif colonne[6] == "A":
        exterieur3 += 1
    elif colonne[6] == "D":
        nul3 += 1

for colonne in bundes1617:
    b += 1
    #print(colonne[4])
    if colonne[6] == "H":
        domicile3 += 1
    elif colonne[6] == "A":
        exterieur3 += 1
    elif colonne[6] == "D":
        nul3 += 1

for colonne in bundes1718:
    b += 1
    #print(colonne[4])
    if colonne[6] == "H":
        domicile3 += 1
    elif colonne[6] == "A":
        exterieur3 += 1
    elif colonne[6] == "D":
        nul3 += 1

for colonne in bundes1819:
    b += 1
    #print(colonne[4])
    if colonne[6] == "H":
        domicile3 += 1
    elif colonne[6] == "A":
        exterieur3 += 1
    elif colonne[6] == "D":
        nul3 += 1

for colonne in calcio0910:
    s += 1
    #print(colonne[4])
    if colonne[6] == "H":
        domicile4 += 1
    elif colonne[6] == "A":
        exterieur4 += 1
    elif colonne[6] == "D":
        nul4 += 1

for colonne in calcio1011:
    s += 1
    #print(colonne[4])
    if colonne[6] == "H":
        domicile4 += 1
    elif colonne[6] == "A":
        exterieur4 += 1
    elif colonne[6] == "D":
        nul4 += 1

for colonne in calcio1112:
    s += 1
    #print(colonne[4])
    if colonne[6] == "H":
        domicile4 += 1
    elif colonne[6] == "A":
        exterieur4 += 1
    elif colonne[6] == "D":
        nul4 += 1

for colonne in calcio1213:
    s += 1
    #print(colonne[4])
    if colonne[6] == "H":
        domicile4 += 1
    elif colonne[6] == "A":
        exterieur4 += 1
    elif colonne[6] == "D":
        nul4 += 1

for colonne in calcio1314:
    s += 1
    #print(colonne[4])
    if colonne[6] == "H":
        domicile4 += 1
    elif colonne[6] == "A":
        exterieur4 += 1
    elif colonne[6] == "D":
        nul4 += 1

for colonne in calcio1415:
    s += 1
    #print(colonne[4])
    if colonne[6] == "H":
        domicile4 += 1
    elif colonne[6] == "A":
        exterieur4 += 1
    elif colonne[6] == "D":
        nul4 += 1

for colonne in calcio1516:
    s += 1
    #print(colonne[4])
    if colonne[6] == "H":
        domicile4 += 1
    elif colonne[6] == "A":
        exterieur4 += 1
    elif colonne[6] == "D":
        nul4 += 1

for colonne in calcio1617:
    s += 1
    #print(colonne[4])
    if colonne[6] == "H":
        domicile4 += 1
    elif colonne[6] == "A":
        exterieur4 += 1
    elif colonne[6] == "D":
        nul4 += 1

for colonne in calcio1718:
    s += 1
    #print(colonne[4])
    if colonne[6] == "H":
        domicile4 += 1
    elif colonne[6] == "A":
        exterieur4 += 1
    elif colonne[6] == "D":
        nul4 += 1

for colonne in calcio1819:
    s += 1
    #print(colonne[4])
    if colonne[6] == "H":
        domicile4 += 1
    elif colonne[6] == "A":
        exterieur4 += 1
    elif colonne[6] == "D":
        nul4 += 1

for colonne in france0910:
    f += 1
    #print(colonne[4])
    if colonne[6] == "H":
        domicile5 += 1
    elif colonne[6] == "A":
        exterieur5 += 1
    elif colonne[6] == "D":
        nul5 += 1

for colonne in france1011:
    f += 1
    #print(colonne[4])
    if colonne[6] == "H":
        domicile5 += 1
    elif colonne[6] == "A":
        exterieur5 += 1
    elif colonne[6] == "D":
        nul5 += 1

for colonne in france1112:
    f += 1
    #print(colonne[4])
    if colonne[6] == "H":
        domicile5 += 1
    elif colonne[6] == "A":
        exterieur5 += 1
    elif colonne[6] == "D":
        nul5 += 1

for colonne in france1213:
    f += 1
    #print(colonne[4])
    if colonne[6] == "H":
        domicile5 += 1
    elif colonne[6] == "A":
        exterieur5 += 1
    elif colonne[6] == "D":
        nul5 += 1

for colonne in france1314:
    f += 1
    #print(colonne[4])
    if colonne[6] == "H":
        domicile5 += 1
    elif colonne[6] == "A":
        exterieur5 += 1
    elif colonne[6] == "D":
        nul5 += 1

for colonne in france1415:
    f += 1
    #print(colonne[4])
    if colonne[6] == "H":
        domicile5 += 1
    elif colonne[6] == "A":
        exterieur5 += 1
    elif colonne[6] == "D":
        nul5 += 1

for colonne in france1516:
    f += 1
    #print(colonne[4])
    if colonne[6] == "H":
        domicile5 += 1
    elif colonne[6] == "A":
        exterieur5 += 1
    elif colonne[6] == "D":
        nul5 += 1

for colonne in france1617:
    f += 1
    #print(colonne[4])
    if colonne[6] == "H":
        domicile5 += 1
    elif colonne[6] == "A":
        exterieur5 += 1
    elif colonne[6] == "D":
        nul5 += 1

for colonne in france1718:
    f += 1
    #print(colonne[4])
    if colonne[6] == "H":
        domicile5 += 1
    elif colonne[6] == "A":
        exterieur5 += 1
    elif colonne[6] == "D":
        nul5 += 1

for colonne in france1819:
    f += 1
    #print(colonne[4])
    if colonne[6] == "H":
        domicile5 += 1
    elif colonne[6] == "A":
        exterieur5 += 1
    elif colonne[6] == "D":
        nul5 += 1

domicileP = domicile/p*100
exterieurP = exterieur/p*100
nulP = nul/p*100
domicileP2 = domicile2/l*100
exterieurP2 = exterieur2/l*100
nulP2 = nul2/l*100
domicileP3 = domicile3/b*100
exterieurP3 = exterieur3/b*100
nulP3 = nul3/b*100
domicileP4 = domicile4/s*100
exterieurP4 = exterieur4/s*100
nulP4 = nul4/s*100
domicileP5 = domicile5/f*100
exterieurP5 = exterieur5/f*100
nulP5 = nul5/f*100

###################################################################

print(" ")
print("D1 = Bundesliga | SP1 = Liga | D1 = Premier League | I1 = Serie A | F1 = Ligue 1")
print("."*10)
print("GAGNANT EN FONCTION DU TERRAIN")
print("D1 | Domicile : " + str(domicile3), "(" + str(domicileP3) + ") |", "Extérieur : " + str(exterieur3), "(" + str(exterieurP3) + ") |", "Nul : " + str(nul3), "(" + str(nulP3) + ").")
print("E0 | Domicile : " + str(domicile), "(" + str(domicileP) + ") |", "Extérieur : " + str(exterieur), "(" + str(exterieurP) + ") |", "Nul : " + str(nul), "(" + str(nulP) + ").")
print("F1 | Domicile : " + str(domicile5), "(" + str(domicileP5) + ") |", "Extérieur : " + str(exterieur5), "(" + str(exterieurP5) + ") |", "Nul : " + str(nul5), "(" + str(nulP5) + ").")
print("I1 | Domicile : " + str(domicile4), "(" + str(domicileP4) + ") |", "Extérieur : " + str(exterieur4), "(" + str(exterieurP4) + ") |", "Nul : " + str(nul4), "(" + str(nulP4) + ").")
print("SP1 | Domicile : " + str(domicile2), "(" + str(domicileP2) + ") |", "Extérieur : " + str(exterieur2), "(" + str(exterieurP2) + ") |", "Nul : " + str(nul2), "(" + str(nulP2) + ").")
print(" ")
print("."*10)
print(" ")


import pandas as pan

futbol = pan.read_csv("futebol.csv")

ligues = futbol.groupby("Div")

print("MOYENNE DE BUTS PAR MATCH")
for buts in ligues:
	print("{} | Buts à domicile = {} | Buts à l'extérieur = {} | Total = {} buts | Moyenne = {} buts par match".format(
		buts[0],
		buts[1].FTHG.sum(),
		buts[1].FTAG.sum(),
		buts[1].FTHG.sum()+buts[1].FTAG.sum(),
		round((buts[1].FTHG.sum()+buts[1].FTAG.sum())/buts[1].Div.count(),2)
		)
	)
print(" ")
print("."*10)
print(" ")
print("MOYENNE DE FAUTES PAR MATCH")
for fautes in ligues:
	print("{} | Fautes à domicile = {} | Fautes à l'extérieur = {} | Total = {} fautes | Moyenne = {} fautes par match".format(
		fautes[0],
		fautes[1].HF.sum(),
		fautes[1].AF.sum(),
		fautes[1].HF.sum()+fautes[1].AF.sum(),
		round((fautes[1].HF.sum()+fautes[1].AF.sum())/fautes[1].Div.count(),2)
		)
	)

print(" ")
print("."*10)
print(" ")
print("MOYENNE DE CARTONS JAUNES PAR MATCH")
for cartonsj in ligues:
	print("{} | Cartons à domicile = {} | Cartons à l'extérieur = {} | Total = {} cartons | Moyenne = {} cartons par match".format(
		cartonsj[0],
		cartonsj[1].HY.sum(),
		cartonsj[1].AY.sum(),
		cartonsj[1].HY.sum()+cartonsj[1].AY.sum(),
		round((cartonsj[1].HY.sum()+cartonsj[1].AY.sum())/cartonsj[1].Div.count(),2)
		)
	)

print(" ")
print("."*10)
print(" ")
print("MOYENNE DE CARTONS ROUGES PAR MATCH")
for cartonsr in ligues:
	print("{} | Cartons à domicile = {} | Cartons à l'extérieur = {} | Total = {} cartons | Moyenne = {} cartons par match".format(
		cartonsr[0],
		cartonsr[1].HR.sum(),
		cartonsr[1].AR.sum(),
		cartonsr[1].HR.sum()+cartonsr[1].AR.sum(),
		round((cartonsr[1].HR.sum()+cartonsr[1].AR.sum())/cartonsr[1].Div.count(),2)
		)
	)

print(" ")
print("."*10)
print(" ")
print("COTE DE PARIS DE BET365 AVANT LES MATCHS")
for paris in ligues:
	print("{} | Domicile = {} | Extérieur = {} | Nul = {}".format(
		paris[0],
		round(paris[1].B365H.sum()/paris[1].Div.count(),2),
        round(paris[1].B365D.sum()/paris[1].Div.count(),2),
        round(paris[1].B365A.sum()/paris[1].Div.count(),2)
		)
	)

print(" ")
print("."*10)
################################################################

