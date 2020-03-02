#include<stdio.h>

void main(){
    int arr[50],n,i,j,temp;
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
        for(j=0;j<n-i;j++){
            if(arr[j]>arr[j+1]){
                temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
            }
        }
    }

    /*Printing shorted array*/
    printf("Shorted array\n");
    for(i=0;i<n;i++){
        printf("%d\n",arr[i]);
    }

}   