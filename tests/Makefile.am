# automake options for Isoquery
#
# Copyright (C) 2007-2008 Tobias Quathamer
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

tests = $(wildcard $(srcdir)/*.test)
EXTRA_DIST = $(tests)

check-local:
	@for test in $(tests); do \
		echo Testing $$test; \
		command=`sed -n -e "2p" $$test`; \
		$(top_builddir)/src/$$command > actual 2>&1; \
		sed -e "0,/# Expected output/d" $$test > expected; \
		diff -u expected actual; \
	done
	@rm -f expected actual
