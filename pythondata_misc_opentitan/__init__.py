import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post13002"
version_tuple = (0, 0, 13002)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post13002")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12860"
data_version_tuple = (0, 0, 12860)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12860")
except ImportError:
    pass
data_git_hash = "4696b83b725c9a0cafd02d3f27e5687893fc1b1c"
data_git_describe = "v0.0-12860-g4696b83b72"
data_git_msg = """\
commit 4696b83b725c9a0cafd02d3f27e5687893fc1b1c
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Thu Jul 7 16:06:09 2022 -0700

    [dv/alert_handler] Add more LPG checkings
    
    Signed-off-by: Cindy Chen <chencindy@opentitan.org>

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
