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
    code_and_field *search = search_get_normalized_code_and_field(code);
    GList *list_entry = g_list_first(entries_list);
    gboolean entry_found = FALSE;
    // Cycle through all entries
    while (list_entry) {
        entry = json_node_get_object(list_entry->data);
        if (json_object_has_member(entry, search->field)) {
            if (!g_strcmp0(search->code, json_object_get_string_member(entry, search->field))) {
                isocodes_show_entry(entry);
                entry_found = TRUE;
                break;
            }
        }
        list_entry = g_list_next(list_entry);
    }
    g_free(search->code);
    g_free(search->field);
    g_free(search);
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
code_and_field *search_get_normalized_code_and_field(gchar * code)
{
    code_and_field *result = g_new(code_and_field, 1);
    // Ensure that the code is valid UTF-8
    if (g_utf8_validate(code, -1, NULL)) {
        result->code = code;
        result->field = g_strdup("code-not-valid");
    }
    if (!g_strcmp0("3166-1", option_standard)) {
        // Convert to upper case
        result->code = g_utf8_strup(code, -1);
        // Determine which field to use for searching
        if (search_is_number(code)) {
            result->field = g_strdup("numeric");
        } else if (g_utf8_strlen(result->code, -1) == 3) {
            result->field = g_strdup("alpha_3");
        } else {
            // Default is alpha-2
            result->field = g_strdup("alpha_2");
        }
    }
    return result;
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
