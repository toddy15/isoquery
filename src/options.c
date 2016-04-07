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
gchar *option_standard;
gchar *option_filename;

/**
 * Define the program command line options.
 */
static GOptionEntry entries[] = {
    {"iso", 'i', 0, G_OPTION_ARG_STRING, &option_standard,
     N_
     ("The ISO standard to use. Possible values: 639-2, 639-3, 639-5, 3166-1, 3166-2, 3166-3, 4217, 15924 (default: 3166-1)."),
     N_("STANDARD")},
    {"filename", 'f', 0, G_OPTION_ARG_FILENAME, &option_filename,
     N_("Use another JSON file with ISO data (default: /usr/share/iso-codes/json/iso_3166-1.json)"),
     N_("FILE")},
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
    GOptionContext *context;

    // Ensure that there are sensible default options.
    options_set_default_values();

    context = g_option_context_new(_("[ISO codes]"));
    g_option_context_add_main_entries(context, entries, GETTEXT_PACKAGE);

    // Count the number of arguments supplied.
    while (arguments[argc] != NULL) {
        argc++;
    }
    // If the parsing fails, return with error.
    if (!g_option_context_parse(context, &argc, &arguments, error)) {
        return FALSE;
    }
    // Validate options
    if (!options_validate(error)) {
        return FALSE;
    }
    return TRUE;
}

/**
 * Set default values for options.
 */
void options_set_default_values(void)
{
    option_standard = "3166-1";
    g_free(option_filename);
    option_filename = NULL;
}

/**
 * Validate values of options.
 */
gboolean options_validate(GError ** error)
{
    // Handle obsolete standards gracefully
    if (!g_strcmp0("3166", option_standard)) {
        option_standard = "3166-1";
    }
    if (!g_strcmp0("639", option_standard)) {
        option_standard = "639-2";
    }
    // Check that the given standard is supported
    int i = 0;
    gboolean supported = FALSE;
    gchar *supported_standards[] = { "639-2", "639-3", "639-5", "3166-1", "3166-2", "3166-3", "4217", "15924", NULL };
    while (supported_standards[i]) {
        if (!g_strcmp0(supported_standards[i], option_standard)) {
            supported = TRUE;
            break;
        }
        i++;
    }
    if (!supported) {
        g_set_error(error, g_quark_from_string(GETTEXT_PACKAGE), 0, "ISO standard \"%s\" is not supported.",
                    option_standard);
        return FALSE;
    }
    // Ensure the correct filename for the standard
    if (!option_filename) {
        option_filename = g_strdup_printf("/usr/share/iso-codes/json/iso_%s.json", option_standard);
    }
    return TRUE;
}
