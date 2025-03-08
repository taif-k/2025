#include<stdio.h>

void menu();

int main() // System Defined Function
{
    menu();
    return 0;
} 

void menu()
{
    printf("\n1- Create Account ");
    printf("\n2- Deposit ");
    printf("\n3- Withdraw ");
    printf("\n4- Display Details ");
    printf("\n5- Check Balance ");
    printf("\n0- Exit");
}