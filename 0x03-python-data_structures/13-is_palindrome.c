#include "lists.h"

/**
 * is_palindrome - finds if linked list is palindrome
 * @head: head of linked list
 *
 * Description: checks all 'n' values in singly linked list
 *
 * Return: 0 if not pilindrome, 1 if it is
 */

int is_palindrome(listint_t **head)
{
	listint_t *mover, *front, *back, *half;
	int count = 0, move = 0;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	front = *head;
	back = *head;
	half = *head;

	while (back->next != NULL)
	{
		count++;
		back = back->next;
	}
	while (move < count)
	{
		half = half->next;
		move++;
		count--;
	}

	mover = half;

	while (front != back)
	{
		if (front->n != back->n)
			return (0);
		if (front->next == back)
			return (1);
		while (mover->next != back)
			mover = mover->next;
		back = mover;
		front = front->next;
		mover = half;
	}

	return (1);
}
