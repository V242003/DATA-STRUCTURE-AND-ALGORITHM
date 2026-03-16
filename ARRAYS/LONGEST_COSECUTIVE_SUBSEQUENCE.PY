arr=[1,99,101,98,2,5,3,97,100,1,1]
my_set=set()
x=0
for i in range(0,len(arr)):
    my_set.add(arr[i])
longest=0
count=0
for num in my_set:
    if num-1 not in my_set:
        x=num
        count=1
        while x+1 in my_set:
            count=count+1
            x=x+1
        longest=max(longest,count)
print(longest)

