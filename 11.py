a = 10
ser1 = []
ser2 = []
ser3 = []
ser4 = []
for i in range(0, a):
    if i % 4 == 0:
        i += 1
        ser1.append(i)
        ser2.append(i+1)
        ser3.append(i+2)
        ser4.append(i+3)
print(ser1, ser2, ser3, ser4)
