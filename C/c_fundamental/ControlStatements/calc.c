#include <stdio.h>

int main()
{
    char option;
    int num1;
    int num2;

    printf("\nEnter 'a' for Addition");
    printf("\nEnter 's' for Subtraction");
    printf("\nEnter 'm' for Multiply");
    printf("\nEnter 'd' for Divison");
    printf("\nEnter option: ");
    scanf("%c", &option);

    if (option == 'a' || option == 's' || option == 'm' || option == 'd')
    {
        printf("\nEnter First Number: ");
        scanf("%d", &num1);
        printf("Enter Second Number: ");
        scanf("%d", &num2);

        if (option == 'a')
        {
            printf("\nAdditon of two number is: %d", num1 + num2);         
        }                                                                     
        else if (option == 's')                                              //if   
        {                                                                   //if
            printf("\nSubtraction of two numbers is: %d", num1 - num2);     //else 
        }
        else if (option == 'm')
        {
            printf("\nMultiplication of two numbers is: %d", num1 * num2);
        }
        else if (option == 'd')
        {
            printf("\nDivison of two numbers is: %f", (float)num1 / num2);
        }
    }
    else
    {
        printf("INCORRECT OPTION");
    }
    return 0;
}
