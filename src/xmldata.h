/*
 * Copyright (C) 2007-2009 Tobias Quathamer
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

#ifndef XMLDATA_H_
#define XMLDATA_H_

#include <libxml++/libxml++.h>


class XMLData
{
private:
	xmlpp::DomParser parser;
	/* ISO standard to use, e.g. 3166, 4217 etc. */
	string iso;
	/* Attribute to display, e.g. name, official_name, common_name */
	string name;
	/* Locale for output */
	string locale;
	/* XML data source */
	string xmlfile;
	/* Separate entries with NULL instead of newline */
	bool use_null_character;
	
	void print_node(const xmlpp::Element *node);
	void print_attributes(const xmlpp::Element *node,
		const Glib::ustring attr_1 = "",
		const Glib::ustring attr_2 = "",
		const Glib::ustring attr_3 = "");
	
public:
	void open(Glib::ustring filename);
	void check(Glib::ustring iso_standard);
	void set_output_locale(Glib::ustring output_locale);
	void set_attribute_name(Glib::ustring attr_name);
	void set_use_null_character(bool use_null);
	vector<Glib::ustring> get_xpaths(Glib::ustring code);
	void show(Glib::ustring code);
};

#endif /*XMLDATA_H_*/
