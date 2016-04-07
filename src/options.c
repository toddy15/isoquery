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
#include <glib/gi18n.h>
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
     N_
     ("The ISO standard to use. Possible values: 639-2, 639-3, 639-5, 3166-1, 3166-2, 3166-3, 4217, 15924 (default: 3166-1)."),
     N_("STANDARD")},
    {NULL}
};

/**
 * Parse the command line arguments.
 *
 * @param arguments Array of arguments
 */
gboolean options_parse_command_line(gchar ** arguments, GError ** error)
{
    int argc;
    gboolean result;
    GOptionContext *context;

    context = g_option_context_new(_("[ISO codes]"));
    g_option_context_add_main_entries(context, entries, GETTEXT_PACKAGE);

    // Count the number of arguments supplied.
    while (arguments[argc] != NULL) {
        argc++;
    }
    result = g_option_context_parse(context, &argc, &arguments, error);
    return result;
}
