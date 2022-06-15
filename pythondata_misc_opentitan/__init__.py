import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12698"
version_tuple = (0, 0, 12698)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12698")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12556"
data_version_tuple = (0, 0, 12556)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12556")
except ImportError:
    pass
data_git_hash = "5948fabb7add084eacddc779fe275872cd7736f1"
data_git_describe = "v0.0-12556-g5948fabb7"
data_git_msg = """\
commit 5948fabb7add084eacddc779fe275872cd7736f1
Author: Timothy Chen <timothytim@google.com>
Date:   Tue Jun 14 14:40:01 2022 -0700

    [prim] Add description to parameters
    
    Signed-off-by: Timothy Chen <timothytim@google.com>

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
