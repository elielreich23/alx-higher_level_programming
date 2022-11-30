#include "lists.h"

/**
 *insert_node - Inserts a num into a sorted singly-linked list
 *@head: A pointer the head of the linked list
 *@num: The num to insert
 *
 *Return: NULL in case of failure
 *	a pointer to the new mode
 */

listint_t *insert_node(listint_t **head, int num)
{
	listint_t *node = *head, *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = num;

	if (node == NULL || node->n >= num)
	{
		new->next = node;
		*head = new;
		return (new);
	}

	while (node && node->next && node->next->n < num)
		node = node->next;

	new->next = node->next;
	node->next = new;s

	return (new);
}