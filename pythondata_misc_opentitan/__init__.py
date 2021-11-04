import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8586"
version_tuple = (0, 0, 8586)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8586")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8474"
data_version_tuple = (0, 0, 8474)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8474")
except ImportError:
    pass
data_git_hash = "9c931d3aa8fc76df7c8d99c7a190c0c86409d915"
data_git_describe = "v0.0-8474-g9c931d3aa"
data_git_msg = """\
commit 9c931d3aa8fc76df7c8d99c7a190c0c86409d915
Author: Weicai Yang <weicai@google.com>
Date:   Tue Aug 31 13:42:54 2021 -0700

    [top/dv] Update RV_DM chip-level testplan
    
    Updated testplan as we discussed in the meeting
    Signed-off-by: Weicai Yang <weicai@google.com>

"""

# Tool version info
tool_version_str = "0.0.post112"
tool_version_tuple = (0, 0, 112)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post112")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
