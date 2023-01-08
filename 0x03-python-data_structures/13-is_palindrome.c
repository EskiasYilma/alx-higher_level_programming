#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: a pointer to the head of a singly linked list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *current;
	listint_t *reversed;
	listint_t *next;

	current = *head;
	reversed = NULL;

	if (*head == NULL)
	{
		return (1);
	}

	while (current != NULL)
	{
		next = current->next;
		current->next = reversed;
		reversed = current;
		current = next;
	}

	current = *head;
	while (current != NULL)
	{
		if (current->n != reversed->n)
		{
			return (0);
		}
		current = current->next;
		reversed = reversed->next;
	}

	return (1);
}
