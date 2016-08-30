========
isoquery
========

Search and display various ISO codes (country, language, ...)
-------------------------------------------------------------

:Date:            2016-08-30
:Version:         3.2.1
:Manual section:  1


SYNOPSIS
========

**isoquery** [*OPTION...*] [*ISO codes*]


DESCRIPTION
===========

This manual page documents briefly the **isoquery** command.
It can be used to generate a tabular output of the ISO standard
codes provided by the package **iso-codes**.
It parses the JSON files and shows all included ISO codes or just
matching entries, if specified on the command line.
Moreover, it's possible to get all available translations for
the ISO standard.


OPTIONS
=======

This program follows the usual GNU command line syntax, with long options
starting with two dashes ('**-**'). **isoquery** supports the following options:

-i STANDARD, --iso=STANDARD  The ISO standard to use. Possible values: 639-2,
                             639-3, 639-5, 3166-1, 3166-2, 3166-3, 4217, 15924
                             (default: 3166-1)

-p PATHNAME, --pathname=PATHNAME  Use *PATHNAME* as prefix for the data files
                                  (default: /usr/share/iso-codes/json)

-l LOCALE, --locale=LOCALE   Use this *LOCALE* for output

-n, --name                   Name for the supplied codes (default)

-o, --official_name          Official name for the supplied codes. This may be
                             the same as --name (only applies to ISO 3166-1)

-c, --common_name            Common name for the supplied codes. This may be
                             the same as --name (only applies to ISO 639-2,
                             639-3, and 3166-1)

-0, --null                   Separate entries with a NULL character instead
                             of newline

-h, --help                   Show summary of options

-v, --version                Show program version and copyright


EXAMPLES
========

If called without any command line options, **isoquery** will put out a
table of all ISO 3166-1 codes. The first three columns contain the alpha-2 code,
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
in which *LOCALE* you'd like to see the output.
Please note that the original English name will be shown if there is no
translation available for the specified *LOCALE*.

::

    $ isoquery --locale=nl fr de es
    FR      FRA     250     Frankrijk
    DE      DEU     276     Duitsland
    ES      ESP     724     Spanje

All of the above works for different ISO standards as well, so you can
switch to the more extensive standard ISO 3166-2 by using the **--iso** command
line option. The columns are ISO 3166-2 code, subset type (e.g. State, Province,
etc.), parent, and name. The third column
(parent) may be empty.

::

  $ isoquery --iso=3166-2
  AD-02   Parish          Canillo
  [...]
  ZW-MW   Province        Mashonaland West

Codes which have been deleted from ISO 3166-1 are available in ISO 3166-3.
The columns are alpha-3 code, alpha-4 code, numeric code, comment,
withdrawal date, and name. The columns for numeric code, comment, and
withdrawal date may be empty.

::

  $ isoquery --iso=3166-3
  AFI     AIDJ    262             1977    French Afars and Issas
  ANT     ANHH    532             1993-07-12      Netherlands Antilles
  [...]
  YUG     YUCS    891             1993-07-28      Yugoslavia, Socialist Federal Republic of
  ZAR     ZRCD    180             1997-07-14      Zaire, Republic of

For ISO 639-2, the first three columns are the alpha-3 code, the
bibliographic code, and the alpha-2 code. The second and third columns
may be empty.

::

  $ isoquery --iso=639-2
  aar             aa      Afar
  abk             ab      Abkhazian
  ace                     Achinese
  [...]
  zun                     Zuni
  zxx                     No linguistic content; Not applicable
  zza                     Zaza; Dimili; Dimli; Kirdki; Kirmanjki; Zazaki

You can trim down the results by specifying only some codes. Moreover,
the option to get translated names is also available.

::

  $ isoquery --iso=639-2 --locale=pt vi bo kl
  vie             vi      Vietnamita
  bod     tib     bo      tibetano
  kal             kl      Kalaallisut; Greenlandic

If you want to use ISO 639-3, the displayed columns are alpha-3, scope, type,
alpha-2, bibliographic, and the language name. Both alpha-2 and bibliographic
may be empty.

::

  $ isoquery -i 639-3 aal new spa guc
  aal     I       L                       Afade
  new     I       L                       Newari
  spa     I       L       es              Spanish
  guc     I       L                       Wayuu

ISO 639-5 is also available. The displayed columns are alpha-3 and name.

::

  $ isoquery -i 639-5 aus tut
  aus     Australian languages
  tut     Altaic languages

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

By default, the JSON files provided by the **iso-codes** package will be used.

| */usr/share/iso-codes/json/iso_639-2.json*
| */usr/share/iso-codes/json/iso_639-3.json*
| */usr/share/iso-codes/json/iso_639-5.json*
| */usr/share/iso-codes/json/iso_3166-1.json*
| */usr/share/iso-codes/json/iso_3166-2.json*
| */usr/share/iso-codes/json/iso_3166-3.json*
| */usr/share/iso-codes/json/iso_4217.json*
| */usr/share/iso-codes/json/iso_15924.json*


AUTHOR
======

Dr. Tobias Quathamer <toddy@debian.org>
