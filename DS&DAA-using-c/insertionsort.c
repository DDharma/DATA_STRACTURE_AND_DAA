#include<stdio.h>

void main(){
    int arr[50],n,i,j,temp;
    /*Taking user input any array*/
    printf("Enter the no of element in array");
    scanf("%d",&n);
    printf("Enter the element of array");
    for(i=0;i<n;i++){
        scanf("%d",&arr[i]);       
    }
    /*Printing unshorted array*/
    printf("Unshorted array\n");
    for(i=0;i<n;i++){
        printf("%d",arr[i]);
    }