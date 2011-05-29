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

import sys
import gettext
from lxml import etree
from code_not_defined_error import CodeNotDefinedError
translation = gettext.translation('isoquery', fallback=True)
_ = translation.ugettext

class XMLFile:
    """Generic class to handle common operations on XML files"""
    def __init__(self, options):
        self.xmlfile = options.xmlfile
        self.iso = options.iso
        self.locale = options.locale
        self.display_name = options.display_name
        self.use_null_character = options.use_null_character
        self.check_file()

    def check_file(self):
        """Test whether the given file meets the expectations"""
        try:
            self.xml = etree.parse(self.xmlfile)
        except IOError:
            sys.stderr.write(_(u"isoquery: The file '%(filename)s' could not " \
                               "be opened.\n").encode("utf-8") % {'filename': self.xmlfile})
            sys.exit(1)
        except etree.XMLSyntaxError:
            sys.stderr.write(_(u"isoquery: The file '%(filename)s' could not " \
                               "be parsed correctly.\n").encode("utf-8") % {'filename': self.xmlfile})
            sys.exit(1)
        root = self.xml.getroot()
        expected_tag = "iso_" + self.iso.replace('-', '_') + "_entries"
        if root.tag != expected_tag:
            sys.stderr.write(_(u"isoquery: The file '%(filename)s' does not contain " \
                               "valid ISO %(standard)s data.\n").encode("utf-8") % \
                               {'filename': self.xmlfile, 'standard': self.iso})
            sys.exit(1)

    def show_codes(self, arguments):
        """Show either all or only selected codes"""
        if (len(arguments) == 0):
            # Show all codes
            self.show_all_codes()
        else:
            # Show just the requested codes
            for code in arguments:
                try:
                    self.show_single_code(code)
                # TODO: Use 'except CodeNotDefinedError as code:'
                # when Python 2.5 is no longer supported (currently,
                # this enables backports to Lenny)
                except CodeNotDefinedError, code:
                    sys.stderr.write(_(u"isoquery: The code '%(code)s' is not " \
                                       "defined in ISO %(standard)s.\n").encode("utf-8") % \
                                       {"code": code.value, "standard": self.iso})

    def show_all_codes(self):
        """Show all codes"""
        wanted_tag = "iso_" + self.iso.replace('-', '_') + "_entry"
        for entry in self.xml.iter():
            if (entry.tag == wanted_tag):
                self.display_entry(entry)

    def show_single_code(self, code):
        """Show a single code"""
        code_not_found = True
        xpaths = self.get_xpaths(code)
        for xpath in xpaths:
            entries = self.xml.xpath(xpath)
            if (len(entries) == 1):
                code_not_found = False
                self.display_entry(entries[0])
                # Exit after successful match, to avoid matching the same
                # entry another time (can happen e.g. in ISO 639, where
                # most entries have the same value for their 2B and 2T code
                break
        if (code_not_found):
            raise CodeNotDefinedError(code)

    def display_entry(self, entry):
        # Set up translation infrastructure, if output locale is provided
        if self.locale != "":
            t = gettext.translation("iso_" + self.iso.replace('-', '_'),
                                    languages=[self.locale])
        output = []
        codes = self.get_display_codes()
        for code in codes:
            # Make sure there is an attribute
            value = entry.get(code)
            if value is not None:
                output.append(value)
            else:
                output.append("")
        names = self.get_display_names(self.display_name)
        for name in names:
            value = entry.get(name)
            if value is None:
                continue
            else:
                if self.locale != "":
                    output.append(t.ugettext(value))
                else:
                    output.append(value)
                break
        sys.stdout.write("\t".join(output).encode("utf-8"))
        if self.use_null_character:
            sys.stdout.write("\0")
        else:
            sys.stdout.write("\n")
