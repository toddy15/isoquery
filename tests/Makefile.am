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

include $(top_srcdir)/build/glib-tap.mk

# Include data and test files directories
EXTRA_DIST += data expected

AM_CPPFLAGS = -I$(top_srcdir)/src $(GLIB_CFLAGS) $(JSON_CFLAGS)
LDADD = $(GLIB_LIBS) $(JSON_LIBS) $(top_builddir)/src/options.o

# test binaries
test_programs = options integration

integration_CPPFLAGS = -DTESTDIR=\"$(srcdir)\" $(AM_CPPFLAGS)
