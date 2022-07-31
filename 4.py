# Карточка
print("Hello, I follow your money.")
print("Enter your balance and how much you are spending")
print("and I will let you know if you have enough money.")
num = int(input("How much money do you have in your account?:"))
print(f"You have on your balance: {num} $")
baza = []
balans = num
while True:
    ras = int(input(f"How much do you want to spend?"))
    if balans > ras:
        baza.append(ras)
        balans -= ras
        print("-----------------------PAYMENT CHECK-----------------------")
        print(f"you spent: {ras}$ you have left on your balance: {balans}$")
        print("-----------------------------------------------------------")
    elif ras == 0 or ras == balans:
        balans = 0
        baza.append(ras)
        print("------PAYMENT ERROR------")
        print("You don't have any more money!")
        break
    elif balans < ras:
        print("------PAYMENT ERROR------")
        print("You don't have that much money! ")
        break
print(f"Purchases made: {len(baza)}")
print(f":Left on the balance: {balans}$")
print("-------------------------")
