
#include <stdio.h>

int main()
{

    int b;
    printf("Enter: ");
    scanf("%d", &b);

    if ( b<=100 && b != 10 && b != 20 && b != 30 && b != 40 && b != 50 )  // always try to avoid multiple conditions in do while's while.
    {
        printf("Matched");
    }
    else
    {
        printf("Not matched");
    }
    return 0;
}
