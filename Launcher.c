#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    char yon[3];
    printf("run CLI or GUI?\n");
    scanf("%s", &yon);
    if (strcmp(yon, "CLI") == 0) {
        system("python Python_Archive_Runner.py");
    } else if (strcmp(yon, "GUI") == 0) {
        system("python Python_Archive_Runnertk.py");
    } else {
        printf("Misson Failed We'll get em' next time!\n");
        system("pause");
    }

    return 0;
}