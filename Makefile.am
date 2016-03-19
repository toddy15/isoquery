# Copyright © 2016 Dr. Tobias Quathamer

SUBDIRS = src tests

# Create and install english manpage
EXTRA_DIST += man/isoquery.rst man/isoquery-man.pot
man1_MANS = isoquery.1
CLEANFILES = isoquery.1
isoquery.1:
	$(RST2MAN) $(top_srcdir)/man/isoquery.rst isoquery.1

# Create and install german manpage
EXTRA_DIST += man/de.po man/de.add
man_dedir = $(mandir)/de/man1
man_de_DATA = man_de/isoquery.1
man_de/isoquery.1: man/isoquery.rst man/de.po man/de.add
	$(MKDIR_P) man_de
	po4a-translate --format text --option markdown \
	--master $(top_srcdir)/man/isoquery.rst \
	--po $(top_srcdir)/man/de.po \
	--addendum $(top_srcdir)/man/de.add \
	--localized man_de/isoquery.rst
	$(RST2MAN) man_de/isoquery.rst man_de/isoquery.1

# Create and install french manpage
EXTRA_DIST += man/fr.po man/fr.add
man_frdir = $(mandir)/fr/man1
man_fr_DATA = man_fr/isoquery.1
man_fr/isoquery.1: man/isoquery.rst man/fr.po man/fr.add
	$(MKDIR_P) man_fr
	po4a-translate --format text --option markdown \
	--master $(top_srcdir)/man/isoquery.rst \
	--po $(top_srcdir)/man/fr.po \
	--addendum $(top_srcdir)/man/fr.add \
	--localized man_fr/isoquery.rst
	$(RST2MAN) man_fr/isoquery.rst man_fr/isoquery.1

# Create and install portuguese manpage
EXTRA_DIST += man/pt.po man/pt.add
man_ptdir = $(mandir)/pt/man1
man_pt_DATA = man_pt/isoquery.1
man_pt/isoquery.1: man/isoquery.rst man/pt.po man/pt.add
	$(MKDIR_P) man_pt
	po4a-translate --format text --option markdown \
	--master $(top_srcdir)/man/isoquery.rst \
	--po $(top_srcdir)/man/pt.po \
	--addendum $(top_srcdir)/man/pt.add \
	--localized man_pt/isoquery.rst
	$(RST2MAN) man_pt/isoquery.rst man_pt/isoquery.1

# Remove temporary build directories for translated manpages
clean-local:
	-rm -rf man_de man_fr man_pt

# Some convenience targets for manpage generation
pot-man:
	po4a-gettextize --format text --option markdown \
	--master $(top_srcdir)/man/isoquery.rst --master-charset UTF-8 \
	--po $(top_srcdir)/man/isoquery-man.pot
	sed -i -e "/^#: /d" $(top_srcdir)/man/isoquery-man.pot
.PHONY: pot-man

update-po-man:
	for i in $(top_srcdir)/man/*.po; do \
		msgmerge --previous --no-location $$i $(top_srcdir)/man/isoquery-man.pot > tmp.po && mv tmp.po $$i ; \
	done
.PHONY: update-po-man
