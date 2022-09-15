import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14222"
version_tuple = (0, 0, 14222)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14222")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14080"
data_version_tuple = (0, 0, 14080)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14080")
except ImportError:
    pass
data_git_hash = "7200ca3677141d0f3c6d9a341c9bcf2d97685d58"
data_git_describe = "v0.0-14080-g7200ca3677"
data_git_msg = """\
commit 7200ca3677141d0f3c6d9a341c9bcf2d97685d58
Author: Alphan Ulusoy <alphan@google.com>
Date:   Tue Sep 6 15:39:15 2022 -0400

    [bazel] Add bazel rules for manual tests
    
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
