/* Copyright © 2013-2014 Tobias Quathamer
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

public class Handle_4217 : Object {
    private static ProgramOptions options;
    private static ISO_4217 iso;
    private static string standard;
    
    public static void show(ProgramOptions opts, string[] codes) {
        options = opts;
        iso = new ISO_4217();
        standard = "4217";
        iso.set_filepath(options.filepath);
        iso.set_locale(options.locale);
        _show_codes(codes);
    }

    private static void _show_item(ISO_4217_Item item) {
        stdout.printf("%s\t", item.letter_code);
        stdout.printf("%s\t", item.numeric_code);
        stdout.printf("%s", item.name);
        if (options.use_null_separator) {
            stdout.printf("%c", 0);
        }
        else {
            stdout.printf("\n");
        }
    }

    private static void _show_codes(string[] codes) {
        if (codes.length == 0) {
            try {
                var items = iso.find_all();
                foreach (var item in items) {
                    _show_item(item);
                }
            }
            catch (ISOCodesError err) {
                stderr.printf(_("isoquery: %(error_message)s\n")
                  .replace("%(error_message)s", err.message));
                // Exit the program with an error status.
                Posix.exit(Posix.EXIT_FAILURE);
            }
        }
        else {
            foreach (var code in codes) {
                try {
                    var item = iso.find_code(code);
                    _show_item(item);
                }
                catch (ISOCodesError err) {
                    stderr.printf(_("isoquery: %(error_message)s\n")
                      .replace("%(error_message)s", err.message));
                    // Exit the program with an error status,
                    // unless the error is "CODE_NOT_DEFINED".
                    if (!(err is ISOCodesError.CODE_NOT_DEFINED)) {
                        Posix.exit(Posix.EXIT_FAILURE);
                    }
                }
            }
        }
    }
}
