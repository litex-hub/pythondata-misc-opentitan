import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14779"
version_tuple = (0, 0, 14779)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14779")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14637"
data_version_tuple = (0, 0, 14637)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14637")
except ImportError:
    pass
data_git_hash = "1045061e816476b70008606739960a481e1c29d5"
data_git_describe = "v0.0-14637-g1045061e81"
data_git_msg = """\
commit 1045061e816476b70008606739960a481e1c29d5
Author: Chris Frantz <cfrantz@google.com>
Date:   Wed Oct 12 10:03:48 2022 -0700

    [rust] Turn on clippy
    
    Signed-off-by: Chris Frantz <cfrantz@google.com>

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
