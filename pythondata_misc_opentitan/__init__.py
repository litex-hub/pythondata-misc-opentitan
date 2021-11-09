import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8642"
version_tuple = (0, 0, 8642)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8642")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8530"
data_version_tuple = (0, 0, 8530)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8530")
except ImportError:
    pass
data_git_hash = "1cb418519a274fdd873e6e6da260ceb1889f08b5"
data_git_describe = "v0.0-8530-g1cb418519"
data_git_msg = """\
commit 1cb418519a274fdd873e6e6da260ceb1889f08b5
Author: Michael Schaffner <msf@google.com>
Date:   Wed Nov 3 13:17:28 2021 -0700

    [syn] Minor scripting alignment with CDC flow
    
    Signed-off-by: Michael Schaffner <msf@google.com>

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
