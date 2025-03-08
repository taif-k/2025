#include <stdio.h>

int main()
{
    char fname[15];
    char lname[20];
    int count = 0;

    scanf("%[^\n]", &fname);
    // scanf("%s",&lname);
    printf(" Name is : %s", fname);

    // for (int i = 0; i < 7; i++)
    // {
    //     if (fname[i] == 'a' || fname[i] == 'i' || fname[i] == 'u' || fname[i] == 'o' || fname[i] == 'e')
    //     {
    //         count++;
    //     }
    // }

    // printf(" total count of vowels : %d ", count);

    return 0;
}