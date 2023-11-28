#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * check_cycle -  function in C that checks if a singly
 * linked list has a cycle in it
 * @list: list that contain node
 *
 * Return: 1 if there is cycle and 0 if no cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *fast, *slow;

	if (!list || list->next)
		return (0);
	fast = list;
	slow = list;

	while (slow != NULL && fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
		{
			return (1);
		}
	}
	return (0);
