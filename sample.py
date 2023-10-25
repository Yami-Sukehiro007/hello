print("Enter numbers: ")
a=list(map(int,input().split()))
print("Sum of numbers is :",sum(a))
m=1
for i in a:
    m=m*i
print("product of numbers is: ",m)