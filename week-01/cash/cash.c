#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int change;
    do
    {
        change = get_int("Change owed (cents): ");
    }
    while (change < 0);

    int coins, count = 0;

    // printf("Atual coins: %i\n", count);
    // .25 .10 .5 .1
    if (change >= 25)
    {
        coins = change / 25;
        count += coins;
        change = change - (coins * 25);
        // printf("coins of 25: %i change: %i\n", coins, change);
        // printf("Atual coins: %i\n", count);
    }
    if (change < 25 && change >= 10)
    {
        coins = change / 10;
        count += coins;
        change = change - (coins * 10);
        // printf("coins of 10: %i change: %i\n", coins, change);
        // printf("Atual coins: %i\n", count);
    }
    if (change < 10 && change >= 5)
    {
        coins = change / 5;
        count += coins;
        change = change - (coins * 5);
        // printf("coins of 5: %i change: %i\n", coins, change);
        // printf("Atual coins: %i\n", count);
    }
    if (change < 5)
    {
        coins = change / 1;
        count += coins;
        change = change - (coins * 1);
        // printf("coins of 1: %i change: %i\n", coins, change);
        // printf("Atual coins: %i\n", count);
    }
    printf("%i\n", count);
}
