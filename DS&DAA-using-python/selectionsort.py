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
    pass