import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8714"
version_tuple = (0, 0, 8714)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8714")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8602"
data_version_tuple = (0, 0, 8602)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8602")
except ImportError:
    pass
data_git_hash = "855baf0e43b2f8f10602feb3e7ea25debeb742ef"
data_git_describe = "v0.0-8602-g855baf0e4"
data_git_msg = """\
commit 855baf0e43b2f8f10602feb3e7ea25debeb742ef
Author: Timothy Chen <timothytim@google.com>
Date:   Fri Nov 12 13:11:56 2021 -0800

    [ci] re-enable entropy and pwrmgr smoke tests
    
    Signed-off-by: Timothy Chen <timothytim@google.com>

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
