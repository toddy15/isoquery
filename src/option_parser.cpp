/*
 * Copyright (C) 2007 Tobias Toedter
 * 
 * This file is part of Isoquery.
 * 
 * Isoquery is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 3 of the License, or
 * (at your option) any later version.
 * 
 * Isoquery is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */

 

#ifdef HAVE_CONFIG_H
#include <config.h>
#endif

#include "gettext.h"
#include "option_parser.h"

#define _ gettext



/**
 * Parse the command line options.
 */
void
OptionParser::parse(int argc, char *argv[])
{
	/* Set up default values */ 
	iso = "3166";
	name = "name";
	locale = "";
	xmlfile = "";
	
	/* Position of additional arguments, if any */
	argument_start = 0;
	
	while (1) {
		static const struct option long_options[] = {
			{"iso", required_argument, 0, 'i'},
			{"name", no_argument, 0, 'n'},
			{"official_name", no_argument, 0, 'o'},
			{"common_name", no_argument, 0, 'c'},
			{"locale", required_argument, 0, 'l'},
			{"xmlfile", required_argument, 0, 'x'},
			{"help", no_argument, 0, 'h'},
			{"version", no_argument, 0, 'v'},
			{0, 0, 0, 0}
		};
		const int opt =
		  getopt_long(argc, argv, "i:nocl:x:hv", long_options, (int *) 0);
		switch (opt) {
			case -1:
				/* If there are additional arguments, return
				   the starting index, otherwise 0. */
				if ((argc - optind) > 0) {
					argument_start = optind;
				}
				return;
			case 'i':
				/* Override iso setting */
				iso = optarg;
				break;
			case 'n':
				/* Use name, this is the default */
				name = "name";
				break;
			case 'o':
				/* Use official_name, this is the default */
				name = "official_name";
				break;
			case 'c':
				/* Use common_name, this is the default */
				name = "common_name";
				break;
			case 'l':
				/* Use this locale for output */
				locale = optarg;
				break;
			case 'x':
				/* Use this XML file as data source */
				xmlfile = optarg;
				break;
			case 'h':
				show_help();
				break;
			case 'v':
				show_version();
				break;
			default:
				return;
		}
	}
}



/**
 * Validate command line options.
 */
void
OptionParser::validate()
{
	/* Check for valid ISO codes */
	if ((iso != "639") and (iso != "3166") and (iso != "4217")) {
		string msg = _("%PROGRAM_NAME: ISO code '%CODE' not supported.");
		msg.replace(msg.find("%PROGRAM_NAME"), strlen("%PROGRAM_NAME"), PACKAGE_NAME);
		msg.replace(msg.find("%CODE"), strlen("%CODE"), iso);
		cerr << msg << endl;
		exit(EXIT_FAILURE);
	} else {
		/* Set up the default XML file */
		if (xmlfile == "") {
			xmlfile = "/usr/share/xml/iso-codes/iso_" + iso + ".xml";
		}
	}

	if (iso == "4217") {
		name = "currency_name";
	}
}



/**
 * Show program help.
 */
void
OptionParser::show_help()
{
	string msg = _("Usage: %PROGRAM_NAME [options] [ISO codes]");
	msg.replace(msg.find("%PROGRAM_NAME"), strlen("%PROGRAM_NAME"), PACKAGE_NAME);
	cout << msg << endl << endl;
	cout << _("Options:") << endl;
	cout << _("  -i, --iso=NUMBER     The ISO standard to use\n\
                       Possible values: 639, 3166, 4217\n\
                       (default: 3166)\n\
  -n, --name           Name for the supplied codes (default)\n\
  -o, --official_name  Official name for the supplied codes\n\
                       This may be the same as --name.\n\
  -c, --common_name    Common name for the supplied codes\n\
                       This may be the same as --name.\n\
  -l, --locale=LOCALE  Use this locale for output\n\
  -x, --xmlfile=FILE   Use another XML file with ISO data\n\
                       (default: /usr/share/xml/iso-codes/iso_3166.xml)\n\
  -h, --help           Show this information\n\
  -v, --version        Show program version and copyright") << endl;
	exit(EXIT_SUCCESS);
}



/**
 * Show program version and copyright.
 */
void
OptionParser::show_version()
{
	string translation;

	cout << PACKAGE_STRING << endl;
	cout << _("Copyright (C) 2007 Tobias Toedter") << endl;

	/* TRANSLATORS: Please change the uppercase words as appropriate for
	your language. */
	translation = _("Translation to LANGUAGE Copyright (C) YEAR YOUR-NAME");

	if (translation.find("LANGUAGE") == string::npos) {
		cout << translation << endl;
	}

    	cout << endl;
	cout << "This program is free software: you can redistribute it and/or modify" << endl;
	cout << "it under the terms of the GNU General Public License as published by" << endl;
	cout << "the Free Software Foundation, either version 3 of the License, or" << endl;
	cout << "(at your option) any later version." << endl;
    	cout << endl;
	cout << "This program is distributed in the hope that it will be useful," << endl;
	cout << "but WITHOUT ANY WARRANTY; without even the implied warranty of" << endl;
	cout << "MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the" << endl;
	cout << "GNU General Public License for more details." << endl;
    	cout << endl;
	cout << "You should have received a copy of the GNU General Public License" << endl;
	cout << "along with this program.  If not, see <http://www.gnu.org/licenses/>." << endl;
	exit(EXIT_SUCCESS);
}
