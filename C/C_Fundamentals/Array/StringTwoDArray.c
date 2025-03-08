#include <stdio.h>

int main()
{
    int count;
    printf("Enter number of Students to Register:  ");
    scanf("%d", &count);

    char contact[count][10]; //   0     1
    char name[count][20];    // {{ },  { }}
    int id[count];
    char address[count][50];

    for (int i = 0; i <count; i++)
    {
        printf("Please enter student id: ");
        scanf("%d", &id[i]); // 4 /n

        printf("Enter you name: ");
        scanf(" %[^\n]", &name[i]); //  "/n" that we got after pressing enter from previous scanf(&id) will be consumed here in this scanf

        printf("Enter address: ");
        scanf(" %[^\n]", &address[i]);

        printf("Enter contact: ");
        scanf(" %s", &contact[i]);
    }

    for (int i = 0; i <count; i++)
    {
        printf("\n ------------Details--------");
        printf("\nUser id:      %d", id[i]);
        printf("\nUser Name:    %s", name[i]);
        printf("\nUser Contact: %s", contact[i]);
        printf("\nUser Address: %s", address[i]);
    }

    printf("\nThank you, Visit again");

    return 0;
}