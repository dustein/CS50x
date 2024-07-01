// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

// TODO: Choose number of buckets in hash table
// aqui sao os buckets para cada letra inicial. Podemos melhorar criando mais buckets
const unsigned int N = 26;
int conta_palavra = 0;

// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO
    // vamos checar o indice usando a funcao hash
    int indice_hash = hash(word);
    // criamos um curso variavel, para percorrer a lista
    // iniciamos apontando o cursos para o head, que é a table na posicao indice_hash
    node *cursor = table[indice_hash];
    // vamos percorrer a lista ate o final, ou seja, ate chegar no NULL que é o seu fim
    while (cursor != 0)
    {
        // checar se a palavra e a mesma encotrada pelo cursos
        if (strcasecmp(word, cursor->word) == 0)
        {
            // se a funcao retornar 0 é porque encontrou a palavra
            return true;
        }
        // se nao for 0, nao encontrou a palavra, passar o cursos para a proxima
        cursor = cursor->next;
    }
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    // A funcao deve receber uma atring e retornar um indice
    // return toupper(word[0]) - 'A';
    unsigned long soma = 0;
    for (int i = 0; i < strlen(word); i++)
    {
        soma += tolower(word[i]);
    }
    return soma % N;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // TODO
    // abrir o arquivo dicionario
    FILE *dicionario = fopen(dictionary, "r");
    if (dicionario == NULL)
    {
        printf("Nao foi possivel abrir %s\n", dictionary);
        return false;
    }
    // ler as strings que tem no arquivo.
    // fscanf vai teronar EOF quando não houver mais string para ler
    char word[LENGTH + 1]; // + 1 porque no final de toda string temos o operador NUL

    while (fscanf(dicionario, "%s", word) != EOF)
    {
        // para fazer uma linked list, temos que criar um node, cuja estrutura é composta por uma
        // palavra e um ponteiro para o próximo node vamos alocar memoria usando a variavel tipo
        // node criada na strut no inicio do codigo
        node *no = malloc(sizeof(node));
        if (no == NULL)
        {
            return false;
        }
        // agora usando strcopy vamos copiar a palavra para o node (word da estruct node)
        strcpy(no->word, word);
        // implementar a função hash trazida no código, que depois vamos melhorar
        // a funcao hash recebe uma string e retorna um indice
        int indice_hash = hash(word);
        no->next = table[indice_hash];
        table[indice_hash] = no;
        conta_palavra++;
    }

    fclose(dicionario);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    // aqui para retornar o tamanho do dicionario é só usarmos o conta_palavras que usamos na funcao
    // load
    return conta_palavra;
}

// Unloads dictionary from memory, returning true if successful, else false

bool unload(void)
{
    // TODO
    for (int i = 0; i < N; i++)
    {
        node *cursor = table[i];
        while (cursor != NULL)
        {
            node *temporario = cursor;
            cursor = cursor->next;
            free(temporario);
        }
    }
    return true;
}
