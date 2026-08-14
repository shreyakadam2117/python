#include <stdio.h>
#include <stdlib.h>

struct Employee
{
    int id;
    char name[30];
    float salary;
    struct Employee *next;
};

struct Employee *head = NULL;

void insert()
{
    struct Employee *newNode, *temp;

    newNode = (struct Employee *)malloc(sizeof(struct Employee));

    printf("Enter ID: ");
    scanf("%d", &newNode->id);

    printf("Enter Name: ");
    scanf("%s", newNode->name);

    printf("Enter Salary: ");
    scanf("%f", &newNode->salary);

    newNode->next = NULL;

    if (head == NULL)
        head = newNode;
    else
    {
        temp = head;

        while (temp->next != NULL)
            temp = temp->next;

        temp->next = newNode;
    }

    printf("Inserted successfully.\n");
}

void deleteEmployee()
{
    int id;
    struct Employee *temp, *prev;

    printf("Enter ID to delete: ");
    scanf("%d", &id);

    temp = head;
    prev = NULL;

    while (temp != NULL && temp->id != id)
    {
        prev = temp;
        temp = temp->next;
    }

    if (temp == NULL)
    {
        printf("Employee not found.\n");
        return;
    }

    if (prev == NULL)
        head = temp->next;
    else
        prev->next = temp->next;

    free(temp);

    printf("Deleted successfully.\n");
}

void search()
{
    int id;
    struct Employee *temp = head;

    printf("Enter ID to search: ");
    scanf("%d", &id);

    while (temp != NULL)
    {
        if (temp->id == id)
        {
            printf("ID: %d\n", temp->id);
            printf("Name: %s\n", temp->name);
            printf("Salary: %.2f\n", temp->salary);
            return;
        }

        temp = temp->next;
    }

    printf("Employee not found.\n");
}

void display()
{
    struct Employee *temp = head;

    if (head == NULL)
    {
        printf("List is empty.\n");
        return;
    }

    while (temp != NULL)
    {
        printf("%d %s %.2f\n",
               temp->id, temp->name, temp->salary);

        temp = temp->next;
    }
}

int main()
{
    int choice;

    do
    {
        printf("\n1.Insert  2.Delete  3.Search  4.Display  5.Exit\n");
        printf("Choice: ");
        scanf("%d", &choice);

        switch (choice)
        {
            case 1:
                insert();
                break;

            case 2:
                deleteEmployee();
                break;

            case 3:
                search();
                break;

            case 4:
                display();
                break;

            case 5:
                printf("Exit.\n");
                break;

            default:
                printf("Invalid choice.\n");
        }

    } while (choice != 5);

    return 0;
}