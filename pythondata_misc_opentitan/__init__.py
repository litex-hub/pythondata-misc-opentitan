import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8423"
version_tuple = (0, 0, 8423)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8423")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8311"
data_version_tuple = (0, 0, 8311)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8311")
except ImportError:
    pass
data_git_hash = "241a82c665d1823ac70f8a63a6943a2cd8dd8ac9"
data_git_describe = "v0.0-8311-g241a82c66"
data_git_msg = """\
commit 241a82c665d1823ac70f8a63a6943a2cd8dd8ac9
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Thu Sep 23 16:32:54 2021 -0700

    [fpv] prim_counter_fpv
    
    1).Set up an initial FPV testbench on prim_counter.
    2).Move around some assertions in design to avoid conditional disable
    assertions in FPV.
    
    Signed-off-by: Cindy Chen <chencindy@opentitan.org>

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
