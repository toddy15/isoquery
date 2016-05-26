# Copyright © 2016 Dr. Tobias Quathamer <toddy@debian.org>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

AC_INIT([isoquery],[2.1.0])

AC_CONFIG_AUX_DIR([build])
AC_CONFIG_MACRO_DIR([build/m4])
AC_REQUIRE_AUX_FILE([tap-driver.sh])

AM_INIT_AUTOMAKE([dist-xz no-dist-gzip foreign subdir-objects])
AM_MAINTAINER_MODE

# Check for required programs
AC_PROG_CC
PKG_PROG_PKG_CONFIG

# Required libraries
PKG_CHECK_MODULES([GLIB], [glib-2.0])
PKG_CHECK_MODULES([JSON], [json-glib-1.0])

# Use testsuite
GLIB_TESTS

# Set up gettext
AM_GNU_GETTEXT([external])
AM_GNU_GETTEXT_VERSION([0.19])
AC_DEFINE([GETTEXT_PACKAGE], ["isoquery"], [Gettext package name.])

# Output
AC_CONFIG_FILES([
  Makefile
  po/Makefile.in
  src/Makefile
  tests/Makefile
])

AC_OUTPUT
