#PROGRAM TO PRINT ALL POSITIVE NUMBERS IN A RANGE:

list=[]
while True:
    x=(input("Enter a number: "))
    if x=='done':break
    value=int(x)
    list.append(value)
print("Input List:",list)
li=[]
for num in list:
    if num>0:
        li.append(int(num))
print("Output List consisting of positive numbers:",li)
