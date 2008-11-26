/*
 * Copyright (C) 2007-2008 Tobias Quathamer
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

#include <cstdlib>
#include <libintl.h>
#include "option_parser.h"
#include "xmldata.h"



/**
 * Main function for Isoquery
 */
int
main(int argc, char *argv[])
{
	OptionParser option;
	XMLData xmldata;
	int q;

	/* Initialize gettext */
	setlocale(LC_ALL, "");
	textdomain(PACKAGE_NAME);

	/* Parse options and set up default values */
	option.parse(argc, argv);
	option.validate();

	/* Open and check for valid XML source file */
	xmldata.open(option.xmlfile);
	xmldata.check(option.iso);
	xmldata.set_output_locale(option.locale);
	xmldata.set_attribute_name(option.name);
	xmldata.set_use_null_character(option.use_null_character);

	if (option.argument_start) {
		for (q = option.argument_start; q < argc; q++) {
			xmldata.show(argv[q]);
		}
	} else {
		xmldata.show("");
	}

	return EXIT_SUCCESS;
}
