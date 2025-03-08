#include <stdio.h>

void names(char name1[10], char name2[10]);
void input();

int main() {

    input();

    return 0;
}

void input()
{
    char first[10]; 
    char second[10];
    printf("Enter names: ");
    scanf(" %s",&first);
    scanf(" %s",&second);

    names(first,second);
}

void names(char name1[10], char name2[10])
{
    printf("First name: %s",name1);
    printf("\nSecond name: %s",name2);
}


