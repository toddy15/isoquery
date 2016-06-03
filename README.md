Isoquery
========

[![Build Status](https://travis-ci.org/toddy15/isoquery.svg?branch=master)](https://travis-ci.org/toddy15/isoquery)

Search and display ISO codes for countries, languages, currencies, and scripts.

Isoquery can be used to generate a tabular output of the ISO standard
codes provided by the package iso-codes. It parses the JSON files and shows
all included ISO codes or just matching entries, if specified on the command
line. Moreover, it's possible to get all available translations for
the ISO standard.

Dependencies
------------

In order to build the program from source, you need rst2man, po4a,
and gettext.

It's also very useful to have iso-codes installed, although this is
not strictly necessary.

Installation
------------

Just run "./configure && make install".

Author and Copyright
--------------------

Copyright © Dr. Tobias Quathamer <toddy@debian.org>

License
-------

This program is released under the GNU General Public License version 3,
see COPYING for details.
