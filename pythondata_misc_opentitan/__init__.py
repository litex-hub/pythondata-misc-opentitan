import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8321"
version_tuple = (0, 0, 8321)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8321")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8209"
data_version_tuple = (0, 0, 8209)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8209")
except ImportError:
    pass
data_git_hash = "aca55394ac35f608dc63f02dfca63f3c08c2d0e8"
data_git_describe = "v0.0-8209-gaca55394a"
data_git_msg = """\
commit aca55394ac35f608dc63f02dfca63f3c08c2d0e8
Author: Srikrishna Iyer <sriyer@google.com>
Date:   Sat Oct 16 02:22:01 2021 -0700

    [dv_macros.svh] minor cleanup
    
    Signed-off-by: Srikrishna Iyer <sriyer@google.com>

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
