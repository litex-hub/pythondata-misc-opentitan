import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5062"
version_tuple = (0, 0, 5062)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5062")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post4971"
data_version_tuple = (0, 0, 4971)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post4971")
except ImportError:
    pass
data_git_hash = "6e293427f83dcaccf38775d4622b4e7c4569a006"
data_git_describe = "v0.0-4971-g6e293427f"
data_git_msg = """\
commit 6e293427f83dcaccf38775d4622b4e7c4569a006
Author: Cindy Chen <chencindy@google.com>
Date:   Thu Feb 18 11:25:35 2021 -0800

    [fpv] Fix FPV compile errors
    
    1. sram_ctrl compile error comes from prim_lc_sync. It requires input
    to be an array, even though the size is 1.
    
    2. RV_DM compile error comes from missing `prim_lc_sync` package.
    
    Signed-off-by: Cindy Chen <chencindy@google.com>

"""

# Tool version info
tool_version_str = "0.0.post91"
tool_version_tuple = (0, 0, 91)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post91")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
