#include <stdio.h>
#include <string.h>

void createaccount(char anumb[12], char hname[10], int bal); // Declaration(has parameters)
void bms();
void menu();

int main()
{
    menu();
    bms();
    return 0;
}

void menu()
{
    printf("\n1- Create Account ");
    printf("\n2- Deposit ");
    printf("\n3- Withdraw ");
    printf("\n4- Display Details ");
    printf("\n5- Check Balance ");
    printf("\n0- Exit ");
}

void bms()
{
    char holdername[10];
    int balance;
    char accountnumber[12];
    int option;

    printf("\n\nEnter task number (from 0 to 5): ");
    scanf("%d", &option);
    if (option == 0)
    {
        return;
    }

    do // do-while
    {
        printf("\n\nEnter task number: ");
        if (scanf("%d", &option) != 1 || option < 1 || option > 5)
        {
            while (getchar() != '\n')
                ;
            continue;
        }

        if (option == 1)
        {
            while (1)
            {
                printf("Enter an 11 digit account number: ");
                scanf(" %s", accountnumber);
                int length = strlen(accountnumber); //  @@64                               // length of string

                if (length == 11)
                {
                    int flag = 0;
                    int zero = 0;
                    for (int i = 0; i < length; i++)
                    {
                        if (accountnumber[i] < '0' || accountnumber[i] > '9') //   range - 0(48) to  9(57)
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
                            for (int i = 0; holdername[i] != '\0'; i++) //  abcdef\0 loop will end just before \0, end of string
                            {
                                if ((holdername[i] < 'a' || holdername[i] > 'z') && holdername[i] != ' ')
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
                            scanf(" %s", &balanceStr); // (Balance)input as string

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
                                    balance = balance * 10 + (balanceStr[i] - '0'); // Converting string to integer
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
            createaccount(accountnumber, holdername, balance); // calling(has Arguments)
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