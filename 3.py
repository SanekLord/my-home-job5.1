#Ведьмаку заплотите чеканной монетой
from random import randint
print("The Witcher defeated the monster that lived under your bed and prevented you from sleeping.")
wed = randint(25, 49)
print(f"The witcher gave you a price for his work: {wed}")
print("-----------------------------------")
mon = int(input("How much will you tip the witcher?:"))
money = wed + mon
print(f"You must give the witcher {money} But it only accepts minted coins.")
input("Want to calculate how many coins you owe? If yes, then press 'ENTER'")
money_cent = 0
money1 = []
while money > 0:
    if money > 25:
        money -= 25
        money1.append(25)
    elif money > 10:
        money -= 10
        money1.append(10)
    elif money > 5:
        money -= 5
        money1.append(5)
    else:
        money -= 1
        money1.append(1)
    money_cent += 1
print(f"You have to give: {money_cent} coin.")
print(f"Coin denomination:{money1}")