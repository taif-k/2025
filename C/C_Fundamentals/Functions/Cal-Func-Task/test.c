#include <stdio.h>

int data(int arr[2])
{
    // printf("%d, %d", arr[0], arr[1]);
    return arr[0];
}

int main()
{
    int array[2] = {4,8};
    printf("%d",data(array)); 

    

    return 0;
}
