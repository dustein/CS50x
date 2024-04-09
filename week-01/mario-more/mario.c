#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int num;
    do
    {
        num = get_int("Height: ");
    }
    while (num <= 0 || num > 8);

    for (int i = 1; i < num + 1; i++)
    {

        for (int j = num - i; j > 0; j--)
        {
            printf(" ");
        }

        for (int l = i; l > 0; l--)
        {
            printf("#");
        }

        printf("  ");

        for (int l = i; l > 0; l--)
        {
            printf("#");
        }

        printf("\n");
    }
}
