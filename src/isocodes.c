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
#include "isocodes.h"
#include "options.h"

/**
 * Validate the given JSON data.
 */
gboolean isocodes_validate(JsonParser * parser, GError ** error)
{
    // Get the root node
    JsonNode *root = json_parser_get_root(parser);
    // Ensure that there is a root element
    if (root == NULL) {
        isocodes_set_validation_error(error);
        return FALSE;
    }
    // Ensure that the root element is an object
    if (g_strcmp0(json_node_type_name(root), "JsonObject")) {
        isocodes_set_validation_error(error);
        return FALSE;
    }
    // Get the root object
    JsonObject *root_object = json_node_get_object(root);
    // Ensure that the root object has only one member
    if (json_object_get_size(root_object) != 1) {
        isocodes_set_validation_error(error);
        return FALSE;
    }
    // The root object must have the standard as only member
    if (!json_object_has_member(root_object, option_standard)) {
        isocodes_set_validation_error(error);
        return FALSE;
    }
    return TRUE;
}

/**
 * Helper function to set the GError
 */
void isocodes_set_validation_error(GError ** error)
{
    // TRANSLATORS:
    // The first placeholder is a filename, including the directory path.
    // The second placeholder is an ISO standard, e.g. 3166-1 or 639-3.
    g_set_error(error, g_quark_from_string(GETTEXT_PACKAGE), 0,
                _("The file \"%s\" does not contain valid ISO %s data."), options_get_filename(), option_standard);
}

/**
 * Show codes from ISO standard
 */
void isocodes_show_codes(JsonParser * parser, gchar * filename, gchar ** codes)
{
    // Get the root node, object, and entries array
    JsonNode *root = json_parser_get_root(parser);
    JsonObject *root_object = json_node_get_object(root);
    JsonNode *standard = json_object_get_member(root_object, option_standard);
    JsonArray *entries_array = json_node_get_array(standard);
    GList *entries_list = json_array_get_elements(entries_array);
    GList *list_entry = g_list_first(entries_list);

    // Set up a JSON object for an entry
    JsonObject *entry;
    // Show all entries
    while (list_entry) {
        entry = json_node_get_object(list_entry->data);
        g_printf("Alpha-2: %s\n", json_object_get_string_member(entry, "alpha_2"));
        list_entry = g_list_next(list_entry);
    }
    // Are there any codes?
    int i = 0;
    while (codes[i]) {
        g_printf("Given code: %s\n", codes[i]);
        i++;
    }

    g_list_free(entries_list);
}
