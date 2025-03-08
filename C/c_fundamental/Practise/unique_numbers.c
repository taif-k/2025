#include <stdio.h>

int main()
{
    int numbers[10] = {1, 1, 4, 5, 5, 0, 2, 3, 7, 7};
    int unique[10];
    int counter = 0;

    for (int i = 0; i < 10; i++)
    {
        int match = 0;
        for (int j = i + 1; j < 10; j++)
        {
            if (numbers[i] == numbers[j])
            {
                match = 1;
                break;
            }
        }

        if (match == 1)
        {
            int count = 0;
            for (int k = 0; k < 10; k++)
            {
                if (numbers[i] == unique[k])
                {
                    count = 1;
                    break;
                }
            }
            if (count == 0)
            {
                unique[counter] = numbers[i];
                counter++;
            }
        }
    }

    for (int i = 0; i < 10; i++)
    {
        int match = 0;
        for (int j = 0; j < 10; j++)
        {
            if (numbers[i] == unique[j])
            {
                match = 1;
                break;
            }
        }

        if (match == 0)
        {
            unique[counter] = numbers[i];
            counter++;
        }
    }

    for (int i = 0; i < counter; i++)
    {
        printf(" %d ", unique[i]);
    }

    return 0;
}