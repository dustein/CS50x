#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int count_letters(char *text);
int count_words(char *text);
int count_sentences(char *text);

int main(void)
{
    string user_text = get_string("Text: ");

    int letter_count = count_letters(user_text);
    int word_count = count_words(user_text);
    int sentence_count = count_sentences(user_text);
    double letter_word = ((float) letter_count / word_count) * 100;
    double sentence_word = ((float) sentence_count / word_count) * 100;
    float index = 0.0588 * letter_word - 0.296 * sentence_word - 15.8;
    int index_round = round(index);
    if (index_round < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (index_round >= 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %i\n", index_round);
    }
}

int count_letters(char *text)
{
    int letter_count = 0;
    int text_size = strlen(text);
    int i = 0;
    while (i < text_size)
    {
        if (isalpha(text[i]))
        {
            letter_count++;
        }
        i++;
    }
    return letter_count;
}

int count_words(char *text)
{
    int word_count = 1;
    int text_size = strlen(text);
    int i = 0;
    while (i < text_size)
    {
        char letra = text[i];
        if (text[i] == ' ')
        {
            word_count++;
        }
        i++;
    }
    return word_count;
}

int count_sentences(char *text)
{
    int ponctuation_count = 0;
    int text_size = strlen(text);
    for (int i = 0; i < text_size; i++)
    {
        if (text[i] == '.' || text[i] == '!' || text[i] == '?')
        {
            ponctuation_count++;
        }
    }
    return ponctuation_count;
}
