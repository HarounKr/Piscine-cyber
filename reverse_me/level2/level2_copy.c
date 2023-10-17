#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void no() {
    printf("Nope.\n");
    exit(1);
}

void ok() {
    printf("Good job\n");
    exit(0);
}

int main(void) {
    char pass[9];
    char buf[24];
    int chunk = 2;
    int i = 1;
    int ret;

    printf("Please enter key: ");
    ret = scanf("%s", buf);
    if (ret != 1) {
        no();
    }
    if (buf[0] != '0' || buf[1] != '0') {
        no();
    }
    memset(pass, 0, 9);
    pass[0] = 'd';
    while (i < 8) {
        char tmp[4];
        strncpy(tmp, &buf[chunk], 3);
        tmp[3] = '\0';
        pass[i] = (char)atoi(tmp);
        chunk += 3;
        i++;
    }
    pass[i] = '\0';
    if (strcmp(pass, "delabere") == 0) {
        ok();
    } else {
        no();
    }

    return 0;
}