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
    int strcmpret;

    printf("Please enter key: ");
    ret = scanf("%s", buf);
    if (ret != 1) {
        no();
    }
    if (buf[0] != '4' || buf[1] != '2') {
        no();
    }
    memset(pass, 0, 9);
    pass[0] = '*';
    while (i < 8) {
        char tmp[4];
        strncpy(tmp, &buf[chunk], 3);
        tmp[3] = '\0';
        pass[i] = (char)atoi(tmp);
        chunk += 3;
        i++;
    }
    pass[i] = '\0';
    strcmpret = strcmp(pass, "********");
    if (strcmpret == 0) {
        ok();
    } 
    else if (strcmpret == -2) {
        no();
    } 
    else if (strcmpret == -1) {
        no();
    } 
    else if (strcmpret == 1) {
        no();
    }
    else if (strcmpret == 2) {
        no();
    }
    else if (strcmpret == 3) {
        no();
    }
     else if (strcmpret == 4) {
        no();
    }
     else if (strcmpret == 115) { // 0x73
        no();
    }
    else {
        no();
    }

    return 0;
}