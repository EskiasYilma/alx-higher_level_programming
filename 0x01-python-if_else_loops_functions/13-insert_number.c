#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: pointer to the head of the list
 * @number: an integer to insert as arguments
 * Return: the address of the new node or NULL if it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node = malloc(sizeof(listint_t));
	listint_t *i = *head;
	listint_t *j = NULL;

	if (new_node == NULL)
	{
		return (NULL);
	}

	new_node->n = number;
	new_node->next = NULL;

	if (*head == NULL)
	{
		*head = new_node;
		return (new_node);
	}


	while (i != NULL && i->n < number)
	{
		j = i;
		i = i->next;
	}

	if (j == NULL)
	{
		new_node->next = *head;
		*head = new_node;
	}
	else
	{
		new_node->next = i;
		j->next = new_node;
	}

	return (new_node);
}
