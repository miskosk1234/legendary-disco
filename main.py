import random
tajne_cislo = random.randint(1, 5)
tip = int(input("Uhádni číslo od 1 do 5:"))
if tip == tajne_cislo:
    print("dobreeeee win")
else:
    print("game over skus to znova. Správne čislo bolo:", tajne_cislo)
