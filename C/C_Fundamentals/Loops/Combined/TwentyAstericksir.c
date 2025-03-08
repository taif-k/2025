#include <stdio.h>

int main()
{
    int option;
    int count = 0;

    printf("Enter 1 for '*' ");
    printf("Enter 2 for 1-20 ");
    scanf("%d", &option);
    while (1)
    {
        count++;
        for (int i = 1; i <= 20; i++)
        {
            if (option == 1)
            {
                printf(" * ");
            }
            else
            {
                printf(" %d ", i);
            }
        }
        printf("\n");
        if (count == 5)
        {
            break;
        }
    }

    return 0;
}