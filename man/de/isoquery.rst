==========
 isoquery
==========

Suche und Anzeige verschiedener ISO-Codes (Land, Sprache, ...)
--------------------------------------------------------------

:Date:            2010-06-28
:Version:         1.0
:Manual section:  1


SYNOPSIS
========

**isoquery** [*Optionen*] [*Datei*] [*ISO-Codes*]


BESCHREIBUNG
============

Diese Handbuchseite erläutert kurz das Programm **isoquery**. Es kann dazu
verwendet werden, die vom Paket iso-codes zur Verfügung gestellten
ISO-Standard-Codes tabellarisch auszugeben. Es wertet die XML-Dateien aus
und zeigt entweder alle enthaltenen ISO-Codes oder lediglich passende
Einträge, wenn diese auf der Kommandozeile angegeben werden. Außerdem ist es
möglich, alle verfügbaren Übersetzungen für den ISO-Standard zu erhalten.


OPTIONEN
========

Dieses Programm folgt dem üblichen Format der GNU Kommandozeilenoptionen, in
dem lange Optionen mit zwei Minuszeichen beginnen (»-«). **isoquery**
unterstützt die folgenden Optionen:

-i NUMMER, --iso=NUMMER     Der gewünschte ISO-Standard. Mögliche Werte: 639, 639-3, 3166, 4217, 15924 (Voreinstellung: 3166)
-n, --name                  Name der übergebenen Codes (Voreinstellung)
-o, --official_name         Offizieller Name der übergebenen Codes. Dies kann das Gleiche sein wie --name.
-c, --common_name           Üblicher Name der übergebenen Codes. Dies kann das Gleiche sein wie --name.
-l LOCALE, --locale=LOCALE  Diese Locale für die Ausgabe verwenden.

-x DATEI, --xmlfile=DATEI   Eine andere XML-Datei mit ISO-Daten verwenden (Voreinstellung: /usr/share/xml/iso-codes/iso_3166.xml)
-0, --null                  Einträge durch ein NULL-Zeichen anstatt des Zeilenumbruches voneinander trennen.
-h, --help                  Anzeige dieser Informationen.
-v, --version               Anzeige der Programmversion und des Copyrights.

BEISPIELE
=========

Wenn **isoquery** ohne Kommandozeilenoptionen aufgerufen wird, gibt das
Programm eine Tabelle mit allen ISO 3166 Codes aus. Die ersten drei Spalten
enthalten den Alpha-2-Code, den Alpha-3-Code und den nummerischen Code, die
dem Land zugewiesen sind, das in der vierten Spalte aufgelistet wird.

::

  $ isoquery
  AF      AFG     004     Afghanistan
  [...]
  ZW      ZWE     716     Zimbabwe

Wenn Sie nur einige Länder benötigen, können Sie Codes angeben, die in den
ersten drei Spalten angezeigt werden. Dadurch wird die Ausgabe auf die
passenden Einträge beschränkt.

::

  $ isoquery so nor 484
  SO      SOM     706     Somalia
  NO      NOR     578     Norway
  MX      MEX     484     Mexico

Wenn Sie die Übersetzung der Ländernamen brauchen, geben Sie einfach die
Locale an, in der Sie die Ausgabe benötigen. Bitte beachten Sie, dass der
ursprüngliche englische Name angezeigt wird, wenn es für die angegebene
Locale keine Übersetzung gibt.

::

    $ isoquery --locale=nl fr de es
    FR      FRA     250     Frankrijk
    DE      DEU     276     Duitsland
    ES      ESP     724     Spanje

All das oben gesagte funktioniert ebenso für andere ISO-Standards, so können
Sie beispielsweise mit der Kommandozeilenoption --iso auf Sprachennamen
umstellen. Bei ISO 639 enthalten die ersten drei Spalten den ISO 639 2B
Code, den ISO 639 2T Code und den ISO 639-1 Code. Die dritte Spalte kann
leer sein.

::

  $ isoquery --iso=639
  aar     aar     aa      Afar
  abk     abk     ab      Abkhazian
  ace     ace             Achinese
  [...]
  zun     zun             Zuni
  zxx     zxx             No linguistic content
  zza     zza             Zaza; Dimili; Dimli; Kirdki

Sie können die Ergebnisse einschränken, indem Sie nur einzelne Codes
angeben. Weiterhin ist auch hier die Möglichkeit vorhanden, übersetzte Namen
zu erhalten.

::

  $ isoquery --iso=639 --locale=pt vi bo kl
  vie     vie     vi      Vietnamita
  tib     bod     bo      tibetano
  kal     kal     kl      Kalaallisut; Greenlandic

Sie können Übersetzungen für ausgewählte Währungsnamen aus dem ISO 4217
Standard erhalten, wenn Sie den folgenden Befehl eingeben. Die ersten beiden
Spalten sind der Alpha-3-Code und der nummerische Code, die der Währung
zugewiesen sind.

::

  $ isoquery --iso=4217 --locale=da cad 392
  CAD     124     Canadisk dollar
  JPY     392     Japansk yen

Wenn Sie Skriptnamen benötigen, können Sie die Tabelle für ISO 15924
verwenden. Die ersten beiden Spalten sind der Alpha-4-Code und der
nummerische Code, die der Währung zugewiesen sind.

::

  $ isoquery --iso=15924 jpan latn 280
  Jpan    413     Japanese (alias for Han + Hiragana + Katakana)
  Latn    215     Latin
  Visp    280     Visible Speech


DATEIEN
=======

In der Voreinstellung werden die Dateien verwendet, die durch das Paket
iso-codes zur Verfügung gestellt werden.

*/usr/share/xml/iso-codes/iso_639.xml*
*/usr/share/xml/iso-codes/iso_639_3.xml*
*/usr/share/xml/iso-codes/iso_3166.xml*
*/usr/share/xml/iso-codes/iso_4217.xml*
*/usr/share/xml/iso-codes/iso_15924.xml*


AUTOR
=====

Tobias Quathamer <toddy@debian.org>


ÜBERSETZUNG
===========

Tobias Quathamer <toddy@debian.org>
