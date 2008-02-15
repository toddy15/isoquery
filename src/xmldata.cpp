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



#ifdef HAVE_CONFIG_H
#include <config.h>
#endif

#include <cstdlib>
#include <cstring>
#include <iostream>
#include <fstream>
#include <libintl.h>
#include <vector>
using namespace std;

#define _ gettext
#include "xmldata.h"



/**
 * Open the specified file
 */
void
XMLData::open(Glib::ustring filename)
{
	ifstream input_file;
	
	// Show a better error message if the XML input file cannot be opened
	input_file.open(filename.c_str());
	input_file.close();
	if (!input_file.good()) {
		Glib::ustring msg = _("The file '%FILENAME' could not be opened.");
		msg.replace(msg.find("%FILENAME"), strlen("%FILENAME"), filename);
		cerr << msg << endl;
		exit(EXIT_FAILURE);
	}
	try {
		// Validate the XML file
		parser.set_validate();
		// Replace entities automatically
		parser.set_substitute_entities();
		parser.parse_file(filename);
		xmlfile = filename;
		if (!parser) {
			cerr << _("Error in setting up the parser.") << endl;
			exit(EXIT_FAILURE);
		}
	} catch (const std::exception &e) {
		Glib::ustring msg = _("libxml++ exception caught: %EXCEPTION");
		msg.replace(msg.find("%EXCEPTION"), strlen("%EXCEPTION"), e.what());
		cerr << msg << endl;
		exit(EXIT_FAILURE);
	}
}



/**
 * Check if the file contains valid ISO code data
 */
void
XMLData::check(Glib::ustring iso_standard)
{
	xmlpp::Node *root_node;

	iso = iso_standard;
	root_node = parser.get_document()->get_root_node();
	if (root_node->get_name() != "iso_" + iso + "_entries") {
		Glib::ustring msg = _("The file '%FILENAME' does not contain valid ISO %CODE data.");
		msg.replace(msg.find("%FILENAME"), strlen("%FILENAME"), xmlfile);
		msg.replace(msg.find("%CODE"), strlen("%CODE"), iso);
		cerr << msg << endl;
		exit(EXIT_FAILURE);
	}
}



/**
 * Set output locale
 */
void
XMLData::set_output_locale(Glib::ustring output_locale)
{
	locale = output_locale;
}



/**
 * Set attribute name
 */
void
XMLData::set_attribute_name(Glib::ustring attr_name)
{
	name = attr_name;
}



/**
 * Return all xpaths, depending on command line options
 */
vector<Glib::ustring>
XMLData::get_xpaths(Glib::ustring code)
{
	vector<Glib::ustring> xpaths;
	Glib::ustring xpath;

	// There are no arguments on the command line, so show all codes
	if (code.empty()) {
		xpath = "iso_" + iso + "_entry";
		xpaths.push_back(xpath);
	} else {
		if (iso == "639") {
			if (code.length() == 2) {
				xpath = "//iso_639_entry[@iso_639_1_code='";
				xpath += code.lowercase();
				xpath += "']";
				xpaths.push_back(xpath);
			} else {
				xpath = "//iso_639_entry[@iso_639_2B_code='";
				xpath += code.lowercase();
				xpath += "']";
				xpaths.push_back(xpath);
				xpath = "//iso_639_entry[@iso_639_2T_code='";
				xpath += code.lowercase();
				xpath += "']";
				xpaths.push_back(xpath);
			}
		} else if (iso == "4217") {
			if (isdigit(code.at(0))) {
				xpath = "//iso_4217_entry[@numeric_code='";
				xpath += code.uppercase();
				xpath += "']";
			} else {
				xpath = "//iso_4217_entry[@letter_code='";
				xpath += code.uppercase();
				xpath += "']";
			}
			xpaths.push_back(xpath);
		} else if (iso == "15924") {
			if (isdigit(code.at(0))) {
				xpath = "//iso_15924_entry[@numeric_code='";
				xpath += code.uppercase();
				xpath += "']";
			} else {
				xpath = "//iso_15924_entry[@alpha_4_code='";
				xpath += code.substr(0, 1).uppercase();
				xpath += code.substr(1, code.length()).lowercase();
				xpath += "']";
			}
			xpaths.push_back(xpath);
		} else {
			// Default to ISO 3166
			if (code.length() == 2) {
				xpath = "//iso_3166_entry[@alpha_2_code='";
				xpath += code.uppercase();
				xpath += "']";
			} else if (isdigit(code.at(0))) {
				xpath = "//iso_3166_entry[@numeric_code='";
				xpath += code.uppercase();
				xpath += "']";
			} else {
				xpath = "//iso_3166_entry[@alpha_3_code='";
				xpath += code.uppercase();
				xpath += "']";
			}
			xpaths.push_back(xpath);
		}
	}

	return xpaths;
}



/**
 * Return the next xpath depending on command line options
 */
Glib::ustring
XMLData::get_next_xpath(Glib::ustring code, bool initialize)
{
	Glib::ustring xpath = "";
	static int xpath_index;
	static bool last_xpath;

	if (initialize) {
		xpath_index = 0;
		last_xpath = false;
	}
	
	// No more xpaths available, so return an empty xpath
	if (last_xpath) {
		last_xpath = false;
		return xpath;
	}
	
	// There are no arguments on the command line, so show all codes
	if (code.empty()) {
		xpath = "iso_" + iso + "_entry";
		last_xpath = true;
	} else {
		if (iso == "639") {
			if (code.length() == 2) {
				xpath = "//iso_639_entry[@iso_639_1_code='";
				xpath += code.lowercase();
				xpath += "']";
				last_xpath = true;
			} else {
				switch (xpath_index) {
				case 0:
					xpath = "//iso_639_entry[@iso_639_2B_code='";
					xpath += code.lowercase();
					xpath += "']";
					xpath_index++;
					break;
				case 1:
					xpath = "//iso_639_entry[@iso_639_2T_code='";
					xpath += code.lowercase();
					xpath += "']";
					xpath_index = 0;
					last_xpath = true;
					break;
				}
			}
		} else if (iso == "4217") {
			if (isdigit(code.at(0))) {
				xpath = "//iso_4217_entry[@numeric_code='";
				xpath += code.uppercase();
				xpath += "']";
			} else {
				xpath = "//iso_4217_entry[@letter_code='";
				xpath += code.uppercase();
				xpath += "']";
			}
			last_xpath = true;
		} else if (iso == "15924") {
			if (isdigit(code.at(0))) {
				xpath = "//iso_15924_entry[@numeric_code='";
				xpath += code.uppercase();
				xpath += "']";
			} else {
				xpath = "//iso_15924_entry[@alpha_4_code='";
				xpath += code.substr(0, 1).uppercase();
				xpath += code.substr(1, code.length()).lowercase();
				xpath += "']";
			}
			last_xpath = true;
		} else {
			// Default to ISO 3166
			if (code.length() == 2) {
				xpath = "//iso_3166_entry[@alpha_2_code='";
				xpath += code.uppercase();
				xpath += "']";
			} else if (isdigit(code.at(0))) {
				xpath = "//iso_3166_entry[@numeric_code='";
				xpath += code.uppercase();
				xpath += "']";
			} else {
				xpath = "//iso_3166_entry[@alpha_3_code='";
				xpath += code.uppercase();
				xpath += "']";
			}
			last_xpath = true;
		}
	}
	return xpath;
}



/**
 * Show codes in the XML data source.
 * 
 * If argc is not null, the selected codes from the command line
 * will be displayed. Otherwise, all codes are shown.
 * 
 * @param int Index of first argument or null
 * @param array Arguments, if any
 */
void
XMLData::show(Glib::ustring code)
{
	vector<Glib::ustring> xpaths;
	vector<Glib::ustring>::iterator xpath;
	xmlpp::NodeSet nodeset;
	xmlpp::NodeSet::iterator iter;
	const xmlpp::Element *current_node;
	bool found = false;

	xpaths = get_xpaths(code);
	for (xpath = xpaths.begin(); xpath != xpaths.end(); xpath++) {
		nodeset = parser.get_document()->get_root_node()->find(*xpath);
		for (iter = nodeset.begin(); iter != nodeset.end(); iter++) {
			current_node = dynamic_cast<xmlpp::Element*> (*iter);
			print_node(current_node);
			found = true;
		}
		if (found) break;
	}
	// Show a warning if the code was not found
	if (!found) {
		Glib::ustring msg = _("The code '%CODE' is not defined in ISO %STANDARD.");
		msg.replace(msg.find("%CODE"), strlen("%CODE"), code);
		msg.replace(msg.find("%STANDARD"), strlen("%STANDARD"), iso);
		cerr << msg << endl;
	}
}



/**
 * Print the actual node
 */
void
XMLData::print_node(const xmlpp::Element *node)
{
	Glib::ustring outputname;

	if (iso == "3166") {
		print_attributes(node, "alpha_2_code", "alpha_3_code", "numeric_code");
	} else if (iso == "639") {
		print_attributes(node, "iso_639_2B_code", "iso_639_2T_code", "iso_639_1_code");
	} else if (iso == "4217") {
		print_attributes(node, "letter_code", "numeric_code");
	} else if (iso == "15924") {
		print_attributes(node, "alpha_4_code", "numeric_code");
	}

	// If 'official_name' or 'common_name' is not set, use
	// 'name' for output
	if (node->get_attribute(name)) {
		outputname = node->get_attribute(name)->get_value();
	} else {
		outputname = node->get_attribute("name")->get_value();
	}

	// If locale is set, try to look up the translation
	if (!locale.empty()) {
		Glib::ustring language_backup = getenv("LANGUAGE");
		setenv("LANGUAGE", locale.c_str(), true);
		
		Glib::ustring domain = "iso_" + iso;
		Glib::ustring translation = dgettext(domain.c_str(), outputname.c_str());
		if (!translation.empty()) {
			outputname = translation;
		}
		
		// Restore the original setting
		if (!language_backup.empty()) {
			setenv("LANGUAGE", language_backup.c_str(), true);
		} else {
			unsetenv("LANGUAGE");
		}
	}
	cout << outputname << endl;
}



/**
 * Helper function for printing values of attributes
 */
void
XMLData::print_attributes(const xmlpp::Element *node,
	const Glib::ustring attr_1,
	const Glib::ustring attr_2,
	const Glib::ustring attr_3)
{
	if (!attr_1.empty()) {
		if (node->get_attribute(attr_1)) {
			cout << node->get_attribute(attr_1)->get_value();
		}
		cout << "\t";
	}
	if (!attr_2.empty()) {
		if (node->get_attribute(attr_2)) {
			cout << node->get_attribute(attr_2)->get_value();
		}
		cout << "\t";
	}
	if (!attr_3.empty()) {
		if (node->get_attribute(attr_3)) {
			cout << node->get_attribute(attr_3)->get_value();
		}
		cout << "\t";
	}
}
