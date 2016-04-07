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

#include <stdlib.h>
#include <glib.h>
#include "options.h"

/**
 * Global variables to hold the program options.
 */
gchar *option_standard = "3166-1";

/**
 * Define the program command line options.
 */
static GOptionEntry entries[] = {
    {"iso", 'i', 0, G_OPTION_ARG_STRING, &option_standard,
     "ISO standard to use", "NUMBER"},
    {NULL}
};

/**
 * Parse the command line arguments.
 *
 * @param arguments Array of arguments
 */
void options_parse_command_line(gchar ** arguments)
{
    GError *error = NULL;
    GOptionContext *context;

    context = g_option_context_new("[ISO codes]");
    g_option_context_add_main_entries(context, entries, GETTEXT_PACKAGE);

    if (!g_option_context_parse_strv(context, &arguments, &error)) {
        g_print("Option parsing failed: %s\n", error->message);
        exit(1);
    }
}
