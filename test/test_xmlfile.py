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
import gettext
from isoquery import xmlfile
translation = gettext.translation('isoquery', fallback=True)
_ = translation.gettext

class Options:
    """Empty class to construct the command line options"""
    pass

class TestXMLFile(unittest.TestCase):
    def setUp(self):
        self.options = Options
        self.options.locale = ""
        self.options.display_name = "name"
        self.options.use_null_character = False
        self.options.iso = "3166"

    def test_01_non_existent_xmlfile(self):
        """Check that a non-existing file throws an Exception"""
        # Temporarily capture output for testing purposes
        orig_stderr = sys.stderr
        sys.stderr = output = StringIO.StringIO()
        self.options.xmlfile = "/does/not/exist"
        self.assertRaises(SystemExit, xmlfile.XMLFile, self.options)
        self.assertEqual(output.getvalue(),
                         _("isoquery: The file '%(filename)s' could not " \
                         "be opened.\n") % \
                         {'filename': self.options.xmlfile})
        # Revert output capturing
        sys.stderr = orig_stderr

    def test_02_empty_xmlfile(self):
        """Check that an empty file throws an Exception"""
        # Temporarily capture output for testing purposes
        orig_stderr = sys.stderr
        sys.stderr = output = StringIO.StringIO()
        self.options.xmlfile = StringIO.StringIO("")
        self.assertRaises(SystemExit, xmlfile.XMLFile, self.options)
        self.assertEqual(output.getvalue(),
                         _("isoquery: The file '%(filename)s' could not " \
                         "be parsed correctly.\n") % \
                         {'filename': self.options.xmlfile})
        # Revert output capturing
        sys.stderr = orig_stderr

    def test_03_wrong_xmlfile(self):
        """Check that a file with wrong XML data fails"""
        # Temporarily capture output for testing purposes
        orig_stderr = sys.stderr
        sys.stderr = output = StringIO.StringIO()
        self.options.xmlfile = StringIO.StringIO("<well><formed></formed></well>")
        self.assertRaises(SystemExit, xmlfile.XMLFile, self.options)
        self.assertEqual(output.getvalue(),
                         _("isoquery: The file '%(filename)s' does not " \
                         "contain valid ISO %(standard)s data.\n") % \
                         {'filename': self.options.xmlfile, 'standard': self.options.iso})
        # Revert output capturing
        sys.stderr = orig_stderr

    def test_04_minimal_xmlfile(self):
        """Check that a minimal file with correct data succeeds"""
        self.options.xmlfile = StringIO.StringIO("<iso_3166_entries></iso_3166_entries>")
        xml = xmlfile.XMLFile(self.options)
        self.assertTrue(xml is not None)

suite = unittest.TestLoader().loadTestsFromTestCase(TestXMLFile)
unittest.TextTestRunner(verbosity=2).run(suite)
