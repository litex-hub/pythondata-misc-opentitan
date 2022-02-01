import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9972"
version_tuple = (0, 0, 9972)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9972")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9848"
data_version_tuple = (0, 0, 9848)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9848")
except ImportError:
    pass
data_git_hash = "bd1bae0e7174e2df7306cc10dc370bb7782268ae"
data_git_describe = "v0.0-9848-gbd1bae0e7"
data_git_msg = """\
commit bd1bae0e7174e2df7306cc10dc370bb7782268ae
Author: Greg Chadwick <gac@lowrisc.org>
Date:   Mon Jan 31 13:32:28 2022 +0000

    [rv_dm] Move to D2
    
    Signed-off-by: Greg Chadwick <gac@lowrisc.org>

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
