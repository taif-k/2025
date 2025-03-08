#include <stdio.h>
#include <string.h>

void Deposit(int bal); // Declaration
void bms();

int main()
{
    bms();
    return 0;
}

void bms()
{
    int balance = 0;
    int depositamount = 0;

    while (1)
    {
        char depositstr[20];
        printf("\nEnter deposit amount ( Minimum-100 ): ");
        scanf(" %s", &depositstr);
        int length = strlen(depositstr);
        int match = 0;
        for (int i = 0; depositstr[i] != '\0'; i++)
        {
            if (depositstr[i] < '0' || depositstr[i] > '9')
            {
                match = 1;
                break;
            }
        }
        if (match == 0)
        {
            depositamount = 0;
            for (int i = 0; i < length; i++)
            {
                depositamount = depositamount * 10 + (depositstr[i] - '0');
            }
            if (depositamount >= 100)
            {
                balance += depositamount;
                break;
            }
        }
    }
    Deposit(balance); // Calling has Arguments
}

void Deposit(int bal) // Defination has parameters(Declared with datatypes)
{
    printf("\nTotal Balance: %d", bal);
}