#совподение чисел (111, 222 или 333 и т.д...)
print("Enter a number, and I'll tell you if all the numbers in it are the same.")
num = int(input("Enter the number:"))
nump = num % 10
otv = "Yes! Numbers match."
while num > nump:
    num //= 10
    if num % 10 != nump:
        otv = "No! Numbers don't match."
    break
print(otv)

# математику я подсмотрел! Так что это не 100% моя работа