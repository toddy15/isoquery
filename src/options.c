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
#include <glib/gprintf.h>
#include "options.h"

/**
 * Global variables to hold the program options.
 */
gchar *option_standard;
gchar *option_pathname;
gchar *option_namefield;
gchar *option_locale;
gboolean *option_null_separator;
gboolean *option_version;

// Helper variables, not to be accessed directly.
gboolean *option_name;
gboolean *option_officialname;
gboolean *option_commonname;

/**
 * Define the program command line options.
 */
static GOptionEntry entries[] = {
    {"iso", 'i', G_OPTION_FLAG_NONE, G_OPTION_ARG_STRING, &option_standard,
     N_
     ("The ISO standard to use. Possible values: 639-2, 639-3, 639-5, 3166-1, 3166-2, 3166-3, 4217, 15924 (default: 3166-1)"),
     N_("STANDARD")},
    {"pathname", 'p', G_OPTION_FLAG_NONE, G_OPTION_ARG_FILENAME, &option_pathname,
     N_("Use pathname as prefix for the data files (default: /usr/share/iso-codes/json)"),
     N_("PATHNAME")},
    {"locale", 'l', G_OPTION_FLAG_NONE, G_OPTION_ARG_STRING, &option_locale,
     N_("Use this locale for output"),
     N_("LOCALE")},
    {"name", 'n', G_OPTION_FLAG_NONE, G_OPTION_ARG_NONE, &option_name,
     N_("Name for the supplied codes (default)"), NULL},
    {"official_name", 'o', G_OPTION_FLAG_NONE, G_OPTION_ARG_NONE, &option_officialname,
     N_("Official name for the supplied codes. This may be the same as --name (only applies to ISO 3166-1)"),
     NULL},
    {"common_name", 'c', G_OPTION_FLAG_NONE, G_OPTION_ARG_NONE, &option_commonname,
     N_("Common name for the supplied codes. This may be the same as --name (only applies to ISO 3166-1)"), NULL},
    {"null", '0', G_OPTION_FLAG_NONE, G_OPTION_ARG_NONE, &option_null_separator,
     N_("Separate entries with a NULL character instead of newline"), NULL},
    {"version", 'v', G_OPTION_FLAG_NONE, G_OPTION_ARG_NONE, &option_version,
     N_("Show program version and copyright"), NULL},
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
    option_pathname = "/usr/share/iso-codes/json";
    option_namefield = "name";
    option_locale = "";
    option_null_separator = FALSE;
    option_version = FALSE;
}

/**
 * Validate values of options.
 */
gboolean options_validate(GError ** error)
{
    // Handle deprecated standards gracefully
    if (!g_strcmp0("3166", option_standard)) {
        option_standard = "3166-1";
        // Print a small warning
        g_printerr("isoquery: The standard 3166 is deprecated, please use 3166-1 instead.\n");
    }
    if (!g_strcmp0("639", option_standard)) {
        option_standard = "639-2";
        // Print a small warning
        g_printerr("isoquery: The standard 639 is deprecated, please use 639-2 instead.\n");
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
        // TRANSLATORS: The placeholder is a string like "1234-5".
        g_set_error(error, g_quark_from_string(GETTEXT_PACKAGE), 0, _("ISO standard \"%s\" is not supported."),
                    option_standard);
        return FALSE;
    }
    // Set the value for the name field
    if (option_officialname) {
        option_namefield = "official_name";
    }
    if (option_commonname) {
        option_namefield = "common_name";
    }
    return TRUE;
}

/**
 * Construct the filename for JSON data, given the pathname and ISO standard.
 *
 * @return gchar * Filename, has to be free'd by the caller.
 */
gchar *options_get_filename(void)
{
    gchar *filename, *complete_path;
    filename = g_strdup_printf("iso_%s.json", option_standard);
    complete_path = g_build_filename(option_pathname, filename, NULL);
    g_free(filename);
    return complete_path;
}

/**
 * Show program version and copyright
 */
void options_show_version(void)
{
    // TRANSLATORS: The placeholder is the version identifier.
    g_printf(_("isoquery %s\n"), VERSION);
    g_printf(_("Copyright © 2007-2016 Dr. Tobias Quathamer\n"));
    // TRANSLATORS: Please change the uppercase words as
    // appropriate for your language.
    gchar *translation = _("Translation to LANGUAGE Copyright © YEAR YOUR-NAME\n");
    if (!g_strrstr(translation, "LANGUAGE")) {
        g_printf("%s", translation);
    }
    g_print("\n");
    g_print("This program is free software: you can redistribute it and/or modify\n");
    g_print("it under the terms of the GNU General Public License as published by\n");
    g_print("the Free Software Foundation, either version 3 of the License, or\n");
    g_print("(at your option) any later version.\n");
    g_print("\n");
    g_print("This program is distributed in the hope that it will be useful,\n");
    g_print("but WITHOUT ANY WARRANTY; without even the implied warranty of\n");
    g_print("MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the\n");
    g_print("GNU General Public License for more details.\n");
    g_print("\n");
    g_print("You should have received a copy of the GNU General Public License\n");
    g_print("along with this program.  If not, see <http://www.gnu.org/licenses/>.\n");
}
