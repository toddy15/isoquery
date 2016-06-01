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
#include "isocodes.h"
#include "search.h"
#include "options.h"

/**
 * Search for a given code
 */
void search_entry(gchar * code, GList * entries_list)
{
    // Set up a JSON object for an entry
    JsonObject *entry;
    gchar **normalized_code_and_field = search_get_normalized_code_and_field(code);
    gchar *normalized_code = normalized_code_and_field[0];
    gchar *field = normalized_code_and_field[1];
    GList *list_entry = g_list_first(entries_list);
    // Cycle through all entries
    while (list_entry) {
        entry = json_node_get_object(list_entry->data);
        if (json_object_has_member(entry, field)) {
            if (!g_strcmp0(normalized_code, json_object_get_string_member(entry, field))) {
                isocodes_show_entry(entry);
            }
        }
        list_entry = g_list_next(list_entry);
    }
    g_strfreev(normalized_code_and_field);
}

/**
 * Return the normalized code and field to search in,
 * depending on ISO standard.
 */
gchar **search_get_normalized_code_and_field(gchar * code)
{
    gchar **res;
    gchar *normalized_code;
    gchar *field;
    if (!g_strcmp0("3166-1", option_standard)) {
        // Convert to upper case
        normalized_code = g_utf8_strup(code, -1);
        // Determine which field to use for searching
        if (search_is_number(code)) {
            field = g_strdup("numeric");
        } else if (g_utf8_strlen(normalized_code, -1) == 3) {
            field = g_strdup("alpha_3");
        } else {
            // Default is alpha-2
            field = g_strdup("alpha_2");
        }
        gchar *result[] = { normalized_code, field, NULL };
        res = g_strdupv(result);
    }
    return res;
}

/**
 * Return true if the code is a number
 */
gboolean search_is_number(gchar * code)
{
    gboolean only_digits = TRUE;
    int i = 0;
    gchar *position = code;
    while (*position) {
        if (!g_unichar_isdigit(g_utf8_get_char_validated(position, -1))) {
            only_digits = FALSE;
        }
        position = g_utf8_next_char(position);
    }
    return only_digits;
}
