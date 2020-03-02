#include<stdio.h>

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

    /*main stetment where shorting perform */
    for(i=0;i<n-1;i++){
        imin = i;
        for(j=i+1;j<n;j++){
            if(arr[j]<arr[imin]){
                imin = j;
            }
        }
        temp = arr[i];
        arr[i] = arr[imin];
        arr[imin] = temp;
    }

    /*Printing shorted array*/
    printf("Shorted array\n");
    for(i=0;i<n;i++){
        printf("%d\n",arr[i]);
    }

}  