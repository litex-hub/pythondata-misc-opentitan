import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14882"
version_tuple = (0, 0, 14882)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14882")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14740"
data_version_tuple = (0, 0, 14740)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14740")
except ImportError:
    pass
data_git_hash = "714edf44aade76fd23cea9572d3b01ba0cef0bec"
data_git_describe = "v0.0-14740-g714edf44aa"
data_git_msg = """\
commit 714edf44aade76fd23cea9572d3b01ba0cef0bec
Author: Jaedon Kim <jdonjdon@google.com>
Date:   Fri Oct 21 13:39:36 2022 +0000

    [flash_ctrl,dv] move rma_err to v2 testplan from v2s
    
    To avoid lint failure, move rma_err test point to v2
    
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
