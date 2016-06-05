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
#include <locale.h>
#include "isocodes.h"
#include "options.h"
#include "search.h"

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
    g_set_error(error, g_quark_from_string(GETTEXT_PACKAGE), 0,
                // TRANSLATORS:
                // The first placeholder is a filename, including the directory path.
                // The second placeholder is an ISO standard, e.g. 3166-1 or 639-3.
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

    // If there are codes given on the command line,
    // only display entries matching those.
    if (codes[0]) {
        int i = 0;
        GError *error;
        while (codes[i]) {
            error = NULL;
            if (!search_entry(codes[i], entries_list, &error)) {
                // TRANSLATORS: This is an error message.
                g_printerr(_("isoquery: %s\n"), error->message);
                g_error_free(error);
            }
            i++;
        }
    } else {
        // Set up a JSON object for an entry
        JsonObject *entry;
        // Show all entries
        while (list_entry) {
            entry = json_node_get_object(list_entry->data);
            isocodes_show_entry(entry);
            list_entry = g_list_next(list_entry);
        }
    }

    g_list_free(entries_list);
}

/**
 * Print the given entry to stdout
 */
void isocodes_show_entry(JsonObject * entry)
{
    gchar **fields = isocodes_get_fields();
    gchar separator = '\n';

    // Ensure that we've got fields to display
    if (!fields) {
        return;
    }
    // Cycle through all fields
    int i = 0;
    while (fields[i]) {
        // Handle optional fields gracefully
        if (json_object_has_member(entry, fields[i])) {
            g_printf("%s", json_object_get_string_member(entry, fields[i]));
        }
        // Always add the tab as separator
        g_printf("\t");
        i++;
    }

    // Special case for the name:
    // switching which field to display,
    // translate the name
    isocodes_show_name(entry);

    // Separate entries, either with NULL byte or newline
    if (option_null_separator) {
        separator = 0;
    }
    g_printf("%c", separator);
    g_strfreev(fields);
}

/**
 * Returns a list of the fields in the current ISO standard
 */
gchar **isocodes_get_fields(void)
{
    gchar **fields = NULL;
    if (!g_strcmp0(option_standard, "639-2")) {
        gchar *f[] = {
            "alpha_3", "bibliographic", "alpha_2", NULL
        };
        fields = g_strdupv(f);
    } else if (!g_strcmp0(option_standard, "639-3")) {
        gchar *f[] = {
            "alpha_3", "scope", "type", "alpha_2", "bibliographic", NULL
        };
        fields = g_strdupv(f);
    } else if (!g_strcmp0(option_standard, "639-5")) {
        gchar *f[] = {
            "alpha_3", NULL
        };
        fields = g_strdupv(f);
    } else if (!g_strcmp0(option_standard, "3166-1")) {
        gchar *f[] = {
            "alpha_2", "alpha_3", "numeric", NULL
        };
        fields = g_strdupv(f);
    } else if (!g_strcmp0(option_standard, "3166-2")) {
        gchar *f[] = {
            "code", "type", "parent", NULL
        };
        fields = g_strdupv(f);
    } else if (!g_strcmp0(option_standard, "3166-3")) {
        gchar *f[] = {
            "alpha_3", "alpha_4", "numeric", "comment", "withdrawal_date", NULL
        };
        fields = g_strdupv(f);
    } else if (!g_strcmp0(option_standard, "4217")) {
        gchar *f[] = {
            "alpha_3", "numeric", NULL
        };
        fields = g_strdupv(f);
    } else if (!g_strcmp0(option_standard, "15924")) {
        gchar *f[] = {
            "alpha_4", "numeric", NULL
        };
        fields = g_strdupv(f);
    }
    return fields;
}

/**
 * Special handling for the name fields
 */
void isocodes_show_name(JsonObject * entry)
{
    const gchar *output;
    // Use the correct name field
    if (json_object_has_member(entry, option_namefield)) {
        output = json_object_get_string_member(entry, option_namefield);
    } else {
        // Fallback: use the "name" field, which is mandatory
        output = json_object_get_string_member(entry, "name");
    }
    // Try to translate, if there's a locale given
    if (strlen(option_locale) > 0) {
        // Save the current locale and environment variable LANGUAGE.
        gchar *locale_backup = setlocale(LC_ALL, NULL);
        gchar *env_backup = g_strdup(getenv("LANGUAGE"));

        // Use the wanted locale to look for a translation
        setenv("LANGUAGE", option_locale, TRUE);
        // Use the default locale, based on the environment variable above
        setlocale(LC_ALL, "");

        // Determine the gettext domain from the standard
        gchar *domain = g_strdup_printf("iso_%s", option_standard);
        // Do the actual translation
        output = dgettext(domain, output);

        // Restore the environment variable LANGUAGE, either
        // to the previous value or unset the variable.
        if (env_backup == NULL) {
            unsetenv("LANGUAGE");
        } else {
            setenv("LANGUAGE", env_backup, TRUE);
        }
        // Restore the locale from backup
        setlocale(LC_ALL, locale_backup);

        g_free(env_backup);
        g_free(domain);
    }
    g_printf("%s", output);
}
