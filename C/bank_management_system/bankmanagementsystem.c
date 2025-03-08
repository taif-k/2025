#include <stdio.h>
#include <string.h>

void createaccount(char anumb[12], char hname[10], int bal); // Declaration
void Deposit(char anumb[12], int bal);
void withdraw(char anumb[12], int bal);
void CheckBalance(char anumb[12], int bal);
void DisplayAccountDetails(char anumb[12], char hname[10], int bal);
void VerifyTaskNo();
void bms();
void menu();

int main() // System Defined Function
{
    printf("\n------------------------Banking Managemnt System------------------------");
    menu();
    bms();
    return 0;
} 

void menu()
{

    printf("\n1- Create Account ");
    printf("\n2- Enter 2 to Deposit ");
    printf("\n3- Enter 3 to Withdraw ");
    printf("\n4- Enter 4 to Display Balance ");
    printf("\n5- Enter 5 to Check Balance ");
}

void bms() // User defined Function
{
    int count = 0;
    char holdername[15];
    int balance = 0;
    char accountnumber[12];
    int depositamount = 0;
    int withdrawamount = 0;
    int option;

    printf("\nEnter task number: ");
    scanf("%d", &option);
    if (option == 0)
    {
        return;
    }

    do // Do-while Loop to handle option 1
    {
        printf("\n\nEnter task number: ");
        if (scanf("%d", &option) != 1 || option < 1 || option > 5)
        {
            while (getchar() != '\n');
            continue;
        }

        if (option == 1)
        {
            while (1)
            {
                printf("Enter an 11 digit account number (only digits): ");
                scanf(" %s", &accountnumber);
                int length = strlen(accountnumber); //  @ @ 64

                if (length == 11)
                {
                    int flag = 0;
                    int zero = 0;
                    for (int i = 0; i < length; i++)
                    {
                        if (accountnumber[i] < '0' || accountnumber[i] > '9') // 0(48)-9(57)
                        {
                            flag = 1;
                            break;
                        }
                        if (accountnumber[i] == '0')
                        {
                            zero++;
                        }
                    }
                    if (zero == 11)
                    {
                        continue;
                    }

                    if (flag == 0)
                    {

                        while (1)
                        {
                            printf("Enter Name: ");
                            scanf(" %[^\n]", &holdername);
                            int match = 0;
                            for (int i = 0; holdername[i] != '\0'; i++) //  abcdef\0
                            {
                                if ((holdername[i] < 'a' || holdername[i] > 'z') && (holdername[i] < 'A' || holdername[i] > 'Z') && holdername[i] != ' ')
                                {
                                    match = 1;
                                    break;
                                }
                            }
                            if (match == 0)
                            {
                                break;
                            }
                        }

                        while (1)
                        {
                            char balanceStr[20];
                            printf("Enter opening balance (Minimum 500): ");
                            scanf(" %s", &balanceStr); //  [a][b][c] [1][0][0]

                            int match = 0;
                            int length = strlen(balanceStr);

                            for (int i = 0; i < length; i++)
                            {
                                if (balanceStr[i] < '0' || balanceStr[i] > '9')
                                {
                                    match = 1;
                                    break;
                                }
                            }

                            if (match == 0)
                            {
                                balance = 0;
                                for (int i = 0; i < length; i++)
                                {
                                    balance = balance * 10 + (balanceStr[i] - '0');
                                }

                                if (balance >= 500)
                                {
                                    break;
                                }
                            }
                        }
                        break;
                    }
                }
            }
            createaccount(accountnumber, holdername, balance);
        }
        else if (option == 0)
        {
            break;
        }
        else
        {
            getchar();
            printf("Choose 1 (create account) to proceed further ");
        }
    } while (option != 1);

    do // Do-while Loop to handle rest options
    {
        printf("\n\nEnter task number : ");
        scanf("%d", &option);
        if (option == 0)
        {
            break;
        }

        if (option == 2)
        {
            while (1)
            {
                char depositstr[20];
                printf("\nEnter deposit amount ( Minimum-100 ): ");
                scanf(" %s", &depositstr); //  [a][b][c] [1][0][0]
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
            Deposit(accountnumber, balance);
        }
        else if (option == 3)
        {

            while (1)
            {
                char withdrawstr[20];
                printf("\nEnter Withdraw Amount: ");
                scanf(" %s", &withdrawstr); //  [a][b][c] [1][0][0]

                int match = 0;
                for (int i = 0; withdrawstr[i] != '\0'; i++)
                {
                    if (withdrawstr[i] < '0' || withdrawstr[i] > '9')
                    {
                        match = 1;
                        break;
                    }
                }
                if (match == 0)
                {
                    withdrawamount = 0;
                    int length = strlen(withdrawstr);
                    for (int i = 0; i < length; i++)
                    {
                        withdrawamount = withdrawamount * 10 + (withdrawstr[i] - '0');
                    }
                    if (withdrawamount > balance)
                    {
                        printf("Withdraw Amount is greater than Total Balance");
                    }
                    else if (withdrawamount % 100 != 0)
                    {
                        printf("Enter valid Amount");
                    }
                    else
                    {
                        balance -= withdrawamount;
                        break;
                    }
                }
            }
            withdraw(accountnumber, balance);
        }
        else if (option == 4)
        {
            DisplayAccountDetails(accountnumber, holdername, balance);
        }
        else if (option == 5)
        {
            CheckBalance(accountnumber, balance);
        }
        else if (option == 0)
        {
            break;
        }
        else
        {
            VerifyTaskNo();
        }

    } while (count == 0);
}

void createaccount(char anumb[12], char hname[10], int bal) // Defination (has parameters)
{

    printf("\nWelcome to ");
    printf("\033[34mInd\033[0m");
    printf("\033[37mi\033[0m");
    printf("\033[38;5;220mBank\033[0m");

    printf("\nAccount number: %s", anumb);
    printf("\nAccount Holder Name: %s", hname);
    printf("\nAccount Balance %d", bal);
}

void Deposit(char anumb[12], int bal)
{

    printf("\nAccount Number: %s", anumb);
    printf("\nTotal Balance: %d", bal);
}

void withdraw(char anumb[12], int bal)
{
    printf("\nAccount Number: %s", anumb);
    printf("\nTotal Balance: %d", bal);
}

void CheckBalance(char anumb[12], int bal)
{
    printf("\nAccount Number: %s", anumb);
    printf("\nTotal Balance: %d", bal);
}

void DisplayAccountDetails(char anumb[12], char hname[10], int bal)
{
    printf("\nAccount Number: %s", anumb);
    printf("\nAccount Holder Name: %s", hname);
    printf("\nBalance: %d", bal);
}
void VerifyTaskNo()
{
    getchar();
    printf("\nChoose valid Task Number");
}