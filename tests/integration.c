/**
 * Copyright © 2016 Dr. Tobias Quathamer <toddy@debian.org>
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */

#include <glib.h>
#include <unistd.h>

// Define the path to the executable for integration testing.
#define ISOQUERY_CALL "../src/isoquery", "../src/isoquery", "-p", "data"

/**
 * Test all codes for ISO standard.
 */
void test_integration_all(gconstpointer data)
{
    gchar *standard = (gchar *) data;
    gchar *filename = g_strdup_printf("expected/iso_%s_all.txt", standard);
    gchar *expected_output = NULL;
    GError *error = NULL;
    g_file_get_contents(filename, &expected_output, NULL, &error);
    g_assert_null(error);
    g_assert_nonnull(expected_output);

    if (g_test_subprocess()) {
        execl(ISOQUERY_CALL, "-i", standard, NULL);
        g_free(filename);
        return;
    }
    g_test_trap_subprocess(NULL, 0, 0);
    g_test_trap_assert_passed();
    g_test_trap_assert_stdout(expected_output);
    g_test_trap_assert_stderr("");
    g_free(filename);
}

/**
 * Test all localized codes for ISO standard.
 */
void test_integration_all_localized(gconstpointer data)
{
    gchar *standard = (gchar *) data;
    gchar *filename = g_strdup_printf("expected/iso_%s_all_localized.txt", standard);
    gchar *expected_output = NULL;
    GError *error = NULL;
    g_file_get_contents(filename, &expected_output, NULL, &error);
    g_assert_null(error);
    g_assert_nonnull(expected_output);

    if (g_test_subprocess()) {
        execl(ISOQUERY_CALL, "-i", standard, "-l", "fr", NULL);
        g_free(filename);
        return;
    }
    g_test_trap_subprocess(NULL, 0, 0);
    g_test_trap_assert_passed();
    g_test_trap_assert_stdout(expected_output);
    g_test_trap_assert_stderr("");
    g_free(filename);
}

/**
 * Test all codes for ISO standard, separated by NULL bytes.
 */
void test_integration_all_null_terminated(gconstpointer data)
{
    gchar *standard = (gchar *) data;
    gchar *filename = g_strdup_printf("expected/iso_%s_all_null_separator.txt", standard);
    gchar *expected_output = NULL;
    GError *error = NULL;
    g_file_get_contents(filename, &expected_output, NULL, &error);
    g_assert_null(error);
    g_assert_nonnull(expected_output);

    if (g_test_subprocess()) {
        execl(ISOQUERY_CALL, "-i", standard, "--null", NULL);
        g_free(filename);
        return;
    }
    g_test_trap_subprocess(NULL, 0, 0);
    g_test_trap_assert_passed();
    g_test_trap_assert_stdout(expected_output);
    g_test_trap_assert_stderr("");
    g_free(filename);
}

/**
 * Test invocation without arguments, should be the same as ISO 3166-1.
 */
void test_integration_simple_call(void)
{
    gchar *expected_output = NULL;
    GError *error = NULL;
    g_file_get_contents("expected/iso_3166-1_all.txt", &expected_output, NULL, &error);
    g_assert_null(error);
    g_assert_nonnull(expected_output);

    if (g_test_subprocess()) {
        execl(ISOQUERY_CALL, NULL);
        return;
    }
    g_test_trap_subprocess(NULL, 0, 0);
    g_test_trap_assert_passed();
    g_test_trap_assert_stdout(expected_output);
    g_test_trap_assert_stderr("");
}

/**
 * Test single code on command line
 */
void test_integration_single_code(void)
{
    gchar *expected_output = NULL;
    GError *error = NULL;
    g_file_get_contents("expected/iso_3166-1_single_code.txt", &expected_output, NULL, &error);
    g_assert_null(error);
    g_assert_nonnull(expected_output);

    if (g_test_subprocess()) {
        execl(ISOQUERY_CALL, "TV", NULL);
        return;
    }
    g_test_trap_subprocess(NULL, 0, 0);
    g_test_trap_assert_passed();
    g_test_trap_assert_stdout(expected_output);
    g_test_trap_assert_stderr("");
}

/**
 * Test multiple codes on command line
 */
void test_integration_multiple_codes(void)
{
    gchar *expected_output = NULL;
    GError *error = NULL;
    g_file_get_contents("expected/iso_3166-1_multiple_codes.txt", &expected_output, NULL, &error);
    g_assert_null(error);
    g_assert_nonnull(expected_output);

    if (g_test_subprocess()) {
        execl(ISOQUERY_CALL, "TV", "Deu", "643", "fra", NULL);
        return;
    }
    g_test_trap_subprocess(NULL, 0, 0);
    g_test_trap_assert_passed();
    g_test_trap_assert_stdout(expected_output);
    g_test_trap_assert_stderr("");
}

/**
 * Test multiple invalid codes on command line
 */
void test_integration_invalid_codes(void)
{
    gchar *expected_output = NULL;
    gchar *expected_errors = NULL;
    GError *error = NULL;
    g_file_get_contents("expected/iso_3166-1_multiple_codes.txt", &expected_output, NULL, &error);
    g_assert_null(error);
    g_assert_nonnull(expected_output);
    g_file_get_contents("expected/iso_3166-1_multiple_codes_errors.txt", &expected_errors, NULL, &error);
    g_assert_null(error);
    g_assert_nonnull(expected_errors);

    if (g_test_subprocess()) {
        execl(ISOQUERY_CALL, "TV", "invalid", "öllö", "Deu", "643", "1234", "007", "URG", "fra", NULL);
        return;
    }
    g_test_trap_subprocess(NULL, 0, 0);
    g_test_trap_assert_passed();
    g_test_trap_assert_stdout(expected_output);
    g_test_trap_assert_stderr(expected_errors);
}

/**
 * Test multiple codes localized on command line
 */
void test_integration_multiple_codes_localized(void)
{
    gchar *expected_output = NULL;
    GError *error = NULL;
    g_file_get_contents("expected/iso_3166-1_multiple_codes_localized.txt", &expected_output, NULL, &error);
    g_assert_null(error);
    g_assert_nonnull(expected_output);

    if (g_test_subprocess()) {
        execl(ISOQUERY_CALL, "--locale", "de", "ua", "frA", "158", NULL);
        return;
    }
    g_test_trap_subprocess(NULL, 0, 0);
    g_test_trap_assert_passed();
    g_test_trap_assert_stdout(expected_output);
    g_test_trap_assert_stderr("");
}

/**
 * Test multiple invalid codes localized on command line
 */
void test_integration_invalid_codes_localized(void)
{
    gchar *expected_output = NULL;
    gchar *expected_errors = NULL;
    GError *error = NULL;
    g_file_get_contents("expected/iso_3166-1_multiple_codes_localized.txt", &expected_output, NULL, &error);
    g_assert_null(error);
    g_assert_nonnull(expected_output);
    g_file_get_contents("expected/iso_3166-1_multiple_codes_errors.txt", &expected_errors, NULL, &error);
    g_assert_null(error);
    g_assert_nonnull(expected_errors);

    if (g_test_subprocess()) {
        execl(ISOQUERY_CALL,  "--locale", "de", "invalid", "öllö", "ua", "frA", "158", "1234", "007", "URG", NULL);
        return;
    }
    g_test_trap_subprocess(NULL, 0, 0);
    g_test_trap_assert_passed();
    g_test_trap_assert_stdout(expected_output);
    g_test_trap_assert_stderr(expected_errors);
}

/**
 * Initializing all test functions
 */
int main(int argc, gchar * argv[])
{
    gchar *standards[] = { "639-2", "639-3", "639-5", "3166-1", "3166-2", "3166-3", "4217", "15924", NULL };
    gchar *testpath;
    int i = 0;

    g_test_init(&argc, &argv, NULL);

    // Add common tests for various standards
    while (standards[i]) {
        testpath = g_strdup_printf("/integration/%s/all", standards[i]);
        g_test_add_data_func(testpath, standards[i], test_integration_all);
        g_free(testpath);

        testpath = g_strdup_printf("/integration/%s/all_localized", standards[i]);
        g_test_add_data_func(testpath, standards[i], test_integration_all_localized);
        g_free(testpath);

        testpath = g_strdup_printf("/integration/%s/all_null_terminated", standards[i]);
        g_test_add_data_func(testpath, standards[i], test_integration_all_null_terminated);
        g_free(testpath);

        i++;
    }

    // Add single tests
    g_test_add_func("/integration/simple_call", test_integration_simple_call);
    g_test_add_func("/integration/3166-1/single_code", test_integration_single_code);
    g_test_add_func("/integration/3166-1/multiple_codes", test_integration_multiple_codes);
    g_test_add_func("/integration/3166-1/invalid_codes", test_integration_invalid_codes);
    g_test_add_func("/integration/3166-1/multiple_codes_localized", test_integration_multiple_codes_localized);
    g_test_add_func("/integration/3166-1/invalid_codes_localized", test_integration_invalid_codes_localized);

    return g_test_run();
}
