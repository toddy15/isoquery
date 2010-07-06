#!/usr/bin/env python
# encoding: utf-8

# Import necessary python modules
import os

# Import canonical version from isoquery
from isoquery import __version__

APPNAME = 'isoquery'
VERSION = __version__

top = '.'
out = 'build'

from waflib import Scripting
Scripting.excludes.append('.eric4project')
Scripting.excludes.append('.ropeproject')
Scripting.excludes.append('debian')
Scripting.excludes.append('isoquery.e4p')

def options(opt):
    # Options for disabling pyc or pyo compilation
    opt.tool_options('python')
    # Support usual directory variables like MANDIR, DATADIR, etc.
    opt.tool_options('gnu_dirs')

def configure(conf):
    # Check that required programs are available
    conf.find_program('msgfmt', var='MSGFMT')
    conf.find_program(['rst2man','rst2man.py'], var='RST2MAN')
    conf.find_program('gzip', var='GZIP')
    conf.find_program('po4a-translate', var='PO4A_TRANSLATE')
    conf.check_tool('python')
    conf.check_python_version((2,4))
    conf.check_tool('gnu_dirs')

def build(bld):
    # Compile python files
    bld(
        features = 'py',
        source = bld.path.ant_glob('isoquery/*.py'),
        install_path = '${PYTHONDIR}/isoquery',
    )
    # Register installation paths
    bld.install_files('${BINDIR}', 'bin/isoquery')
    bld.install_files('${DOCDIR}', ['ChangeLog', 'README', 'TODO', 'AUTHORS'])

    # Manpages
    # Generate man page from rst source files
    bld(
        source = 'man/isoquery.rst',
        target = 'man/isoquery.1',
        rule = '${RST2MAN} ${SRC} ${TGT}',
    )
    bld(
        source = 'man/de.add man/de.po man/isoquery.rst',
        target = 'man/de/isoquery.rst',
        rule = '${PO4A_TRANSLATE} ' + \
               '--format text ' + \
               '--option markdown ' + \
               '--addendum ${SRC[0].bldpath()} ' + \
               '--po ${SRC[1].bldpath()} ' + \
               '--master ${SRC[2].bldpath()} ' + \
               '--master-charset UTF-8 ' + \
               '--localized ${TGT}',
    )
    bld(
        source = 'man/de/isoquery.rst',
        target = 'man/de/isoquery.1',
        rule = '${RST2MAN} ${SRC} ${TGT}',
    )
    # Compress and install man pages
    bld(
        source = 'man/isoquery.1',
        target = 'man/isoquery.1.gz',
        rule = '${GZIP} --best --stdout ${SRC} > ${TGT}',
    )
    bld.install_files('${MANDIR}/man1', 'man/isoquery.1.gz')
    bld(
        source = 'man/de/isoquery.1',
        target = 'man/de/isoquery.1.gz',
        rule = '${GZIP} --best --stdout ${SRC} > ${TGT}',
    )
    bld.install_files('${MANDIR}/de/man1', 'man/de/isoquery.1.gz')

    # Generate .mo files
    for translation in bld.path.ant_glob('po/*.po'):
        # Get locale from basename of the file, without extension (.po)
        locale = os.path.basename(translation.path_from(bld.path))[:-3]
        # Create a task for each translation file
        mo_file = bld(
            source = translation,
            target = translation.change_ext('.mo'),
            rule = '${MSGFMT} --check --output ${TGT} ${SRC}',
        )
        # The file needs a new name for installation
        bld.install_as(
            '${LOCALEDIR}/%s/LC_MESSAGES/isoquery.mo' % locale,
            mo_file.target
        )
