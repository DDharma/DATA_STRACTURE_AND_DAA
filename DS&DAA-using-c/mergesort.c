#include<stdio.h>

//Function Decleration
void mergesort(int arr[], int start, int end);
void merge(int *arr,int staet, int end);
//Function which perform sorting
void mergesort(int arr[], int start, int end){
    if(start>=end)
        return;
    int mid = (start+end)/2;

    mergesort(arr,start,mid);
    mergesort(arr,mid+1,end);
    merge(arr,start,end);
}

/*Function for merging sub arrays*/
void merge(int *arr,int start, int end){
    int mid = (start+end)/2;
    int i = start;
    int j = mid+1;
    int k = start;
    int temp[100];

    while(i<=mid && j<=end){
        if(arr[i] < arr[j]){
            temp[k] = arr[i];
            i = i+1;
            k = k+1;
        }
        else{
            temp[k] = arr[j];
            j = j+1;
            k = k+1;
        }
    }
    while(i<=mid){
        temp[k] = arr[i];
        i = i+1;
        k = k+1;
    }
    while(j<=end){
        temp[k] = arr[j];
        j = j+1;
        k = k+1;
    }
    for(int i = start;i<=end;i++){
        arr[i] = temp[i];
    }    
}
void main(){
    int arr[50],n,i,j;
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
    /*main stetment where shorting perform */
    mergesort(arr,0,n-1);
    /*Printing the sorted array*/
    printf("Shorted array\n");
    for(i=0;i<n;i++){
        printf("%d\n",arr[i]);
    }
}