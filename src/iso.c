#include <stdio.h>
#include <glib.h>
#include "number.h"

int main(int argc, char* argv[])
{
	int a = get_number();
	printf("The value of 'a' is now %d.\n", a);
	return 0;
}
