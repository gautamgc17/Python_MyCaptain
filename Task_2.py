#PROGRAM FOR FIBONACCI SERIES:

n=int(input("Enter number of terms: "))
a=0
b=1
c=0
print("The required Fibonacci series is: ")
for i in range(0,n):
  print(a)
  c=a+b
  a=b
  b=c
