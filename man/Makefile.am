# automake options for Isoquery
#
# Copyright (C) 2007-2009 Tobias Quathamer
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

all-local: man.stamp

# FIXME: Use a stamp file until po4a supports them internally.
man.stamp:
	po4a --no-backups --variable srcdir=$(srcdir) \
		$(srcdir)/isoquery.cfg
	touch $@

clean-local:
	for lang in $(LINGUAS); do \
		if [ -d $(srcdir)/$$lang ]; then \
			rm -rf $(srcdir)/$$lang ; \
		fi ; \
		rm -f $(srcdir)/$$lang.po~ ; \
	done
	rm -f man.stamp

update-po:
	po4a --no-backups --force --variable srcdir=$(srcdir) ./isoquery.cfg

# Extract the list of languages from the po4a config file.
LINGUAS = $(shell sed -ne 's/^.*\[po4a_langs\] \(.*\)$$/\1/p' $(srcdir)/isoquery.cfg)

install-data-local:
	for lang in $(LINGUAS); do \
		if [ -d $(srcdir)/$$lang ]; then \
			files=$$(echo $(srcdir)/$$lang/*.[1-9]); \
			$(MAKE) install-man \
				mandir="$(mandir)/$$lang" \
				man_MANS="" \
				dist_man_MANS="$$files"; \
		fi \
	done

uninstall-local:
	for lang in $(LINGUAS); do \
		if [ -d $(srcdir)/$$lang ]; then \
			files=$$(echo $(srcdir)/$$lang/*.[1-9]); \
			$(MAKE) uninstall-man \
				mandir="$(mandir)/$$lang" \
				man_MANS="" \
				dist_man_MANS="$$files"; \
		fi \
	done

dist-hook: man.stamp
	cp $(srcdir)/man.stamp $(distdir)/
	for lang in $(LINGUAS); do \
		cp $(srcdir)/$$lang.po $(distdir)/; \
		cp $(srcdir)/$$lang.add $(distdir)/; \
		$(mkdir_p) $(distdir)/$$lang; \
		cp -r $(srcdir)/$$lang $(distdir)/; \
	done

dist_man_MANS = isoquery.1

EXTRA_DIST = isoquery.cfg isoquery-man.pot

.PHONY: update-po
