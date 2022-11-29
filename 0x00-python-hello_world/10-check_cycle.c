#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle
 * @list: head of linked list
 *
 * Return: 0 if no circle
 * 1 if circle
 */

int check_cycle(listint_t *list)
{
	listint_s *temp = list;

	while (temp)
	{
		temp = temp->next;
		if (temp == list)
		{
			printf("Singly linked list has a circle");
			return (1);
		}
	}
	return (0);
}
