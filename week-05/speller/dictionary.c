// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <strings.h>
#include <string.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

// TODO: Choose number of buckets in hash table
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
    while (cursor != NULL)
    {
        // checar se a palavra e a mesma encotrada pelo cursos
        if(strcasecmp(cursor -> word, word) == 0)
        {
            // se a funcao retornar 0 é porque encontrou a palavra
            return true;
        }
        // se nao for 0, nao encontrou a palavra, passar o cursos para a proxima
        cursor = cursor -> next;
    }
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    return toupper(word[0]) - 'A';
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // TODO
    //abrir o arquivo dicionario
    FILE *dicionario = fopen(dictionary, "r");
    if (dicionario == NULL)
    {
        return false;
    }
    // ler as strings que tem no arquivo.
    //fscanf vai teronar EOF quando não houver mais string para ler
    char palavra[LENGTH + 1]; // + 1 porque no final de toda string temos o operador NUL
    while(fscanf(dicionario, "%s", palavra) != EOF)
    {
        // para fazer uma linked list, temos que criar um node, cuja estrutura é composta por uma palavra e um ponteiro para o próximo node
        // vamos alocar memoria usando a variavel tipo node criada na strut no inicio do codigo
        node *node_alocado = malloc(sizeof(node));
        if (node_alocado == NULL)
        {
            return false;
        }
        // agora usando strcopy vamos copiar a palavra para o node (word da estruct node)
        strcpy(node_alocado -> word, palavra);
        // implementar a função hash trazida no código, que depois vamos melhorar
        // a funcao hash recebe uma string e retorna um indice
        int indice = hash(palavra);
        // fazendo a lista,
        // checar se o header item aponta para NULL, se existe algum item
        if (table[indice] == NULL)
        {
            // nesse caso, vamos inserir o primeiro item, primeiro apontamos o indice para NULL, usando o next definido na estruct
            node_alocado -> next = NULL;
        }
        else
        {
            // ou apontar para o primeiro node da lista
            node_alocado -> next = table[indice];
        }
        // apontar o header para o indice
        table[indice] = node_alocado;

        // vamos contar quantas palavras carregamos conforme lemor o dicionario
        conta_palavra++;
    }

    fclose(dicionario);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    // aqui para retornar o tamanho do dicionario é só usarmos o conta_palavras que usamos na funcao load
    return conta_palavra;
}

// Unloads dictionary from memory, returning true if successful, else false
// funcao auxiliar para liberar memoria dos node no final
void free_node(node *n)
{
    if (n -> next != NULL)
    {
        free_node(n -> next);
    }
    free(n);
}

bool unload(void)
{
    // TODO
    for (int i = 0; i < N; i++)
    {
        if (table[i] != NULL)
        {
            free_node(table[i]);
        }
    }
    return false;
}
