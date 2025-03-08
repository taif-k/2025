#include <stdio.h>

int main()
{
    int score[5];
    int newScore[5];
    printf(" Please enter score in 5 subjects:  ");

    for (int i = 0; i < 5; i++)
    {
        scanf("%d", &score[i]);
    }

    for (int i = 0; i < 5; i++)
    {
        newScore[i] = score[i];
        printf("\nNew Score, Index %d: %d", i, newScore[i]);
    }

    return 0;
}