# Some convenience targets

pot:
	xgettext --output-dir=po/ --output=isoquery.pot --language=Python \
	  --add-comments=TRANSLATORS --msgid-bugs-address=toddy@debian.org isoquery/*py
.PHONY: pot

update-po:
	for i in po/*.po; do \
		msgmerge --previous $$i po/isoquery.pot > tmp.po && mv tmp.po $$i ; \
	done
.PHONY: update-po

pot-man:
	po4a-gettextize --format text --option markdown \
	--master man/isoquery.rst --master-charset UTF-8 \
	--po man/isoquery-man.pot
	# Remove location lines
	sed -i -e "/^#: /d" man/isoquery-man.pot
.PHONY: pot-man

update-po-man:
	for i in man/*.po; do \
		msgmerge --previous --no-location $$i man/isoquery-man.pot > tmp.po && mv tmp.po $$i ; \
	done
.PHONY: update-po-man

check:
	nosetests
.PHONY: check
