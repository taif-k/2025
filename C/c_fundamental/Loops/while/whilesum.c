#include <stdio.h>

int main()
{

    int num = 1;
    int sum = 0;
    while (num <= 10)
    {
        sum += num;
        printf(" \n%d ",num);
        num++;
        // break;
    }
    printf(" \n%d ",sum);

    return 0;
}