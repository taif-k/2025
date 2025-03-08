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

    

    // for (int i = 0; i < 4; i++) //  4
    // {
    //     int count = 0;
    //     for (int j = i + 1; j < 4; j++)
    //     {
    //         if (arr3[i] > arr3[j])
    //         {
    //             count = 1;
    //             break;
    //         }
    //     }

    //     if (count == 1)
    //     {
    //         largest = arr3[i];
    //     }
    // }
    // printf(" %d ", largest);

    return 0;
}