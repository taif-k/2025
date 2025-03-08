
#include <stdio.h>

int main()
{
    int b;
    printf("Enter amount: ");
    scanf("%d", &b);

    if ( b == 100 || b == 200 || b == 500 )
    {
        printf("Matched");
    }
    else
    {
        printf("Not matched");
    }
    return 0;
}