#taking array input from user
n = int(input("Enter the no of ekement in unsoterd array\n"))
arr = []
print("Enter the elements of array")
for i in range(n):
    arr.append(int(input()))

#printing unsorted array
print("Unsorted array\n",arr)

#main stetment where shorting perform
for i in range(1,n):
    value = arr[i]
    hole = i

    while(hole>0 and arr[hole-1]>value):
        arr[hole] = arr[hole-1]
        hole = hole-1

    arr[hole] = value

#printing unsorted array
print("Sorted array\n",arr)    