import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9960"
version_tuple = (0, 0, 9960)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9960")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9836"
data_version_tuple = (0, 0, 9836)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9836")
except ImportError:
    pass
data_git_hash = "bd1c161f1c35f03bf3e603d1aa46c5083640cea2"
data_git_describe = "v0.0-9836-gbd1c161f1"
data_git_msg = """\
commit bd1c161f1c35f03bf3e603d1aa46c5083640cea2
Author: Michael Munday <mike.munday@lowrisc.org>
Date:   Tue Feb 1 10:06:21 2022 +0000

    [COMMITTERS] Add Timothy Trippel to COMMITTERS list
    
    The Technical Committee has agreed to make Timothy a committer in the
    OpenTitan project.
    
    Congratulations! Thanks for all your hard work on OpenTitan so far.
    We're really excited to see your future contributions to the project.
    
    Signed-off-by: Michael Munday <mike.munday@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post124"
tool_version_tuple = (0, 0, 124)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post124")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
