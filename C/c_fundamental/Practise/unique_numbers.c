#include <stdio.h>

void unique_numbers(int numb[10], char uniq[10]);

int main()
{
    int numbers[10] = {1, 1, 4, 5, 5, -1, 2, 3, -1, 7};
    char unique[10];

    unique_numbers(numbers, unique);
    return 0;
}

void unique_numbers(int numb[10], char uniq[10])
{
    int counter = 0;
    for (int i = 0; i < 10; i++)
    {
        int match = 0;
        for (int j = i + 1; j < 10; j++)
        {
            if (numb[i] == numb[j])
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
                if (numb[i] == numb[k])
                {
                    count = 1;
                    break;
                }
            }
            if (count == 0)
            {
                uniq[counter] = numb[i];
                counter++;
            }
        }
    }

    for (int i = 0; i < 10; i++)
    {
        int match = 0;
        for (int j = 0; j < 10; j++)
        {
            if (numb[i] == uniq[j])
            {
                match = 1;
                break;
            }
        }

        if (match == 0)
        {
            uniq[counter] = numb[i];
            counter++;
        }
    }

    for (int i = 0; i < counter; i++)
    {
        printf(" %d ", uniq[i]);
    }
}