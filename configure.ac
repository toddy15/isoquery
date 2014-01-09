# Process this file with autoconf to produce a configure script.
#
# Copyright © 2013-2014 Tobias Quathamer
#
# This file is part of isoquery.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# Set up autoconf
AC_PREREQ(2.69)
AC_INIT([isoquery], [1.8], [toddy@debian.org])
AC_CONFIG_HEADERS([config.h])
AC_CONFIG_AUX_DIR([build-aux])
AC_CONFIG_MACRO_DIR([m4])

# Set up automake
AM_INIT_AUTOMAKE([1.13 foreign subdir-objects silent-rules no-dist-gzip dist-xz])
AM_MAINTAINER_MODE

# Check for compilers and pkg-config
AM_PROG_VALAC([0.20])
AC_PROG_CC
AM_PROG_CC_C_O
PKG_PROG_PKG_CONFIG

# Set up gettext
AM_GNU_GETTEXT([external])
AM_GNU_GETTEXT_VERSION([0.18])
AC_DEFINE([GETTEXT_PACKAGE], ["isoquery"], [Gettext package name.])

# Detect the needed libraries
PKG_CHECK_MODULES([GOBJECT], [gobject-2.0])
PKG_CHECK_MODULES([GLIB], [glib-2.0])
PKG_CHECK_MODULES([LIBISOCODES], [libisocodes])

# Write configuration files
AC_CONFIG_FILES([
	Makefile
	po/Makefile.in
])

# Terminate script
AC_OUTPUT
