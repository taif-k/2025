#include <stdio.h>

void multiplication();
void division();
void addition();
void subtraction();
int a, b;
char option;

int main()
{
    int count = 0;
    printf("Enter number one: ");
    scanf("%d", &a);
    printf("Enter number two: ");
    scanf("%d", &b);

    do
    {
        printf("Select m, s, a or d: ");
        scanf(" %[^\n]", &option);

        if (option == 'a')
        {
            addition();
            break;
        }
        else if (option == 's')
        {
            subtraction();
            break;
        }
        else if (option == 'm')
        {
            multiplication();
            break;
        }
        else if (option == 'd')
        {
            division();
            break;
        }
        else
            ("Invalid option");

    } while (count == 0);

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
