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
	listint_s *slow, *fast;

	slow = fast = list;

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
		{
			printf("Singly linked list has a circle");
			return (1);
		}
	}
	return (0);
}
