#include <stdio.h>

int main()
{
    int arr1[4] = {2, 4};
    int arr2[2] = {2, 6};
    int arr3[4]; // 2 4 2 6
    int largest = 0;

    for (int i = 0; i < 4; i++)
    {
        arr3[i] = arr1[i];
    }

    for (int i = 0; i < 4; i++)
    {
        arr3[i] = arr2[i];
        printf(" %d ",arr3[i]);
    }

    

    return 0;
}