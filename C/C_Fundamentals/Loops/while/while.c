#include <stdio.h>

int main()
{
    int num = 0;
    int value;

    printf("Enter the number: ");
    scanf("%d", &value);

    while (1)
    {
        num++;
        printf(" %d ", num);

        if (num == value)
        {
            break;
        }
    }

    return 0;
}