# - encoding: UTF-8 -
#
# Copyright © 2007-2010 Tobias Quathamer
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
from isoquery import xmlfile_4217
from isoquery.code_not_defined_error import CodeNotDefinedError


class Options:
    """Empty class to construct the command line options"""
    pass

class TestXMLFile_4217(unittest.TestCase):
    def setUp(self):
        self.options = Options
        self.options.locale = ""
        self.options.display_name = "currency_name"
        self.options.use_null_character = False
        self.options.iso = "4217"
        self.options.xmlfile = StringIO.StringIO("""
<iso_4217_entries>
	<iso_4217_entry
		letter_code="EUR"
		numeric_code="978"
		currency_name="Euro" />
	<iso_4217_entry
		letter_code="GBP"
		numeric_code="826"
		currency_name="Pound Sterling" />
	<iso_4217_entry
		letter_code="INR"
		numeric_code="356"
		currency_name="Indian Rupee" />
</iso_4217_entries>""")

    def test_01_show_all_codes(self):
        """Check that all codes are extracted"""
        xml = xmlfile_4217.XMLFile_4217(self.options)
        self.assertTrue(xml is not None)
        # Temporarily capture output for testing purposes
        orig_stdout = sys.stdout
        sys.stdout = output = StringIO.StringIO()
        xml.show_all_codes()
        self.assertEqual(output.getvalue(),
"""\
EUR\t978\tEuro
GBP\t826\tPound Sterling
INR\t356\tIndian Rupee
""")
        # Revert output capturing
        sys.stdout = orig_stdout

    def test_02_show_requested_codes(self):
        """Check that requested codes are extracted"""
        xml = xmlfile_4217.XMLFile_4217(self.options)
        self.assertTrue(xml is not None)
        # Temporarily capture output for testing purposes
        orig_stdout = sys.stdout
        sys.stdout = output = StringIO.StringIO()
        for code in ("EUR", "INR", "826"):
            xml.show_single_code(code)
        self.assertEqual(output.getvalue(),
"""\
EUR\t978\tEuro
INR\t356\tIndian Rupee
GBP\t826\tPound Sterling
""")
        # Revert output capturing
        sys.stdout = orig_stdout

    def test_03_show_requested_codes_with_variations(self):
        """Check that requested codes are extracted although variations are used"""
        xml = xmlfile_4217.XMLFile_4217(self.options)
        self.assertTrue(xml is not None)
        # Temporarily capture output for testing purposes
        orig_stdout = sys.stdout
        sys.stdout = output = StringIO.StringIO()
        for code in ("inR", "Eur", "gbp"):
            xml.show_single_code(code)
        self.assertEqual(output.getvalue(),
"""\
INR\t356\tIndian Rupee
EUR\t978\tEuro
GBP\t826\tPound Sterling
""")
        # Revert output capturing
        sys.stdout = orig_stdout

    def test_04_show_warning_on_not_found_codes(self):
        """Check that missing codes are reported"""
        xml = xmlfile_4217.XMLFile_4217(self.options)
        self.assertTrue(xml is not None)
        for code in ("notthere", "007", "ppp"):
            self.assertRaises(CodeNotDefinedError,
                              xml.show_single_code, code)

    def test_05_show_requested_codes_and_warnings(self):
        """Check that correct codes are shown and missing codes are reported"""
        xml = xmlfile_4217.XMLFile_4217(self.options)
        self.assertTrue(xml is not None)
        # Temporarily capture output for testing purposes
        orig_stdout = sys.stdout
        sys.stdout = output = StringIO.StringIO()
        for code in ("INR", "drul", "240", "826"):
            if code in ("drul", "240"):
                self.assertRaises(CodeNotDefinedError,
                                  xml.show_single_code, code)
            else:
                xml.show_single_code(code)
        # Ensure that the correct ISO codes generate an output
        self.assertEqual(output.getvalue(),
"""\
INR\t356\tIndian Rupee
GBP\t826\tPound Sterling
""")
        # Revert output capturing
        sys.stdout = orig_stdout

    def test_06_show_all_codes_localized(self):
        """Check that all codes are extracted and shown localized"""
        self.options.locale = "de"
        xml = xmlfile_4217.XMLFile_4217(self.options)
        self.assertTrue(xml is not None)
        # Temporarily capture output for testing purposes
        orig_stdout = sys.stdout
        sys.stdout = output = StringIO.StringIO()
        xml.show_all_codes()
        self.assertEqual(output.getvalue(),
"""\
EUR\t978\tEuro
GBP\t826\tPfund Sterling
INR\t356\tIndische Rupie
""")
        # Revert output capturing
        sys.stdout = orig_stdout

    def test_07_show_requested_codes_localized(self):
        """Check that requested codes are extracted and shown localized"""
        self.options.locale = "nl"
        xml = xmlfile_4217.XMLFile_4217(self.options)
        self.assertTrue(xml is not None)
        # Temporarily capture output for testing purposes
        orig_stdout = sys.stdout
        sys.stdout = output = StringIO.StringIO()
        for code in ("gbp", "inr"):
            xml.show_single_code(code)
        self.assertEqual(output.getvalue(),
"""\
GBP\t826\tpond sterling
INR\t356\tIndiase rupee
""")
        # Revert output capturing
        sys.stdout = orig_stdout

    def test_08_show_requested_codes_with_variations_localized(self):
        """Check that requested codes are extracted although variations are used
        and then shown localized"""
        self.options.locale = "da"
        xml = xmlfile_4217.XMLFile_4217(self.options)
        self.assertTrue(xml is not None)
        # Temporarily capture output for testing purposes
        orig_stdout = sys.stdout
        sys.stdout = output = StringIO.StringIO()
        for code in ("978", "GbP", "inr"):
            xml.show_single_code(code)
        self.assertEqual(output.getvalue(),
"""\
EUR\t978\tEuro
GBP\t826\tBritisk pund sterling
INR\t356\tIndisk rupee
""")
        # Revert output capturing
        sys.stdout = orig_stdout

    def test_09_show_warning_on_not_found_codes_localized(self):
        """Check that missing codes are reported, not dependend on locale"""
        self.options.locale = "he"
        xml = xmlfile_4217.XMLFile_4217(self.options)
        self.assertTrue(xml is not None)
        for code in ("none", "007"):
            self.assertRaises(CodeNotDefinedError,
                              xml.show_single_code, code)

    def test_10_show_requested_codes_and_warnings_localized(self):
        """Check that correct codes are shown localized and missing codes are reported"""
        self.options.locale = "nb"
        xml = xmlfile_4217.XMLFile_4217(self.options)
        self.assertTrue(xml is not None)
        # Temporarily capture output for testing purposes
        orig_stdout = sys.stdout
        sys.stdout = output = StringIO.StringIO()
        for code in ("GBP", "miss", "356", "724"):
            if code in ("miss", "724"):
                self.assertRaises(CodeNotDefinedError,
                                  xml.show_single_code, code)
            else:
                xml.show_single_code(code)
        # Ensure that the correct ISO codes generate an output
        self.assertEqual(output.getvalue(),
"""\
GBP\t826\tBritiske pund
INR\t356\tIndiske rupier
""")
        # Revert output capturing
        sys.stdout = orig_stdout

    def test_11_show_all_codes_with_null_character(self):
        """Check that all codes are extracted and separated with the null character"""
        self.options.use_null_character = True
        xml = xmlfile_4217.XMLFile_4217(self.options)
        self.assertTrue(xml is not None)
        # Temporarily capture output for testing purposes
        orig_stdout = sys.stdout
        sys.stdout = output = StringIO.StringIO()
        xml.show_all_codes()
        self.assertEqual(output.getvalue(),
"""\
EUR\t978\tEuro\0\
GBP\t826\tPound Sterling\0\
INR\t356\tIndian Rupee\0\
""")
        # Revert output capturing
        sys.stdout = orig_stdout

suite = unittest.TestLoader().loadTestsFromTestCase(TestXMLFile_4217)
unittest.TextTestRunner(verbosity=2).run(suite)
