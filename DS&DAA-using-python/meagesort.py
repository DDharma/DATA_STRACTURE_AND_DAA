#function for sorting
def mergesort(arr): 
    if len(arr) >1: 
        mid = len(arr)//2 #Finding the mid of the array 
        L = arr[:mid] # Dividing the array elements  
        R = arr[mid:] # into 2 halves 
  
        mergesort(L) # Sorting the first half 
        mergesort(R) # Sorting the second half 
  
        i = j = k = 0
          
        # Copy data to temp arrays L[] and R[] 
        while i < len(L) and j < len(R): 
            if L[i] < R[j]: 
                arr[k] = L[i] 
                i+=1
            else: 
                arr[k] = R[j] 
                j+=1
            k+=1
          
        # Checking if any element was left 
        while i < len(L): 
            arr[k] = L[i] 
            i+=1
            k+=1
          
        while j < len(R): 
            arr[k] = R[j] 
            j+=1
            k+=1

#taking array input from user
n = int(input("Enter the no of ekement in unsoterd array\n"))
arr = []
print("Enter the elements of array")
for i in range(n):
    arr.append(int(input()))

#printing unsorted array
print("Unsorted array\n",arr)

#main stetment where shorting perform
mergesort(arr)

#prining the sorted aaray
print("Sorted\n",arr)