#include <stdio.h>

int main()
{
    int array[5] = {3, 3, 3, 4, 4};
    int duplicate[5] = {0, 0, 0, 0, 0};  // 3  4
    int counter = 0;

    for (int i = 0; i < 5; i++) // 3  3  3  4  4
    {
        int match = 0;
        for (int j = i + 1; j < 5; j++) // 3  3  4 4
        {
            if (array[i] == array[j])
            {
                match = 1;
                break;
            }
        }

        if (match == 1)
        {
            int count = 0;
            for (int k = 0; k < 5; k++)
            {
                if (array[i] == duplicate[k])
                {
                    count = 1;
                    break;
                }
            }

            if (count == 0)
            {
                duplicate[counter] = array[i];
                counter++;
            }
        }
    }

    for (int i = 0; i < counter; i++)
    {
        printf(" %d ", duplicate[i]);
    }

    return 0;
}