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
    gchar **command_line = g_strsplit("isoquery", " ", -1);

    options_parse_command_line(command_line);

    g_assert_nonnull(option_standard);
    g_assert_cmpstr(option_standard, ==, "3166-1");
}

/**
 * Test provided value for ISO standard.
 */
void test_opt_standard_provided(void)
{
    gchar **command_line = g_strsplit("isoquery -i 639-2", " ", -1);

    options_parse_command_line(command_line);

    g_assert_nonnull(option_standard);
    g_assert_cmpstr(option_standard, ==, "639-2");
}

int main(int argc, gchar * argv[])
{
    g_test_init(&argc, &argv, NULL);
    g_test_add_func("/options/iso_default", test_opt_standard_default);
    g_test_add_func("/options/iso_provided", test_opt_standard_provided);
    return g_test_run();
}
