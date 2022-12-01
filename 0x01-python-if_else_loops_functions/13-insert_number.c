#include "lists.h"
#include <stdlib.h>

/*
 * insert_node - insert a number into a sorted singly linked list
 * @head: head pointer
 * @number: value to insert
 *
 * Return: the address of the new node, or NULL if it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	unsigned int i = 0;
	listint_t *new, *hold = *head;

	if (!(hold) || (*hold).n > number)
	{
		new = malloc(sizeof(listint_t));
		if (!new)
			return (NULL);

		(*new).n = number;
		(*new).next = *head;

		*head = new;

		return (*head);
	}

	while (hold)
	{
		if (!((*hold).next) || (*hold).next->n > number)
		{
			new = malloc(sizeof(listint_t));
			if (!new)
				return (NULL);
			(*new).n = number;
			(*new).next = (*hold).next;
			(*hold).next = new;
			return (new);
		}
		hold = (*hold).next;
		i++;
	}

	return (NULL);
}
