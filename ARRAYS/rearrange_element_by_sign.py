arr=[3,1,-2,-5,2,4]
n=len(arr)
new_array=[0]*n
positive=0
negative=1

for num in range(0,n) :
    if arr[num]>=0 and positive<n:
        new_array[positive]=arr[num]
        positive+=2
    elif negative<n:
        new_array[negative]=arr[num]
        negative+=2
print(new_array)
