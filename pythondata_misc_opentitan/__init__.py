import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5396"
version_tuple = (0, 0, 5396)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5396")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5301"
data_version_tuple = (0, 0, 5301)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5301")
except ImportError:
    pass
data_git_hash = "a40e98ab4d2a215b3297a0f9ea93ac7efb0e6447"
data_git_describe = "v0.0-5301-ga40e98ab4"
data_git_msg = """\
commit a40e98ab4d2a215b3297a0f9ea93ac7efb0e6447
Author: Weicai Yang <weicai@google.com>
Date:   Mon Mar 15 14:19:54 2021 -0700

    [dv] Fix CI failure at EDN
    
    The update #5532 had null pointer error, somehow, CI didn't fail
    This should fix it
    
    Signed-off-by: Weicai Yang <weicai@google.com>

"""

# Tool version info
tool_version_str = "0.0.post95"
tool_version_tuple = (0, 0, 95)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post95")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
