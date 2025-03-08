#include <stdio.h>

int main()
{

    int input;
    int count = 0;  //default negative

    for (int i = 0; i < 3; i++)
    {
        printf("Enter num: "); //  -1  2  3
        scanf("%d", &input);
        if (input > 0)
        {
            count = 1;
        }
    }
    if (count < 1)
    {
        printf("\nNegative");
    }
    else
    {
        printf("Positive no is present");
    }

    return 0;
}