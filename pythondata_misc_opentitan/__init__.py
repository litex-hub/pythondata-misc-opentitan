import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5869"
version_tuple = (0, 0, 5869)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5869")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5774"
data_version_tuple = (0, 0, 5774)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5774")
except ImportError:
    pass
data_git_hash = "587b7a3cb073cb47cb85f953e1981f1767affdd9"
data_git_describe = "v0.0-5774-g587b7a3cb"
data_git_msg = """\
commit 587b7a3cb073cb47cb85f953e1981f1767affdd9
Author: Eunchan Kim <eunchan@opentitan.org>
Date:   Wed Apr 14 15:39:28 2021 -0700

    [dvsim] Fix local run error.
    
    Signed-off-by: Eunchan Kim <eunchan@opentitan.org>

"""

# Tool version info
tool_version_str = "0.0.post95"
tool_version_tuple = (0, 0, 95)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post95")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
