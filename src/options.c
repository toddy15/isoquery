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
 * Return a pointer to the allocated option struct.
 *
 * @return Pointer to allocated option struct.
 */
struct options *options_get_options()
{
    static struct options *opts = NULL;
    if (!opts) {
        opts = g_new0(struct options, 1);
        // Provide default values
        opts->iso = "3166-1";
    }
    return opts;
}

void options_free()
{
    g_free(options_get_options());
}

/**
 * Parse the command line arguments.
 *
 * @param argc Argument count
 * @param argv Array of arguments
 */
void options_parse_command_line(int argc, char *argv[])
{
    GError *error = NULL;
    GOptionContext *context;
    struct options *opts;

    opts = options_get_options();
    context = g_option_context_new("[ISO codes]");

    if (!g_option_context_parse(context, &argc, &argv, &error)) {
        g_print("option parsing failed: %s\n", error->message);
        exit(1);
    }
}
