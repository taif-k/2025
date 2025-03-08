#include <stdio.h>

int sum(int a, int b);
int subtraction(int a, int b);
int multiplication(int a, int b);
void calculator();
void dashboard();

int main()
{
    
    calculator();
    return 0;
}

void calculator()
{
    int first;
    int second;
    int option;
    int count = 0;

        printf("\n\nEnter number one: ");
        scanf("%d", &first);
        printf("Enter number two: ");
        scanf("%d", &second);

        do
        {
            dashboard();
            printf("\nEnter option ");
            scanf("%d", &option);

            switch (option)
            {
            case 1:
                printf("Sum is: %d", sum(first, second));
                break;

            case 2:
                printf("Subtraction is: %d", subtraction(first, second));
                break;

            case 3:
                printf("Multiplication is: %d", multiplication(first, second));
                break;

            case 4:
                count = 1;
                break;

            default:
                getchar();
            }

        } while (count == 0);
}

void dashboard()
{
    printf(" \n |Enter 1 for Addition| ");
    printf(" |Enter 2 for Subtraction| ");
    printf(" |Enter 3 for Multiplication| ");
    printf(" |Enter 4 for Exit| ");
}

int sum(int a, int b)
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
