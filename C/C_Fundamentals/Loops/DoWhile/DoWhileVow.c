#include <stdio.h>

int main()
{
    char input;
    int count = 0;
    do
    {
        count++;
        printf("Enter vowel: ");
        scanf(" %c", &input);

        if (input == 'a' || input == 'i' || input == 'o' || input == 'u' || input == 'e')
        {
            break;
        }

    } while (count < 3);
    return 0;
}
