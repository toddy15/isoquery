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
from isoquery import xmlfile_3166
from isoquery.code_not_defined_error import CodeNotDefinedError


class Options:
    """Empty class to construct the command line options"""
    pass

class TestXMLFile_3166(unittest.TestCase):
    def setUp(self):
        self.options = Options
        self.options.locale = ""
        self.options.display_name = "name"
        self.options.use_null_character = False
        self.options.iso = "3166"
        self.options.xmlfile = StringIO.StringIO("""
<iso_3166_entries>
	<iso_3166_entry
		alpha_2_code="DE"
		alpha_3_code="DEU"
		numeric_code="276"
		name="Germany"
		official_name="Federal Republic of Germany" />
	<iso_3166_entry
		alpha_2_code="FR"
		alpha_3_code="FRA"
		numeric_code="250"
		name="France"
		official_name="French Republic" />
	<iso_3166_entry
		alpha_2_code="ES"
		alpha_3_code="ESP"
		numeric_code="724"
		name="Spain"
		official_name="Kingdom of Spain" />
	<iso_3166_entry
		alpha_2_code="TW"
		alpha_3_code="TWN"
		numeric_code="158"
		common_name="Taiwan"
		name="Taiwan, Province of China"
		official_name="Taiwan, Province of China" />
</iso_3166_entries>""")

    def test_01_show_all_codes(self):
        """Check that all codes are extracted"""
        xml = xmlfile_3166.XMLFile_3166(self.options)
        self.assertTrue(xml is not None)
        # Temporarily capture output for testing purposes
        orig_stdout = sys.stdout
        sys.stdout = output = StringIO.StringIO()
        xml.show_all_codes()
        self.assertEqual(output.getvalue(),
"""\
DE\tDEU\t276\tGermany
FR\tFRA\t250\tFrance
ES\tESP\t724\tSpain
TW\tTWN\t158\tTaiwan, Province of China
""")
        # Revert output capturing
        sys.stdout = orig_stdout

    def test_02_show_requested_codes(self):
        """Check that requested codes are extracted"""
        xml = xmlfile_3166.XMLFile_3166(self.options)
        self.assertTrue(xml is not None)
        # Temporarily capture output for testing purposes
        orig_stdout = sys.stdout
        sys.stdout = output = StringIO.StringIO()
        for code in ("ES", "DEU", "250"):
            xml.show_single_code(code)
        self.assertEqual(output.getvalue(),
"""\
ES\tESP\t724\tSpain
DE\tDEU\t276\tGermany
FR\tFRA\t250\tFrance
""")
        # Revert output capturing
        sys.stdout = orig_stdout

    def test_03_show_requested_codes_with_variations(self):
        """Check that requested codes are extracted although variations are used"""
        xml = xmlfile_3166.XMLFile_3166(self.options)
        self.assertTrue(xml is not None)
        # Temporarily capture output for testing purposes
        orig_stdout = sys.stdout
        sys.stdout = output = StringIO.StringIO()
        for code in ("es", "Deu", "250", "dEU"):
            xml.show_single_code(code)
        self.assertEqual(output.getvalue(),
"""\
ES\tESP\t724\tSpain
DE\tDEU\t276\tGermany
FR\tFRA\t250\tFrance
DE\tDEU\t276\tGermany
""")
        # Revert output capturing
        sys.stdout = orig_stdout

    def test_04_show_warning_on_not_found_codes(self):
        """Check that missing codes are reported"""
        xml = xmlfile_3166.XMLFile_3166(self.options)
        self.assertTrue(xml is not None)
        for code in ("esalu", "hrg", "007"):
            self.assertRaises(CodeNotDefinedError,
                              xml.show_single_code, code)

    def test_05_show_requested_codes_and_warnings(self):
        """Check that correct codes are shown and missing codes are reported"""
        xml = xmlfile_3166.XMLFile_3166(self.options)
        self.assertTrue(xml is not None)
        # Temporarily capture output for testing purposes
        orig_stdout = sys.stdout
        sys.stdout = output = StringIO.StringIO()
        for code in ("de", "esalu", "hrg", "724", "007"):
            if code in ("esalu", "hrg", "007"):
                self.assertRaises(CodeNotDefinedError,
                                  xml.show_single_code, code)
            else:
                xml.show_single_code(code)
        # Ensure that the correct ISO codes generate an output
        self.assertEqual(output.getvalue(),
"""\
DE\tDEU\t276\tGermany
ES\tESP\t724\tSpain
""")
        # Revert output capturing
        sys.stdout = orig_stdout

    def test_06_show_all_codes_localized(self):
        """Check that all codes are extracted and shown localized"""
        self.options.locale = "de"
        xml = xmlfile_3166.XMLFile_3166(self.options)
        self.assertTrue(xml is not None)
        # Temporarily capture output for testing purposes
        orig_stdout = sys.stdout
        sys.stdout = output = StringIO.StringIO()
        xml.show_all_codes()
        self.assertEqual(output.getvalue(),
"""\
DE\tDEU\t276\tDeutschland
FR\tFRA\t250\tFrankreich
ES\tESP\t724\tSpanien
TW\tTWN\t158\tTaiwan, Chinesische Provinz
""")
        # Revert output capturing
        sys.stdout = orig_stdout

    def test_07_show_requested_codes_localized(self):
        """Check that requested codes are extracted and shown localized"""
        self.options.locale = "fr"
        xml = xmlfile_3166.XMLFile_3166(self.options)
        self.assertTrue(xml is not None)
        # Temporarily capture output for testing purposes
        orig_stdout = sys.stdout
        sys.stdout = output = StringIO.StringIO()
        for code in ("ES", "DEU", "250"):
            xml.show_single_code(code)
        self.assertEqual(output.getvalue(),
"""\
ES\tESP\t724\tEspagne
DE\tDEU\t276\tAllemagne
FR\tFRA\t250\tFrance
""")
        # Revert output capturing
        sys.stdout = orig_stdout

    def test_08_show_requested_codes_with_variations_localized(self):
        """Check that requested codes are extracted although variations are used
        and then shown localized"""
        self.options.locale = "pt_BR"
        xml = xmlfile_3166.XMLFile_3166(self.options)
        self.assertTrue(xml is not None)
        # Temporarily capture output for testing purposes
        orig_stdout = sys.stdout
        sys.stdout = output = StringIO.StringIO()
        for code in ("es", "Deu", "250", "dEU"):
            xml.show_single_code(code)
        self.assertEqual(output.getvalue(),
"""\
ES\tESP\t724\tEspanha
DE\tDEU\t276\tAlemanha
FR\tFRA\t250\tFrança
DE\tDEU\t276\tAlemanha
""")
        # Revert output capturing
        sys.stdout = orig_stdout

    def test_09_show_warning_on_not_found_codes_localized(self):
        """Check that missing codes are reported, not dependend on locale"""
        self.options.locale = "es_ES"
        xml = xmlfile_3166.XMLFile_3166(self.options)
        self.assertTrue(xml is not None)
        for code in ("esalu", "hrg", "007"):
            self.assertRaises(CodeNotDefinedError,
                              xml.show_single_code, code)

    def test_10_show_requested_codes_and_warnings_localized(self):
        """Check that correct codes are shown localized and missing codes are reported"""
        self.options.locale = "ru"
        xml = xmlfile_3166.XMLFile_3166(self.options)
        self.assertTrue(xml is not None)
        # Temporarily capture output for testing purposes
        orig_stdout = sys.stdout
        sys.stdout = output = StringIO.StringIO()
        for code in ("de", "esalu", "hrg", "724", "007"):
            if code in ("esalu", "hrg", "007"):
                self.assertRaises(CodeNotDefinedError,
                                  xml.show_single_code, code)
            else:
                xml.show_single_code(code)
        # Ensure that the correct ISO codes generate an output
        self.assertEqual(output.getvalue(),
"""\
DE\tDEU\t276\tГермания
ES\tESP\t724\tИспания
""")
        # Revert output capturing
        sys.stdout = orig_stdout

    def test_11_show_all_codes_with_official_name(self):
        """Check that all codes are extracted and shown with their official name"""
        self.options.display_name = "official_name"
        xml = xmlfile_3166.XMLFile_3166(self.options)
        self.assertTrue(xml is not None)
        # Temporarily capture output for testing purposes
        orig_stdout = sys.stdout
        sys.stdout = output = StringIO.StringIO()
        xml.show_all_codes()
        self.assertEqual(output.getvalue(),
"""\
DE\tDEU\t276\tFederal Republic of Germany
FR\tFRA\t250\tFrench Republic
ES\tESP\t724\tKingdom of Spain
TW\tTWN\t158\tTaiwan, Province of China
""")
        # Revert output capturing
        sys.stdout = orig_stdout

    def test_12_show_all_codes_with_common_name(self):
        """Check that all codes are extracted and shown with their common name"""
        self.options.display_name = "common_name"
        xml = xmlfile_3166.XMLFile_3166(self.options)
        self.assertTrue(xml is not None)
        # Temporarily capture output for testing purposes
        orig_stdout = sys.stdout
        sys.stdout = output = StringIO.StringIO()
        xml.show_all_codes()
        self.assertEqual(output.getvalue(),
"""\
DE\tDEU\t276\tGermany
FR\tFRA\t250\tFrance
ES\tESP\t724\tSpain
TW\tTWN\t158\tTaiwan
""")
        # Revert output capturing
        sys.stdout = orig_stdout

    def test_13_show_all_codes_with_official_name_localized(self):
        """Check that all codes are extracted and shown with their localized official name"""
        self.options.locale = "uk"
        self.options.display_name = "official_name"
        xml = xmlfile_3166.XMLFile_3166(self.options)
        self.assertTrue(xml is not None)
        # Temporarily capture output for testing purposes
        orig_stdout = sys.stdout
        sys.stdout = output = StringIO.StringIO()
        xml.show_all_codes()
        self.assertEqual(output.getvalue(),
"""\
DE\tDEU\t276\tФедеративна Республіка Німеччина
FR\tFRA\t250\tФранцузька Республіка
ES\tESP\t724\tКоролівство Іспанія
TW\tTWN\t158\tТайвань, провінція Китаю
""")
        # Revert output capturing
        sys.stdout = orig_stdout

    def test_14_show_all_codes_with_common_name_localized(self):
        """Check that all codes are extracted and shown with their localized common name"""
        self.options.locale = "uk"
        self.options.display_name = "common_name"
        xml = xmlfile_3166.XMLFile_3166(self.options)
        self.assertTrue(xml is not None)
        # Temporarily capture output for testing purposes
        orig_stdout = sys.stdout
        sys.stdout = output = StringIO.StringIO()
        xml.show_all_codes()
        self.assertEqual(output.getvalue(),
"""\
DE\tDEU\t276\tНімеччина
FR\tFRA\t250\tФранція
ES\tESP\t724\tІспанія
TW\tTWN\t158\tТайвань
""")
        # Revert output capturing
        sys.stdout = orig_stdout

    def test_15_show_all_codes_with_null_character(self):
        """Check that all codes are extracted and separated with the null character"""
        self.options.use_null_character = True
        xml = xmlfile_3166.XMLFile_3166(self.options)
        self.assertTrue(xml is not None)
        # Temporarily capture output for testing purposes
        orig_stdout = sys.stdout
        sys.stdout = output = StringIO.StringIO()
        xml.show_all_codes()
        self.assertEqual(output.getvalue(),
"""\
DE\tDEU\t276\tGermany\0\
FR\tFRA\t250\tFrance\0\
ES\tESP\t724\tSpain\0\
TW\tTWN\t158\tTaiwan, Province of China\0\
""")
        # Revert output capturing
        sys.stdout = orig_stdout

suite = unittest.TestLoader().loadTestsFromTestCase(TestXMLFile_3166)
unittest.TextTestRunner(verbosity=2).run(suite)
