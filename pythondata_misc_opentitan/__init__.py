import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post13210"
version_tuple = (0, 0, 13210)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post13210")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post13068"
data_version_tuple = (0, 0, 13068)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post13068")
except ImportError:
    pass
data_git_hash = "7c4d32f80bfa74bcace17905b174cdba78efd314"
data_git_describe = "v0.0-13068-g7c4d32f80b"
data_git_msg = """\
commit 7c4d32f80bfa74bcace17905b174cdba78efd314
Author: Jaedon Kim <jdonjdon@google.com>
Date:   Mon Jul 18 12:32:24 2022 +0000

    [flash_ctrl,dv] do_direct_read update
    
     - pass abort signal to caller
     - subsequent update all tests uses do_direct_read with a new signature
    
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
