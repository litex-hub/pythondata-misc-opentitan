import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10099"
version_tuple = (0, 0, 10099)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10099")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9975"
data_version_tuple = (0, 0, 9975)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9975")
except ImportError:
    pass
data_git_hash = "78d0839fd7cdec1b23834bbdb26244665c55cc33"
data_git_describe = "v0.0-9975-g78d0839fd"
data_git_msg = """\
commit 78d0839fd7cdec1b23834bbdb26244665c55cc33
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Sun Feb 6 10:26:43 2022 -0800

    [fpv/flash_ctrl] Fix compile error
    
    This PR fixes the compile error due to index out of bound.
    
    Signed-off-by: Cindy Chen <chencindy@opentitan.org>

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
