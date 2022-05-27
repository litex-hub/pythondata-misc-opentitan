import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12393"
version_tuple = (0, 0, 12393)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12393")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12253"
data_version_tuple = (0, 0, 12253)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12253")
except ImportError:
    pass
data_git_hash = "41bc0ceab8527aa283b44f4499f1be172b9165fc"
data_git_describe = "v0.0-12253-g41bc0ceab"
data_git_msg = """\
commit 41bc0ceab8527aa283b44f4499f1be172b9165fc
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Thu May 26 14:17:50 2022 +0100

    [otbn,dv] Clear RND cache at start of operation
    
    This matches the changes made in the RTL in 8e97525 and the
    documentation in 46e134f.
    
    Signed-off-by: Rupert Swarbrick <rswarbrick@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post140"
tool_version_tuple = (0, 0, 140)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post140")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
