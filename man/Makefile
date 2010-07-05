# Copyright (C) 2007-2010 Tobias Quathamer
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

srcdir=.

# Extract the list of languages from the po4a config file.
LINGUAS = $(shell sed -ne 's/^.*\[po4a_langs\] \(.*\)$$/\1/p' $(srcdir)/isoquery.cfg)

clean:
	for lang in $(LINGUAS); do \
		if [ -d $(srcdir)/$$lang ]; then \
			rm -rf $(srcdir)/$$lang ; \
		fi ; \
		rm -f $(srcdir)/$$lang.po~ ; \
	done

.PHONY: update-po
update-po:
	po4a --no-backups --variable srcdir=$(srcdir) ./isoquery.cfg
