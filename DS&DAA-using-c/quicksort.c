#include<stdio.h>

/* Function to do partition on array*/
int partition(int arr[],int start, int end){
    int pivot = arr[end];
    int pindex = start;
    for(int i = start; i<end; i++){
        if (arr[i] <= pivot){
            int temp = arr[i];
            arr[i] = arr[pindex];
            arr[pindex] = temp;
            pindex = pindex+1;
        }
    }
    int temp = arr[pindex];
    arr[pindex] = arr[end];
    arr[end] = temp;
    return pindex;
}

/*Function to de sorting*/
void quicksort(int arr[],int start, int end){
    if(start < end){
        int pindex = partition(arr,start,end);
        quicksort(arr,start,pindex-1);
        quicksort(arr,pindex+1,end);
    }
}
void main(){
    int arr[50],n,i,j,temp,imin;
    /*Taking user input any array*/
    printf("Enter the no of element in array\n");
    scanf("%d",&n);
    printf("Enter the element of array\n");
    for(i=0;i<n;i++){
        scanf("%d",&arr[i]);       
    }
    
    /*Printing unshorted array*/
    printf("Unshorted array\n");
    for(i=0;i<n;i++){
        printf("%d\n",arr[i]);
    }
    printf("Sorting Start");

    /*main stetment where shorting perform */
    quicksort(arr,0,n);

    /*Printing shorted array*/
    printf("Shorted array\n");
    for(i=0;i<n;i++){
        printf("%d\n",arr[i]);
    }
}