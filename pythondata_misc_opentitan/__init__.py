import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9005"
version_tuple = (0, 0, 9005)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9005")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8893"
data_version_tuple = (0, 0, 8893)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8893")
except ImportError:
    pass
data_git_hash = "67744911c3dd563b7e16f22c81d4c9010e51defe"
data_git_describe = "v0.0-8893-g67744911c"
data_git_msg = """\
commit 67744911c3dd563b7e16f22c81d4c9010e51defe
Author: Guillermo Maturana <maturana@google.com>
Date:   Fri Dec 3 14:13:14 2021 -0800

    [dv/pwrmgr] Remove unnecessary "rand" attribute
    
    Signed-off-by: Guillermo Maturana <maturana@google.com>

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
