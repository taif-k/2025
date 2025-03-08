#include<stdio.h>

int main()
{
    int num;
    printf("Enter Number: ");
    scanf("%d",&num);
    if(num>0)
    {
        printf("\nPositive no");
    }
    else if(num<0)
    {
        printf("\nnegative no");
    }
    else
    {
        printf("\nNumber is Zero");
    }
      return 0;
}