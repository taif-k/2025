#include <stdio.h>

int main()
{

    int numbers[5] = {5, 10, 15, 20, 25};
    int sum = 0; // 5  //15  30

    for (int i = 0; i < 5; i++)
    {
        sum += numbers[i];
        printf(" %d ", sum);
    }
    printf("\n %d ", sum);
    return 0;
}