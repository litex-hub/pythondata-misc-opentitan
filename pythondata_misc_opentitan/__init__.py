import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5812"
version_tuple = (0, 0, 5812)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5812")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5717"
data_version_tuple = (0, 0, 5717)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5717")
except ImportError:
    pass
data_git_hash = "6c5f7a7d702ede73a4ade4bd440e9e8d3078d5a8"
data_git_describe = "v0.0-5717-g6c5f7a7d7"
data_git_msg = """\
commit 6c5f7a7d702ede73a4ade4bd440e9e8d3078d5a8
Author: Michael Schaffner <msf@google.com>
Date:   Fri Apr 9 11:51:10 2021 -0700

    [pinout] Update flash test mode and voltage signals/pads
    
    This instantiates the newly added analog pad for the flash test voltage,
    and updates the flash test mode pinout (reduction from 4 to 2 bit).
    
    Signed-off-by: Michael Schaffner <msf@google.com>

"""

# Tool version info
tool_version_str = "0.0.post95"
tool_version_tuple = (0, 0, 95)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post95")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
