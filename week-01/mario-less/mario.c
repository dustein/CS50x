#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int num;

    do
    {
        num = get_int("Height: ");
    }
    while (num <= 0);

    for (int i = 0; i < num; i++)
    {

        for (int j = 1; j < num - i; j++)
        {
            printf(" ");
        }

        for (int k = 0; k < i + 1; k++)
        {
            printf("#");
        }

        printf("\n");
    }
}
