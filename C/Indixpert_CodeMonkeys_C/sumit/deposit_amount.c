#include <stdio.h>

void Deposit(int bal); // Declaration

int main()
{
    int balance = 0;
    Deposit(balance);
    return 0;
}

void Deposit(int bal)
{
    while (1)
    {
        int depositamount;
        printf("\nEnter deposit amount should be minimu 100: ");
        scanf("%d", &depositamount);

        if (depositamount >= 100)
        {
            bal += depositamount;
            break;
        }
    }
    printf("\nTotal Balance: %d", bal);
}
