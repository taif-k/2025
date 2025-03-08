#include <stdio.h>

void withdraw(int bal); //declaration

int main()  // system defined function
{
    int balance = 500;   // Initial balance 
    withdraw(balance);   // calling
    return 0;
}

void withdraw(int bal)  // defination
{

    int withdrawAmount=0;  
    printf("Balance is : %d",bal);
    printf("\nEnter the amount to withdraw:");
    scanf("%d", &withdrawAmount); 

    if (withdrawAmount > bal)
    {
        printf("\nInsufficient Amount");
    }
    else if (withdrawAmount % 100 != 0)                         
    {
        printf("\nAmount not multiple of 100");
    }
    else
    {
        bal -= withdrawAmount;
        printf("Withdrawal successful!\n");
        printf("Total Balance: %d", bal);
    }
}