#include <stdio.h>

int main()
{

    char fname[2][20];  //[row][column]  or  { "taif", "khan"}

    for (int j = 0; j < 2; j++)
    {

        scanf("%s", &fname[j]);
    }

    for (int j = 0; j < 2; j++)
    {

        printf("%s", fname[j]);
    }

    return 0;
}