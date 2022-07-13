import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post13060"
version_tuple = (0, 0, 13060)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post13060")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12918"
data_version_tuple = (0, 0, 12918)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12918")
except ImportError:
    pass
data_git_hash = "7aad73af8d0e3c9f1df970428b12b5275adda2a0"
data_git_describe = "v0.0-12918-g7aad73af8d"
data_git_msg = """\
commit 7aad73af8d0e3c9f1df970428b12b5275adda2a0
Author: Jaedon Kim <jdonjdon@google.com>
Date:   Tue Jul 12 03:48:48 2022 +0000

    [dv,flash_ctrl] regression fix : mp_region test
    
    Signed-off-by: Jaedon Kim <jdonjdon@google.com>

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
