import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10140"
version_tuple = (0, 0, 10140)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10140")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10016"
data_version_tuple = (0, 0, 10016)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10016")
except ImportError:
    pass
data_git_hash = "6f7e546d8152f0d0714259917d0084de0ef2e00f"
data_git_describe = "v0.0-10016-g6f7e546d8"
data_git_msg = """\
commit 6f7e546d8152f0d0714259917d0084de0ef2e00f
Author: Michael Schaffner <msf@opentitan.org>
Date:   Mon Feb 7 16:43:53 2022 -0800

    [tlul] Return all-one upon all data read errors
    
    Fixes #10611
    
    Signed-off-by: Michael Schaffner <msf@opentitan.org>

"""

# Tool version info
tool_version_str = "0.0.post124"
tool_version_tuple = (0, 0, 124)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post124")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
