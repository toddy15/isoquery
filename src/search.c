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
#include <glib/gi18n.h>
#include "isocodes.h"
#include "search.h"
#include "options.h"

/**
 * Search for a given code
 */
gboolean search_entry(gchar * code, GList * entries_list, GError ** error)
{
    // Set up a JSON object for an entry
    JsonObject *entry;
    // Set up fields in which to search
    gchar *fields[] = { "alpha_2", "alpha_3", "alpha_4", "numeric", "code", "bibliographic", NULL };
    gchar *normalized_code = search_get_normalized_code(code);
    GList *list_entry = g_list_first(entries_list);
    gboolean entry_found = FALSE;
    // Cycle through all entries
    while (list_entry) {
        entry = json_node_get_object(list_entry->data);
        int i = 0;
        while (fields[i]) {
            if (json_object_has_member(entry, fields[i])) {
                if (!g_strcmp0(normalized_code, json_object_get_string_member(entry, fields[i]))) {
                    isocodes_show_entry(entry);
                    entry_found = TRUE;
                    break;
                }
            }
            i++;
        }
        if (entry_found) {
            break;
        }
        list_entry = g_list_next(list_entry);
    }
    g_free(normalized_code);
    if (!entry_found) {
        // TRANSLATORS: The first placeholder is a code like "urgl" or
        // "does-not-exist", the second placeholder is the current
        // ISO standard like "3166-1" or "15924".
        g_set_error(error, g_quark_from_string(GETTEXT_PACKAGE), 0, _("The code \"%s\" is not defined in ISO %s."),
                    code, option_standard);
    }
    return entry_found;
}

/**
 * Return the normalized code and field to search in,
 * depending on ISO standard.
 */
gchar *search_get_normalized_code(gchar * code)
{
    gchar *normalized_code;
    if (!g_strcmp0("639-2", option_standard)) {
        // Convert to lower case
        normalized_code = g_utf8_strdown(code, -1);
    } else if (!g_strcmp0("3166-1", option_standard)) {
        // Convert to upper case
        normalized_code = g_utf8_strup(code, -1);
    }
    return normalized_code;
}
