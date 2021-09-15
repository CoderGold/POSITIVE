a={}
i=0
count=0
n=eval(input("How Many Integers Would You Like To Enter: "))
print("Enter The Integers In The Range One By One: ")
while(i<n):
    a[i]=eval(input())
    i+=1
print("The List Is: ")
for element in a:
    print(a[element],end=' ')
print()
print("The Positive Integers Are: ")
for element in a:
    if a[element]<0:
        count+=1
    else:
        break
if count==n:
    print("NONE")
else:
    for element in a:
        if a[element]>0:
            print(a[element],end=' ')
        else:
            continue
