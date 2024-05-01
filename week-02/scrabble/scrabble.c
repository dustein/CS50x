#include <cs50.h>
#include <stdio.h>
#include <string.h>

int count_score(char *word);

int main(void)
{
    string user1 = get_string("Player 1: ");
    string user2 = get_string("Player 2: ");

    int user1_score = count_score(user1);
    int user2_score = count_score(user2);

    if (user1_score > user2_score)
    {
        printf("Player 1 wins!\n");
    }
    else if (user1_score < user2_score)
    {
        printf("Player 2 wins!\n");
    }
    else
    {
        printf("Tie!\n");
    }
}

int count_score(char *word)
{
    int word_length = strlen(word);

    int count = 0;
    for (int i = 0; i < word_length; i++)
    {
        if (word[i] >= 97)
        {
            word[i] = word[i] - 32;
        }

        if (word[i] == 65 || word[i] == 69 || word[i] == 73 || word[i] == 76 || word[i] == 78 ||
            word[i] == 79 || (word[i] >= 82 && word[i] <= 85))
        {
            count += 1;
        }
        else if (word[i] == 70 || word[i] == 72 || word[i] == 86 || word[i] == 87 || word[i] == 90)
        {
            count += 4;
        }
        else if (word[i] == 66 || word[i] == 67 || word[i] == 77 || word[i] == 80)
        {
            count += 3;
        }
        else if (word[i] == 68 || word[i] == 71)
        {
            count += 2;
        }
        else if (word[i] == 74 || word[i] == 88)
        {
            count += 8;
        }
        else if (word[i] == 81 || word[i] == 90)
        {
            count += 10;
        }
        else if (word[i] == 75)
        {
            count += 5;
        }
    }
    return count;
}