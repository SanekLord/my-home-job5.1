# Cчётчик слов (Сколько слов)
print("Hello I am a word counter")
print("I will help you count the words. ")
print("Enter the words one by one and press 'ENTER.'")
print("When you want to count everything, enter the word 'STOP'")
slov = ""
mas = []
while slov not in ("stop", "STOP"):
    slov = input(f"|{len(mas)+1}| Enter a word:")
    mas.append(slov)
mas.pop(-1)
print(f"Your word count is: |{len(mas)}|")
input("If you want to see the words you entered, then press 'ENTER'")
if len(mas) == 0:
    print("You didn't enter anything!")
else:
    print(f"Your words:{mas}")


