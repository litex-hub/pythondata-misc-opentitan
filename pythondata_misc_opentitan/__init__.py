import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post15277"
version_tuple = (0, 0, 15277)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post15277")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post15135"
data_version_tuple = (0, 0, 15135)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post15135")
except ImportError:
    pass
data_git_hash = "2fda8fa3159893257d289e93047565d0ec301af5"
data_git_describe = "v0.0-15135-g2fda8fa315"
data_git_msg = """\
commit 2fda8fa3159893257d289e93047565d0ec301af5
Author: Michael Schaffner <msf@google.com>
Date:   Fri Nov 4 18:12:01 2022 -0700

    [test] Minor updates to sysrst_ctrl_ec_rst_l test
    
    Aligns some names, adds more comments, checks and debug printouts.
    
    Signed-off-by: Michael Schaffner <msf@google.com>

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
