#include "lists.h"

/**
 * is_palindrome - determine if singly linked list is palindrome
 * @head: pointer to head of singly linked list
 * Return: 0 if not, 1 if palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp = *head;
	unsigned int size = 0, i = 0;
	int *array = (int *)malloc(size * sizeof(int));
	if (head == NULL) 
		return (0);

	if (*head == NULL)
		return (1);

	while (temp)
	{
		temp = temp->next;
		size += 1;
	}
	if (size == 1) 
		return (1);

	temp = *head;
	while (temp) 
	{
		array[i++] = temp->n;
		temp = temp->next;
	}

	for (i = 0; i <= (size/2); i++)
	{
		if (array[i] != array[size - i - 1])
			return (0);
	}
	return (1);
}
