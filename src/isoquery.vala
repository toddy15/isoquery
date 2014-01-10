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

public struct ProgramOptions {
    string iso;
    string filepath;
    string locale;
    bool name;
    bool official_name;
    bool common_name;
    bool use_null_separator;
    bool version;
}

public class Isoquery : Object {
    private static void _check_options(ref ProgramOptions options) {
        // Display version and copyright.
        if (options.version == true) {
            _show_version_and_copyright();
            Posix.exit(Posix.EXIT_SUCCESS);
        }
        // Ensure the default ISO standard is set
        if (options.iso == null) {
            options.iso = "3166";
        }
        // Ensure a valid and supported standard
        string[] supported_standards = { "639", "639-3", "3166", "3166-2", "4217", "15924" };
        bool supported = false;
        foreach (var standard in supported_standards) {
            if (options.iso == standard) {
                supported = true;
                break;
            }
        }
        if (!supported) {
            stderr.printf(_("isoquery: ISO standard '%s' is not supported.\n"), options.iso);
            Posix.exit(Posix.EXIT_FAILURE);
        }
    }

    private static void _show_version_and_copyright() {
        stdout.printf(_("isoquery %s\n"), Config.VERSION);
        stdout.printf(_("Copyright © 2007-2014 Tobias Quathamer\n"));
        // TRANSLATORS: Please change the uppercase words as appropriate for
        // your language.
        var translation = _("Translation to LANGUAGE Copyright © YEAR YOUR-NAME\n");
        if (!("LANGUAGE" in translation)) {
            stdout.printf(translation);
        }
        stdout.printf("""
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
""");
    }

    public static int main(string[] args) {
        // Set up I18N infrastructure
        Intl.bindtextdomain(Config.GETTEXT_PACKAGE, Config.LOCALEDIR);
        Intl.bind_textdomain_codeset(Config.GETTEXT_PACKAGE, "UTF-8");
        Intl.setlocale(LocaleCategory.ALL, "");
        // Setup the possible command line options.
        var options = ProgramOptions();
        var commandline_options = new OptionEntry[9];
        commandline_options[0] = {
            "iso", 'i', 0, OptionArg.STRING, ref options.iso, _("The ISO standard to use. Possible values: 639, 639-3, 3166, 3166-2, 4217, 15924 (default: 3166)."), _("STANDARD")
        };
        commandline_options[1] = {
            "xmlfile", 'x', 0, OptionArg.STRING, ref options.filepath, _("Use another XML file with ISO data (default: /usr/share/xml/iso-codes/iso_3166.xml)"), _("FILE")
        };
        commandline_options[2] = {
            "locale", 'l', 0, OptionArg.STRING, ref options.locale, _("Use this locale for output."), _("LOCALE")
        };
        commandline_options[3] = {
            "name", 'n', 0, OptionArg.NONE, ref options.name, _("Name for the supplied codes (default).")
        };
        commandline_options[4] = {
            "official_name", 'o', 0, OptionArg.NONE, ref options.official_name, _("Official name for the supplied codes. This may be the same as --name (only applies to ISO 3166).")
        };
        commandline_options[5] = {
            "common_name", 'c', 0, OptionArg.NONE, ref options.common_name, _("Common name for the supplied codes. This may be the same as --name (only applies to ISO 3166).")
        };
        commandline_options[6] = {
            "null", '0', 0, OptionArg.NONE, ref options.use_null_separator, _("Separate entries with a NULL character instead of newline.")
        };
        commandline_options[7] = {
            "version", 'v', 0, OptionArg.NONE, ref options.version, _("Show program version and copyright.")
        };
        // Terminate list of options.
        commandline_options[8] = { null };
        // Parse command line options.
        try {
            var opt_context = new OptionContext(_("[ISO codes]"));
            opt_context.set_help_enabled(true);
            opt_context.add_main_entries(commandline_options, null);
            opt_context.parse(ref args);
        } catch (OptionError err) {
            // TRANSLATORS: This is an error message.
            stderr.printf(_("isoquery: %s\n"), err.message);
            stderr.printf(_("Run '%s --help' to see a full list of available command line options.\n"), args[0]);
            // Exit the program with an error status.
            Posix.exit(Posix.EXIT_FAILURE);
        }
        // Check options.
        _check_options(ref options);
        // Remove the program name from the argument list.
        args = args[1:args.length];
        switch (options.iso) {
            case "639":
                Handle_639.show(options, args);
                break;
            case "639-3":
                Handle_639_3.show(options, args);
                break;
            case "3166":
                Handle_3166.show(options, args);
                break;
            case "3166-2":
                Handle_3166_2.show(options, args);
                break;
            case "4217":
                Handle_4217.show(options, args);
                break;
            case "15924":
                Handle_15924.show(options, args);
                break;
            default:
                // We should normally never reach this, as all supported
                // ISO codes are checked during the option parsing.
                stderr.printf(_("isoquery: Internal error. Please report this bug.\n"));
                return Posix.EXIT_FAILURE;
        }
        return Posix.EXIT_SUCCESS;
    }
}
