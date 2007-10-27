# automake options for Isoquery
#
# Copyright (C) 2007 Tobias Toedter
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

bin_PROGRAMS = isoquery
isoquery_SOURCES = \
	isoquery.cpp \
	option_parser.cpp \
	option_parser.h \
	xmldata.cpp \
	xmldata.h \
	gettext.h

# Add include path found by configure
INCLUDES= $(all_includes) $(LIBXML_CFLAGS)

# Add library search path
isoquery_LDFLAGS = $(all_libraries) $(LIBXML_LIBS)
