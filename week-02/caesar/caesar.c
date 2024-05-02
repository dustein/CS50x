#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

string cipher(string text, int key);

int main(int argc, string argv[])
{
    if (!argv[1] || argc != 2)
    {
        printf("nao argv ou mais de um\n");
        return 1;
    }
    else
    {
        string user_key = argv[1];
        int key = atoi(user_key);

        if (key == 0)
        {
            printf("key must be a number\n");
            return 1;
        }

        string text = get_string("plaintext: ");
        string response = cipher(text, key);
        printf("ciphertext: %s\n", response);
    }
    return 0;
}

string cipher( string text, int key)
{
    int text_lenght = strlen(text);

    if (key > 26)
    {
        key -= 26;
    }

    for (int i = 0; i < text_lenght; i++)
    {
        int maiusculas = text[i] >= 65 & text[i] <= 90;
        int minusculas = text[i] >= 97 & text[i] <= 122;
        if (maiusculas)
        {
            if (text[i] + key > 90)
            {
                text[i] = key - (90 - text[i]) + 64;
            }
            else
            {
                text[i] = text[i] + key;
            }
        }
        else if (minusculas)
        {
            text[i] = key - (122 - text[i]) + 96;
        }
        else
        {
            text[i] = text[i] + key;
        }
    }
    return text;
}


// :( encrypts "barfoo" as "yxocll" using 23 as key
    // output not valid ASCII text
// :) encrypts "BARFOO" as "EDUIRR" using 3 as key
// :) encrypts "BaRFoo" as "FeVJss" using 4 as key
// :( encrypts "barfoo" as "onesbb" using 65 as key
    // output not valid ASCII text
// :( encrypts "world, say hello!" as "iadxp, emk tqxxa!" using 12 as key
    // output not valid ASCII text
// :( handles non-numeric key
    // timed out while waiting for program to exit
