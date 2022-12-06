#include <stdio.h>
#include "lists.h"

/**
 * is_palindrome - Checks if a singly linked list is a palindrome
 * @head: Start of the linked list
 * Return: 0 if it is not a palindrome and 1 if it is palindrome
 */

int is_palindrome(listint_t **head)
{
	int a[1000];
	int i, j, start, end;
/* store content of each node as we go down and store them in a normal list */
	for (i = 0; (*head)->next != NULL; i++)
	{
		a[i] = (*head)->n;
		(*head) = (*head)->next;
	}
	a[i] = (*head)->n;

/* check if for each element and the corresponding number is equal */
	end = i;
	start = 0;

	for (j = 0; start < i / 2; j++)
	{
		if (a[start] == a[end])
		{
			start++;
			end--;
			continue;
		}
		else
			return (0);
	}

	return (1);
}
