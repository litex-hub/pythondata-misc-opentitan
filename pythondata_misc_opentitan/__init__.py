import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8976"
version_tuple = (0, 0, 8976)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8976")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8864"
data_version_tuple = (0, 0, 8864)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8864")
except ImportError:
    pass
data_git_hash = "4e9df5489bae93f95969dd6f6859ddad8e28d1e3"
data_git_describe = "v0.0-8864-g4e9df5489"
data_git_msg = """\
commit 4e9df5489bae93f95969dd6f6859ddad8e28d1e3
Author: Michael Schaffner <msf@opentitan.org>
Date:   Thu Dec 2 16:47:20 2021 -0800

    [reggen] Add tentative list of assets and cm types
    
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
