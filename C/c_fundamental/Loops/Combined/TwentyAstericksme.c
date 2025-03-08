#include <stdio.h>

int main()
{

    int option;
    int count = 0;

    while (count<2)
    {
        count++;
        printf("Enter 1 or 2");
        scanf("%d", &option);
        if (option == 1)
        {
            for (int i = 1; i <= 5; i++)
            {
                for (int j = 1; j <= 20; j++)
                {
                    printf(" * ");
                }
                printf("\n");
            }
        }
        if (option == 2)
        {
            for (int i = 1; i <= 5; i++)
            {
                for (int j = 1; j <= 20; j++)
                {
                    printf(" %d ", j);
                }
                printf("\n");
            }
        }
    }

    return 0;
}