#include <stdio.h>

int sum(int a, int b);
int subtraction(int a, int b);
int multiplication(int a, int b);
void calculator();
void dashboard();

int main()
{
    dashboard();
    calculator();

    return 0;
}

void calculator()
{
    int first;
    int second;
    int option;

    while (1)
    {
        
        printf("\n\nEnter number one: ");
        scanf("%d", &first);
        printf("Enter number two: ");
        scanf("%d", &second);
        printf("\n\nEnter option ");
        scanf("%d", &option);

        if (option == 1)
        {
            printf("\nSum is: %d", sum(first, second));
            getchar();
        }
        else if (option == 2)
        {
            printf("\nSubtraction is: %d", subtraction(first, second));
            getchar();
        }
        else if (option == 3)
        {
            printf("\nMultiplication is: %d", multiplication(first, second));
            getchar();
        }
        else if (option == 4)
        {
            break;
        }
        else
        {
            getchar();
        }
    }
}

void dashboard()
{
    printf("\nPress 1 for Addition | Press 2 for Subtraction | Press 3 for Multiplication | Press 4 for Exit");
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
