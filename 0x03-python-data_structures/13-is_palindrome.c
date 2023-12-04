#include <stdio.h>
#include <stdlib.h>

/**
 * is_palindrome -  function in C that checks if a singly
 * linked list is a palindrome.
 * @node: node of the element
 * @next: pointer to the next node
 *
 * Return: 0 if successful otherwise 1
 */


listint_t *new_node(int value)
{
	int value;
	listint *next;

	listint_t *node = (listint *) malloc(sizeof(listint_t));

	node->value value;
	node->next = NULL;
	return (node);
}

void push(listint_t **head, int value)
{
	listint_t *node = new_node(value);

	node->next = *head;
	*head = node;
}

int is_palindrome(listint_t **head)
{
	if (*head == NULL)
	{
		return (1);
	}
	listint_t *prev = NULL;
	listint_t *slow = *head;
	listint_t *fast = *head;

	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		listint_t *temp = slow;

		slow = slow->next;
		temp->next = prev;
		prev = temp;
	}
	listint_t *middle = slow;

	while (middle != NULL)
	{
		if (middle->value != (*head)->value)
		{
			return (0);
		}
		middle = middle->next;
		*head = (*head)->next;
	}
	return (1);
}

int main(void)
{
	listint_t *head = NULL;

	push(&head, 1);
	push(&head, 2);
	push(&head, 3);
	push(&head, 2);
	push(&head, 1);

	if (is_palindrome(&head))
	{
		printf("The list is a palindrome.\n");
	}
	else
	{
		printf("The list is not a palindrome.\n");
	}
	return (0);
}
