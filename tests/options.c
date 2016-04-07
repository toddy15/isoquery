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
#include "options.h"

/**
 * Test default value for ISO standard.
 */
void test_opt_standard_default(void)
{
    GError *error = NULL;
    gboolean result = FALSE;

    gchar **command_line = g_strsplit("isoquery", " ", -1);
    result = options_parse_command_line(command_line, &error);
    g_strfreev(command_line);

    g_assert_true(result);
    g_assert_null(error);
    g_assert_nonnull(option_standard);
    g_assert_cmpstr(option_standard, ==, "3166-1");
}

/**
 * Test provided value for ISO standard.
 */
void test_opt_standard_provided(void)
{
    GError *error = NULL;
    gboolean result = FALSE;

    gchar **command_line = g_strsplit("isoquery -i 639-2", " ", -1);
    result = options_parse_command_line(command_line, &error);
    g_strfreev(command_line);

    g_assert_true(result);
    g_assert_null(error);
    g_assert_nonnull(option_standard);
    g_assert_cmpstr(option_standard, ==, "639-2");
}

/**
 * Test obsolete provided value for ISO standard.
 */
void test_opt_standard_obsolete_639(void)
{
    GError *error = NULL;
    gboolean result = FALSE;

    gchar **command_line = g_strsplit("isoquery -i 639", " ", -1);
    result = options_parse_command_line(command_line, &error);
    g_strfreev(command_line);

    g_assert_true(result);
    g_assert_null(error);
    g_assert_nonnull(option_standard);
    g_assert_cmpstr(option_standard, ==, "639-2");
}

/**
 * Test obsolete provided value for ISO standard.
 */
void test_opt_standard_obsolete_3166(void)
{
    GError *error = NULL;
    gboolean result = FALSE;

    gchar **command_line = g_strsplit("isoquery -i 3166", " ", -1);
    result = options_parse_command_line(command_line, &error);
    g_strfreev(command_line);

    g_assert_true(result);
    g_assert_null(error);
    g_assert_nonnull(option_standard);
    g_assert_cmpstr(option_standard, ==, "3166-1");
}

/**
 * Test default value for filename.
 */
void test_opt_filename_default(void)
{
    GError *error = NULL;
    gboolean result = FALSE;

    gchar **command_line = g_strsplit("isoquery", " ", -1);
    result = options_parse_command_line(command_line, &error);
    g_strfreev(command_line);

    g_assert_true(result);
    g_assert_null(error);
    g_assert_nonnull(option_filename);
    g_assert_cmpstr(option_filename, ==, "/usr/share/iso-codes/json/iso_3166-1.json");
}

/**
 * Test provided value for filename.
 */
void test_opt_filename_provided(void)
{
    GError *error = NULL;
    gboolean result = FALSE;

    gchar **command_line = g_strsplit("isoquery -f /path/to/another_filename", " ", -1);
    result = options_parse_command_line(command_line, &error);
    g_strfreev(command_line);

    g_assert_true(result);
    g_assert_null(error);
    g_assert_nonnull(option_filename);
    g_assert_cmpstr(option_filename, ==, "/path/to/another_filename");
}

/**
 * Test default value for filename from other standard.
 */
void test_opt_filename_from_standard(void)
{
    GError *error = NULL;
    gboolean result = FALSE;

    gchar **command_line = g_strsplit("isoquery -i 15924", " ", -1);
    result = options_parse_command_line(command_line, &error);
    g_strfreev(command_line);

    g_assert_true(result);
    g_assert_null(error);
    g_assert_nonnull(option_standard);
    g_assert_cmpstr(option_standard, ==, "15924");
    g_assert_nonnull(option_filename);
    g_assert_cmpstr(option_filename, ==, "/usr/share/iso-codes/json/iso_15924.json");
}

/**
 * Test invalid option.
 */
void test_opt_invalid_option(void)
{
    GError *error = NULL;
    gboolean result = FALSE;

    gchar **command_line = g_strsplit("isoquery -t", " ", -1);
    result = options_parse_command_line(command_line, &error);
    g_strfreev(command_line);

    g_assert_false(result);
    g_assert_nonnull(error);
    g_assert_cmpint(error->code, ==, G_OPTION_ERROR_UNKNOWN_OPTION);
}

int main(int argc, gchar * argv[])
{
    g_test_init(&argc, &argv, NULL);
    g_test_add_func("/options/standard_default", test_opt_standard_default);
    g_test_add_func("/options/standard_provided", test_opt_standard_provided);
    g_test_add_func("/options/standard_obsolete_639", test_opt_standard_obsolete_639);
    g_test_add_func("/options/standard_obsolete_3166", test_opt_standard_obsolete_3166);
    g_test_add_func("/options/filename_default", test_opt_filename_default);
    g_test_add_func("/options/filename_provided", test_opt_filename_provided);
    g_test_add_func("/options/filename_from_standard", test_opt_filename_from_standard);
    g_test_add_func("/options/invalid_option", test_opt_invalid_option);
    return g_test_run();
}
