#include <stdio.h>

int main()
{

    int input;
    int count=0;

    for (int i = 0; i < 3; i++)
    {
        scanf("%d", &input);
        if (input < 0)
        {
            count = 1; //  1  -2  3
        }
    }

    if(count == 1)
    {
    printf("\nNegative");
    }
    else  // count !=1
    {
      printf("\nAll Positive");
    }

    return 0;
}