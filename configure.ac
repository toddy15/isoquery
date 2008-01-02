# Configure options for Isoquery
# Process this file with autoconf to produce a configure script.
#
# Copyright (C) 2007-2008 Tobias Toedter
#
# This file is part of Isoquery.
# 
# Isoquery is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
# 
# Isoquery is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

AC_INIT([isoquery], [0.9], [Tobias Toedter <t.toedter@gmx.net>])
AM_MAINTAINER_MODE
AM_INIT_AUTOMAKE([foreign])

# setup for C++ language
AC_LANG([C++])
AC_PROG_CXX

# require needed headers
AC_CHECK_HEADERS([getopt.h])

# setup libxml++
AC_PATH_PROG(PKG_CONFIG, pkg-config)
if test -n "$PKG_CONFIG"; then
  vers=`$PKG_CONFIG --modversion libxml++-2.6 2>/dev/null | awk 'BEGIN { FS = "."; } { printf "%d", ($1 * 1000 + $2) * 1000 + $3;}'`
  if test -n "$vers" && test "$vers" -ge 2006000
  then
     LIBXML_LIBS="-lxml++-2.6"
     LIBXML_CFLAGS="`$PKG_CONFIG --cflags libxml++-2.6`"
  else
     AC_MSG_ERROR([You need at least libxml++ 2.6.0])
  fi
fi
AC_SUBST(LIBXML_LIBS)
AC_SUBST(LIBXML_CFLAGS)

# require gettext
AM_GNU_GETTEXT([external])
AM_GNU_GETTEXT_VERSION([0.16])
ALL_LINGUAS="de fr"

# Specify the Makefiles
AC_CONFIG_FILES(Makefile man/Makefile po/Makefile.in src/Makefile tests/Makefile)

# Write the configure script
AC_OUTPUT
