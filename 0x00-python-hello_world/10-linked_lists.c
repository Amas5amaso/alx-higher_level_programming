#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * check_cycle - check if a singly-linked list contains a cycle
 * @list: A singly-linked list
 *
 * Return: if there is no cycle 0 or -1 if there is cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	if (list == NULL || list->next == NULL)
		return (0);

	slow = list->next;
	fast = list->next->next;

	while (slow && fast && fast->next)
	{
		if (slow == fast)
			return (1);

		slow = slow->next;
		fast = fast->next;
	}
	return (0);
}
