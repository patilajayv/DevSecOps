print("!!!!!Calculator!!!!!!")
print("Select Action 1) addition 2) multiplication 3) substraction 4) dividationn")
def add(c,b):
     result =b+c
     print(result)
def sub(c,b):
    result =b-c
    print(result)
def mul(c,b):
     result =b*c
     print(result)
def div(c,b):
     result =b/c
     print(result)
A = input("(1/2/3/4) ? ")
b = float(input("Num1: "))
c = float(input("Num2: "))
if(A=='1'):  
   add(c,b)
elif(A=='2'):
   sub(c,b)
elif(A=='3'):
    mul(c,b)
elif(A=='4'):
    div(c,b)
elif(A==''):
     print("No input")
else:
     print("invalid input")

#Prashant.dey@herovired.com
#https://join.slack.com/t/hackthevired/shared_invite/zt-1m72riylc-ejR7VRfVmYP9lBkCn~RX~g