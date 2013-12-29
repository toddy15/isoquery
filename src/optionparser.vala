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

public class Options : Object {
    internal static string iso;
    internal static bool version;

    private const OptionEntry[] options = {
        { "iso", 'i', 0, OptionArg.STRING, ref iso, "The ISO standard to use. Possible values: 639, 639-3, 3166, 3166-2, 4217, 15924 (default: 3166).", "STANDARD" },
        { "version", 'v', 0, OptionArg.NONE, ref version, "Show program version and copyright.", null },
        // Terminate list of options
        { null }
    };

    public static bool parse_arguments(ref unowned string[] args) {
        bool success = true;
        try {
            var opt_context = new OptionContext("[ISO codes]");
            opt_context.set_help_enabled(true);
            opt_context.add_main_entries(options, null);
            opt_context.parse(ref args);
        } catch (OptionError err) {
            // TRANSLATORS: This is an error message.
            stderr.printf(_("isoquery: %s\n"), err.message);
            stderr.printf(_("Run '%s --help' to see a full list of available command line options.\n"), args[0]);
            // Exit the program with an error status.
            success = false;
        }
        return success;
    }
}
