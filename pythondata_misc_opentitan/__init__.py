import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10836"
version_tuple = (0, 0, 10836)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10836")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10710"
data_version_tuple = (0, 0, 10710)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10710")
except ImportError:
    pass
data_git_hash = "5a2a27100b6233739b821139141d0071bd84a773"
data_git_describe = "v0.0-10710-g5a2a27100"
data_git_msg = """\
commit 5a2a27100b6233739b821139141d0071bd84a773
Author: Michael Schaffner <msf@google.com>
Date:   Thu Mar 10 13:42:34 2022 -0800

    [kmac] Add missing CM IDs and sec buffer
    
    Signed-off-by: Michael Schaffner <msf@google.com>

"""

# Tool version info
tool_version_str = "0.0.post126"
tool_version_tuple = (0, 0, 126)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post126")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
