#function to de partition on array
def partiton(arr,start,end):
    pivot = arr[end]
    pindex = start
    for i in range(start,end):
        if(arr[i]<=pivot):
            temp = arr[i]
            arr[i] = arr[pindex]
            arr[pindex] = temp
            pindex = pindex+1

    temp = arr[pindex]
    arr[pindex] = arr[end]
    arr[end] = temp
    return pindex

#Function to do sorting
def quicksort(arr,start,end):
    if(start < end):
        pindex = partiton(arr,start,end)
        quicksort(arr,start,pindex-1)
        quicksort(arr,pindex+1,end)


#taking array input from user
n = int(input("Enter the no of ekement in unsoterd array\n"))
arr = []
print("Enter the elements of array")
for i in range(n):
    arr.append(int(input()))

#printing unsorted array
print("Unsorted array\n",arr)

#main stetment where shorting perform
quicksort(arr,0,n-1)

#prining the sorted aaray
print("Sorted\n",arr)