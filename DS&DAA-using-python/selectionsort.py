#taking array input from user
n = int(input("Enter the no of ekement in unsoterd array\n"))
arr = []
print("Enter the elements of array")
for i in range(n):
    arr.append(int(input()))

#printing unsorted array
print("Unsorted array\n",arr)

#main stetment where shorting perform
for i in range(0,n-1):
    imin = i
    for j in range(i+1,n):
        if(arr[j]<arr[imin]):
            imin = j
    temp = arr[i]
    arr[i] = arr[imin]
    arr[imin] = temp

#printing unsorted array
print("Sorted array\n",arr)    
