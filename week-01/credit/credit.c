#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
   long num;
   do
    {
        num = get_long("Number: ");
    }
    while (num < 0);

    long a = num;
    long b = 0;
    int pair = 0;
    int odd = 0;

    for (int i = 0;  i < 16; i++)
    {
        b = a % 10;
        if (b < 0 || b > 9) {
            printf("menor que zero e maior que nove");
        }
        int c = 0;
        if (i % 2 != 0)
        {
            c = b*2;
            if (c > 9)
            {
                c = (c % 10) + (c - c % 10) / 10;
            }
            odd += c;
        }
        else if (i % 2 == 0)
        {
            pair += b;
        }

        a = (a - b) / 10;
    }
    printf("pair: %i odd: %i", pair, odd);
    // 4003600000000014 - nove zeros
    // Multiply every other digit by 2, starting with the number’s second-to-last digit, and then add those products’ digits together.

    // Add the sum to the sum of the digits that weren’t multiplied by 2.

    // If the total’s last digit is 0 (or, put more formally, if the total modulo 10 is congruent to 0), the number is valid!

    //printf("MASTERCARD\n")/
}

int get_card(num)
{
    int count = 0;
    while (num > 0)
    {
        num = num / 10;
        count ++;
    }
    printf("card digitis : %i ", count);

    return 0;
}

