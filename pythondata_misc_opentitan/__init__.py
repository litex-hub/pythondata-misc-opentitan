import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8670"
version_tuple = (0, 0, 8670)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8670")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8558"
data_version_tuple = (0, 0, 8558)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8558")
except ImportError:
    pass
data_git_hash = "23f6f5da78fcab7cd7e3c9111fd43ae661916931"
data_git_describe = "v0.0-8558-g23f6f5da7"
data_git_msg = """\
commit 23f6f5da78fcab7cd7e3c9111fd43ae661916931
Author: Weicai Yang <weicai@google.com>
Date:   Tue Nov 9 13:51:47 2021 -0800

    [prim] Remove extra semicolon
    
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
