#include <stdio.h>

int main()
{
    int num1;
    int num2;
    int num3;
    int num4;

    printf("Enter num 1: ");
    scanf("%d", &num1);
    printf("Enter num 2: ");
    scanf("%d", &num2);
    printf("Enter num 3: ");
    scanf("%d", &num3);
    printf("Enter num 4: ");
    scanf("%d", &num4);

    int largest = num1;   //  100 101 99 96
    
    if (num2 > largest)
    {
        largest = num2;
    }
    if (num3 > largest)
    {
        largest = num3;
    }
    if (num4 > largest)
    {
        largest = num4;
    }
    printf("\nLargest number is: %d", largest);

    return 0;
}