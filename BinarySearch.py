a=[]
n=int(input('Enter the size of List : '))
print('Enter the elements of List : ')
for i in range(n):
    a.append(int(input()))

a.sort()
f=0
r=n-1
key=int(input('Enter key : '))
while f<=r:
    m=(f+r)//2
    if a[m]==key:
        print('Found')
        break
    elif a[m]<key:
        f=m+1
    else:
        r=m-1
else:
    print('Not found')