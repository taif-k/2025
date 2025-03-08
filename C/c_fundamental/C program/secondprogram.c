#include<stdio.h>


int digit() //Global
{
    return 10;
}

int main()
{
    printf("The number is: %d",digit());
    int sum = 3+1;
    sum = 20;
    sum = sum + 1;
    printf("\nAnother number is: %d",sum);
    return 0;
}