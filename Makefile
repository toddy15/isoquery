# Some convenience targets

pot:
	xgettext --output-dir=po/ --output=isoquery.pot --language=Python \
	  --add-comments=TRANSLATORS --msgid-bugs-address=toddy@debian.org isoquery/*py
.PHONY: pot

update-po:
	for i in po/*.po; do \
		msgmerge $$i po/isoquery.pot > tmp.po && mv tmp.po $$i ; \
	done
.PHONY: update-po

check:
	nosetests
.PHONY: check
