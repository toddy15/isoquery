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
from isoquery import xmlfile_3166_2
from isoquery.code_not_defined_error import CodeNotDefinedError


class Options:
    """Empty class to construct the command line options"""
    pass

class TestXMLFile_3166_2(unittest.TestCase):
    def setUp(self):
        self.options = Options
        self.options.locale = ""
        self.options.display_name = "name"
        self.options.use_null_character = False
        self.options.iso = "3166-2"
        self.options.xmlfile = StringIO.StringIO("""
<iso_3166_2_entries>
	<!-- Malawi -->
<iso_3166_country code="MW">
<iso_3166_subset type="Region">
	<iso_3166_2_entry
		code="MW C"	name="Central Region" />
	<iso_3166_2_entry
		code="MW N"	name="Northern Region" />
	<iso_3166_2_entry
		code="MW S"	name="Southern Region" />
</iso_3166_subset>
<iso_3166_subset type="District">
	<iso_3166_2_entry
		code="MW-BA"	name="Balaka"	parent="S" />
	<iso_3166_2_entry
		code="MW-BL"	name="Blantyre"	parent="S" />
	<iso_3166_2_entry
		code="MW-CK"	name="Chikwawa"	parent="S" />
	<iso_3166_2_entry
		code="MW-CR"	name="Chiradzulu"	parent="S" />
	<iso_3166_2_entry
		code="MW-CT"	name="Chitipa"	parent="N" />
	<iso_3166_2_entry
		code="MW-DE"	name="Dedza"	parent="C" />
	<iso_3166_2_entry
		code="MW-DO"	name="Dowa"	parent="C" />
	<iso_3166_2_entry
		code="MW-KR"	name="Karonga"	parent="N" />
	<iso_3166_2_entry
		code="MW-KS"	name="Kasungu"	parent="C" />
	<iso_3166_2_entry
		code="MW-LK"	name="Likoma"	parent="N" />
	<iso_3166_2_entry
		code="MW-LI"	name="Lilongwe"	parent="C" />
	<iso_3166_2_entry
		code="MW-MH"	name="Machinga"	parent="S" />
	<iso_3166_2_entry
		code="MW-MG"	name="Mangochi"	parent="S" />
	<iso_3166_2_entry
		code="MW-MC"	name="Mchinji"	parent="C" />
	<iso_3166_2_entry
		code="MW-MU"	name="Mulanje"	parent="S" />
	<iso_3166_2_entry
		code="MW-MW"	name="Mwanza"	parent="S" />
	<iso_3166_2_entry
		code="MW-MZ"	name="Mzimba"	parent="N" />
	<iso_3166_2_entry
		code="MW-NE"	name="Neno"	parent="N" />
	<iso_3166_2_entry
		code="MW-NB"	name="Nkhata Bay"	parent="N" />
	<iso_3166_2_entry
		code="MW-NK"	name="Nkhotakota"	parent="C" />
	<iso_3166_2_entry
		code="MW-NS"	name="Nsanje"	parent="S" />
	<iso_3166_2_entry
		code="MW-NU"	name="Ntcheu"	parent="C" />
	<iso_3166_2_entry
		code="MW-NI"	name="Ntchisi"	parent="C" />
	<iso_3166_2_entry
		code="MW-PH"	name="Phalombe"	parent="S" />
	<iso_3166_2_entry
		code="MW-RU"	name="Rumphi"	parent="N" />
	<iso_3166_2_entry
		code="MW-SA"	name="Salima"	parent="C" />
	<iso_3166_2_entry
		code="MW-TH"	name="Thyolo"	parent="S" />
	<iso_3166_2_entry
		code="MW-ZO"	name="Zomba"	parent="S" />
</iso_3166_subset>
</iso_3166_country>
	<!-- New Zealand -->
<iso_3166_country code="NZ">
<iso_3166_subset type="Island">
	<iso_3166_2_entry
		code="NZ-N"	name="North Island" />
	<iso_3166_2_entry
		code="NZ-S"	name="South Island" />
</iso_3166_subset>
<iso_3166_subset type="Regional council">
	<iso_3166_2_entry
		code="NZ-AUK"	name="Auckland"	parent="N" />
	<iso_3166_2_entry
		code="NZ-BOP"	name="Bay of Plenty"	parent="N" />
	<iso_3166_2_entry
		code="NZ-CAN"	name="Canterbury"	parent="S" />
	<iso_3166_2_entry
		code="NZ-HKB"	name="Hawke's Bay"	parent="N" />
	<iso_3166_2_entry
		code="NZ-MWT"	name="Manawatu-Wanganui"	parent="N" />
	<iso_3166_2_entry
		code="NZ-NTL"	name="Northland"	parent="N" />
	<iso_3166_2_entry
		code="NZ-OTA"	name="Otago"	parent="S" />
	<iso_3166_2_entry
		code="NZ-STL"	name="Southland"	parent="S" />
	<iso_3166_2_entry
		code="NZ-TKI"	name="Taranaki"	parent="N" />
	<iso_3166_2_entry
		code="NZ-WKO"	name="Waikato"	parent="N" />
	<iso_3166_2_entry
		code="NZ-WGN"	name="Wellington"	parent="N" />
	<iso_3166_2_entry
		code="NZ-WTC"	name="West Coast"	parent="S" />
</iso_3166_subset>
<iso_3166_subset type="Unitary authority">
	<iso_3166_2_entry
		code="NZ-GIS"	name="Gisborne District"	parent="N" />
	<iso_3166_2_entry
		code="NZ-MBH"	name="Marlborough District"	parent="S" />
	<iso_3166_2_entry
		code="NZ-NSN"	name="Nelson City"	parent="S" />
	<iso_3166_2_entry
		code="NZ-TAS"	name="Tasman District"	parent="S" />
</iso_3166_subset>
<iso_3166_subset type="Special island authority">
	<iso_3166_2_entry
		code="NZ-CIT"	name="Chatham Islands Territory" />
</iso_3166_subset>
</iso_3166_country>
</iso_3166_2_entries>""")

    def test_01_show_all_codes(self):
        """Check that all codes are extracted"""
        xml = xmlfile_3166_2.XMLFile_3166_2(self.options)
        self.assertTrue(xml is not None)
        # Temporarily capture output for testing purposes
        orig_stdout = sys.stdout
        sys.stdout = output = StringIO.StringIO()
        xml.show_all_codes()
        self.assertEqual(output.getvalue(),
"""\
MW\tRegion\tMW C\t\tCentral Region
MW\tRegion\tMW N\t\tNorthern Region
MW\tRegion\tMW S\t\tSouthern Region
MW\tDistrict\tMW-BA\tS\tBalaka
MW\tDistrict\tMW-BL\tS\tBlantyre
MW\tDistrict\tMW-CK\tS\tChikwawa
MW\tDistrict\tMW-CR\tS\tChiradzulu
MW\tDistrict\tMW-CT\tN\tChitipa
MW\tDistrict\tMW-DE\tC\tDedza
MW\tDistrict\tMW-DO\tC\tDowa
MW\tDistrict\tMW-KR\tN\tKaronga
MW\tDistrict\tMW-KS\tC\tKasungu
MW\tDistrict\tMW-LK\tN\tLikoma
MW\tDistrict\tMW-LI\tC\tLilongwe
MW\tDistrict\tMW-MH\tS\tMachinga
MW\tDistrict\tMW-MG\tS\tMangochi
MW\tDistrict\tMW-MC\tC\tMchinji
MW\tDistrict\tMW-MU\tS\tMulanje
MW\tDistrict\tMW-MW\tS\tMwanza
MW\tDistrict\tMW-MZ\tN\tMzimba
MW\tDistrict\tMW-NE\tN\tNeno
MW\tDistrict\tMW-NB\tN\tNkhata Bay
MW\tDistrict\tMW-NK\tC\tNkhotakota
MW\tDistrict\tMW-NS\tS\tNsanje
MW\tDistrict\tMW-NU\tC\tNtcheu
MW\tDistrict\tMW-NI\tC\tNtchisi
MW\tDistrict\tMW-PH\tS\tPhalombe
MW\tDistrict\tMW-RU\tN\tRumphi
MW\tDistrict\tMW-SA\tC\tSalima
MW\tDistrict\tMW-TH\tS\tThyolo
MW\tDistrict\tMW-ZO\tS\tZomba
NZ\tIsland\tNZ-N\t\tNorth Island
NZ\tIsland\tNZ-S\t\tSouth Island
NZ\tRegional council\tNZ-AUK\tN\tAuckland
NZ\tRegional council\tNZ-BOP\tN\tBay of Plenty
NZ\tRegional council\tNZ-CAN\tS\tCanterbury
NZ\tRegional council\tNZ-HKB\tN\tHawke's Bay
NZ\tRegional council\tNZ-MWT\tN\tManawatu-Wanganui
NZ\tRegional council\tNZ-NTL\tN\tNorthland
NZ\tRegional council\tNZ-OTA\tS\tOtago
NZ\tRegional council\tNZ-STL\tS\tSouthland
NZ\tRegional council\tNZ-TKI\tN\tTaranaki
NZ\tRegional council\tNZ-WKO\tN\tWaikato
NZ\tRegional council\tNZ-WGN\tN\tWellington
NZ\tRegional council\tNZ-WTC\tS\tWest Coast
NZ\tUnitary authority\tNZ-GIS\tN\tGisborne District
NZ\tUnitary authority\tNZ-MBH\tS\tMarlborough District
NZ\tUnitary authority\tNZ-NSN\tS\tNelson City
NZ\tUnitary authority\tNZ-TAS\tS\tTasman District
NZ\tSpecial island authority\tNZ-CIT\t\tChatham Islands Territory
""")
        # Revert output capturing
        sys.stdout = orig_stdout

    def test_02_show_requested_codes(self):
        """Check that requested codes are extracted"""
        xml = xmlfile_3166_2.XMLFile_3166_2(self.options)
        self.assertTrue(xml is not None)
        # Temporarily capture output for testing purposes
        orig_stdout = sys.stdout
        sys.stdout = output = StringIO.StringIO()
        for code in ("NZ-AUK", "MW C", "MW-RU"):
            xml.show_single_code(code)
        self.assertEqual(output.getvalue(),
"""\
NZ\tRegional council\tNZ-AUK\tN\tAuckland
MW\tRegion\tMW C\t\tCentral Region
MW\tDistrict\tMW-RU\tN\tRumphi
""")
        # Revert output capturing
        sys.stdout = orig_stdout

    def test_03_show_requested_codes_with_variations(self):
        """Check that requested codes are extracted although variations are used"""
        xml = xmlfile_3166_2.XMLFile_3166_2(self.options)
        self.assertTrue(xml is not None)
        # Temporarily capture output for testing purposes
        orig_stdout = sys.stdout
        sys.stdout = output = StringIO.StringIO()
        for code in ("mw n", "NZ-Wgn", "nz-ota"):
            xml.show_single_code(code)
        self.assertEqual(output.getvalue(),
"""\
MW\tRegion\tMW N\t\tNorthern Region
NZ\tRegional council\tNZ-WGN\tN\tWellington
NZ\tRegional council\tNZ-OTA\tS\tOtago
""")
        # Revert output capturing
        sys.stdout = orig_stdout

    def test_04_show_warning_on_not_found_codes(self):
        """Check that missing codes are reported"""
        xml = xmlfile_3166_2.XMLFile_3166_2(self.options)
        self.assertTrue(xml is not None)
        for code in ("NZ-NON", "hrg", "007"):
            self.assertRaises(CodeNotDefinedError,
                              xml.show_single_code, code)

    def test_05_show_requested_codes_and_warnings(self):
        """Check that correct codes are shown and missing codes are reported"""
        xml = xmlfile_3166_2.XMLFile_3166_2(self.options)
        self.assertTrue(xml is not None)
        # Temporarily capture output for testing purposes
        orig_stdout = sys.stdout
        sys.stdout = output = StringIO.StringIO()
        for code in ("NZ-HKB", "esalu", "hrg", "MW-NK", "007"):
            if code in ("esalu", "hrg", "007"):
                self.assertRaises(CodeNotDefinedError,
                                  xml.show_single_code, code)
            else:
                xml.show_single_code(code)
        # Ensure that the correct ISO codes generate an output
        self.assertEqual(output.getvalue(),
"""\
NZ\tRegional council\tNZ-HKB\tN\tHawke's Bay
MW\tDistrict\tMW-NK\tC\tNkhotakota
""")
        # Revert output capturing
        sys.stdout = orig_stdout

    def test_06_show_all_codes_localized(self):
        """Check that all codes are extracted and shown localized"""
        self.options.locale = "fr"
        xml = xmlfile_3166_2.XMLFile_3166_2(self.options)
        self.assertTrue(xml is not None)
        # Temporarily capture output for testing purposes
        orig_stdout = sys.stdout
        sys.stdout = output = StringIO.StringIO()
        xml.show_all_codes()
        self.assertEqual(output.getvalue(),
"""\
MW\tRegion\tMW C\t\tRégion centrale
MW\tRegion\tMW N\t\tRégion septentrionale
MW\tRegion\tMW S\t\tRégion méridionale
MW\tDistrict\tMW-BA\tS\tBalaka
MW\tDistrict\tMW-BL\tS\tBlantyre
MW\tDistrict\tMW-CK\tS\tChikwawa
MW\tDistrict\tMW-CR\tS\tChiradzulu
MW\tDistrict\tMW-CT\tN\tChitipa
MW\tDistrict\tMW-DE\tC\tDedza
MW\tDistrict\tMW-DO\tC\tDowa
MW\tDistrict\tMW-KR\tN\tKaronga
MW\tDistrict\tMW-KS\tC\tKasungu
MW\tDistrict\tMW-LK\tN\tLikoma
MW\tDistrict\tMW-LI\tC\tLilongwe
MW\tDistrict\tMW-MH\tS\tMachinga
MW\tDistrict\tMW-MG\tS\tMangochi
MW\tDistrict\tMW-MC\tC\tMchinji
MW\tDistrict\tMW-MU\tS\tMulanje
MW\tDistrict\tMW-MW\tS\tMwanza
MW\tDistrict\tMW-MZ\tN\tMzimba
MW\tDistrict\tMW-NE\tN\tNeno
MW\tDistrict\tMW-NB\tN\tBaie de Nkhata
MW\tDistrict\tMW-NK\tC\tNkhotakota
MW\tDistrict\tMW-NS\tS\tNsanje
MW\tDistrict\tMW-NU\tC\tNtcheu
MW\tDistrict\tMW-NI\tC\tNtchisi
MW\tDistrict\tMW-PH\tS\tPhalombe
MW\tDistrict\tMW-RU\tN\tRumphi
MW\tDistrict\tMW-SA\tC\tSalima
MW\tDistrict\tMW-TH\tS\tThyolo
MW\tDistrict\tMW-ZO\tS\tZomba
NZ\tIsland\tNZ-N\t\tÎle du Nord
NZ\tIsland\tNZ-S\t\tÎle du Sud
NZ\tRegional council\tNZ-AUK\tN\tAuckland
NZ\tRegional council\tNZ-BOP\tN\tBaie de Plenty
NZ\tRegional council\tNZ-CAN\tS\tCanterbury
NZ\tRegional council\tNZ-HKB\tN\tBaie de Hawke
NZ\tRegional council\tNZ-MWT\tN\tManawatu-Wanganui
NZ\tRegional council\tNZ-NTL\tN\tPays du Nord
NZ\tRegional council\tNZ-OTA\tS\tOtago
NZ\tRegional council\tNZ-STL\tS\tPays du Sud
NZ\tRegional council\tNZ-TKI\tN\tTaranaki
NZ\tRegional council\tNZ-WKO\tN\tWaikato
NZ\tRegional council\tNZ-WGN\tN\tWellington
NZ\tRegional council\tNZ-WTC\tS\tCôte occidentale
NZ\tUnitary authority\tNZ-GIS\tN\tDistrict de Gisborne
NZ\tUnitary authority\tNZ-MBH\tS\tDistrict de Marlborough
NZ\tUnitary authority\tNZ-NSN\tS\tNelson City
NZ\tUnitary authority\tNZ-TAS\tS\tDistrict de Tasmanie
NZ\tSpecial island authority\tNZ-CIT\t\tTerritoire des îles Chatham
""")
        # Revert output capturing
        sys.stdout = orig_stdout

    def test_07_show_requested_codes_localized(self):
        """Check that requested codes are extracted and shown localized"""
        self.options.locale = "fr"
        xml = xmlfile_3166_2.XMLFile_3166_2(self.options)
        self.assertTrue(xml is not None)
        # Temporarily capture output for testing purposes
        orig_stdout = sys.stdout
        sys.stdout = output = StringIO.StringIO()
        for code in ("MW S", "MW-LK", "NZ-WTC"):
            xml.show_single_code(code)
        self.assertEqual(output.getvalue(),
"""\
MW\tRegion\tMW S\t\tRégion méridionale
MW\tDistrict\tMW-LK\tN\tLikoma
NZ\tRegional council\tNZ-WTC\tS\tCôte occidentale
""")
        # Revert output capturing
        sys.stdout = orig_stdout

    def test_08_show_requested_codes_with_variations_localized(self):
        """Check that requested codes are extracted although variations are used
        and then shown localized"""
        self.options.locale = "fr"
        xml = xmlfile_3166_2.XMLFile_3166_2(self.options)
        self.assertTrue(xml is not None)
        # Temporarily capture output for testing purposes
        orig_stdout = sys.stdout
        sys.stdout = output = StringIO.StringIO()
        for code in ("MW s", "Mw-Lk", "nz-wtc"):
            xml.show_single_code(code)
        self.assertEqual(output.getvalue(),
"""\
MW\tRegion\tMW S\t\tRégion méridionale
MW\tDistrict\tMW-LK\tN\tLikoma
NZ\tRegional council\tNZ-WTC\tS\tCôte occidentale
""")
        # Revert output capturing
        sys.stdout = orig_stdout

    def test_09_show_warning_on_not_found_codes_localized(self):
        """Check that missing codes are reported, not dependend on locale"""
        self.options.locale = "fr"
        xml = xmlfile_3166_2.XMLFile_3166_2(self.options)
        self.assertTrue(xml is not None)
        for code in ("esalu", "hrg", "007"):
            self.assertRaises(CodeNotDefinedError,
                              xml.show_single_code, code)

    def test_10_show_requested_codes_and_warnings_localized(self):
        """Check that correct codes are shown localized and missing codes are reported"""
        self.options.locale = "fr"
        xml = xmlfile_3166_2.XMLFile_3166_2(self.options)
        self.assertTrue(xml is not None)
        # Temporarily capture output for testing purposes
        orig_stdout = sys.stdout
        sys.stdout = output = StringIO.StringIO()
        for code in ("MW S", "esalu", "hrg", "MW-LK", "007"):
            if code in ("esalu", "hrg", "007"):
                self.assertRaises(CodeNotDefinedError,
                                  xml.show_single_code, code)
            else:
                xml.show_single_code(code)
        # Ensure that the correct ISO codes generate an output
        self.assertEqual(output.getvalue(),
"""\
MW\tRegion\tMW S\t\tRégion méridionale
MW\tDistrict\tMW-LK\tN\tLikoma
""")
        # Revert output capturing
        sys.stdout = orig_stdout

    def test_11_show_all_codes_with_null_character(self):
        """Check that all codes are extracted and separated with the null character"""
        self.options.use_null_character = True
        xml = xmlfile_3166_2.XMLFile_3166_2(self.options)
        self.assertTrue(xml is not None)
        # Temporarily capture output for testing purposes
        orig_stdout = sys.stdout
        sys.stdout = output = StringIO.StringIO()
        xml.show_all_codes()
        self.assertEqual(output.getvalue(),
"""\
MW\tRegion\tMW C\t\tCentral Region\0\
MW\tRegion\tMW N\t\tNorthern Region\0\
MW\tRegion\tMW S\t\tSouthern Region\0\
MW\tDistrict\tMW-BA\tS\tBalaka\0\
MW\tDistrict\tMW-BL\tS\tBlantyre\0\
MW\tDistrict\tMW-CK\tS\tChikwawa\0\
MW\tDistrict\tMW-CR\tS\tChiradzulu\0\
MW\tDistrict\tMW-CT\tN\tChitipa\0\
MW\tDistrict\tMW-DE\tC\tDedza\0\
MW\tDistrict\tMW-DO\tC\tDowa\0\
MW\tDistrict\tMW-KR\tN\tKaronga\0\
MW\tDistrict\tMW-KS\tC\tKasungu\0\
MW\tDistrict\tMW-LK\tN\tLikoma\0\
MW\tDistrict\tMW-LI\tC\tLilongwe\0\
MW\tDistrict\tMW-MH\tS\tMachinga\0\
MW\tDistrict\tMW-MG\tS\tMangochi\0\
MW\tDistrict\tMW-MC\tC\tMchinji\0\
MW\tDistrict\tMW-MU\tS\tMulanje\0\
MW\tDistrict\tMW-MW\tS\tMwanza\0\
MW\tDistrict\tMW-MZ\tN\tMzimba\0\
MW\tDistrict\tMW-NE\tN\tNeno\0\
MW\tDistrict\tMW-NB\tN\tNkhata Bay\0\
MW\tDistrict\tMW-NK\tC\tNkhotakota\0\
MW\tDistrict\tMW-NS\tS\tNsanje\0\
MW\tDistrict\tMW-NU\tC\tNtcheu\0\
MW\tDistrict\tMW-NI\tC\tNtchisi\0\
MW\tDistrict\tMW-PH\tS\tPhalombe\0\
MW\tDistrict\tMW-RU\tN\tRumphi\0\
MW\tDistrict\tMW-SA\tC\tSalima\0\
MW\tDistrict\tMW-TH\tS\tThyolo\0\
MW\tDistrict\tMW-ZO\tS\tZomba\0\
NZ\tIsland\tNZ-N\t\tNorth Island\0\
NZ\tIsland\tNZ-S\t\tSouth Island\0\
NZ\tRegional council\tNZ-AUK\tN\tAuckland\0\
NZ\tRegional council\tNZ-BOP\tN\tBay of Plenty\0\
NZ\tRegional council\tNZ-CAN\tS\tCanterbury\0\
NZ\tRegional council\tNZ-HKB\tN\tHawke's Bay\0\
NZ\tRegional council\tNZ-MWT\tN\tManawatu-Wanganui\0\
NZ\tRegional council\tNZ-NTL\tN\tNorthland\0\
NZ\tRegional council\tNZ-OTA\tS\tOtago\0\
NZ\tRegional council\tNZ-STL\tS\tSouthland\0\
NZ\tRegional council\tNZ-TKI\tN\tTaranaki\0\
NZ\tRegional council\tNZ-WKO\tN\tWaikato\0\
NZ\tRegional council\tNZ-WGN\tN\tWellington\0\
NZ\tRegional council\tNZ-WTC\tS\tWest Coast\0\
NZ\tUnitary authority\tNZ-GIS\tN\tGisborne District\0\
NZ\tUnitary authority\tNZ-MBH\tS\tMarlborough District\0\
NZ\tUnitary authority\tNZ-NSN\tS\tNelson City\0\
NZ\tUnitary authority\tNZ-TAS\tS\tTasman District\0\
NZ\tSpecial island authority\tNZ-CIT\t\tChatham Islands Territory\0\
""")
        # Revert output capturing
        sys.stdout = orig_stdout

suite = unittest.TestLoader().loadTestsFromTestCase(TestXMLFile_3166_2)
unittest.TextTestRunner(verbosity=2).run(suite)
