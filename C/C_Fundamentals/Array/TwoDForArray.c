#include <stdio.h>

int main()
{
    char name[2][20];
    printf("Enter name: ");

    for (int i = 0; i < 2; i++)
    {
        scanf(" %s", &name[i]);
    }

    for (int i = 0; i < 2; i++)
    {
        printf("\nName is: %s", name[i]);
    }

    return 0;
}