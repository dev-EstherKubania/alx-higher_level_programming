#include "lists.h"

/**
 * reverse_list - Reverses a linked list.
 * @head: Pointer to the head of the linked list.
 * Return: Pointer to the new head of the reversed list.
 */
listint_t *reverse_list(listint_t *head)
{
	listint_t *prev = NULL;
	listint_t *current = head;
	listint_t *next;

	while (current != NULL)
	{
	next = current->next;
	current->next = prev;
	prev = current;
	current = next;
	}

	return (prev);
}

/**
 * compare_lists - Compares two linked lists.
 * @list1: Pointer to the first linked list.
 * @list2: Pointer to the second linked list.
 * Return: 1 if the lists are identical, 0 otherwise.
 */
int compare_lists(listint_t *list1, listint_t *list2)
{
	while (list1 != NULL && list2 != NULL)
	{
	if (list1->n != list2->n)
	{
	return (0);
	}
	list1 = list1->next;
	list2 = list2->next;
	}

	return (1);
}

/**
 * is_palindrome - Checks if a linked list is a palindrome.
 * @head: Pointer to the head of the linked list.
 * Return: 1 if the linked list is a palindrome, 0 otherwise.
 */
int is_palindrome(listint_t **head)
{
	if (*head == NULL || (*head)->next == NULL)
	{
	return (1);
	}

	listint_t *tortoise = *head;
	listint_t *hare = *head;
	listint_t *prev_tortoise = *head;
	listint_t *second_half;
	int is_palindrome = 1;

	while (hare != NULL && hare->next != NULL)
	{
	hare = hare->next->next;
	prev_tortoise = tortoise;
	tortoise = tortoise->next;
	}

	if (hare != NULL)
	{
	tortoise = tortoise->next;
	}

	second_half = tortoise;
	prev_tortoise->next = NULL;

	second_half = reverse_list(second_half);
	is_palindrome = compare_lists(*head, second_half);

	second_half = reverse_list(second_half);
	prev_tortoise->next = second_half;

	return (is_palindrome);
}

