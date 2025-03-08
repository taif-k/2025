#include <stdio.h>

int main()
{
    int arr1[2] = {100, 4};
    int arr2[2] = {99, 102};
    int arr3[4];
    int largest = 0;

    for (int i = 0; i < 2; i++)
    {
        arr3[i] = arr1[i];
    }

    for (int i = 0; i < 2; i++)
    {
        arr3[i + 2] = arr2[i];
    }

    for (int i = 0; i < 4; i++)
    {
        if (arr3[i] > largest)
        {
            largest = arr3[i];
        }
    }

    printf("\nLargest is %d ", largest);
    // for (int i = 0; i < 4; i++) // 8  4 3 6
    // {
    //     int count = 0;
    //     for (int j = i + 1; j < 4; j++) // 4 2 6
    //     {
    //         if (arr3[i] > arr3[j])
    //         {
    //             arr3[i] = arr3[i] + arr3[j]; // 8 + 4
    //             arr3[j] = arr3[i] - arr3[j]; // 12 - 4
    //             arr3[i] = arr3[i] - arr3[j]; //
    //         }
    //     }
    // }
    // printf(" Largest number is: %d ", arr3[3]);

    return 0;
}