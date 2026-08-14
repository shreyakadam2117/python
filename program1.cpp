#include <stdio.h>
#include <string.h>

#define MAX 100

struct Student {
    int roll_no;
    char name[50];
    float marks;
};

void addStudent(struct Student *s, int *count) {
    if (*count >= MAX) {
        printf("Student record is full!\n");
        return;
    }

    printf("\nEnter Roll Number: ");
    scanf("%d", &s[*count].roll_no);

    printf("Enter Name: ");
    scanf(" %[^\n]", s[*count].name);

    printf("Enter Marks: ");
    scanf("%f", &s[*count].marks);

    (*count)++;

    printf("Student added successfully!\n");
}

void displayStudents(struct Student *s, int count) {
    if (count == 0) {
        printf("\nNo student records found.\n");
        return;
    }

    printf("\n--- Student Records ---\n");

    for (int i = 0; i < count; i++) {
        printf("\nRoll Number : %d", s[i].roll_no);
        printf("\nName        : %s", s[i].name);
        printf("\nMarks       : %.2f\n", s[i].marks);
    }
}

void searchStudent(struct Student *s, int count) {
    int roll, found = 0;

    printf("\nEnter Roll Number to search: ");
    scanf("%d", &roll);

    for (int i = 0; i < count; i++) {
        if (s[i].roll_no == roll) {
            printf("\nStudent Found!\n");
            printf("Roll Number : %d\n", s[i].roll_no);
            printf("Name        : %s\n", s[i].name);
            printf("Marks       : %.2f\n", s[i].marks);
            found = 1;
            break;
        }
    }

    if (!found)
        printf("\nStudent not found!\n");
}

int main() {
    struct Student students[MAX];
    int count = 0;
    int choice;

    while (1) {
        printf("\n\n===== STUDENT RECORD SYSTEM =====");
        printf("\n1. Add Student");
        printf("\n2. Display Students");
        printf("\n3. Search Student");
        printf("\n4. Exit");

        printf("\nEnter your choice: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                addStudent(students, &count);
                break;

            case 2:
                displayStudents(students, count);
                break;

            case 3:
                searchStudent(students, count);
                break;

            case 4:
                printf("\nProgram ended.\n");
                return 0;

            default:
                printf("\nInvalid choice!");
        }
    }

    return 0;
}