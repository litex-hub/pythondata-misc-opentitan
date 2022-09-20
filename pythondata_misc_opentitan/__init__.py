import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14315"
version_tuple = (0, 0, 14315)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14315")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14173"
data_version_tuple = (0, 0, 14173)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14173")
except ImportError:
    pass
data_git_hash = "838afcd5d8f73da7c62f6eb355ceb861c6fca96b"
data_git_describe = "v0.0-14173-g838afcd5d8"
data_git_msg = """\
commit 838afcd5d8f73da7c62f6eb355ceb861c6fca96b
Author: Alphan Ulusoy <alphan@google.com>
Date:   Mon Sep 19 16:51:40 2022 -0400

    [bazel, ci] Group tests with the same ROM
    
    Fixes #13202
    
    Signed-off-by: Alphan Ulusoy <alphan@google.com>

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
