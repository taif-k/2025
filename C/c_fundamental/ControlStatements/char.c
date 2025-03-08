#include<stdio.h>

int main()
{
    char ch;

    printf("Enter: ");
    scanf("%c",&ch);

    if(ch == 'a' || ch == 'i'|| ch == 'o'||ch == 'u' || ch == 'e')
    {
 printf("It is a vowel");
    }
    else
    {
        printf("Not a vowel");
    }
    return 0;
}