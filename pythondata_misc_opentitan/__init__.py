import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post13168"
version_tuple = (0, 0, 13168)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post13168")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post13026"
data_version_tuple = (0, 0, 13026)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post13026")
except ImportError:
    pass
data_git_hash = "409c80ece81e6e77e6fdc0bb7b81c48e2d403294"
data_git_describe = "v0.0-13026-g409c80ece8"
data_git_msg = """\
commit 409c80ece81e6e77e6fdc0bb7b81c48e2d403294
Author: Greg Chadwick <gac@lowrisc.org>
Date:   Fri Jul 15 18:27:37 2022 +0100

    [otbn, rtl/doc] Update security countermeasures
    
    This documents more, already implemented, security countermeasures that
    had previously been left off the countermeasure list.
    
    Signed-off-by: Greg Chadwick <gac@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post142"
tool_version_tuple = (0, 0, 142)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post142")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
