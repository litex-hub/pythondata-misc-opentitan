import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8549"
version_tuple = (0, 0, 8549)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8549")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8437"
data_version_tuple = (0, 0, 8437)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8437")
except ImportError:
    pass
data_git_hash = "2f8d20428eea7ea4bcbd530e9cccfccdc7e9292c"
data_git_describe = "v0.0-8437-g2f8d20428"
data_git_msg = """\
commit 2f8d20428eea7ea4bcbd530e9cccfccdc7e9292c
Author: Michael Schaffner <msf@opentitan.org>
Date:   Fri Oct 29 11:49:36 2021 -0700

    [sram_ctrl] Connect second bus integ failure
    
    Fix #8970
    
    Signed-off-by: Michael Schaffner <msf@opentitan.org>

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
