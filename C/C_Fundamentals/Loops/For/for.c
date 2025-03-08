#include <stdio.h>

int main()
{

    for (int x = 2; x <= 5; x++)
    {
        for (int i = 1; i <= 10; i++)
        {
            printf(" %d", x * i);
        }
        printf("  ");
    }

    return 0;
}