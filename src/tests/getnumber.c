#include <glib.h>

void test_foo(void)
{
	g_assert(TRUE);
}

int main(int argc, char *argv[])
{
	g_test_init(&argc, &argv, NULL);
	g_test_add_func("/unit/foo", test_foo);
	return g_test_run();
}
