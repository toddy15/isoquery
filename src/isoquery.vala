/* Copyright © 2013 Tobias Quathamer
 *
 * This file is part of isoquery.
 *
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 3 of the License, or
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

using libisocodes;

public class Isoquery : Object {
    public static int main(string[] args) {
        // Set up I18N infrastructure
        Intl.bindtextdomain(Config.GETTEXT_PACKAGE, Config.LOCALEDIR);
        Intl.bind_textdomain_codeset(Config.GETTEXT_PACKAGE, "UTF-8");
        Intl.setlocale(LocaleCategory.ALL, "");
        // Parse command line options.
        Options.parse_arguments(ref args);
        var a = new ISO_3166();
        try {
            foreach (var i in a.find_all()) {
                stdout.printf("%s\n", i.name);
            }
        }
        catch (ISOCodesError err) {
            // TRANSLATORS: This is an error message.
            stderr.printf(_("isoquery: %s\n"), err.message);
        }
        return Posix.EXIT_SUCCESS;
    }
}
