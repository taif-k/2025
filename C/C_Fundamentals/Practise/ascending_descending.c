#include <stdio.h>

int main()
{
    int numbers[10] = {13, 5, 14, 2, 8, 3, 4, 12, 6, 1}; // 2 13 14 5
    int option;

    printf("\n1 for Ascending");
    printf("\n2 for Descending");
    scanf("%d", &option);

    if (option == 1)
    {
        for (int i = 0; i < 10; i++) 
        {
            for (int j = i + 1; j < 10; j++) // After the 1 iteration of 2nd loop "i" of outer loop will be updated but index is still 0, in the 2nd iteration, comparsion will be of 5 & 14 and not 13 and 14 
            {
                if (numbers[i] > numbers[j])
                {
                    numbers[i] = numbers[i] + numbers[j];
                    numbers[j] = numbers[i] - numbers[j];
                    numbers[i] = numbers[i] - numbers[j];
                }
            }
        }
    }
    else if (option == 2)
    { 
        for (int i = 0; i < 10; i++)
        {
            for (int j = i + 1; j < 10; j++)
            {
                if (numbers[i] < numbers[j])
                {
                    numbers[i] = numbers[i] + numbers[j];
                    numbers[j] = numbers[i] - numbers[j];
                    numbers[i] = numbers[i] - numbers[j];
                }
            }
        }
    }

    for (int i = 0; i < 10; i++)
    {
        printf(" %d ", numbers[i]);
    }
    printf("\n");

    return 0;
}