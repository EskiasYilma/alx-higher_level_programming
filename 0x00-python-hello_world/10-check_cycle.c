#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list: singly linked list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *a = list;
	listint_t *b = list->next;

	if (list == NULL || list->next == NULL)
	{
		return (0);
	}
	if (list->next == list)
	{
		return (1);
	}

	while (a != NULL && b != NULL && b->next != NULL)
	{
		if (a == b)
		{
			return (1);
		}
		a = a->next;
		b = b->next->next;
	}

	return (0);
}
