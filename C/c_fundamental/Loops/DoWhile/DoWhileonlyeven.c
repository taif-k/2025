#include <stdio.h>

int main()
{

    int input;

    do
    {
        printf("Please enter even number only: ");
        scanf("%d", &input);

    } while (input % 2 != 0);
         
      printf("Thank you!");   
    
    return 0;
}
