import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post13173"
version_tuple = (0, 0, 13173)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post13173")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post13031"
data_version_tuple = (0, 0, 13031)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post13031")
except ImportError:
    pass
data_git_hash = "a5f10de566481af010cacd099f9a963c36ed1300"
data_git_describe = "v0.0-13031-ga5f10de566"
data_git_msg = """\
commit a5f10de566481af010cacd099f9a963c36ed1300
Author: Timothy Trippel <ttrippel@google.com>
Date:   Mon Jul 18 14:15:01 2022 -0700

    [dif/entropy_src] add missing unit tests
    
    This adds missing unit tests for all remaining DIFs that have been
    implemented.
    
    Signed-off-by: Timothy Trippel <ttrippel@google.com>

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
