import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10853"
version_tuple = (0, 0, 10853)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10853")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10727"
data_version_tuple = (0, 0, 10727)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10727")
except ImportError:
    pass
data_git_hash = "b0fd9bf680319c101c16c9f0bc50909b1d9acfc4"
data_git_describe = "v0.0-10727-gb0fd9bf68"
data_git_msg = """\
commit b0fd9bf680319c101c16c9f0bc50909b1d9acfc4
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Thu Mar 10 12:31:01 2022 -0800

    [rstmgr/rtl] Swap alert_test alerts orders
    
    I believe the order of alert_test is swapped.
    
    Signed-off-by: Cindy Chen <chencindy@opentitan.org>

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
