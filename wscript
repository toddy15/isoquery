# Import necessary python modules
import os

# Import helper from waf
import Scripting

# Import canonical version from isoquery
from isoquery import __version__

APPNAME = 'isoquery'
VERSION = __version__

top = '.'
out = 'build'

Scripting.excludes.append('.eric4project')
Scripting.excludes.append('.ropeproject')
Scripting.excludes.append('debian')
Scripting.excludes.append('isoquery.e4p')

def set_options(opt):
    opt.tool_options('python')

def configure(conf):
    # Check that required programs are available
    conf.find_program('msgfmt', var='MSGFMT', mandatory=True)
    conf.check_tool('python')
    conf.check_python_version((2,4))

def build(bld):
    # Compile python files
    obj = bld.new_task_gen('py')
    obj.find_sources_in_dirs('./isoquery')
    obj.install_path = '${PYTHONDIR}/isoquery'
    # Register installation paths
    bld.install_files('${PREFIX}/bin', ['bin/isoquery'])
    bld.install_files('${PREFIX}/share/man/man1', ['man/isoquery.1'])
    # TODO: This needs to be generalized
    bld.install_files('${PREFIX}/share/man/de/man1', ['man/de/isoquery.1'])
    bld.install_files('${PREFIX}/share/doc/isoquery',
        ['ChangeLog', 'README', 'TODO', 'AUTHORS'])
    # Generate .mo files
    for translation in bld.path.ant_glob('po/*.po').split():
        # Get locale from basename of the file, without extension (.po)
        locale = os.path.basename(translation)[:-3]
        # Create a task for each translation file
        mo_file = bld(
            source = translation,
            target = translation.replace('.po', '.mo'),
            rule = bld.env['MSGFMT'] + ' --check --output ${TGT} ${SRC}',
        )
        # The file needs a new name for installation
        bld.install_as(
            '${PREFIX}/share/locale/' + locale + '/LC_MESSAGES/isoquery.mo',
            mo_file.target
        )
