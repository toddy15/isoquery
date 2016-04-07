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

#include <stdio.h>
#include <glib.h>
#include <glib/gi18n.h>
#include <libintl.h>
#include "options.h"

int main(int argument_count, gchar ** arguments)
{
    GError *error = NULL;

    // Set up I18N infrastructure
    bindtextdomain(GETTEXT_PACKAGE, "/usr/share/locale");
    bind_textdomain_codeset(GETTEXT_PACKAGE, "UTF-8");
    textdomain(GETTEXT_PACKAGE);
    setlocale(LC_ALL, "");

    // Parse command line and report possible errors
    if (!options_parse_command_line(arguments, &error)) {
        // TRANSLATORS: This is an error message.
        fprintf(stderr, _("isoquery: %s\n"), error->message);
        fprintf(stderr, _("Run \"isoquery --help\" to see a full list of available command line options.\n"));
        g_error_free(error);
        return 1;
    }

    return 0;
}
