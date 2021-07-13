#include <stdio.h>
#include <stdlib.h>

typedef struct Node
{
    int data;
    struct Node * next;
}Node;

void dequeue(struct Node **head)
{
    if(!(*head))
    printf("E M P T Y.\n");
    else
    *head = (*head)->next;
}

void pop(struct Node **head)
{
    if(!(*head))
    return;

    struct node *current = *head;
    *head = (*head)->next;
    free(current);
    return;
}

void push(struct Node **head)
{
    struct Node *newNode = (struct Node * )malloc(sizeof(struct Node));
    newNode->next = *head;
    printf("Enter the new element: ");
    scanf("%d", &newNode->data);
    *head = newNode;
}

void enqueue(struct Node **head, struct Node **tail)
{
    struct Node * newNode = (struct Node *)malloc(sizeof(struct Node));
    printf("Enter the data: ");
    scanf("%d", &newNode->data);
    newNode->next = NULL;

    if (!(*head))
    {

        *head = *tail = newNode;
    }
    else
    {
        (*tail)->next = newNode;
        *tail = newNode;
    }
}

void insert(struct Node **head)
{   
    struct Node *new = (struct Node *)malloc(sizeof(struct Node));
    scanf("%d", &new->data);
    new->next = NULL;

    if(!(*head))
    *head = new;
    else
    {
        struct Node *current = *head;
        while (current->next)
        current = current->next;

        current->next = new;
        printf("new\n");
    }
}

void display(struct Node *head)
{
    if (!head)
    {   
        printf("E M P T Y.\n");
        return;
    }
    
    while(head)
    {
        printf("%d->", head->data);
        head = head->next;
    }
}


struct Node * Ddelete(struct Node **head)
{
    int key;
    printf("Enter the value to be del : ");
    scanf("%d", &key);


    struct Node **current = head;
    while((*current)->data != key)
    current = &(*current)->next;

    *current = (*current)->next;
}

struct Node * delete(struct Node *head)
{
    int key;
    printf("Enter the value to be del : ");
    scanf("%d", &key);

    if(key == head->data)
    return head->next;
    else
    {
        struct Node *prev = NULL, *current = head;
        while(current)
        {
            if(current->data == key)
            {
                prev->next = current->next;
                free(current);
                return head;
            }

            prev = current;
            current = current->next;

        }
        printf("Key not found.\n");
        return head;
    }
}

struct Node * Rdelete(struct Node * head, int key)
{
    if(!head)
    {
        printf("Not Found.\n");
        return head;
    }
    else
    {
        if(head->data == key)
        return head->next;

        head->next = Rdelete(head->next, key);
        return head;
    }
}


int main() 
{
    int choice, key;
    struct Node* head = NULL, *tail = NULL;
    // Push(&head);
    // Push(&head);
    // Push(&head);
    // pop(&head);

    do
    {
        printf("Enter your choice : ");
        scanf("%d", &choice);

        switch (choice)
        {
        case 1:
            insert(&head);
            break;
        case 2:
            Ddelete(&head);
            break;
        case 3:
            display(head);
            break;
        case 4:
            pop(&head);

            break;
        default:
            break;
        }
    } while (choice < 5);
    
}
