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
#include "isocodes.h"
#include "options.h"

/**
 * Validate the given JSON data.
 */
gboolean isocodes_validate(JsonParser * parser, GError ** error)
{
    // Get the root node
    JsonNode *root = json_parser_get_root(parser);
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
    // The second placeholder is an ISO standard, e.g. 3166 or 639-3.
    g_set_error(error, g_quark_from_string(GETTEXT_PACKAGE), 0,
                _("The file \"%s\" does not contain valid ISO %s data."), option_filename, option_standard);
}
