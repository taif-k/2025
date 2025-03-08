//    1   2   3   4
//    5   6   7   8
//    9   10  11  12 [2][3]

#include <stdio.h>

int main()
{                        //     [0]               [1]              [2]
    int TwoDArray[3][4]; //  {{[0][1][2][3]}, {[0][1][2][3]}, {[0][1][2][3]}}
    printf("Enter 12 numbers  [3X4]");
    printf("\n");

    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 4; j++)
        {
            scanf("%d", &TwoDArray[i][j]);
        }
        printf("\n");
    }
    printf("output: ");
    printf("\n");

    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 4; j++)
        {
            printf(" %d ", TwoDArray[i][j]);
        }
        printf("\n");
    }

    return 0;
}


