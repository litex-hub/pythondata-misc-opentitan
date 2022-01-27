import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9834"
version_tuple = (0, 0, 9834)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9834")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9712"
data_version_tuple = (0, 0, 9712)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9712")
except ImportError:
    pass
data_git_hash = "b9597e56af20e0407ea0a5dffd0574d09c6ceec0"
data_git_describe = "v0.0-9712-gb9597e56a"
data_git_msg = """\
commit b9597e56af20e0407ea0a5dffd0574d09c6ceec0
Author: Weicai Yang <weicai@google.com>
Date:   Tue Jan 25 14:37:06 2022 -0800

    [tlul] Move to V2
    
    All common TLUL verification items have been completed.
    Xbar coverage has reached V2 status
    SCORE   LINE    COND    TOGGLE  FSM     BRANCH  ASSERT  GROUP
    98.47   100.00  95.59   98.47   --      97.30   99.50   100.00
    
    Signed-off-by: Weicai Yang <weicai@google.com>

"""

# Tool version info
tool_version_str = "0.0.post122"
tool_version_tuple = (0, 0, 122)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post122")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
