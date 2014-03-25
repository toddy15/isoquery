========
isoquery
========

Search and display various ISO codes (country, language, ...)
-------------------------------------------------------------

:Date:            2014-03-25
:Version:         2.0
:Manual section:  1


SYNOPSIS
========

**isoquery** [*options*] [*file*] [*ISO codes*]


DESCRIPTION
===========

This manual page documents briefly the **isoquery** command.
It can be used to generate a tabular output of the ISO standard
codes provided by the package **iso-codes**.
It parses the XML files and shows all included ISO codes or just
matching entries, if specified on the command line.
Moreover, it's possible to get all available translations for
the ISO standard.


OPTIONS
=======

This program follows the usual GNU command line syntax, with long options
starting with two dashes ('**-**'). **isoquery** supports the following options:

-i standard, --iso=standard  The ISO standard to use. Possible values: 639,
                             639-3, 3166, 3166-2, 4217, 15924 (default: 3166).

-x file, --xmlfile=file      Use another XML *file* with ISO data
                             (default: /usr/share/xml/iso-codes/iso_3166.xml).

-l locale, --locale=locale   Use this *locale* for output.

-n, --name                   Name for the supplied codes (default).

-o, --official_name          Official name for the supplied codes. This may be
                             the same as --name (only applies to ISO 3166).

-c, --common_name            Common name for the supplied codes. This may be
                             the same as --name (only applies to ISO 3166).

-0, --null                   Separate entries with a NULL character instead
                             of newline.

-h, --help                   Show summary of options.

-v, --version                Show program version and copyright.


EXAMPLES
========

If called without any command line options, **isoquery** will put out a
table of all ISO 3166 codes. The first three columns contain the alpha-2 code,
the alpha-3 code, and the numerical code assigned to the country listed
in the fourth column.

::

  $ isoquery
  AF      AFG     004     Afghanistan
  [...]
  ZW      ZWE     716     Zimbabwe

If you need only some countries, you can specify any of the codes in
the first three columns to cut down the output.

::

  $ isoquery so nor 484
  SO      SOM     706     Somalia
  NO      NOR     578     Norway
  MX      MEX     484     Mexico

Should you need the translations of the countries' names, just specify
in which *locale* you'd like to see the output.
Please note that the original English name will be shown if there is no
translation available for the specified *locale*.

::

    $ isoquery --locale=nl fr de es
    FR      FRA     250     Frankrijk
    DE      DEU     276     Duitsland
    ES      ESP     724     Spanje

All of the above works for different ISO standards as well, so you can
switch to the more extensive standard ISO 3166-2 by using the **--iso** command
line option. The columns are country code, subset type (e.g. State, Province,
etc.), ISO 3166-2 code, parent, and name. The fourth column
(parent) may be empty.

::

  $ isoquery --iso=3166-2
  AD      Parish          AD-07           Andorra la Vella
  [...]
  ZW      Province        ZW-MI           Midlands

For ISO 639, the first three columns are the ISO 639 2B code, the
ISO 639 2T code and the ISO 639-1 code. The third column may be empty.

::

  $ isoquery --iso=639
  aar     aar     aa      Afar
  abk     abk     ab      Abkhazian
  ace     ace             Achinese
  [...]
  zun     zun             Zuni
  zxx     zxx             No linguistic content; Not applicable
  zza     zza             Zaza; Dimili; Dimli; Kirdki; Kirmanjki; Zazaki

You can trim down the results by specifying only some codes. Moreover,
the option to get translated names is also available.

::

  $ isoquery --iso=639 --locale=pt vi bo kl
  vie     vie     vi      Vietnamita
  tib     bod     bo      tibetano
  kal     kal     kl      Kalaallisut; Greenlandic

If you want to use ISO 639-3, the displayed columns are id, scope, type,
part 1 code, part 2 code, and the language name. Both part 1 and part 2
may be empty.

::

  $ isoquery -i 639-3 aal new spa guc
  aal     I       L                       Afade
  new     I       L               new     Newari
  spa     I       L       es      spa     Spanish
  guc     I       L                       Wayuu

You can get selected translations of currency names from the ISO 4217
standard by using the following command. The first two columns are the
alpha-3 code and the numerical code assigned to the currency.

::

  $ isoquery --iso=4217 --locale=da cad 392
  CAD     124     Canadisk dollar
  JPY     392     Yen

If you need to get script names, you can use the ISO 15924 table.
The first two columns are the alpha-4 code and the numerical code
assigned to the script.

::

  $ isoquery --iso=15924 jpan latn 280
  Jpan    413     Japanese (alias for Han + Hiragana + Katakana)
  Latn    215     Latin
  Visp    280     Visible Speech


FILES
=====

By default, the XML files provided by the **iso-codes** package will be used.

| */usr/share/xml/iso-codes/iso_639.xml*
| */usr/share/xml/iso-codes/iso_639_3.xml*
| */usr/share/xml/iso-codes/iso_3166.xml*
| */usr/share/xml/iso-codes/iso_3166_2.xml*
| */usr/share/xml/iso-codes/iso_4217.xml*
| */usr/share/xml/iso-codes/iso_15924.xml*


AUTHOR
======

Tobias Quathamer <toddy@debian.org>
