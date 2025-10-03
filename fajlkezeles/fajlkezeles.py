# open(path, mode): fájl megnyitása
    # path: a megnyitni kívánt fájl elérési útvonala (str)
    # mode: a fájlmegnyitás módja (str)
        # r: olvasás
        # w: írás (felülírja)
        # a: fájl végéhez való hozzáfűzés
        # x: kizárólagos létrehozás

# fájl megnyitása olvasásra
file = open("be.txt", "r")

# teljes fájl beolvasása soronként listába
tartalom = file.readlines()

# fájl bezárása
file.close()

# sorok feldolgozása
for sor in tartalom:
    sor = sor.rstrip()  # sorvégi \n eltávolítása
    print(sor)

# kontextuskezelő mechanizmus 
with open("be.txt", "r") as file:
    for sor in file:  # közvetlenül a fájlon iterálunk
        sor = sor.rstrip()  # sorvégi \n eltávolítása
        print(sor)