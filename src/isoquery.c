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
#include <locale.h>
#include <json-glib/json-glib.h>
#include "options.h"
#include "isocodes.h"

int main(int argument_count, gchar ** arguments)
{
    GError *error = NULL;
    JsonParser *parser;
    gchar *filename;
    gchar **codes;

    // Set up I18N infrastructure
    // @TODO: Use LOCALEDIR
    bindtextdomain(GETTEXT_PACKAGE, "/usr/share/locale");
    bind_textdomain_codeset(GETTEXT_PACKAGE, "UTF-8");
    textdomain(GETTEXT_PACKAGE);
    setlocale(LC_ALL, "");

    // Parse command line and report possible errors
    if (!options_parse_command_line(arguments, &error)) {
        // TRANSLATORS: This is an error message.
        g_printerr(_("isoquery: %s\n"), error->message);
        if (error->domain == g_quark_from_string("g-option-context-error-quark")) {
            g_printerr(_("Run \"isoquery --help\" to see a full list of available command line options.\n"));
        }
        g_error_free(error);
        return EXIT_FAILURE;
    }
    // Try opening and parsing the given file
    parser = json_parser_new();
    filename = options_get_filename();
    if (!json_parser_load_from_file(parser, filename, &error)) {
        // TRANSLATORS: This is an error message.
        g_printerr(_("isoquery: %s\n"), error->message);
        g_error_free(error);
        g_free(filename);
        g_object_unref(parser);
        return EXIT_FAILURE;
    }
    // The file could be parsed, now see if there's
    // valid iso-codes data in it.
    if (!isocodes_validate(parser, &error)) {
        // TRANSLATORS: This is an error message.
        g_printerr(_("isoquery: %s\n"), error->message);
        g_error_free(error);
        g_free(filename);
        g_object_unref(parser);
        return EXIT_FAILURE;
    }
    // Remove the program name from the arguments and collect
    // remaining arguments as codes to search for.
    codes = &arguments[1];

    // Finally, show the codes
    isocodes_show_codes(parser, filename, codes);

    // Cleanup and exit
    g_free(filename);
    g_object_unref(parser);
    return EXIT_SUCCESS;
}
