import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8303"
version_tuple = (0, 0, 8303)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8303")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8191"
data_version_tuple = (0, 0, 8191)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8191")
except ImportError:
    pass
data_git_hash = "9f7e6d7246903d9095e99c540f39d21d4b93c7d6"
data_git_describe = "v0.0-8191-g9f7e6d724"
data_git_msg = """\
commit 9f7e6d7246903d9095e99c540f39d21d4b93c7d6
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Thu Oct 14 10:42:44 2021 -0700

    [fpv] FPV testbench rename
    
    This PR updates the batch script and use the _tb name for DUT names.
    
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
