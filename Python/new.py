name = input('Enter Number with Space: ')
numList = name.split()
a = []
print(numList)
for i in range(len (numList)):
    if int(numList [i]) % 2 == 0:
        a.append(int(numList [i]))
print(a)