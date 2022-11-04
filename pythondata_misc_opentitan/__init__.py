import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post15242"
version_tuple = (0, 0, 15242)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post15242")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post15100"
data_version_tuple = (0, 0, 15100)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post15100")
except ImportError:
    pass
data_git_hash = "f0ddbd78b0f71a4f2637ef5f84640878ae15321f"
data_git_describe = "v0.0-15100-gf0ddbd78b0"
data_git_msg = """\
commit f0ddbd78b0f71a4f2637ef5f84640878ae15321f
Author: Chris Frantz <cfrantz@google.com>
Date:   Thu Nov 3 10:20:13 2022 -0700

    [rust] Update serde-annotate to v0.0.6
    
    Signed-off-by: Chris Frantz <cfrantz@google.com>

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
