#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: a pointer to the head of a singly linked list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *current = *head;
	int values[1000];
	int num_values = 0, i = 0;

	if (*head == NULL)
	{
		return (1);
	}

	while (current != NULL)
	{
		values[num_values] = current->n;
		num_values++;
		current = current->next;
	}

	for (i = 0; i < num_values / 2; i++)
	{
		if (values[i] != values[num_values - i - 1])
		{
			return (0);
		}
	}

	return (1);
}
