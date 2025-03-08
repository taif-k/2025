#include <stdio.h>

int SUM(int a, int b);
int subtraction(int a, int b);
int multiplication(int a, int b);
void calculator();
void Dashboard();

int main()
{
    Dashboard();
    calculator();

    return 0;
}

int SUM(int a, int b)
{
    return a + b;
}

int subtraction(int a, int b)
{
    return a - b;
}

int multiplication(int a, int b)
{
    return a * b;
}

void Dashboard()
{

    printf("\n|Press 1 for Addition| ");
    printf("|Press 2 for Subtraction| ");
    printf("|Press 3 for Multiplication| ");
    printf("|Press 4 for Exit| ");
}

void calculator()
{
    int first;
    int second;
    int option;
    int count = 0;

    printf("\nEnter number one: ");
    scanf("%d", &first);
    printf("Enter number two: ");
    scanf("%d", &second);

    do
    {
        printf("\nEnter option ");
        scanf("%d", &option);

        if (option == 1)
        {
            printf("Sum is: %d", SUM(first, second));
        }
        else if (option == 2)
        {
            printf("Subtraction is: %d", subtraction(first, second));
        }
        else if (option == 3)
        {
            printf("Multiplication is: %d", multiplication(first, second));
        }
        else if (option == 4)
        {
            printf("Thank you");
            break;
        }
        else
        {
            getchar();
        }
    } while (count == 0);
}
