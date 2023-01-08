#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: a pointer to the head of a singly linked list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *current = *head;
	int *temp, *values = NULL;
	int num_values = 0, i = 0;

	if (*head == NULL)
		return (1);
	values = malloc(sizeof(int));
	if (values == NULL)
		return (0);
	while (current != NULL)
	{
		values[num_values] = current->n;
		num_values++;
		temp = realloc(values, (num_values + 1) * sizeof(int));
		if (temp == NULL)
		{
			free(values);
			return (0);
		}
		values = temp;
		current = current->next;
	}

	for (i = 0; i < num_values / 2; i++)
	{
		if (values[i] != values[num_values - i - 1])
		{
			free(values);
			return (0);
		}
	}
	free(values);
	return (1);
}
