#!/usr/bin/env python
# - encoding: UTF-8 -
#
# Copyright © 2012 Tobias Quathamer
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

from distutils.command.build import build
from distutils.command.clean import clean
from distutils.dep_util import newer
from distutils.core import setup

from isoquery import __version__

import sys
import os
import glob

data_files = []

docfiles = ["AUTHORS", "COPYING", "README", "TODO"]
data_files.append((os.path.join("share", "doc", "isoquery"), docfiles))

# The following code must only be executed upon clean
class custom_clean(clean):
    def run(self):
        clean.run(self)
        # Clean up previously generated files
        os.system("rm -rf build/mo")
        os.system("rm -rf build/man")

# The following code must only be executed upon build
class custom_build(build):
    def run(self):
        build.run(self)
        # Compile message catalogs
        pofiles = glob.glob(os.path.join("po", "*.po"))
        for pofile in pofiles:
            locale = os.path.basename(pofile)[:-3]
            directory = os.path.join("build", "mo", locale)
            if not os.path.exists(directory):
                os.makedirs(directory)
            mofile = os.path.join(directory, "isoquery.mo")
            if newer(pofile, mofile):
                result = os.system("msgfmt --check --output %s %s" % (mofile, pofile))
                if result != 0:
                    sys.stderr.write("Fatal error: the mo file could not be generated.\n")
                    sys.exit(1)
            directory = os.path.join("share", "locale", locale, "LC_MESSAGES")
            data_files.append((directory, [mofile]))
        
        # Generate manpage
        if not os.path.exists(os.path.join("build", "man")):
            os.makedirs(os.path.join("build", "man"))
        source = os.path.join("man", "isoquery.rst")
        dest = os.path.join("build", "man", "isoquery.1")
        gzip = os.path.join("build", "man", "isoquery.1.gz")
        if newer(source, dest):
            result = os.system("rst2man %s %s" % (source, dest))
            if result != 0:
                sys.stderr.write("Fatal error: the manpage could not be generated with rst2man.\n")
                sys.exit(1)
            result = os.system("gzip --force --best %s" % dest)
            if result != 0:
                sys.stderr.write("Fatal error: the manpage could not be compressed with gzip.\n")
                sys.exit(1)
        directory = os.path.join("share", "man", "man1")
        data_files.append((directory, [os.path.join("build", "man", "isoquery.1.gz")]))
        
        # Generate translated manpages
        pofiles = glob.glob(os.path.join("man", "*.po"))
        for pofile in pofiles:
            locale = os.path.basename(pofile)[:-3]
            directory = os.path.join("build", "man", locale)
            if not os.path.exists(directory):
                os.makedirs(directory)
            master = os.path.join("man", "isoquery.rst")
            addendum = pofile[:-3] + ".add"
            translation = os.path.join(directory, "isoquery.rst")
            if (newer(master, translation) or
                newer(pofile, translation) or
                newer(addendum, translation)):
                cmd = "po4a-translate --format text --option markdown " + \
                      "--master %s --po %s --addendum %s --localized %s" % (master, pofile, addendum, translation)
                result = os.system(cmd)
                if result != 0:
                    sys.stderr.write("Fatal error: the manpage could not be generated with po4a.\n")
                    sys.exit(1)
                # Generate manpage
                dest = os.path.join(directory, "isoquery.1")
                result = os.system("rst2man %s %s" % (translation, dest))
                if result != 0:
                    sys.stderr.write("Fatal error: the manpage could not be generated with rst2man.\n")
                    sys.exit(1)
                result = os.system("gzip --force --best %s" % dest)
                if result != 0:
                    sys.stderr.write("Fatal error: the manpage could not be compressed with gzip.\n")
                    sys.exit(1)
            directory = os.path.join("share", "man", "man1", locale)
            data_files.append((directory, [os.path.join("build", "man", locale, "isoquery.1.gz")]))


setup(
    name = "isoquery",
    version = __version__,
    description = "Search and display various ISO codes (country, language, ...)",
    author = "Tobias Quathamer",
    author_email = "toddy@debian.org",
    url = "http://alioth.debian.org/projects/pkg-isocodes",
    packages = ["isoquery"],
    scripts = ["bin/isoquery"],
    data_files = data_files,
    cmdclass = {"clean": custom_clean, "build": custom_build},
)
