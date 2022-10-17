#include <stdio.h>

void black() {
    printf("\033[0;30m");
}
void black_bold() {
    printf("\033[1;30m");
}

void blue() {
    printf("\033[0;34m");
}
void blue_bold() {
    printf("\033[1;34m");
}

void cyan() {
    printf("\033[0;36m");
}
void cyan_bold() {
    printf("\033[1;36m");
}

void green() {
    printf("\033[0;32m");
}
void green_bold() {
    printf("\033[1;32m");
}

void purple() {
    printf("\033[0;35m");
}
void purple_bold() {
    printf("\033[1;35m");
}

void red() {
    printf("\033[0;31m");
}
void red_bold() {
    printf("\033[1;31m");
}

void white() {
    printf("\033[0;37m");
}
void white_bold() {
    printf("\033[1;37m");
}

void yellow() {
    printf("\033[0;33m");
}
void yellow_bold() {
    printf("\033[1;33m");
}

void reset() {
    printf("\033[0m");
}

int main() {
    red();
    printf("Hello ");
    yellow();
    printf("world\n");
    reset();
    return 0;
}
