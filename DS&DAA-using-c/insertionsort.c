#include<stdio.h>

void main(){
    int arr[50],n,i,hole,value,temp;
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
    for(i=1;i<n;i++){
        value = arr[i];
        hole = i;
        while(hole>0 && arr[hole-1]>value){
            arr[hole] = arr[hole-1];
            hole = hole-1;
        }
        arr[hole] = value;
    }
    /*Printing shorted array*/
    printf("Shorted array\n");
    for(i=0;i<n;i++){
        printf("%d\n",arr[i]);
    }
}
