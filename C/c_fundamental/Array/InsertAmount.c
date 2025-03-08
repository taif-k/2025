#include <stdio.h>

int main()
{

    int account[5]; //  0  1  2  3  4
    int check[5];
    int count = 0;
    printf("Enter amount: ");

    for (int i = 0; i < 5; i++)
    {
        scanf("%d", &check[i]);
        if (check[i] >= 10 && check[i] <= 100)
        {
            account[count] = check[i];
            count++;
        }
    }

    for (int i = 0; i < count; i++)
    {
        printf(" Output: %d", account[i]);
    }

    return 0;
}