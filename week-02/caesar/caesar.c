#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

string cipher(string text, int key);
int check_valid(string key);

int main(int argc, string argv[])
{
    if (!argv[1] || argc != 2)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }
    else
    {
        string user_key = argv[1];

        if (check_valid(user_key) == 1)
        {
            return 1;
        }

        int key = atoi(user_key);

        string text = get_string("plaintext: ");
        string response = cipher(text, key);
        printf("ciphertext: %s\n", response);
    }
    return 0;
}

int check_valid(string key)
{
    int key_len = strlen(key);
    for (int i = 0; i < key_len; i++)
    {
        if (key[i] < 48 || key[i] > 57)
        {
            printf("Usage: ./caesar key\n");
            return 1;
        }
    }
    return 0;
}

string cipher(string text, int key)
{
    int text_lenght = strlen(text);

    while (key > 26)
    {
        key -= 26;
    }

    for (int i = 0; i < text_lenght; i++)
    {
        if (text[i] >= 65 & text[i] <= 90)
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
        else if (text[i] >= 97 & text[i] <= 122)
        {
            if (text[i] + key > 122)
            {
                text[i] = key - (122 - text[i]) + 96;
            }
            else
            {
                text[i] = text[i] + key;
            }
        }
    }
    return text;
}
