# - encoding: UTF-8 -
#
# Copyright © 2007-2012 Tobias Quathamer
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
from isoquery import xmlfile_639
from isoquery.code_not_defined_error import CodeNotDefinedError


class Options:
    """Empty class to construct the command line options"""
    pass

class TestXMLFile_639(unittest.TestCase):
    def setUp(self):
        self.options = Options
        self.options.locale = ""
        self.options.display_name = "name"
        self.options.use_null_character = False
        self.options.iso = "639"
        self.options.xmlfile = StringIO.StringIO("""
<iso_639_entries>
	<iso_639_entry
		iso_639_2B_code="aar"
		iso_639_2T_code="aar"
		iso_639_1_code="aa"
		name="Afar" />
	<iso_639_entry
		iso_639_2B_code="alg"
		iso_639_2T_code="alg"
		name="Algonquian languages" />
	<iso_639_entry
		iso_639_2B_code="heb"
		iso_639_2T_code="heb"
		iso_639_1_code="he"
		name="Hebrew" />
	<iso_639_entry
		iso_639_2B_code="tib"
		iso_639_2T_code="bod"
		iso_639_1_code="bo"
		name="Tibetan" />
</iso_639_entries>""")

    def test_01_show_all_codes(self):
        """Check that all codes are extracted"""
        xml = xmlfile_639.XMLFile_639(self.options)
        self.assertTrue(xml is not None)
        # Temporarily capture output for testing purposes
        orig_stdout = sys.stdout
        sys.stdout = output = StringIO.StringIO()
        xml.show_all_codes()
        self.assertEqual(output.getvalue(),
"""\
aar\taar\taa\tAfar
alg\talg\t\tAlgonquian languages
heb\theb\the\tHebrew
tib\tbod\tbo\tTibetan
""")
        # Revert output capturing
        sys.stdout = orig_stdout

    def test_02_show_requested_codes(self):
        """Check that requested codes are extracted"""
        xml = xmlfile_639.XMLFile_639(self.options)
        self.assertTrue(xml is not None)
        # Temporarily capture output for testing purposes
        orig_stdout = sys.stdout
        sys.stdout = output = StringIO.StringIO()
        for code in ("heb", "bod", "aa", "tib", "alg"):
            xml.show_single_code(code)
        self.assertEqual(output.getvalue(),
"""\
heb\theb\the\tHebrew
tib\tbod\tbo\tTibetan
aar\taar\taa\tAfar
tib\tbod\tbo\tTibetan
alg\talg\t\tAlgonquian languages
""")
        # Revert output capturing
        sys.stdout = orig_stdout

    def test_03_show_requested_codes_with_variations(self):
        """Check that requested codes are extracted although variations are used"""
        xml = xmlfile_639.XMLFile_639(self.options)
        self.assertTrue(xml is not None)
        # Temporarily capture output for testing purposes
        orig_stdout = sys.stdout
        sys.stdout = output = StringIO.StringIO()
        for code in ("ALG", "Tib", "aA"):
            xml.show_single_code(code)
        self.assertEqual(output.getvalue(),
"""\
alg\talg\t\tAlgonquian languages
tib\tbod\tbo\tTibetan
aar\taar\taa\tAfar
""")
        # Revert output capturing
        sys.stdout = orig_stdout

    def test_04_show_warning_on_not_found_codes(self):
        """Check that missing codes are reported"""
        xml = xmlfile_639.XMLFile_639(self.options)
        self.assertTrue(xml is not None)
        for code in ("notthere", "250", "pp"):
            self.assertRaises(CodeNotDefinedError,
                              xml.show_single_code, code)

    def test_05_show_requested_codes_and_warnings(self):
        """Check that correct codes are shown and missing codes are reported"""
        xml = xmlfile_639.XMLFile_639(self.options)
        self.assertTrue(xml is not None)
        # Temporarily capture output for testing purposes
        orig_stdout = sys.stdout
        sys.stdout = output = StringIO.StringIO()
        for code in ("he", "drul", "240", "alg"):
            if code in ("drul", "240"):
                self.assertRaises(CodeNotDefinedError,
                                  xml.show_single_code, code)
            else:
                xml.show_single_code(code)
        # Ensure that the correct ISO codes generate an output
        self.assertEqual(output.getvalue(),
"""\
heb\theb\the\tHebrew
alg\talg\t\tAlgonquian languages
""")
        # Revert output capturing
        sys.stdout = orig_stdout

    def test_06_show_all_codes_localized(self):
        """Check that all codes are extracted and shown localized"""
        self.options.locale = "de"
        xml = xmlfile_639.XMLFile_639(self.options)
        self.assertTrue(xml is not None)
        # Temporarily capture output for testing purposes
        orig_stdout = sys.stdout
        sys.stdout = output = StringIO.StringIO()
        xml.show_all_codes()
        self.assertEqual(output.getvalue(),
"""\
aar\taar\taa\tDanakil-Sprache
alg\talg\t\tAlgonkin-Sprachen
heb\theb\the\tHebräisch
tib\tbod\tbo\tTibetisch
""")
        # Revert output capturing
        sys.stdout = orig_stdout

    def test_07_show_requested_codes_localized(self):
        """Check that requested codes are extracted and shown localized"""
        self.options.locale = "fr"
        xml = xmlfile_639.XMLFile_639(self.options)
        self.assertTrue(xml is not None)
        # Temporarily capture output for testing purposes
        orig_stdout = sys.stdout
        sys.stdout = output = StringIO.StringIO()
        for code in ("he", "alg"):
            xml.show_single_code(code)
        self.assertEqual(output.getvalue(),
"""\
heb\theb\the\thébreu
alg\talg\t\talgonquines, langues
""")
        # Revert output capturing
        sys.stdout = orig_stdout

    def test_08_show_requested_codes_with_variations_localized(self):
        """Check that requested codes are extracted although variations are used
        and then shown localized"""
        self.options.locale = "pl"
        xml = xmlfile_639.XMLFile_639(self.options)
        self.assertTrue(xml is not None)
        # Temporarily capture output for testing purposes
        orig_stdout = sys.stdout
        sys.stdout = output = StringIO.StringIO()
        for code in ("aa", "Tib", "hEB"):
            xml.show_single_code(code)
        self.assertEqual(output.getvalue(),
"""\
aar\taar\taa\tafarski
tib\tbod\tbo\ttybetański
heb\theb\the\thebrajski
""")
        # Revert output capturing
        sys.stdout = orig_stdout

    def test_09_show_warning_on_not_found_codes_localized(self):
        """Check that missing codes are reported, not dependend on locale"""
        self.options.locale = "nl"
        xml = xmlfile_639.XMLFile_639(self.options)
        self.assertTrue(xml is not None)
        for code in ("none", "007"):
            self.assertRaises(CodeNotDefinedError,
                              xml.show_single_code, code)

    def test_10_show_requested_codes_and_warnings_localized(self):
        """Check that correct codes are shown localized and missing codes are reported"""
        self.options.locale = "da"
        xml = xmlfile_639.XMLFile_639(self.options)
        self.assertTrue(xml is not None)
        # Temporarily capture output for testing purposes
        orig_stdout = sys.stdout
        sys.stdout = output = StringIO.StringIO()
        for code in ("tib", "miss", "heb", "724"):
            if code in ("miss", "724"):
                self.assertRaises(CodeNotDefinedError,
                                  xml.show_single_code, code)
            else:
                xml.show_single_code(code)
        # Ensure that the correct ISO codes generate an output
        self.assertEqual(output.getvalue(),
"""\
tib\tbod\tbo\tTibetansk
heb\theb\the\tHebraisk
""")
        # Revert output capturing
        sys.stdout = orig_stdout

    def test_11_show_all_codes_with_null_character(self):
        """Check that all codes are extracted and separated with the null character"""
        self.options.use_null_character = True
        xml = xmlfile_639.XMLFile_639(self.options)
        self.assertTrue(xml is not None)
        # Temporarily capture output for testing purposes
        orig_stdout = sys.stdout
        sys.stdout = output = StringIO.StringIO()
        xml.show_all_codes()
        self.assertEqual(output.getvalue(),
"""\
aar\taar\taa\tAfar\0\
alg\talg\t\tAlgonquian languages\0\
heb\theb\the\tHebrew\0\
tib\tbod\tbo\tTibetan\0\
""")
        # Revert output capturing
        sys.stdout = orig_stdout

suite = unittest.TestLoader().loadTestsFromTestCase(TestXMLFile_639)
unittest.TextTestRunner(verbosity=2).run(suite)
