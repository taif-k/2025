#include <stdio.h>

void multiplication();
void division();
void addition();
void subtraction();
int a, b;
char option;

int main()
{

    printf("Enter number one: ");
    scanf("%d", &a);
    printf("Enter number two: ");
    scanf("%d", &b);

    do
    {
        printf("Select m, s, a or d: ");
        scanf(" %[^\n]", &option); // if i enter qaaa, waa,vdtgtd, m1261 or anything first letter is taken into consideration rest gets ignored

        if (option == 'a')
        {
            addition();
        }
        else if (option == 's')
        {
            subtraction();
        }
        else if (option == 'm')
        {
            multiplication();
        }
        else if (option == 'd')
        {
            division();
        }
        else
            ("Invalid option");

    } while (option != 'a' && option != 's' && option != 'm' && option != 'd');

    return 0;
}

void subtraction()
{
    printf("\nSubtraction is: %d", a - b);
}

void addition()
{

    printf("\nAddition is: %d", a + b);
}

void multiplication()
{

    printf("\nMultiplication is: %d", a * b);
}

void division()
{
    printf("\n\nDivision is: %f", (float)a / b); // 10/20 = 0.5
}
