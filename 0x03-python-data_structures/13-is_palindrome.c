#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: double pointer to list.
 *
 *Return: 1 if palindrome, 0 if not palindrom.
 */
int is_palindrome(listint_t **head)
{
  return (check(head, *head));
}

/**
 * checkPalindrome - recursive function ot check if sinly linked list
 * is a palindrome.
 * @headptr: double pointer to list.
 * @tptr: pointer to list.
 *
 * Return: 1 or 0
 */
int check(listint_t **hptr, listint_t *ptr)
{
  int result;

  if (ptr == NULL)
    return (1);
  result = check(hptr, ptr->next) && ((*hptr)->n == ptr->n);
  return (result);
}
