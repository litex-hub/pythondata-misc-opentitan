import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12680"
version_tuple = (0, 0, 12680)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12680")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12538"
data_version_tuple = (0, 0, 12538)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12538")
except ImportError:
    pass
data_git_hash = "6d1f15d88e1b194d5d7558e680c386774d1e8058"
data_git_describe = "v0.0-12538-g6d1f15d88"
data_git_msg = """\
commit 6d1f15d88e1b194d5d7558e680c386774d1e8058
Author: Michael Schaffner <msf@opentitan.org>
Date:   Fri Jun 10 16:08:15 2022 +0200

    [tlul_lc_gate] Align error/active with active/error transition
    
    This is to make the module more generic.
    The module also resets into the StError now so that the TL-UL access is
    blocked by default to stay on the prudent side.
    
    Signed-off-by: Michael Schaffner <msf@opentitan.org>

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
