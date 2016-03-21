#include <glib.h>
#include "number.h"

void test_foo(void)
{
	g_assert(TRUE);
}

void test_get_number(void)
{
	int a = get_number();
	g_assert_cmpint(a, ==, 42);
}

int main(int argc, char *argv[])
{
	g_test_init(&argc, &argv, NULL);
	g_test_add_func("/unit/foo", test_foo);
	g_test_add_func("/unit/number", test_get_number);
	return g_test_run();
}
