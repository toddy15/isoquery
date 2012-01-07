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
from isoquery import xmlfile_15924
from isoquery.code_not_defined_error import CodeNotDefinedError


class Options:
    """Empty class to construct the command line options"""
    pass

class TestXMLFile_15924(unittest.TestCase):
    def setUp(self):
        self.options = Options
        self.options.locale = ""
        self.options.display_name = "name"
        self.options.use_null_character = False
        self.options.iso = "15924"
        self.options.xmlfile = StringIO.StringIO("""
<iso_15924_entries>
	<iso_15924_entry
		alpha_4_code="Beng"
		numeric_code="325"
		name="Bengali" />
	<iso_15924_entry
		alpha_4_code="Cyrl"
		numeric_code="220"
		name="Cyrillic" />
	<iso_15924_entry
		alpha_4_code="Grek"
		numeric_code="200"
		name="Greek" />
	<iso_15924_entry
		alpha_4_code="Latn"
		numeric_code="215"
		name="Latin" />
</iso_15924_entries>""")

    def test_01_show_all_codes(self):
        """Check that all codes are extracted"""
        xml = xmlfile_15924.XMLFile_15924(self.options)
        self.assertTrue(xml is not None)
        # Temporarily capture output for testing purposes
        orig_stdout = sys.stdout
        sys.stdout = output = StringIO.StringIO()
        xml.show_all_codes()
        self.assertEqual(output.getvalue(),
"""\
Beng\t325\tBengali
Cyrl\t220\tCyrillic
Grek\t200\tGreek
Latn\t215\tLatin
""")
        # Revert output capturing
        sys.stdout = orig_stdout

    def test_02_show_requested_codes(self):
        """Check that requested codes are extracted"""
        xml = xmlfile_15924.XMLFile_15924(self.options)
        self.assertTrue(xml is not None)
        # Temporarily capture output for testing purposes
        orig_stdout = sys.stdout
        sys.stdout = output = StringIO.StringIO()
        for code in ("Beng", "Grek", "220"):
            xml.show_single_code(code)
        self.assertEqual(output.getvalue(),
"""\
Beng\t325\tBengali
Grek\t200\tGreek
Cyrl\t220\tCyrillic
""")
        # Revert output capturing
        sys.stdout = orig_stdout

    def test_03_show_requested_codes_with_variations(self):
        """Check that requested codes are extracted although variations are used"""
        xml = xmlfile_15924.XMLFile_15924(self.options)
        self.assertTrue(xml is not None)
        # Temporarily capture output for testing purposes
        orig_stdout = sys.stdout
        sys.stdout = output = StringIO.StringIO()
        for code in ("LATN", "cyrl", "bENG", "GRek"):
            xml.show_single_code(code)
        self.assertEqual(output.getvalue(),
"""\
Latn\t215\tLatin
Cyrl\t220\tCyrillic
Beng\t325\tBengali
Grek\t200\tGreek
""")
        # Revert output capturing
        sys.stdout = orig_stdout

    def test_04_show_warning_on_not_found_codes(self):
        """Check that missing codes are reported"""
        xml = xmlfile_15924.XMLFile_15924(self.options)
        self.assertTrue(xml is not None)
        for code in ("notthere", "007", "None"):
            self.assertRaises(CodeNotDefinedError,
                              xml.show_single_code, code)

    def test_05_show_requested_codes_and_warnings(self):
        """Check that correct codes are shown and missing codes are reported"""
        xml = xmlfile_15924.XMLFile_15924(self.options)
        self.assertTrue(xml is not None)
        # Temporarily capture output for testing purposes
        orig_stdout = sys.stdout
        sys.stdout = output = StringIO.StringIO()
        for code in ("Latn", "None", "200", "123"):
            if code in ("None", "123"):
                self.assertRaises(CodeNotDefinedError,
                                  xml.show_single_code, code)
            else:
                xml.show_single_code(code)
        # Ensure that the correct ISO codes generate an output
        self.assertEqual(output.getvalue(),
"""\
Latn\t215\tLatin
Grek\t200\tGreek
""")
        # Revert output capturing
        sys.stdout = orig_stdout

    def test_06_show_all_codes_localized(self):
        """Check that all codes are extracted and shown localized"""
        self.options.locale = "de"
        xml = xmlfile_15924.XMLFile_15924(self.options)
        self.assertTrue(xml is not None)
        # Temporarily capture output for testing purposes
        orig_stdout = sys.stdout
        sys.stdout = output = StringIO.StringIO()
        xml.show_all_codes()
        self.assertEqual(output.getvalue(),
"""\
Beng\t325\tBengalisch
Cyrl\t220\tKyrillisch
Grek\t200\tGriechisch
Latn\t215\tLateinisch
""")
        # Revert output capturing
        sys.stdout = orig_stdout

    def test_07_show_requested_codes_localized(self):
        """Check that requested codes are extracted and shown localized"""
        self.options.locale = "nl"
        xml = xmlfile_15924.XMLFile_15924(self.options)
        self.assertTrue(xml is not None)
        # Temporarily capture output for testing purposes
        orig_stdout = sys.stdout
        sys.stdout = output = StringIO.StringIO()
        for code in ("Grek", "220"):
            xml.show_single_code(code)
        self.assertEqual(output.getvalue(),
"""\
Grek\t200\tGrieks
Cyrl\t220\tCyrillisch
""")
        # Revert output capturing
        sys.stdout = orig_stdout

    def test_08_show_requested_codes_with_variations_localized(self):
        """Check that requested codes are extracted although variations are used
        and then shown localized"""
        self.options.locale = "da"
        xml = xmlfile_15924.XMLFile_15924(self.options)
        self.assertTrue(xml is not None)
        # Temporarily capture output for testing purposes
        orig_stdout = sys.stdout
        sys.stdout = output = StringIO.StringIO()
        for code in ("215", "grek", "BENG"):
            xml.show_single_code(code)
        self.assertEqual(output.getvalue(),
"""\
Latn\t215\tlatinsk
Grek\t200\tgræsk
Beng\t325\tbengalesisk
""")
        # Revert output capturing
        sys.stdout = orig_stdout

    def test_09_show_warning_on_not_found_codes_localized(self):
        """Check that missing codes are reported, not dependend on locale"""
        self.options.locale = "pl"
        xml = xmlfile_15924.XMLFile_15924(self.options)
        self.assertTrue(xml is not None)
        for code in ("None", "007"):
            self.assertRaises(CodeNotDefinedError,
                              xml.show_single_code, code)

    def test_10_show_requested_codes_and_warnings_localized(self):
        """Check that correct codes are shown localized and missing codes are reported"""
        self.options.locale = "he"
        xml = xmlfile_15924.XMLFile_15924(self.options)
        self.assertTrue(xml is not None)
        # Temporarily capture output for testing purposes
        orig_stdout = sys.stdout
        sys.stdout = output = StringIO.StringIO()
        for code in ("Latn", "Miss", "200", "007"):
            if code in ("Miss", "007"):
                self.assertRaises(CodeNotDefinedError,
                                  xml.show_single_code, code)
            else:
                xml.show_single_code(code)
        # Ensure that the correct ISO codes generate an output
        self.assertEqual(output.getvalue(),
"""\
Latn\t215\tלטינית
Grek\t200\tיוונית
""")
        # Revert output capturing
        sys.stdout = orig_stdout

    def test_11_show_all_codes_with_null_character(self):
        """Check that all codes are extracted and separated with the null character"""
        self.options.use_null_character = True
        xml = xmlfile_15924.XMLFile_15924(self.options)
        self.assertTrue(xml is not None)
        # Temporarily capture output for testing purposes
        orig_stdout = sys.stdout
        sys.stdout = output = StringIO.StringIO()
        xml.show_all_codes()
        self.assertEqual(output.getvalue(),
"""\
Beng\t325\tBengali\0\
Cyrl\t220\tCyrillic\0\
Grek\t200\tGreek\0\
Latn\t215\tLatin\0\
""")
        # Revert output capturing
        sys.stdout = orig_stdout

suite = unittest.TestLoader().loadTestsFromTestCase(TestXMLFile_15924)
unittest.TextTestRunner(verbosity=2).run(suite)
