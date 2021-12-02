import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8967"
version_tuple = (0, 0, 8967)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8967")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8855"
data_version_tuple = (0, 0, 8855)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8855")
except ImportError:
    pass
data_git_hash = "34ba5e45f9af7d8ca6c9bdae8bd11eeeeb669d6c"
data_git_describe = "v0.0-8855-g34ba5e45f"
data_git_msg = """\
commit 34ba5e45f9af7d8ca6c9bdae8bd11eeeeb669d6c
Author: Michael Schaffner <msf@google.com>
Date:   Tue Nov 16 14:01:13 2021 -0800

    [secded/fpv] Add new ECC code FPV testbenches
    
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
