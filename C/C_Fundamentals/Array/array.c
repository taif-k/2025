#include <stdio.h>

int main()
{

    int numbers[5] = {1, 2, 3, 4, 5};
    int sum = 0;

    for (int i = 0; i < 5; i++)
    {
        sum += numbers[i];
    }
    printf("Sum is: %d", sum);
    return 0;
}
