# - encoding: UTF-8 -
#
# Copyright © 2007-2011 Tobias Quathamer
#
# This file is part of isoquery.
#
# isoquery is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# isoquery is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import unittest
import sys
import StringIO
import gettext
from isoquery import cmdline_parser
translation = gettext.translation('isoquery', fallback=True)
_ = translation.gettext

class TestCmdlineParser(unittest.TestCase):
    def test_01_empty_commandline(self):
        """Check that an empty command line yields sensible defaults"""
        p = cmdline_parser.CmdlineParser()
        (options, args) = p.parse("")
        self.assertEqual(options.iso, "3166")
        self.assertEqual(options.xmlfile, "/usr/share/xml/iso-codes/iso_3166.xml")
        self.assertEqual(options.display_name, "name")
        self.assertEqual(options.use_null_character, False)

    def test_02_valid_isostandards(self):
        """Check that all supported ISO standards are parsed correctly"""
        supported = ["639", "639-3", "3166", "3166-2", "4217", "15924"]
        for standard in supported:
            p = cmdline_parser.CmdlineParser()
            cmdline = "-i" + standard
            (options, args) = p.parse(cmdline)
            self.assertEqual(options.iso, standard)
            cmdline = "--iso=" + standard
            (options, args) = p.parse(cmdline)
            self.assertEqual(options.iso, standard)

    def test_03_invalid_isostandards(self):
        """Check that unsupported ISO standards are rejected"""
        unsupported = ["1234", "letters"]
        for standard in unsupported:
            p = cmdline_parser.CmdlineParser()
            # Temporarily capture output for testing purposes
            orig_stderr = sys.stderr
            sys.stderr = output = StringIO.StringIO()
            cmdline = "-i" + standard
            self.assertRaises(SystemExit, p.parse, cmdline)
            self.assertEqual(output.getvalue(),
                             _("isoquery: ISO standard '%(standard)s' is not supported.\n") % \
                             {"standard": standard})
            # Re-open a new output for the next comparison
            sys.stderr = output = StringIO.StringIO()
            cmdline = "--iso=" + standard
            self.assertRaises(SystemExit, p.parse, cmdline)
            self.assertEqual(output.getvalue(),
                             _("isoquery: ISO standard '%(standard)s' is not supported.\n") % \
                             {"standard": standard})
            # Revert output capturing
            sys.stderr = orig_stderr

    def test_04_default_xmlfiles(self):
        """Check for correct default XML file, depending on ISO standard"""
        supported = ["639", "639-3", "3166", "3166-2", "4217", "15924"]
        xml_path = "/usr/share/xml/iso-codes/iso_"
        for standard in supported:
            p = cmdline_parser.CmdlineParser()
            cmdline = "-i" + standard
            default_xmlfile = xml_path + standard.replace('-', '_') + ".xml"
            (options, args) = p.parse(cmdline)
            self.assertEqual(options.xmlfile, default_xmlfile)
            cmdline = "--iso=" + standard
            (options, args) = p.parse(cmdline)
            self.assertEqual(options.xmlfile, default_xmlfile)

    def test_05_custom_xmlfiles(self):
        """Check that custom XML files are recognized"""
        xml_file = "/this/is/a/path/to/my/xmlfile.xml"
        p = cmdline_parser.CmdlineParser()
        cmdline = "-x" + xml_file
        (options, args) = p.parse(cmdline)
        self.assertEqual(options.xmlfile, xml_file)
        cmdline = "--xmlfile=" + xml_file
        (options, args) = p.parse(cmdline)
        self.assertEqual(options.xmlfile, xml_file)

    def test_06_locale(self):
        """Check that a specified locale is used"""
        locales = ["de", "fr_FR", "pt_BR.UTF-8"]
        p = cmdline_parser.CmdlineParser()
        for locale in locales:
            cmdline = "-l " + locale
            (options, args) = p.parse(cmdline)
            self.assertEqual(options.locale, locale)
            cmdline = "--locale=" + locale
            (options, args) = p.parse(cmdline)
            self.assertEqual(options.locale, locale)

    def test_07_wrong_locale(self):
        """Check that an error message is shown if the locale does not exist"""
        p = cmdline_parser.CmdlineParser()
        locale = "unknown"
        # Temporarily capture output for testing purposes
        orig_stderr = sys.stderr
        sys.stderr = output = StringIO.StringIO()
        cmdline = "-l " + locale
        (options, args) = p.parse(cmdline)
        self.assertEqual(output.getvalue(),
                         _("isoquery: The locale '%(locale)s' is not " \
                           "available for ISO %(standard)s.\n") % \
                           {"locale": locale, "standard": "3166"})
        # Re-open a new output for the next comparison
        sys.stderr = output = StringIO.StringIO()
        cmdline = "--locale=" + locale
        (options, args) = p.parse(cmdline)
        self.assertEqual(output.getvalue(),
                         _("isoquery: The locale '%(locale)s' is not " \
                           "available for ISO %(standard)s.\n") % \
                           {"locale": locale, "standard": "3166"})
        # Revert output capturing
        sys.stderr = orig_stderr

    def test_08_display_names(self):
        """Check that the specified name is used for display"""
        p = cmdline_parser.CmdlineParser()
        cmdline = "-n"
        (options, args) = p.parse(cmdline)
        self.assertEqual(options.display_name, "name")
        cmdline = "--name"
        (options, args) = p.parse(cmdline)
        self.assertEqual(options.display_name, "name")
        cmdline = "-o"
        (options, args) = p.parse(cmdline)
        self.assertEqual(options.display_name, "official_name")
        cmdline = "--official_name"
        (options, args) = p.parse(cmdline)
        self.assertEqual(options.display_name, "official_name")
        cmdline = "-c"
        (options, args) = p.parse(cmdline)
        self.assertEqual(options.display_name, "common_name")
        cmdline = "--common_name"
        (options, args) = p.parse(cmdline)
        self.assertEqual(options.display_name, "common_name")

    def test_09_use_null_as_separator(self):
        """Use the NULL character as separator between entries"""
        p = cmdline_parser.CmdlineParser()
        cmdline = "-0"
        (options, args) = p.parse(cmdline)
        self.assertEqual(options.use_null_character, True)
        cmdline = "--null"
        (options, args) = p.parse(cmdline)
        self.assertEqual(options.use_null_character, True)

suite = unittest.TestLoader().loadTestsFromTestCase(TestCmdlineParser)
unittest.TextTestRunner(verbosity=2).run(suite)
