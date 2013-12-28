## Process this file with automake to produce Makefile.in.
#
# Copyright © 2013 Tobias Quathamer
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

ACLOCAL_AMFLAGS = -I m4

# This is needed for gettext, it is too much work to rewrite
# po/Makefile.in.in for a non-recursive approach.
SUBDIRS = po

EXTRA_DIST = vapi/config.vapi

bin_PROGRAMS = isoquery

isoquery_SOURCES = \
	src/isoquery.vala \
	src/optionparser.vala

VALAFLAGS = \
	--pkg libisocodes \
	--vapidir=vapi --pkg config

# Here are two quotes needed due to expansion by libtool
isoquery_CPPFLAGS = -include config.h -DLOCALEDIR=\""$(localedir)"\"
isoquery_CFLAGS = $(GOBJECT_CFLAGS) $(GLIB_CFLAGS) $(LIBISOCODES_CFLAGS)
isoquery_LDADD = $(GOBJECT_LIBS) $(GLIB_LIBS) $(LIBISOCODES_LIBS)
