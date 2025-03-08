#include<stdio.h>

int main()
{
    int num;
    printf("\nEnter only odd number: ");
    scanf("%d",&num);

   if(num%2!=0)
   {
    printf("Yes,Number is odd: %d",num);
   }
   else
   {
     printf("Number is not odd");
   }

    return 0;
}