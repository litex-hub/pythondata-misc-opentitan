import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8555"
version_tuple = (0, 0, 8555)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8555")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8443"
data_version_tuple = (0, 0, 8443)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8443")
except ImportError:
    pass
data_git_hash = "9b32cd1b3d815cf31294065984d63f486661a1d4"
data_git_describe = "v0.0-8443-g9b32cd1b3"
data_git_msg = """\
commit 9b32cd1b3d815cf31294065984d63f486661a1d4
Author: Michael Schaffner <msf@opentitan.org>
Date:   Fri Oct 29 14:44:24 2021 -0700

    [otp_ctrl] Convert HW_CFG EN chicken bits to mubi8 types
    
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
