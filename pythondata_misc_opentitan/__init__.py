import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8363"
version_tuple = (0, 0, 8363)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8363")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8251"
data_version_tuple = (0, 0, 8251)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8251")
except ImportError:
    pass
data_git_hash = "2b90842733363f8d07b32ccb7b71b9c72bc81466"
data_git_describe = "v0.0-8251-g2b9084273"
data_git_msg = """\
commit 2b90842733363f8d07b32ccb7b71b9c72bc81466
Author: Timothy Trippel <ttrippel@google.com>
Date:   Wed Oct 20 19:28:49 2021 +0000

    [dif/rv-timer] Fix autogen DIFs dependency architecture.
    
    This fixes #8755 for the rv_timer, to fix a CI failure, since #8756 was
    merged after #8733, without updating the rv-timer autogen DIFs. (CI
    tests passed for #8756, before #8733 was merged.)
    
    Signed-off-by: Timothy Trippel <ttrippel@google.com>

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
