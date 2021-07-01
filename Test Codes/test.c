#include <stdio.h>
#include<stdio.h>
#define max 100

void insertion_sort(int[],int);
int main() 
{
    int A[5] = {3, 2, 1, 5, 4}; 
    int n = 5,i;
    
    printf("Before sorting : ");
    for(i=0;i<n;i++)
        printf("\n%d",A[i]);
    insertion_sort(A,n);
    printf("after sorting data is");
    for(i=0;i<n;i++)
        printf("\n%d",A[i]);

    return 0;
}

void insertion_sort(int arr[],int n) 
{
    int i,j,key;

    for(i=1;i<n;i++) 
    {
        key=arr[i];
        j=i-1;

        while(j >= 0 && key < arr[j])
        {
            arr[j+1]=arr[j];
            j -= 1;
        }
        arr[j+1]=key;
    
        printf("\nAfter round %d array is : ", i - 1);
        for(int k=0;k<n;k++)
        printf("\n%d",arr[k]);
    }
}