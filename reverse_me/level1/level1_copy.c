#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main() {
    int ret;
    char buf[100];

    char *pass = strdup("__stack_check");
    printf("Please enter key: ");
    scanf("%s", buf);
    ret = strcmp(pass, buf);
    if (ret == 0) {
        printf("Good job.\n");
    }
    else {
        printf("Nope.\n");
    }
    free(pass);
    return 0;
}