/*
 * Copyright (C) 2007-2008 Tobias Toedter
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

#ifndef OPTION_PARSER_H_
#define OPTION_PARSER_H_

#include <iostream>
#include <string>
using namespace std;

#include <getopt.h>


class OptionParser
{
public:
	/* ISO standard to use, e.g. 3166, 4217 etc. */
	string iso;
	/* Attribute to display, e.g. name, official_name, common_name */
	string name;
	/* Locale for output */
	string locale;
	/* XML data source */
	string xmlfile;
	/* Index of remaining arguments, if any */
	int argument_start;
	
	void show_help();
	void show_version();
	void parse(int argc, char *argv[]);
	void validate();
};

#endif /*OPTION_PARSER_H_*/
