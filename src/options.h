/**
 * Copyright © 2016 Dr. Tobias Quathamer <toddy@debian.org>
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */

/**
 * Global variables to hold program options.
 */
extern gchar *option_standard;
extern gchar *option_pathname;
extern gchar *option_namefield;
extern gchar *option_locale;
extern gboolean *option_version;

gboolean options_parse_command_line(gchar ** arguments, GError ** error);
void options_set_default_values(void);
gboolean options_validate(GError ** error);
gchar *options_get_filename(void);
void options_show_version(void);
